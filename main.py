version = "0.3.1"
window_title = f"GD Recruit Assistant Beta ({version})"
import sys
import platform
import logging
logging.basicConfig(filename="./gdrecruit.log",
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(asctime)s %(name)s: %(threadName)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p'
)
logger = logging.getLogger(__name__)

import os, os.path
from os import path
from queue import Queue
import datetime, time
import requests
import traceback
from playwright.async_api import async_playwright
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *
from mypackages.mainwindow_ui import Ui_MainWindow
from mypackages.wis_cred_dialog import Ui_WISCredentialDialog
from mypackages.new_season_dialog import Ui_DialogNewSeason
from mypackages.load_season_dialog import Ui_DialogLoadSeason
from mypackages.bold_attributes_dialog import Ui_DialogBoldAttributes
from mypackages.grab_season_data_widget import Ui_WidgetGrabSeasonData
from mypackages.world_lookup import wid_world_list
from mypackages.browser import *
import configparser
from progress.bar import Bar
import pandas as pd
import numpy as np
from pathlib import Path


# https://stackoverflow.com/questions/61316258/how-to-overwrite-qdialog-accept




def logQueryError(query):
    logging.error(f"{datetime.datetime.now()}: query: last error: {query.lastError()}")
    logging.error(f"{datetime.datetime.now()}: query: last query: {query.lastQuery()}")


wis_gd_df = ''
gdr_csv = ''
bold_attributes_csv = ''
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    gdr_csv = f"{Path(sys._MEIPASS) / 'data' / 'gdr.csv'}"
    #bold_attributes_csv = f"{Path(sys._MEIPASS) / 'data' / 'bold_attributes.csv'}"
else:
    gdr_csv = f"./data/gdr.csv"
    #bold_attributes_csv = f"./data/bold_attributes.csv"
logger.info(f"gdr.csv path is = {gdr_csv}")
#logger.info(f"bold_attributes.csv path is = {bold_attributes_csv}")
wis_gd_df = pd.read_csv(gdr_csv, header=0, index_col=0)
#bold_attributes_df = pd.read_csv(bold_attributes_csv, header = 0, index_col=0)


def query_Recruit_IDs(type, dbconn):
    openDB(dbconn)
    logger.info(f"query_Recruit_IDs: Database name = {dbconn.databaseName()} Connection name = {dbconn.connectionName()} Tables = {dbconn.tables()}")
    queryRecruitIDs = QSqlQuery(dbconn)
    rids = []
    if type == "all":
        if not queryRecruitIDs.exec_("SELECT id,pos FROM recruits"):
            logQueryError(queryRecruitIDs)
        while queryRecruitIDs.next():
            r = queryRecruitIDs.value('id')
            position = queryRecruitIDs.value('pos')
            rids.append([r, position])
    elif type == "unsigned":
        if not queryRecruitIDs.exec_("SELECT id FROM recruits WHERE signed=0"):
            logQueryError(queryRecruitIDs)
        while queryRecruitIDs.next():
            rids.append(queryRecruitIDs.value('id'))
    queryRecruitIDs.finish()
    logger.info(f"Closing {dbconn.databaseName()}...")
    dbconn.close()
    logger.info("End of query_Recruit_IDs function")
    return rids


class InitializeWorker(QObject):
    finished = Signal()
    progress = Signal(int, int)
    
    
    
    def run(self):
        """Long-running Initialize Recruit task goes here."""
        logger.info("Started InitializeWorker.run function")
        # Thread signaling start
        self.progress.emit(0, 1)

        
        coachid, user, pwd, config = load_config()
        requests_session = requests.Session()
        db_t.setDatabaseName(db.databaseName())
        openDB(db_t)
        createRecruitTableQuery = QSqlQuery(db_t)
        if not createRecruitTableQuery.exec_(
            """
            CREATE TABLE IF NOT EXISTS recruits (
                id INTEGER PRIMARY KEY,
                name TEXT,
                pos TEXT,
                height TEXT,
                weight INTEGER,
                rating INTEGER,
                rank TEXT,
                hometown TEXT,
                miles INTEGER,
                considering TEXT,
                ath INTEGER,
                spd INTEGER,
                dur INTEGER,
                we INTEGER,
                sta INTEGER,
                str INTEGER,
                blk INTEGER,
                tkl INTEGER,
                han INTEGER,
                gi INTEGER,
                elu INTEGER,
                tec INTEGER,
                r1 REAL,
                r2 REAL,
                r3 REAL,
                r4 REAL,
                r5 REAL,
                r6 REAL,
                gpa REAL,
                pot TEXT,
                signed INTEGER,
                watched INTEGER
            )
            """
        ):
            logQueryError(createRecruitTableQuery)
        createRecruitTableQuery.finish()
        logger.info(f"db tables = {db_t.tables()}")
        # The above query only creates a new table if it doesn't already exist
        # This next step ensures deletion of any prior data in recruits table
        createRecruitTableQuery2 = QSqlQuery(db_t)
        if db_t.tables() == ['recruits']:
            if not createRecruitTableQuery2.exec_("DELETE from recruits"):
                logQueryError(createRecruitTableQuery2)
        createRecruitTableQuery2.finish()
        logger.info(f"db tables = {db_t.tables()}")
        db_t.close()
        
        #Thread progress signaling DB was created
        self.progress.emit(1, 1)
        result = wis_browser(config, user, pwd, "scrape_recruit_IDs", db_t, self.progress)
        if result:
            # After grabbing all Recruit IDs and storing in DB.
            # This thread is finished and now need to signal 
            # creation of new threads for grabbing static attributes of recruits.
            self.finished.emit()
        else:
            # Implies there was an error authenticating to WIS
            self.progress.emit(999999,1)


#https://www.learnpyqt.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/
class Worker(QRunnable):
    """Worker thread for running background tasks."""

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        try:
            logger.debug("Worker QRunnable 'try' section")
            result = self.fn(
                *self.args, **self.kwargs,
            )
        except:
            logger.debug("Worker QRunnable 'except' section")
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            logger.debug("Worker QRunnable 'else' section")
            self.signals.result.emit(result)
        finally:
            logger.debug("Worker QRunnable 'finally' section")
            self.signals.finished.emit()


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.
    Supported signals are:
    finished
        No data
    error
        `tuple` (exctype, value, traceback.format_exc() )
    result
        `object` data returned from processing, anything
    """
    finished = Signal()
    error = Signal(tuple)
    result =Signal(object)
    progress = Signal(int)


class QueueMonitorWorker(QObject):
    finished = Signal()
    progress = Signal(int)
    
    def __init__(self, q, rc, rl, t):
        super(QueueMonitorWorker, self).__init__()
        self.q = q      # Queue object
        self.rc = rc    # recruit ID list, either an initialize list or update list
        self.rl = rl    # recruit list length
        self.t = t      # type = 'initialize' or 'update'

    def run(self):
        logger.info("Started QueueMonitorWorker.run function")
        # Loop to monitor queue size
        while self.q.qsize() > 0:
            logger.debug(f"Queue size = {self.q.qsize()}")
            self.progress.emit(self.q.qsize())
            time.sleep(1)
        # Once queue is empty, update each recruit in the DB
        self.progress.emit(self.q.qsize())
        logger.debug(f"Queue is empty -> Queue size = {self.q.qsize()}")
        db_t.setDatabaseName(db.databaseName())        
        openDB(db_t)
        query = QSqlQuery(db_t)
        if self.t == "initialize":
            logger.info(f"Initializing recruit attributes in database...")
            query.prepare("UPDATE recruits "
                                "SET ath = :ath, "
                                    "spd = :spd, "
                                    "dur = :dur, "
                                    "we = :we, "
                                    "sta = :sta, "
                                    "str = :str, "
                                    "blk = :blk, "
                                    "tkl = :tkl, "
                                    "han = :han, "
                                    "gi = :gi, "
                                    "elu = :elu, "
                                    "tec = :tec, "
                                    "r1 = :r1, "
                                    "r2 = :r2, "
                                    "r3 = :r3, "
                                    "r4 = :r4, "
                                    "r5 = :r5, "
                                    "r6 = :r6, "
                                    "gpa = :gpa "
                                "WHERE id = :id")
            # Signal that we are now updating DB
            self.progress.emit(11111111)
            counter = 1000000
            with Bar('Initializing Recruit Static Data...', max=self.rl) as bar:
                for r in self.rc:
                    query.bindValue(":ath", r['ath'])
                    query.bindValue(":spd", r['spd'])
                    query.bindValue(":dur", r['dur'])
                    query.bindValue(":we", r['we'])
                    query.bindValue(":sta", r['sta'])
                    query.bindValue(":str", r['strength'])
                    query.bindValue(":blk", r['blk'])
                    query.bindValue(":tkl", r['tkl'])
                    query.bindValue(":han", r['han'])
                    query.bindValue(":gi", r['gi'])
                    query.bindValue(":elu", r['elu'])
                    query.bindValue(":tec", r['tec'])
                    query.bindValue(":r1", float(r['role_rating']['r1']))
                    query.bindValue(":r2", float(r['role_rating']['r2']))
                    query.bindValue(":r3", float(r['role_rating']['r3']))
                    query.bindValue(":r4", float(r['role_rating']['r4']))
                    query.bindValue(":r5", float(r['role_rating']['r5']))
                    query.bindValue(":r6", float(r['role_rating']['r6']))
                    query.bindValue(":gpa", r['gpa'])
                    query.bindValue(":id", r['rid'])

                    if not query.exec_():
                        logQueryError(query)
                    counter += 1
                    self.progress.emit(counter)
                    bar.next()
        elif self.t == "update":
            logger.info(f"Updating recruit considering in database...")
            query.prepare("UPDATE recruits "
                                            "SET considering = :considering, "
                                            "signed = :signed "
                                            "WHERE id = :id")
            with Bar('Update Recruits Considering...', max=self.rl) as bar:
                for each in self.rc:
                    rid = each[0]
                    signed = each[1]
                    considering = each[2]
                    query.bindValue(":considering", considering[:-1]) # remove newline at end
                    query.bindValue(":signed", signed)
                    query.bindValue(":id", rid)
                    if not query.exec_():
                        logQueryError(query)
                    bar.next()
        query.finish()
        db_t.close()
        self.finished.emit()


class MarkRecruitsWorker(QObject):
    finished = Signal()
    progress = Signal(int)
    
    def run(self):
        
        potential_lookup = {
                            '?': '?',
                            'VL': "0-VL",
                            'L': "1-L",
                            'A': "2-A",
                            'H': "3-H",
                            'VH': "4-VH"
        }
        
        """Long-running Initialize Recruit task goes here."""

        # Thread signaling start
        self.progress.emit(0)

        # Launch playwright browser to grab watched recruits
        coachid, user, pwd, config = load_config()
        db_t.setDatabaseName(db.databaseName())
        page = wis_browser(config, user, pwd, "grab_watched_recruits", db_t, self.progress)
        if page == "":
            # Implies issues loading Recruit Summary page.
            self.progress.emit(2000)
        elif page == False:
            # Implies issue with WIS Authentication
            self.progress.emit(999999)
        else:
            self.progress.emit(3)
            # Check if total watched recruits list is empty
            total_unsigned_recruits_span = page.find(id="ctl00_ctl00_ctl00_Main_Main_Main_TotalRecruitCountLbl")
            #print(total_unsigned_recruits_span)
            if total_unsigned_recruits_span != None:
                total_unsigned_watched = int(total_unsigned_recruits_span.next_sibling)
            else:
                total_unsigned_watched = 0
            unsigned_table = page.find(id="recruits")
            watchlist = {}
            if total_unsigned_watched == 0 or "Not watching any recruits." in unsigned_table.text:
                logger.info("There are no unsigned recruits in the watchlist.")
            else:
                # https://stackoverflow.com/questions/14257717/python-beautifulsoup-wildcard-attribute-id-search
                unsigned_recruit_rows = unsigned_table.find_all("tr",
                                                                {"id": lambda L: L and L.startswith("ctl00_ctl00_ctl00_Main_Main_Main_rptPriorities_ct")}
                                                                )
                for row in unsigned_recruit_rows:
                    columns = row.find_all("td")
                    recruit_a_tag = columns[4].find("a")
                    link = recruit_a_tag.attrs['href']
                    link_re = re.search(r"(\d{8})", link)
                    rid = int(link_re.group(1))
                    potential = potential_lookup[columns[9].text]
                    watchlist.update({rid: potential})
            signed_table = page.find(id="signed")
            if signed_table.text == "\n\n\n":
                logger.info("There are no signed recruits in the watchlist.")
            else:
                signed_recruit_tbody = signed_table.find_all("tbody")
                # The first tbody is the header row for signed recruits table.
                # The second tbody is the table with signed recruits.
                signed_recruit_rows = signed_recruit_tbody[1].find_all("tr")
                for row in signed_recruit_rows:
                    columns = row.find_all("td")
                    recruit_a_tag = columns[4].find("a")
                    link = recruit_a_tag.attrs['href']
                    link_re = re.search(r"(\d{8})", link)
                    rid = int(link_re.group(1))
                    potential = potential_lookup[columns[9].text]
                    watchlist.update({rid: potential})

            logger.info(f"Length of watchlist = {len(watchlist)}")

            # First we clear all watched recruits from the db
            openDB(db_t)
            queryUpdate = QSqlQuery(db_t)
            if not queryUpdate.exec_(
                """
                UPDATE recruits SET watched = 0
                """
            ):
                logQueryError(queryUpdate)
            queryUpdate.finish()

            # Now we set watched = 1 for the rids in watchlist
            query_watched_update = QSqlQuery(db_t)
            query_watched_update.prepare("UPDATE recruits "
                                        "SET watched = 1, "
                                        "pot = :pot "
                                        "WHERE id = :id")
            for k, v in watchlist.items():
                query_watched_update.bindValue(":id", k)
                query_watched_update.bindValue(":pot", v)
                if not query_watched_update.exec_():
                    logQueryError(query_watched_update)
            query_watched_update.finish()

            db_t.close()

            # Report done
            self.progress.emit(1000)
            mw.statusbar.showMessage(f"{len(watchlist)} recruits marked from watchlist.")
        self.finished.emit()


class GrabSeasonData(QDialog, Ui_WidgetGrabSeasonData):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Queue to process recruit IDs
        self.rid_queue = Queue()
        self.threadpool = QThreadPool()
        self.threadCount = QThreadPool.globalInstance().maxThreadCount()
        self.requests_session = requests.Session()
        self.recruit_initialize_list = []
        self.recruit_considering = []
        self.rids_unsigned_length = 0
        self.rids_all = query_Recruit_IDs("all", db)
        self.rids_all_length = len(self.rids_all)
        if self.rids_all_length == 0:
            self.pushButtonInitializeRecruits.setText(QCoreApplication.translate("MainWindow", u"&Initialize Recruits", None))
            self.pushButtonUpdateConsideringSigned.setVisible(False)
            self.pushButtonMarkRecruitsFromWatchlist.setVisible(False)
        else:
            self.pushButtonMarkRecruitsFromWatchlist.setEnabled(True)
            self.labelRecruitsInitialized.setText(f"Recruits Initialized = {self.rids_all_length}")
            self.labelRecruitsInitialized.setStyleSheet(u"color: rgb(0, 128, 0);")
            self.pushButtonInitializeRecruits.setText(QCoreApplication.translate("MainWindow", u"&Re-Initialize Recruits", None))
        
        self.pushButtonUpdateConsideringSigned.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"&Update Considering / Signed", None))
        self.pushButtonMarkRecruitsFromWatchlist.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"&Mark Recruits From Watchlist", None))

        # Hide all progress check marks and text until button is pressed
        self.labelAuthWIS_MarkRecruits.setVisible(False)
        self.labelCheckMarkAuthWIS_Error.setVisible(False)
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setVisible(False)
        self.labelCheckMarkAuthWIS_MarkRecruits.setVisible(False)
        self.labelCheckMarkCreateDB.setVisible(False)
        self.labelCheckMarkAuthWIS.setVisible(False)
        self.labelCheckMarkGrabUnsigned.setVisible(False)
        self.labelCheckMarkGrabSigned.setVisible(False)
        self.labelCheckMarkGrabStaticData.setVisible(False)
        self.labelProgressCreateRecruitDB.setVisible(False)
        self.labelAuthWIS.setVisible(False)
        self.labelGrabUnsigned.setVisible(False)
        self.labelGrabSigned.setVisible(False)
        self.labelGrabStaticData.setVisible(False)
        self.progressBarInitializeRecruits.setVisible(False)
        self.progressBarInitializeRecruits.setValue(0)
        self.progressBarUpdateConsidering.setVisible(False)
        self.progressBarUpdateConsidering.setValue(0)
        self.labelUpdateProgressBarMax.setVisible(False)
        self.pushButtonInitializeRecruits.clicked.connect(self.runInitializeJob)
        self.pushButtonUpdateConsideringSigned.clicked.connect(self.queue_run_update_considering)
        self.pushButtonMarkRecruitsFromWatchlist.clicked.connect(self.runMarkRecruitsJob)
        self.progressBarMarkWatchlist.setVisible(False)

    def accept(self):
        super().accept()


    def runInitializeJob(self):
        logger.info("Button Pressed: Initialize Recruits")
        # Step 1: Create a QThread object
        self.thread = QThread()
        # Step 2: Create a worker object
        self.worker = InitializeWorker()
        # Step 3: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 4: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportInitializeProgress)
        # Step 6: Start the thread
        self.thread.start()
        # Final resets
        self.labelRecruitsInitialized.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.labelRecruitsInitialized.setText(f"Recruits Initialized = 0")
        self.pushButtonInitializeRecruits.setEnabled(False)
        self.pushButtonMarkRecruitsFromWatchlist.setVisible(False)
        self.pushButtonUpdateConsideringSigned.setVisible(False)
        self.labelCheckMarkCreateDB.setVisible(False)
        self.labelCheckMarkAuthWIS.setVisible(False)
        self.labelCheckMarkAuthWIS_Error.setVisible(False)
        self.labelCheckMarkGrabUnsigned.setVisible(False)
        self.labelCheckMarkGrabSigned.setVisible(False)
        self.labelCheckMarkGrabStaticData.setVisible(False)
        self.thread.finished.connect(self.queue_run_initialize_attributes)

    def reportInitializeProgress(self, n, m):
        # print(f"n = {n}\nm = {m}")
        if n == 0:
            self.progressBarMarkWatchlist.setVisible(False)
            self.progressBarUpdateConsidering.setVisible(False)
            self.labelProgressCreateRecruitDB.setVisible(True)
            self.labelAuthWIS.setVisible(True)
            self.labelGrabUnsigned.setVisible(True)
            self.labelGrabSigned.setVisible(True)
            self.labelGrabStaticData.setVisible(True)
            self.progressBarInitializeRecruits.setRange(0, 0)
            self.progressBarInitializeRecruits.setVisible(True)
        if n == 1:
            # DB created
            self.labelCheckMarkCreateDB.setVisible(True)
        if n == 2:
            # WIS Auth Completed
            self.labelCheckMarkAuthWIS.setVisible(True)
        if n == 100:
            # Starting to grab unsigned recruits
            self.progressBarInitializeRecruits.setRange(0, 100)
            self.progressBarInitializeRecruits.setVisible(True)
        if 100 < n <= 110:
            self.progressBarInitializeRecruits.setValue((n - 100) * 10)
            if n == 110:
                self.labelCheckMarkGrabUnsigned.setVisible(True)
        if n == 200:
            # Starting to grab signed recruits
            self.progressBarInitializeRecruits.setRange(0, 100)
            self.progressBarInitializeRecruits.value()
        if 200 < n <= 210:
            self.progressBarInitializeRecruits.setValue((n - 200) * 10)
            self.progressBarInitializeRecruits.value()
            if n == 210:
                self.labelCheckMarkGrabSigned.setVisible(True)
        if n == 1000:
            # Starting to grab recruit static data
            self.labelRecruitsInitialized.setText(f"Initializing {m} Recruits...")
            self.progressBarInitializeRecruits.setRange(0, m)
            self.progressBarInitializeRecruits.setValue(0)
            self.progressBarInitializeRecruits.value()
        if n > 1000:
            #percent_done = (n - 1000) / m * 100
            #print(percent_done)
            self.progressBarInitializeRecruits.setValue(n - 1000)
        if n > 1000 and (n - 1000) == m:
            self.labelCheckMarkGrabStaticData.setVisible(True)
            self.labelRecruitsInitialized.setText(f"Recruits Initialized = {m}")
            self.pushButtonUpdateConsideringSigned.setVisible(True)
            self.pushButtonUpdateConsideringSigned.setEnabled(True)
            self.pushButtonMarkRecruitsFromWatchlist.setVisible(True)
            self.pushButtonMarkRecruitsFromWatchlist.setEnabled(True)
        if n == 999999:
            self.labelCheckMarkAuthWIS_Error.setVisible(True)
            mw.statusbar.showMessage("ERROR: There was a problem authenticating to WIS.")
            self.progressBarInitializeRecruits.setVisible(False)


    def queue_run_initialize_attributes(self):
        logger.info(f"Running queue_run_initialize_attributes function")
        self.queue_rid_urls(self.rid_queue, "all")
        self.labelRecruitsInitialized.setText(f"Initializing {self.rids_all_length} Recruits...")
        self.progressBarInitializeRecruits.setRange(0, self.rids_all_length)
        self.progressBarInitializeRecruits.setValue(0)
        self.progressBarInitializeRecruits.value()
        self.stopped = False
        self.run_threads(self.recruit_initialize, self.completed)


    def recruit_initialize(self, progress_callback):
        while self.rid_queue.qsize() > 0:
            logger.debug(f"Looking for the next Recruit ID...")
            rid = self.rid_queue.get()
            logger.debug(f"Processing {rid}")
            r = rid[0]
            position = rid[1]
            page = rid[2]
            recruitpage = self.requests_session.get(page)
            recruitpage_soup = BeautifulSoup(recruitpage.content, "lxml")
            recruit_ratings_section = recruitpage_soup.find(class_="ratingsDisplayCtl")
            recruit_ratings_values = recruit_ratings_section.find_all(class_="value")
            gpa_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_gpa")
            recruit = {
                        'rid': r,
                        'gpa': float(gpa_section.text),
                        'ath': int(recruit_ratings_values[0].text),
                        'spd': int(recruit_ratings_values[1].text),
                        'dur': int(recruit_ratings_values[2].text),
                        'we': int(recruit_ratings_values[3].text),
                        'sta': int(recruit_ratings_values[4].text),
                        'strength': int(recruit_ratings_values[5].text),
                        'blk': int(recruit_ratings_values[6].text),
                        'tkl': int(recruit_ratings_values[7].text),
                        'han': int(recruit_ratings_values[8].text),
                        'gi': int(recruit_ratings_values[9].text),
                        'elu': int(recruit_ratings_values[10].text),
                        'tec': int(recruit_ratings_values[11].text),
                        'role_rating': ""
            }

            recruit['role_rating'] = self.calculate_role_rating(position, recruit)

            self.recruit_initialize_list.append(recruit)
            self.rid_queue.task_done()
            progress_callback.emit(self.rid_queue.qsize())
            if self.stopped == True:
                return
        return


    def calculate_role_rating(self, pos, ratings):
        rating_formulas = {
            'QB': {
                'r1': [10, 4, 0, 0, 0, 26, 0, 0, 0, 24, 8, 28],
                'r2': [8, 18, 2, 1, 3, 24, 0, 0, 0, 16, 20, 8],
                'r3': [8, 4, 1, 1, 2, 26, 0, 0, 0, 26, 8, 24],
                'r4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'r5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'r6': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            'RB': {
                'r1': [8, 22, 1, 1, 3, 21, 0, 0, 3, 11, 22, 8],
                'r2': [8, 0, 1, 1, 3, 36, 30, 0, 0, 0, 13, 8],
                'r3': [8, 24, 1, 1, 3, 20, 0, 0, 0, 10, 25, 8],
                'r4': [8, 20, 1, 1, 3, 25, 0, 0, 0, 10, 24, 8],
                'r5': [8, 22, 1, 1, 3, 21, 0, 0, 3, 11, 22, 8],
                'r6': [8, 22, 1, 1, 3, 21, 0, 0, 3, 11, 22, 8]
            },
            'WR': {
                'r1': [15, 18, 1, 1, 3, 0, 0, 0, 18, 20, 16, 8],
                'r2': [16, 12, 1, 1, 3, 0, 0, 0, 24, 24, 11, 8],
                'r3': [12, 23, 1, 1, 3, 0, 0, 0, 11, 18, 23, 8],
                'r4': [15, 18, 1, 1, 3, 0, 0, 0, 18, 20, 16, 8],
                'r5': [15, 18, 1, 1, 3, 0, 0, 0, 18, 20, 16, 8],
                'r6': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            'TE': {
                'r1': [14, 6, 1, 1, 2, 18, 13, 0, 13, 18, 6, 8],
                'r2': [11, 0, 1, 1, 2, 36, 26, 0, 0, 15, 0, 8],
                'r3': [16, 12, 1, 1, 2, 0, 0, 0, 24, 24, 12, 8],
                'r4': [14, 6, 1, 1, 2, 18, 13, 0, 13, 18, 6, 8],
                'r5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'r6': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            'OL': {
                'r1': [12, 0, 1, 1, 2, 32, 32, 0, 0, 12, 0, 8],
                'r2': [12, 0, 1, 1, 2, 23, 41, 0, 0, 12, 0, 8],
                'r3': [12, 0, 1, 1, 2, 41, 23, 0, 0, 12, 0, 8],
                'r4': [12, 0, 1, 1, 2, 32, 32, 0, 0, 12, 0, 8],
                'r5': [12, 0, 1, 1, 2, 32, 32, 0, 0, 12, 0, 8],
                'r6': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            'DL': {
                'r1': [13, 8, 1, 1, 2, 32, 0, 20, 0, 15, 0, 8],
                'r2': [12, 6, 1, 1, 2, 38, 0, 17, 0, 15, 0, 8],
                'r3': [12, 15, 1, 1, 2, 22, 0, 24, 0, 15, 0, 8],
                'r4': [13, 8, 1, 1, 2, 32, 0, 20, 0, 15, 0, 8],
                'r5': [13, 8, 1, 1, 2, 32, 0, 20, 0, 15, 0, 8],
                'r6': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            'LB': {
                'r1': [15, 8, 1, 1, 2, 30, 0, 20, 0, 15, 0, 8],
                'r2': [12, 4, 1, 1, 2, 38, 0, 22, 0, 12, 0, 8],
                'r3': [13, 12, 1, 1, 2, 21, 0, 21, 0, 21, 0, 8],
                'r4': [13, 19, 1, 1, 2, 15, 0, 20, 0, 21, 0, 8],
                'r5': [15, 8, 1, 1, 2, 30, 0, 20, 0, 15, 0, 8],
                'r6': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            'DB': {
                'r1': [16, 20, 1, 1, 4, 10, 0, 10, 10, 20, 0, 8],
                'r2': [18, 17, 1, 1, 4, 12, 0, 12, 10, 17, 0, 8],
                'r3': [21, 21, 1, 1, 4, 7, 0, 7, 12, 18, 0, 8],
                'r4': [15, 20, 1, 1, 4, 11, 0, 20, 8, 12, 0, 8],
                'r5': [15, 20, 1, 1, 4, 11, 0, 20, 8, 12, 0, 8],
                'r6': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            'K': {
                'r1': [8, 4, 1, 1, 0, 36, 0, 0, 0, 14, 0, 36],
                'r2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'r3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'r4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'r5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'r6': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            'P': {
                'r1': [8, 4, 1, 1, 0, 36, 0, 0, 0, 14, 0, 36],
                'r2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'r3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'r4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'r5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                'r6': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            }
        }

        recruit = [
            ratings['ath'],
            ratings['spd'],
            ratings['dur'],
            ratings['we'],
            ratings['sta'],
            ratings['strength'],
            ratings['blk'],
            ratings['tkl'],
            ratings['han'],
            ratings['gi'],
            ratings['elu'],
            ratings['tec']
        ]

        recruit_role_ratings = {
            'r1': round(np.dot(rating_formulas[pos]['r1'], recruit)/100, 1),
            'r2': round(np.dot(rating_formulas[pos]['r2'], recruit)/100, 1),
            'r3': round(np.dot(rating_formulas[pos]['r3'], recruit)/100, 1),
            'r4': round(np.dot(rating_formulas[pos]['r4'], recruit)/100, 1),
            'r5': round(np.dot(rating_formulas[pos]['r5'], recruit)/100, 1),
            'r6': round(np.dot(rating_formulas[pos]['r6'], recruit)/100, 1)
        }

        return recruit_role_ratings


    def queue_rid_urls(self, q=Queue(), t=str()):
        rids = query_Recruit_IDs(t, db)
        if t == "all":
            self.rids_all_length = len(rids)
            logger.info(f"All recruits = {self.rids_unsigned_length}")
            url_base = "https://www.whatifsports.com/gd/RecruitProfile/Ratings.aspx?rid="
            for each in rids:
                rid = each[0]
                position = each[1]
                recruit = (rid, position, f"{url_base}{rid}")
                logger.debug(f"Queuing ({t}): {recruit}")
                q.put(recruit)
        elif t == "unsigned":
            self.rids_unsigned_length = len(rids)
            logger.info(f"Unsigned recruits = {self.rids_unsigned_length}")
            url_base = "https://www.whatifsports.com/gd/RecruitProfile/Considering.aspx?rid="
            url_suffix = "&section=Ratings"
            for rid in rids:
                recruit = (rid, f"{url_base}{rid}")
                logger.debug(f"Queuing ({t}): {recruit}")
                q.put(recruit)
            

    def progress_fn(self, msg):
        #self.info.append(str(msg))
        logger.debug("Running progress_fn function")
        return


    def run_threads(self, process, on_complete):
        # Step 1: Create thread object to monitor queue
        self.thread = QThread()
        # Step 2: Create a worker object
        if process.__func__.__name__ == "recruit_update":
            logger.debug("run_threads function -> recruit_update conditional statement")
            self.worker = QueueMonitorWorker(self.rid_queue, self.recruit_considering, self.rids_unsigned_length, "update")
            # Step 3: Move worker to the thread
            self.worker.moveToThread(self.thread)
            # Step 4: Connect signals and slots
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.progress.connect(self.queue_monitor_update_progress)
            # Step 6: Start the thread
            self.thread.start()
            # Final resets
            self.pushButtonInitializeRecruits.setEnabled(False)
            self.pushButtonUpdateConsideringSigned.setEnabled(False)
            self.pushButtonMarkRecruitsFromWatchlist.setEnabled(False)
            self.thread.finished.connect(self.update_finished)
        elif process.__func__.__name__ == "recruit_initialize":
            logger.debug("run_threads function -> recruit_initialize conditional statement")
            self.worker = QueueMonitorWorker(self.rid_queue, self.recruit_initialize_list, self.rids_all_length, "initialize")
            # Step 3: Move worker to the thread
            self.worker.moveToThread(self.thread)
            # Step 4: Connect signals and slots
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.progress.connect(self.queue_monitor_initialize_progress)
            # Step 6: Start the thread
            self.thread.start()
            # Final resets
            #self.pushButtonInitializeRecruits.setEnabled(False)
            #self.pushButtonUpdateConsideringSigned.setEnabled(False)
            #self.pushButtonMarkRecruitsFromWatchlist.setEnabled(False)
            self.thread.finished.connect(self.initialize_finished)
        else:
            raise Exception

        """Execute a function in the background with a worker"""
        for i in range(self.threadCount - 1):
            worker = Worker(fn=process)
            self.threadpool.start(worker)
            worker.signals.finished.connect(on_complete)
            worker.signals.progress.connect(self.progress_fn)
            #self.progressbar.setRange(0,0)
        return


    def initialize_finished(self):
        logger.debug("Running initialized_finished function")
        self.pushButtonUpdateConsideringSigned.setVisible(True)
        self.pushButtonUpdateConsideringSigned.setEnabled(True)
        self.pushButtonMarkRecruitsFromWatchlist.setVisible(True)
        self.pushButtonMarkRecruitsFromWatchlist.setEnabled(True)
        self.labelRecruitsInitialized.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.labelRecruitsInitialized.setText(f"Initialized {self.rids_all_length} Recruits...")


    def update_finished(self):
        logger.debug("Running update_finished function")
        self.pushButtonUpdateConsideringSigned.setEnabled(True)
        self.pushButtonInitializeRecruits.setEnabled(True)
        self.pushButtonMarkRecruitsFromWatchlist.setEnabled(True)


    def recruit_update(self, progress_callback):
        while self.rid_queue.qsize() > 0:
            logger.debug(f"Length of queue = {self.rid_queue.qsize()}")
            logger.debug(f"Looking for the next Recruit ID...")
            rid = self.rid_queue.get()
            logger.debug(f"Processing {rid}")
            recruitpage = self.requests_session.get(rid[1])
            recruitpage_soup = BeautifulSoup(recruitpage.content, "lxml")
            teams_table = recruitpage_soup.find("table", id="tblTeams")
            teams_table_body = teams_table.find("tbody")
            team_rows = teams_table_body.find_all("tr")
            considering = ''
            signed = 0
            for row in team_rows:
                team_data = row.find_all("td")
                if "undecided" in team_data[0].text:
                    considering = "undecided\n"
                elif "already signed" in team_data[0].text:
                    find_signed_with = recruitpage_soup.find("a", id="ctl00_ctl00_ctl00_Main_Main_signedWithTeam")
                    href_tag = find_signed_with.attrs['href']
                    href_tag_re = re.search(r'(\d{5})', href_tag)
                    team_id = int(href_tag_re.group(1))
                    considering = f"{wis_gd_df.school_short[team_id]}\n"
                    signed = 1
                else:
                    school = team_data[0].text
                    coach = team_data[1].text
                    division = team_data[2].text
                    scholarships_total = team_data[3].text
                    scholarships_open = team_data[4].text
                    distance = team_data[5].text # WIS bug always shows N/A for distance???
                    considering += f"{school} ({coach}) {division} {scholarships_total}|{scholarships_open}\n"
            self.recruit_considering.append((rid[0], signed, considering))
            self.rid_queue.task_done()    
            progress_callback.emit(self.rid_queue.qsize())
            if self.stopped == True:
                return
        return

    def queue_run_update_considering(self):
        self.progressBarUpdateConsidering.setVisible(True)
        self.pushButtonInitializeRecruits.setEnabled(False)
        self.pushButtonMarkRecruitsFromWatchlist.setEnabled(False)
        self.pushButtonUpdateConsideringSigned.setEnabled(False)
        self.labelUpdateProgressBarMax.setVisible(True)
        self.queue_rid_urls(self.rid_queue, "unsigned")
        self.labelUpdateProgressBarMax.setText(f"of {self.rids_unsigned_length}")
        self.progressBarUpdateConsidering.setRange(0, self.rids_unsigned_length)
        self.stopped = False
        self.run_threads(self.recruit_update, self.completed)

    def stop(self):
        self.stopped=True
        return

    def completed(self):
        logger.debug(f"Running threading completed function")
        return


    def queue_monitor_initialize_progress(self, n):
        if n == 0:
            logger.debug("Queue is empty.")
            completed = self.rids_all_length - n
            self.progressBarInitializeRecruits.setValue(completed)
            self.labelCheckMarkGrabStaticData.setVisible(True)
        elif n > 0 and n < 1000000:
            completed = self.rids_all_length - n
            self.progressBarInitializeRecruits.setValue(completed)
        elif n == 1000000:
            self.progressBarInitializeRecruits.setValue(0)
        elif n > 1000000:
            self.progressBarInitializeRecruits.setValue(n - 1000000)


    def queue_monitor_update_progress(self, n):
        if n == 0:
            logger.debug("Queue is empty.")
            completed = self.rids_unsigned_length - n
            self.progressBarUpdateConsidering.setValue(completed)
        else:
            completed = self.rids_unsigned_length - n
            self.progressBarUpdateConsidering.setValue(completed)



    def runMarkRecruitsJob(self):
        logger.info("Button Pressed: Mark Recruits From Watchlist")
        # Step 1: Create a QThread object
        self.thread = QThread()
        # Step 2: Create a worker object
        self.worker = MarkRecruitsWorker()
        # Step 3: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 4: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportMarkRecruitsProgress)
        # Step 6: Start the thread
        self.thread.start()
        # Final resets
        self.labelAuthWIS_MarkRecruits.setVisible(True)
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setVisible(False)
        self.labelCheckMarkAuthWIS_MarkRecruits.setVisible(False)
        self.pushButtonInitializeRecruits.setEnabled(False)
        self.pushButtonUpdateConsideringSigned.setEnabled(False)
        self.pushButtonMarkRecruitsFromWatchlist.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.pushButtonMarkRecruitsFromWatchlist.setEnabled(True)
        )


    def reportMarkRecruitsProgress(self, n):
        if n == 0:
            self.progressBarMarkWatchlist.setStyleSheet("color: blue")
            self.progressBarUpdateConsidering.setVisible(False)
            self.progressBarMarkWatchlist.setVisible(True)
            self.progressBarMarkWatchlist.setEnabled(True)
            self.progressBarMarkWatchlist.setRange(0, 0)
            logger.info("Thread started for Marking Recruits From Watchlist")
        if n == 1:
            logger.info("WIS auth through playwright browser completed.")
            self.labelCheckMarkAuthWIS_MarkRecruits.setVisible(True)
            self.progressBarMarkWatchlist.setRange(0, 100)
            self.progressBarMarkWatchlist.setValue(40)
        if n == 2:
            self.progressBarMarkWatchlist.setValue(60)
        if n == 3:
            self.progressBarMarkWatchlist.setValue(80)
        if n == 1000:
            self.progressBarMarkWatchlist.setValue(100)
            self.pushButtonInitializeRecruits.setEnabled(True)
            self.pushButtonUpdateConsideringSigned.setEnabled(True)
        if n == 2000:
            self.pushButtonInitializeRecruits.setEnabled(True)
            self.pushButtonUpdateConsideringSigned.setEnabled(True)
            mw.statusbar.showMessage("ERROR: There was a problem loading Recruit Summary Page.")
        if n == 999999:
            self.pushButtonInitializeRecruits.setEnabled(True)
            self.pushButtonUpdateConsideringSigned.setEnabled(True)
            self.labelCheckMarkAuthWIS_Error_MarkRecruits.setVisible(True)
            self.progressBarMarkWatchlist.setVisible(False)
            mw.statusbar.showMessage("ERROR: There was a problem authenticating to WIS.")


class LoadSeason(QDialog, Ui_DialogLoadSeason):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        db_files = [x for x in os.listdir() if x.endswith(".db")]
        if len(db_files) > 0:
            self.comboBoxSelectSeason.addItems(db_files)
        else:
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

    def accept(self):
        season_filename = self.comboBoxSelectSeason.currentText()
        db.close()
        db.setDatabaseName(season_filename)
        super().accept()

class NewSeason(QDialog, Ui_DialogNewSeason):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        config = configparser.ConfigParser()
        config.read('./config.ini')
        if config.has_section('Schools') and len(config['Schools']) > 0:
            school_list = config.items('Schools')
            names_only = []
            for each in school_list:
                names_only.append(f"{each[1]} {each[0]}")
            self.comboBoxTeamID.addItems(names_only)
            #self.comboBoxTeamID.addItems(config['Schools'])
        self.onlyInt = QIntValidator(1,999)
        self.lineEditSeasonNumber.setValidator(self.onlyInt)
        self.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)
        self.lineEditSeasonNumber.textChanged.connect(self.buttonstate)

    def buttonstate(self):
        if self.lineEditSeasonNumber.text() != '':
            self.buttonBox.button(QDialogButtonBox.Save).setEnabled(True)
            
        else:
            self.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)

    def accept(self):
        selected = self.comboBoxTeamID.currentText()
        seasonnum = self.lineEditSeasonNumber.text()
        season_filename = f"{seasonnum} - {selected}.db"
        print(f"Setting database name to: {season_filename}")
        db.setDatabaseName(season_filename)
        db.close()
        db.open()
        super().accept()


class WISCred(QDialog, Ui_WISCredentialDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        coachid, wisuser, pwd, config = load_config()
        self.setupUi(self, coachid, wisuser, pwd)
        self.buttonstate()
        self.labelCheckMarkcoachIDValidated.setVisible(False)
        self.labelCheckMarkcoachIDValidationError.setVisible(False)
        # Validate coachid from config file is proper
        if coachid != "":
            self.validate_coach_profile()
        self.lineEditWISCoachID.textChanged.connect(self.buttonstate)
        self.lineEditWISCoachID.editingFinished.connect(self.validate_coach_profile)
        self.lineEditWISUsername.textChanged.connect(self.buttonstate)
        self.lineEditWISPassword.textChanged.connect(self.buttonstate)
        

    def buttonstate(self):
        if self.lineEditWISCoachID.text() != '' and self.lineEditWISPassword.text() != '' and self.lineEditWISUsername.text() != '':
            self.buttonBox.button(QDialogButtonBox.Save).setEnabled(True)
        else:
            self.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)


    def validate_coach_profile(self):
        requests_session = requests.Session()
        coachid = self.lineEditWISCoachID.text()
        if coachid == "":
            self.labelCheckMarkcoachIDValidationError.setVisible(False)
            self.labelCheckMarkcoachIDValidated.setVisible(False)
        else:
            coach_profile_page = requests_session.get(f"https://www.whatifsports.com/account/UserProfile/Games/GridironDynasty/?user={coachid}")
            if coach_profile_page.status_code == 200:
                logger.info(f"Validated coach ID: {coachid} (status code = {coach_profile_page.status_code})")
                self.labelCheckMarkcoachIDValidationError.setVisible(False)
                self.labelCheckMarkcoachIDValidated.setVisible(True)
            else:
                logger.info(f"Error validating coach ID: {coachid} (status code = {coach_profile_page.status_code})")
                self.labelCheckMarkcoachIDValidationError.setVisible(True)
                self.labelCheckMarkcoachIDValidated.setVisible(False)


    def accept(self):
        coachid = self.lineEditWISCoachID.text()
        logger.info(f"Coach ID = {coachid}")
        user = self.lineEditWISUsername.text()
        pwd = self.lineEditWISPassword.text()
        config = configparser.ConfigParser()
        config.read('./config.ini')
        config.set('WISCreds', 'coachid', coachid)
        config.set('WISCreds', 'username', user)
        config.set('WISCreds', 'password', pwd)
        with open("./config.ini", 'w') as file:
            config.write(file)
        update_active_teams(coachid)
        super().accept()


class BoldAttributes(QDialog, Ui_DialogBoldAttributes):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Bold Attributes Dialog")
        
        # Check the boxes according to the loaded dataframe
        
        enable_check = {1: True, 0: False}

        # QB Section
        self.checkBox_QB_ATH.setChecked(enable_check[bold_attributes_df['ath']['qb']])
        self.checkBox_QB_SPD.setChecked(enable_check[bold_attributes_df['spd']['qb']])
        self.checkBox_QB_DUR.setChecked(enable_check[bold_attributes_df['dur']['qb']])
        self.checkBox_QB_WE.setChecked(enable_check[bold_attributes_df['we']['qb']])
        self.checkBox_QB_STA.setChecked(enable_check[bold_attributes_df['sta']['qb']])
        self.checkBox_QB_STR.setChecked(enable_check[bold_attributes_df['str']['qb']])
        self.checkBox_QB_BLK.setChecked(enable_check[bold_attributes_df['blk']['qb']])
        self.checkBox_QB_TKL.setChecked(enable_check[bold_attributes_df['tkl']['qb']])
        self.checkBox_QB_HAN.setChecked(enable_check[bold_attributes_df['han']['qb']])
        self.checkBox_QB_GI.setChecked(enable_check[bold_attributes_df['gi']['qb']])
        self.checkBox_QB_ELU.setChecked(enable_check[bold_attributes_df['elu']['qb']])
        self.checkBox_QB_TEC.setChecked(enable_check[bold_attributes_df['tec']['qb']])

        # RB Section
        self.checkBox_RB_ATH.setChecked(enable_check[bold_attributes_df['ath']['rb']])
        self.checkBox_RB_SPD.setChecked(enable_check[bold_attributes_df['spd']['rb']])
        self.checkBox_RB_DUR.setChecked(enable_check[bold_attributes_df['dur']['rb']])
        self.checkBox_RB_WE.setChecked(enable_check[bold_attributes_df['we']['rb']])
        self.checkBox_RB_STA.setChecked(enable_check[bold_attributes_df['sta']['rb']])
        self.checkBox_RB_STR.setChecked(enable_check[bold_attributes_df['str']['rb']])
        self.checkBox_RB_BLK.setChecked(enable_check[bold_attributes_df['blk']['rb']])
        self.checkBox_RB_TKL.setChecked(enable_check[bold_attributes_df['tkl']['rb']])
        self.checkBox_RB_HAN.setChecked(enable_check[bold_attributes_df['han']['rb']])
        self.checkBox_RB_GI.setChecked(enable_check[bold_attributes_df['gi']['rb']])
        self.checkBox_RB_ELU.setChecked(enable_check[bold_attributes_df['elu']['rb']])
        self.checkBox_RB_TEC.setChecked(enable_check[bold_attributes_df['tec']['rb']])

        # WR Section
        self.checkBox_WR_ATH.setChecked(enable_check[bold_attributes_df['ath']['wr']])
        self.checkBox_WR_SPD.setChecked(enable_check[bold_attributes_df['spd']['wr']])
        self.checkBox_WR_DUR.setChecked(enable_check[bold_attributes_df['dur']['wr']])
        self.checkBox_WR_WE.setChecked(enable_check[bold_attributes_df['we']['wr']])
        self.checkBox_WR_STA.setChecked(enable_check[bold_attributes_df['sta']['wr']])
        self.checkBox_WR_STR.setChecked(enable_check[bold_attributes_df['str']['wr']])
        self.checkBox_WR_BLK.setChecked(enable_check[bold_attributes_df['blk']['wr']])
        self.checkBox_WR_TKL.setChecked(enable_check[bold_attributes_df['tkl']['wr']])
        self.checkBox_WR_HAN.setChecked(enable_check[bold_attributes_df['han']['wr']])
        self.checkBox_WR_GI.setChecked(enable_check[bold_attributes_df['gi']['wr']])
        self.checkBox_WR_ELU.setChecked(enable_check[bold_attributes_df['elu']['wr']])
        self.checkBox_WR_TEC.setChecked(enable_check[bold_attributes_df['tec']['wr']])

        # TE Section
        self.checkBox_TE_ATH.setChecked(enable_check[bold_attributes_df['ath']['te']])
        self.checkBox_TE_SPD.setChecked(enable_check[bold_attributes_df['spd']['te']])
        self.checkBox_TE_DUR.setChecked(enable_check[bold_attributes_df['dur']['te']])
        self.checkBox_TE_WE.setChecked(enable_check[bold_attributes_df['we']['te']])
        self.checkBox_TE_STA.setChecked(enable_check[bold_attributes_df['sta']['te']])
        self.checkBox_TE_STR.setChecked(enable_check[bold_attributes_df['str']['te']])
        self.checkBox_TE_BLK.setChecked(enable_check[bold_attributes_df['blk']['te']])
        self.checkBox_TE_TKL.setChecked(enable_check[bold_attributes_df['tkl']['te']])
        self.checkBox_TE_HAN.setChecked(enable_check[bold_attributes_df['han']['te']])
        self.checkBox_TE_GI.setChecked(enable_check[bold_attributes_df['gi']['te']])
        self.checkBox_TE_ELU.setChecked(enable_check[bold_attributes_df['elu']['te']])
        self.checkBox_TE_TEC.setChecked(enable_check[bold_attributes_df['tec']['te']])

         # OL Section
        self.checkBox_OL_ATH.setChecked(enable_check[bold_attributes_df['ath']['ol']])
        self.checkBox_OL_SPD.setChecked(enable_check[bold_attributes_df['spd']['ol']])
        self.checkBox_OL_DUR.setChecked(enable_check[bold_attributes_df['dur']['ol']])
        self.checkBox_OL_WE.setChecked(enable_check[bold_attributes_df['we']['ol']])
        self.checkBox_OL_STA.setChecked(enable_check[bold_attributes_df['sta']['ol']])
        self.checkBox_OL_STR.setChecked(enable_check[bold_attributes_df['str']['ol']])
        self.checkBox_OL_BLK.setChecked(enable_check[bold_attributes_df['blk']['ol']])
        self.checkBox_OL_TKL.setChecked(enable_check[bold_attributes_df['tkl']['ol']])
        self.checkBox_OL_HAN.setChecked(enable_check[bold_attributes_df['han']['ol']])
        self.checkBox_OL_GI.setChecked(enable_check[bold_attributes_df['gi']['ol']])
        self.checkBox_OL_ELU.setChecked(enable_check[bold_attributes_df['elu']['ol']])
        self.checkBox_OL_TEC.setChecked(enable_check[bold_attributes_df['tec']['ol']])

        # DL Section
        self.checkBox_DL_ATH.setChecked(enable_check[bold_attributes_df['ath']['dl']])
        self.checkBox_DL_SPD.setChecked(enable_check[bold_attributes_df['spd']['dl']])
        self.checkBox_DL_DUR.setChecked(enable_check[bold_attributes_df['dur']['dl']])
        self.checkBox_DL_WE.setChecked(enable_check[bold_attributes_df['we']['dl']])
        self.checkBox_DL_STA.setChecked(enable_check[bold_attributes_df['sta']['dl']])
        self.checkBox_DL_STR.setChecked(enable_check[bold_attributes_df['str']['dl']])
        self.checkBox_DL_BLK.setChecked(enable_check[bold_attributes_df['blk']['dl']])
        self.checkBox_DL_TKL.setChecked(enable_check[bold_attributes_df['tkl']['dl']])
        self.checkBox_DL_HAN.setChecked(enable_check[bold_attributes_df['han']['dl']])
        self.checkBox_DL_GI.setChecked(enable_check[bold_attributes_df['gi']['dl']])
        self.checkBox_DL_ELU.setChecked(enable_check[bold_attributes_df['elu']['dl']])
        self.checkBox_DL_TEC.setChecked(enable_check[bold_attributes_df['tec']['dl']])

        # LB Section
        self.checkBox_LB_ATH.setChecked(enable_check[bold_attributes_df['ath']['lb']])
        self.checkBox_LB_SPD.setChecked(enable_check[bold_attributes_df['spd']['lb']])
        self.checkBox_LB_DUR.setChecked(enable_check[bold_attributes_df['dur']['lb']])
        self.checkBox_LB_WE.setChecked(enable_check[bold_attributes_df['we']['lb']])
        self.checkBox_LB_STA.setChecked(enable_check[bold_attributes_df['sta']['lb']])
        self.checkBox_LB_STR.setChecked(enable_check[bold_attributes_df['str']['lb']])
        self.checkBox_LB_BLK.setChecked(enable_check[bold_attributes_df['blk']['lb']])
        self.checkBox_LB_TKL.setChecked(enable_check[bold_attributes_df['tkl']['lb']])
        self.checkBox_LB_HAN.setChecked(enable_check[bold_attributes_df['han']['lb']])
        self.checkBox_LB_GI.setChecked(enable_check[bold_attributes_df['gi']['lb']])
        self.checkBox_LB_ELU.setChecked(enable_check[bold_attributes_df['elu']['lb']])
        self.checkBox_LB_TEC.setChecked(enable_check[bold_attributes_df['tec']['lb']])

        # DB Section
        self.checkBox_DB_ATH.setChecked(enable_check[bold_attributes_df['ath']['db']])
        self.checkBox_DB_SPD.setChecked(enable_check[bold_attributes_df['spd']['db']])
        self.checkBox_DB_DUR.setChecked(enable_check[bold_attributes_df['dur']['db']])
        self.checkBox_DB_WE.setChecked(enable_check[bold_attributes_df['we']['db']])
        self.checkBox_DB_STA.setChecked(enable_check[bold_attributes_df['sta']['db']])
        self.checkBox_DB_STR.setChecked(enable_check[bold_attributes_df['str']['db']])
        self.checkBox_DB_BLK.setChecked(enable_check[bold_attributes_df['blk']['db']])
        self.checkBox_DB_TKL.setChecked(enable_check[bold_attributes_df['tkl']['db']])
        self.checkBox_DB_HAN.setChecked(enable_check[bold_attributes_df['han']['db']])
        self.checkBox_DB_GI.setChecked(enable_check[bold_attributes_df['gi']['db']])
        self.checkBox_DB_ELU.setChecked(enable_check[bold_attributes_df['elu']['db']])
        self.checkBox_DB_TEC.setChecked(enable_check[bold_attributes_df['tec']['db']])

        # K Section
        self.checkBox_K_ATH.setChecked(enable_check[bold_attributes_df['ath']['k']])
        self.checkBox_K_SPD.setChecked(enable_check[bold_attributes_df['spd']['k']])
        self.checkBox_K_DUR.setChecked(enable_check[bold_attributes_df['dur']['k']])
        self.checkBox_K_WE.setChecked(enable_check[bold_attributes_df['we']['k']])
        self.checkBox_K_STA.setChecked(enable_check[bold_attributes_df['sta']['k']])
        self.checkBox_K_STR.setChecked(enable_check[bold_attributes_df['str']['k']])
        self.checkBox_K_BLK.setChecked(enable_check[bold_attributes_df['blk']['k']])
        self.checkBox_K_TKL.setChecked(enable_check[bold_attributes_df['tkl']['k']])
        self.checkBox_K_HAN.setChecked(enable_check[bold_attributes_df['han']['k']])
        self.checkBox_K_GI.setChecked(enable_check[bold_attributes_df['gi']['k']])
        self.checkBox_K_ELU.setChecked(enable_check[bold_attributes_df['elu']['k']])
        self.checkBox_K_TEC.setChecked(enable_check[bold_attributes_df['tec']['k']])

         # P Section
        self.checkBox_P_ATH.setChecked(enable_check[bold_attributes_df['ath']['p']])
        self.checkBox_P_SPD.setChecked(enable_check[bold_attributes_df['spd']['p']])
        self.checkBox_P_DUR.setChecked(enable_check[bold_attributes_df['dur']['p']])
        self.checkBox_P_WE.setChecked(enable_check[bold_attributes_df['we']['p']])
        self.checkBox_P_STA.setChecked(enable_check[bold_attributes_df['sta']['p']])
        self.checkBox_P_STR.setChecked(enable_check[bold_attributes_df['str']['p']])
        self.checkBox_P_BLK.setChecked(enable_check[bold_attributes_df['blk']['p']])
        self.checkBox_P_TKL.setChecked(enable_check[bold_attributes_df['tkl']['p']])
        self.checkBox_P_HAN.setChecked(enable_check[bold_attributes_df['han']['p']])
        self.checkBox_P_GI.setChecked(enable_check[bold_attributes_df['gi']['p']])
        self.checkBox_P_ELU.setChecked(enable_check[bold_attributes_df['elu']['p']])
        self.checkBox_P_TEC.setChecked(enable_check[bold_attributes_df['tec']['p']])

    def accept(self):

        # Save the state of the check boxes in dataframe and save to csv
        
        check_enabled = {0: 0, 2: 1}

        # QB Section
        bold_attributes_df['ath']['qb'] = check_enabled[self.checkBox_QB_ATH.checkState()]
        bold_attributes_df['spd']['qb'] = check_enabled[self.checkBox_QB_SPD.checkState()]
        bold_attributes_df['dur']['qb'] = check_enabled[self.checkBox_QB_DUR.checkState()]
        bold_attributes_df['we']['qb'] = check_enabled[self.checkBox_QB_WE.checkState()]
        bold_attributes_df['sta']['qb'] = check_enabled[self.checkBox_QB_STA.checkState()]
        bold_attributes_df['str']['qb'] = check_enabled[self.checkBox_QB_STR.checkState()]
        bold_attributes_df['blk']['qb'] = check_enabled[self.checkBox_QB_BLK.checkState()]
        bold_attributes_df['tkl']['qb'] = check_enabled[self.checkBox_QB_TKL.checkState()]
        bold_attributes_df['han']['qb'] = check_enabled[self.checkBox_QB_HAN.checkState()]
        bold_attributes_df['gi']['qb'] = check_enabled[self.checkBox_QB_GI.checkState()]
        bold_attributes_df['elu']['qb'] = check_enabled[self.checkBox_QB_ELU.checkState()]
        bold_attributes_df['tec']['qb'] = check_enabled[self.checkBox_QB_TEC.checkState()]

        # RB Section
        bold_attributes_df['ath']['rb'] = check_enabled[self.checkBox_RB_ATH.checkState()]
        bold_attributes_df['spd']['rb'] = check_enabled[self.checkBox_RB_SPD.checkState()]
        bold_attributes_df['dur']['rb'] = check_enabled[self.checkBox_RB_DUR.checkState()]
        bold_attributes_df['we']['rb'] = check_enabled[self.checkBox_RB_WE.checkState()]
        bold_attributes_df['sta']['rb'] = check_enabled[self.checkBox_RB_STA.checkState()]
        bold_attributes_df['str']['rb'] = check_enabled[self.checkBox_RB_STR.checkState()]
        bold_attributes_df['blk']['rb'] = check_enabled[self.checkBox_RB_BLK.checkState()]
        bold_attributes_df['tkl']['rb'] = check_enabled[self.checkBox_RB_TKL.checkState()]
        bold_attributes_df['han']['rb'] = check_enabled[self.checkBox_RB_HAN.checkState()]
        bold_attributes_df['gi']['rb'] = check_enabled[self.checkBox_RB_GI.checkState()]
        bold_attributes_df['elu']['rb'] = check_enabled[self.checkBox_RB_ELU.checkState()]
        bold_attributes_df['tec']['rb'] = check_enabled[self.checkBox_RB_TEC.checkState()]

        # WR Section
        bold_attributes_df['ath']['wr'] = check_enabled[self.checkBox_WR_ATH.checkState()]
        bold_attributes_df['spd']['wr'] = check_enabled[self.checkBox_WR_SPD.checkState()]
        bold_attributes_df['dur']['wr'] = check_enabled[self.checkBox_WR_DUR.checkState()]
        bold_attributes_df['we']['wr'] = check_enabled[self.checkBox_WR_WE.checkState()]
        bold_attributes_df['sta']['wr'] = check_enabled[self.checkBox_WR_STA.checkState()]
        bold_attributes_df['str']['wr'] = check_enabled[self.checkBox_WR_STR.checkState()]
        bold_attributes_df['blk']['wr'] = check_enabled[self.checkBox_WR_BLK.checkState()]
        bold_attributes_df['tkl']['wr'] = check_enabled[self.checkBox_WR_TKL.checkState()]
        bold_attributes_df['han']['wr'] = check_enabled[self.checkBox_WR_HAN.checkState()]
        bold_attributes_df['gi']['wr'] = check_enabled[self.checkBox_WR_GI.checkState()]
        bold_attributes_df['elu']['wr'] = check_enabled[self.checkBox_WR_ELU.checkState()]
        bold_attributes_df['tec']['wr'] = check_enabled[self.checkBox_WR_TEC.checkState()]

        # TE Section
        bold_attributes_df['ath']['te'] = check_enabled[self.checkBox_TE_ATH.checkState()]
        bold_attributes_df['spd']['te'] = check_enabled[self.checkBox_TE_SPD.checkState()]
        bold_attributes_df['dur']['te'] = check_enabled[self.checkBox_TE_DUR.checkState()]
        bold_attributes_df['we']['te'] = check_enabled[self.checkBox_TE_WE.checkState()]
        bold_attributes_df['sta']['te'] = check_enabled[self.checkBox_TE_STA.checkState()]
        bold_attributes_df['str']['te'] = check_enabled[self.checkBox_TE_STR.checkState()]
        bold_attributes_df['blk']['te'] = check_enabled[self.checkBox_TE_BLK.checkState()]
        bold_attributes_df['tkl']['te'] = check_enabled[self.checkBox_TE_TKL.checkState()]
        bold_attributes_df['han']['te'] = check_enabled[self.checkBox_TE_HAN.checkState()]
        bold_attributes_df['gi']['te'] = check_enabled[self.checkBox_TE_GI.checkState()]
        bold_attributes_df['elu']['te'] = check_enabled[self.checkBox_TE_ELU.checkState()]
        bold_attributes_df['tec']['te'] = check_enabled[self.checkBox_TE_TEC.checkState()]

        # OL Section
        bold_attributes_df['ath']['ol'] = check_enabled[self.checkBox_OL_ATH.checkState()]
        bold_attributes_df['spd']['ol'] = check_enabled[self.checkBox_OL_SPD.checkState()]
        bold_attributes_df['dur']['ol'] = check_enabled[self.checkBox_OL_DUR.checkState()]
        bold_attributes_df['we']['ol'] = check_enabled[self.checkBox_OL_WE.checkState()]
        bold_attributes_df['sta']['ol'] = check_enabled[self.checkBox_OL_STA.checkState()]
        bold_attributes_df['str']['ol'] = check_enabled[self.checkBox_OL_STR.checkState()]
        bold_attributes_df['blk']['ol'] = check_enabled[self.checkBox_OL_BLK.checkState()]
        bold_attributes_df['tkl']['ol'] = check_enabled[self.checkBox_OL_TKL.checkState()]
        bold_attributes_df['han']['ol'] = check_enabled[self.checkBox_OL_HAN.checkState()]
        bold_attributes_df['gi']['ol'] = check_enabled[self.checkBox_OL_GI.checkState()]
        bold_attributes_df['elu']['ol'] = check_enabled[self.checkBox_OL_ELU.checkState()]
        bold_attributes_df['tec']['ol'] = check_enabled[self.checkBox_OL_TEC.checkState()]

        # DL Section
        bold_attributes_df['ath']['dl'] = check_enabled[self.checkBox_DL_ATH.checkState()]
        bold_attributes_df['spd']['dl'] = check_enabled[self.checkBox_DL_SPD.checkState()]
        bold_attributes_df['dur']['dl'] = check_enabled[self.checkBox_DL_DUR.checkState()]
        bold_attributes_df['we']['dl'] = check_enabled[self.checkBox_DL_WE.checkState()]
        bold_attributes_df['sta']['dl'] = check_enabled[self.checkBox_DL_STA.checkState()]
        bold_attributes_df['str']['dl'] = check_enabled[self.checkBox_DL_STR.checkState()]
        bold_attributes_df['blk']['dl'] = check_enabled[self.checkBox_DL_BLK.checkState()]
        bold_attributes_df['tkl']['dl'] = check_enabled[self.checkBox_DL_TKL.checkState()]
        bold_attributes_df['han']['dl'] = check_enabled[self.checkBox_DL_HAN.checkState()]
        bold_attributes_df['gi']['dl'] = check_enabled[self.checkBox_DL_GI.checkState()]
        bold_attributes_df['elu']['dl'] = check_enabled[self.checkBox_DL_ELU.checkState()]
        bold_attributes_df['tec']['dl'] = check_enabled[self.checkBox_DL_TEC.checkState()]

        # LB Section
        bold_attributes_df['ath']['lb'] = check_enabled[self.checkBox_LB_ATH.checkState()]
        bold_attributes_df['spd']['lb'] = check_enabled[self.checkBox_LB_SPD.checkState()]
        bold_attributes_df['dur']['lb'] = check_enabled[self.checkBox_LB_DUR.checkState()]
        bold_attributes_df['we']['lb'] = check_enabled[self.checkBox_LB_WE.checkState()]
        bold_attributes_df['sta']['lb'] = check_enabled[self.checkBox_LB_STA.checkState()]
        bold_attributes_df['str']['lb'] = check_enabled[self.checkBox_LB_STR.checkState()]
        bold_attributes_df['blk']['lb'] = check_enabled[self.checkBox_LB_BLK.checkState()]
        bold_attributes_df['tkl']['lb'] = check_enabled[self.checkBox_LB_TKL.checkState()]
        bold_attributes_df['han']['lb'] = check_enabled[self.checkBox_LB_HAN.checkState()]
        bold_attributes_df['gi']['lb'] = check_enabled[self.checkBox_LB_GI.checkState()]
        bold_attributes_df['elu']['lb'] = check_enabled[self.checkBox_LB_ELU.checkState()]
        bold_attributes_df['tec']['lb'] = check_enabled[self.checkBox_LB_TEC.checkState()]

        # DB Section
        bold_attributes_df['ath']['db'] = check_enabled[self.checkBox_DB_ATH.checkState()]
        bold_attributes_df['spd']['db'] = check_enabled[self.checkBox_DB_SPD.checkState()]
        bold_attributes_df['dur']['db'] = check_enabled[self.checkBox_DB_DUR.checkState()]
        bold_attributes_df['we']['db'] = check_enabled[self.checkBox_DB_WE.checkState()]
        bold_attributes_df['sta']['db'] = check_enabled[self.checkBox_DB_STA.checkState()]
        bold_attributes_df['str']['db'] = check_enabled[self.checkBox_DB_STR.checkState()]
        bold_attributes_df['blk']['db'] = check_enabled[self.checkBox_DB_BLK.checkState()]
        bold_attributes_df['tkl']['db'] = check_enabled[self.checkBox_DB_TKL.checkState()]
        bold_attributes_df['han']['db'] = check_enabled[self.checkBox_DB_HAN.checkState()]
        bold_attributes_df['gi']['db'] = check_enabled[self.checkBox_DB_GI.checkState()]
        bold_attributes_df['elu']['db'] = check_enabled[self.checkBox_DB_ELU.checkState()]
        bold_attributes_df['tec']['db'] = check_enabled[self.checkBox_DB_TEC.checkState()]

        # K Section
        bold_attributes_df['ath']['k'] = check_enabled[self.checkBox_K_ATH.checkState()]
        bold_attributes_df['spd']['k'] = check_enabled[self.checkBox_K_SPD.checkState()]
        bold_attributes_df['dur']['k'] = check_enabled[self.checkBox_K_DUR.checkState()]
        bold_attributes_df['we']['k'] = check_enabled[self.checkBox_K_WE.checkState()]
        bold_attributes_df['sta']['k'] = check_enabled[self.checkBox_K_STA.checkState()]
        bold_attributes_df['str']['k'] = check_enabled[self.checkBox_K_STR.checkState()]
        bold_attributes_df['blk']['k'] = check_enabled[self.checkBox_K_BLK.checkState()]
        bold_attributes_df['tkl']['k'] = check_enabled[self.checkBox_K_TKL.checkState()]
        bold_attributes_df['han']['k'] = check_enabled[self.checkBox_K_HAN.checkState()]
        bold_attributes_df['gi']['k'] = check_enabled[self.checkBox_K_GI.checkState()]
        bold_attributes_df['elu']['k'] = check_enabled[self.checkBox_K_ELU.checkState()]
        bold_attributes_df['tec']['k'] = check_enabled[self.checkBox_K_TEC.checkState()]

        # P Section
        bold_attributes_df['ath']['p'] = check_enabled[self.checkBox_P_ATH.checkState()]
        bold_attributes_df['spd']['p'] = check_enabled[self.checkBox_P_SPD.checkState()]
        bold_attributes_df['dur']['p'] = check_enabled[self.checkBox_P_DUR.checkState()]
        bold_attributes_df['we']['p'] = check_enabled[self.checkBox_P_WE.checkState()]
        bold_attributes_df['sta']['p'] = check_enabled[self.checkBox_P_STA.checkState()]
        bold_attributes_df['str']['p'] = check_enabled[self.checkBox_P_STR.checkState()]
        bold_attributes_df['blk']['p'] = check_enabled[self.checkBox_P_BLK.checkState()]
        bold_attributes_df['tkl']['p'] = check_enabled[self.checkBox_P_TKL.checkState()]
        bold_attributes_df['han']['p'] = check_enabled[self.checkBox_P_HAN.checkState()]
        bold_attributes_df['gi']['p'] = check_enabled[self.checkBox_P_GI.checkState()]
        bold_attributes_df['elu']['p'] = check_enabled[self.checkBox_P_ELU.checkState()]
        bold_attributes_df['tec']['p'] = check_enabled[self.checkBox_P_TEC.checkState()]

        # Write to csv file
        bold_attributes_df.to_csv(bold_attributes_csv)
        super().accept()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.recruit_tableView.setEditTriggers(QTableView.NoEditTriggers)
        h_header = self.recruit_tableView.horizontalHeader()
        h_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        v_header = self.recruit_tableView.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.ResizeToContents)

        # This can format the text of the entire table view.
        #self.recruit_tableView.setStyleSheet("""
        #                                   color: #123456;
        #                                    """)

        # Disable Recruit Table until a DB table is loaded.
        self.recruit_tableView.setEnabled(False)
        
        
        # Disable all filters by default. They will be enabled when model is loaded.
        self.pushButtonClearRatingsFilters.setText(QCoreApplication.translate("MainWindow", u"&Clear", None))
        self.pushButtonApplyRatingsFilters.setText(QCoreApplication.translate("MainWindow", u"&Apply", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menudata.setTitle(QCoreApplication.translate("MainWindow", u"&Data", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"&Options", None))
        self.actionNew_Season.setText(QCoreApplication.translate("MainWindow", u"&New Season", None))
        self.actionLoad_Season.setText(QCoreApplication.translate("MainWindow", u"&Load Season", None))
        self.actionGrabSeasonData.setText(QCoreApplication.translate("MainWindow", u"&Grab Recruit Data", None))
        self.actionWIS_Credentials.setText(QCoreApplication.translate("MainWindow", u"&WIS Credentials", None))
        self.actionBold_Attributes.setText(QCoreApplication.translate("MainWindow", u"&Bold Attributes", None))
        self.comboBoxPositionFilter.setEnabled(False)
        self.checkBoxHideSigned.setEnabled(False)
        self.checkBoxUndecided.setEnabled(False)
        self.checkBoxWatched.setEnabled(False)
        self.comboBoxMilesFilter.setEnabled(False)
        self.pushButtonApplyRatingsFilters.setEnabled(False)
        self.pushButtonClearRatingsFilters.setEnabled(False)
        self.lineEditConsideringTextSearch.setEnabled(False)
        self.lineEditfilterATH.setEnabled(False)
        self.lineEditfilterBLK.setEnabled(False)
        self.lineEditfilterDUR.setEnabled(False)
        self.lineEditfilterELU.setEnabled(False)
        self.lineEditfilterGI.setEnabled(False)
        self.lineEditfilterHAN.setEnabled(False)
        self.lineEditfilterSPD.setEnabled(False)
        self.lineEditfilterSTA.setEnabled(False)
        self.lineEditfilterSTR.setEnabled(False)
        self.lineEditfilterTEC.setEnabled(False)
        self.lineEditfilterTKL.setEnabled(False)
        self.lineEditfilterWE.setEnabled(False)
        self.lineEditfilterGPA.setEnabled(False)
        
        # Allow only integers to be entered into the ratings filter fields
        self.onlyInt = QIntValidator()
        self.onlyDouble = QDoubleValidator(bottom=0, top=4, decimals=2)
        self.lineEditfilterATH.setValidator(self.onlyInt)
        self.lineEditfilterSPD.setValidator(self.onlyInt)
        self.lineEditfilterDUR.setValidator(self.onlyInt)
        self.lineEditfilterWE.setValidator(self.onlyInt)
        self.lineEditfilterSTA.setValidator(self.onlyInt)
        self.lineEditfilterSTR.setValidator(self.onlyInt)
        self.lineEditfilterBLK.setValidator(self.onlyInt)
        self.lineEditfilterTKL.setValidator(self.onlyInt)
        self.lineEditfilterHAN.setValidator(self.onlyInt)
        self.lineEditfilterGI.setValidator(self.onlyInt)
        self.lineEditfilterELU.setValidator(self.onlyInt)
        self.lineEditfilterTEC.setValidator(self.onlyInt)
        self.lineEditfilterGPA.setValidator(self.onlyDouble)
        
        # UI triggers
        self.actionWIS_Credentials.triggered.connect(self.open_WIS_cred)
        self.actionNew_Season.triggered.connect(self.open_New_Season)
        self.actionLoad_Season.triggered.connect(self.open_Load_Season)
        self.actionGrabSeasonData.triggered.connect(self.open_Grab_Season_Data)
        self.actionBold_Attributes.triggered.connect(self.open_Bold_Attributes)
        self.comboBoxPositionFilter.activated.connect(self.position_filter)
        self.comboBoxMilesFilter.activated.connect(self.miles_filter)
        self.checkBoxHideSigned.stateChanged.connect(self.hide_signed_filter)
        self.checkBoxUndecided.stateChanged.connect(self.undecided_filter)
        self.checkBoxWatched.stateChanged.connect(self.watched_filter)
        self.pushButtonApplyRatingsFilters.clicked.connect(self.apply_ratings_filters)
        self.pushButtonClearRatingsFilters.clicked.connect(self.clear_ratings_filter_fields)
        self.recruit_tableView.clicked.connect(self.tableclickaction)
        
        # Filter data structure used to track which filters are active
        # And then used to build the filter string
        self.string_filter = {
            'pos': "",
            'hide_signed': "",
            'undecided': "",
            'miles': "",
            'ath': "",
            'spd': "",
            'dur': "",
            'we': "",
            'sta': "",
            'str': "",
            'blk': "",
            'tkl': "",
            'han': "",
            'gi': "",
            'elu': "",
            'tec': "",
            'gpa':""
        }
        
        if self.check_stored_creds():
            # Grab coachid from config file
            # Use it to grab active GD teams from coach profile page
            # Then store teams in config.ini
            coachid, user, pwd, config = load_config()
            if coachid != '':
                update_active_teams(coachid)
        else:
            False


    def tableclickaction(self, item):
        print(f"You clicked on column {item.column()} and row {item.row()} with cell data = {item.data()}")
        if item.column() == 0:
            # This is recruit ID field so open link to recruit profile.
            base_url = "https://www.whatifsports.com/gd/RecruitProfile/Ratings.aspx?rid="
            rid = item.data()
            url = QUrl(f"{base_url}{rid}")
            print(f"Opening URL --> {url}")
            logger.info(f"Opening URL --> {url}")
            QDesktopServices.openUrl(url)

        if item.column() == 7:
            # This is hometown so open link to GD Analyst.
            # Need to know correct world and division.
            dbfilename = db.databaseName()
            wis_id_re = re.search(r"(\d{5})", dbfilename)
            wis_id = int(wis_id_re.group(1))
            world = wis_gd_df.world[wis_id]
            division = wis_gd_df.division[wis_id]
            url = QUrl(f"https://gdanalyst.herokuapp.com/world/{world}/{division}/town?town={item.data()}")
            print(f"Opening URL --> {url}")
            logger.info(f"Opening URL --> {url}")
            QDesktopServices.openUrl(url)


    def newFilter(self, model):
        filter = self.getFilterString()
        logger.info(f"New filter string = {filter}")
        model.setFilter(filter)
        model.select()


    def getFilterString(self):
        filter_string_list = []
        separator = " and "
        # Grab all the filter strings that are not empty
        for v in self.string_filter.values():
            if v:
                filter_string_list.append(v)
        l = len(filter_string_list)
        if l == 0:
            return ""
        elif l == 1:
            return filter_string_list[0]
        else:
            filter_string = separator.join(filter_string_list)
            return filter_string

    def clear_ratings_filter_fields(self):
        logger.info("Clear Ratings Filters button was clicked!")
        logger.info(f"Previous filter = {self.getFilterString()}")
        self.lineEditConsideringTextSearch.setText("")
        self.lineEditfilterATH.setText("")
        self.lineEditfilterSPD.setText("")
        self.lineEditfilterWE.setText("")
        self.lineEditfilterDUR.setText("")
        self.lineEditfilterSTA.setText("")
        self.lineEditfilterSTR.setText("")
        self.lineEditfilterBLK.setText("")
        self.lineEditfilterTKL.setText("")
        self.lineEditfilterHAN.setText("")
        self.lineEditfilterGI.setText("")
        self.lineEditfilterELU.setText("")
        self.lineEditfilterTEC.setText("")
        self.lineEditfilterGPA.setText("")
        text_fields = {
            'ath': self.lineEditfilterATH.text(),
            'spd': self.lineEditfilterSPD.text(),
            'we': self.lineEditfilterWE.text(),
            'dur': self.lineEditfilterDUR.text(),
            'sta': self.lineEditfilterSTA.text(),
            'str': self.lineEditfilterSTR.text(),
            'blk': self.lineEditfilterBLK.text(),
            'tkl': self.lineEditfilterTKL.text(),
            'han': self.lineEditfilterHAN.text(),
            'gi': self.lineEditfilterGI.text(),
            'elu': self.lineEditfilterELU.text(),
            'tec': self.lineEditfilterTEC.text(),
            'gpa': self.lineEditfilterGPA.text()
            }
        
        for k, v in text_fields.items():
            self.apply_helper(k, v)
        
        logger.info(f"Clearing Considering filter...")
        self.string_filter['considering'] = ""
        
        self.newFilter(self.model)


    def apply_helper(self, k, v):
            if v:
                logger.info(f"Enabling {k} filter...")
                if k == 'gpa':
                    self.string_filter[k] = f"{k} >= {float(v)}"
                else:
                    self.string_filter[k] = f"{k} >= {int(v)}"
            else:
                logger.info(f"Clearing {k} filter...")
                self.string_filter[k] = ""


    def apply_ratings_filters(self):
        logger.info("Ratings Filters Apply button was clicked!")
        logger.info(f"Previous filter = {self.getFilterString()}")
        text_fields = {
            'ath': self.lineEditfilterATH.text(),
            'spd': self.lineEditfilterSPD.text(),
            'we': self.lineEditfilterWE.text(),
            'dur': self.lineEditfilterDUR.text(),
            'sta': self.lineEditfilterSTA.text(),
            'str': self.lineEditfilterSTR.text(),
            'blk': self.lineEditfilterBLK.text(),
            'tkl': self.lineEditfilterTKL.text(),
            'han': self.lineEditfilterHAN.text(),
            'gi': self.lineEditfilterGI.text(),
            'elu': self.lineEditfilterELU.text(),
            'tec': self.lineEditfilterTEC.text(),
            'gpa': self.lineEditfilterGPA.text()
            }
        
        for k, v in text_fields.items():
            self.apply_helper(k, v)

        # Considering handled separately since it needs different operator
        considering = self.lineEditConsideringTextSearch.text()
        if considering:
            logger.info(f"Enabling Considering filter...")
            self.string_filter['considering'] = f"considering LIKE '%{considering}%'"
        else:
            logger.info(f"Clearing Considering filter...")
            self.string_filter['considering'] = ""

        self.newFilter(self.model)


    def undecided_filter(self):
        state = self.checkBoxUndecided.checkState()
        logger.info(f"Previous filter = {self.getFilterString()}")
        if state == 0:
            logger.info("Clearing Undecided filter...")
            self.string_filter['undecided'] = ""
        elif state == 2:
            logger.info("Enabling Undecided filter...")
            self.string_filter['undecided'] = "considering = 'undecided'"
        else:
            raise Exception
        
        self.newFilter(self.model)


    def watched_filter(self):
        state = self.checkBoxWatched.checkState()
        logger.info(f"Previous filter = {self.getFilterString()}")
        if state == 0:
            logger.info("Clearing Watched filter...")
            self.string_filter['watched'] = ""
        elif state == 2:
            logger.info("Enabling Watched filter...")
            self.string_filter['watched'] = "watched = 1"
        else:
            raise Exception

        self.newFilter(self.model)


    def hide_signed_filter(self):
        state = self.checkBoxHideSigned.checkState()
        logger.info(f"Previous filter = {self.getFilterString()}")
        if state == 0:
            logger.info("Clearing Hide Signed filter...")
            self.string_filter['hide_signed'] = ""
        elif state == 2:
            logger.info("Enabling Hide Signed filter...")
            self.string_filter['hide_signed'] = "signed = 0"
        else:
            raise Exception
        
        self.newFilter(self.model)
    

    def miles_filter(self):
        combo_box_filter = f"miles < {self.comboBoxMilesFilter.currentText()}"
        logger.info(f"Previous filter = {self.getFilterString()}")
        if self.comboBoxMilesFilter.currentText() == "Any":
            logger.info("Clearing Miles Filter...")
            self.string_filter['miles'] = ""
        else:
            logger.info("Adding Miles Filter...")
            self.string_filter['miles'] = combo_box_filter
        
        self.newFilter(self.model)


    def position_filter(self):
        combo_box_filter = f"pos = '{self.comboBoxPositionFilter.currentText()}'"
        logger.info(f"Previous filter = {self.getFilterString()}")
        if self.comboBoxPositionFilter.currentText() == "ALL":
            logger.info("Clearing Position Filter...")
            self.string_filter['pos'] = ""
        else:
            logger.info("Adding Position Filter...")
            self.string_filter['pos'] = combo_box_filter
        
        self.newFilter(self.model)


    def open_WIS_cred(self):
        dialog = WISCred()
        dialog.ui = Ui_WISCredentialDialog()        
        dialog.exec_()
        dialog.show()
        self.check_stored_creds()


    def open_New_Season(self):
        dialog = NewSeason()
        dialog.ui = Ui_DialogNewSeason()
        dialog.exec_()
        dialog.show()
        logger.info("Exiting New Season dialog")
        logger.info(f"database name = {db.databaseName()}")
        if db.databaseName() != "":
            self.setWindowTitle(f"{window_title} - {db.databaseName()}")
            self.actionGrabSeasonData.setEnabled(True)
            self.loadModel()
            
            
    def open_Load_Season(self):
        dialog = LoadSeason()
        dialog.ui = Ui_DialogLoadSeason()
        dialog.exec_()
        dialog.show()
        logger.info("Exiting Load Season dialog")
        logger.info(f"database name = {db.databaseName()}")
        if db.databaseName() != "":
            self.setWindowTitle(f"{window_title} - {db.databaseName()}")
            self.actionGrabSeasonData.setEnabled(True)
            self.loadModel()
            

    def open_Grab_Season_Data(self):
        dialog = GrabSeasonData()
        dialog.ui = Ui_WidgetGrabSeasonData()
        dialog.exec_()
        dialog.show()
        logger.info("Exiting Grab Season Data dialog")
        logger.info(f"database name = {db.databaseName()}")
        if db.databaseName() != "":
            self.loadModel()


    def open_Bold_Attributes(self):
        logger.debug("Entering Bold Attributes dialog")
        dialog = BoldAttributes()
        dialog.ui = Ui_DialogBoldAttributes()
        dialog.exec_()
        dialog.show() 
        logger.debug("Exiting Bold Attributes dialog")
        if db.databaseName() != "":
            self.loadModel()


    def check_stored_creds(self):
        coachid, user, pwd, config = load_config()
        if user == '' or pwd == '':
            self.actionNew_Season.setEnabled(False)
            self.actionLoad_Season.setEnabled(False)
            return False
        else:
            self.actionNew_Season.setEnabled(True)
            self.actionLoad_Season.setEnabled(True)
            return True
   

    def loadModel(self):
        self.model = TableModel()
        # initializeModel(self.model)
        self.recruit_tableView.setModel(self.model)
        self.recruit_tableView.setEnabled(True)
        self.recruit_tableView.setColumnHidden(30, True)
        self.comboBoxPositionFilter.setEnabled(True)
        self.checkBoxHideSigned.setEnabled(True)
        self.checkBoxUndecided.setEnabled(True)
        self.checkBoxWatched.setEnabled(True)
        self.comboBoxMilesFilter.setEnabled(True)
        self.pushButtonApplyRatingsFilters.setEnabled(True)
        self.pushButtonClearRatingsFilters.setEnabled(True)
        self.lineEditConsideringTextSearch.setEnabled(True)
        self.lineEditfilterATH.setEnabled(True)
        self.lineEditfilterBLK.setEnabled(True)
        self.lineEditfilterDUR.setEnabled(True)
        self.lineEditfilterELU.setEnabled(True)
        self.lineEditfilterGI.setEnabled(True)
        self.lineEditfilterHAN.setEnabled(True)
        self.lineEditfilterSPD.setEnabled(True)
        self.lineEditfilterSTA.setEnabled(True)
        self.lineEditfilterSTR.setEnabled(True)
        self.lineEditfilterTEC.setEnabled(True)
        self.lineEditfilterTKL.setEnabled(True)
        self.lineEditfilterWE.setEnabled(True)
        self.lineEditfilterGPA.setEnabled(True)

def load_config():
    config = configparser.ConfigParser()
    configfile = config.read('./config.ini')
    if  configfile == []:
        logger.info("config.ini file not found")
        logger.info("Creating config.ini with WISCreds section")
        config['WISCreds'] = {
                        'coachid' : '',
                        'username' : '',
                        'password' : ''
                        }
    else:
        logger.info("config.ini file found")
        # If config file exists but does not contain WISCreds section, add it
        if config.has_section('WISCreds'):
            logger.info("Config WISCreds section found")
            if not config.has_option('WISCreds','coachid'):
                logger.info("Adding missing coachid option to WISCreds section")
                config['WISCreds']['coachid'] = ''
            if not config.has_option('WISCreds','username'):
                logger.info("Adding missing username option to WISCreds section")
                config['WISCreds']['username'] = ''
            if not config.has_option('WISCreds','password'):
                logger.info("Adding missing password option to WISCreds section")
                config['WISCreds']['password'] = ''
        else:
            logger.info("Adding missing WISCreds section")
            config['WISCreds'] = {
                        'coachid' : '',
                        'username' : '',
                        'password' : ''
                        }
    
    with open("./config.ini", 'w') as file:
            config.write(file)


    coachid = config['WISCreds']['coachid']
    username = config['WISCreds']['username']
    password = config['WISCreds']['password']

    return coachid, username, password, config


def update_active_teams(coachid):
    cid, user, pwd, config = load_config()
    config.remove_section('Schools')
    config.add_section('Schools')
    requests_session = requests.Session()
    coach_profile_page = requests_session.get(f"https://www.whatifsports.com/account/UserProfile/Games/GridironDynasty/?user={coachid}")
    if coach_profile_page.status_code == 200:
        logger.info(f"Request to grab {coachid} profile page successful.")
        coach_profile_page_soup = BeautifulSoup(coach_profile_page.content, "lxml")
        active_teams_list = coach_profile_page_soup.find("ul", class_="UnorderedItemList")
        active_teams = active_teams_list.find_all("li")
        if len(active_teams) != 0:
            logger.info(f"{coachid} has {len(active_teams)} active GD teams.")
            for each in active_teams:
                team_span = each.find("span", class_="teamName")
                team_a_link = team_span.find("a")
                team_name = team_a_link.text
                team_href = team_a_link.attrs['href']
                team_href_re = re.search(r'(\d{5})', team_href)
                teamid = f"{team_href_re.group(1)}"
                world_span = each.find("span", class_="world")
                world_a_link = world_span.find("a")
                world_name = world_a_link.text
                config.set('Schools',teamid,f"{team_name} ({world_name})")
            
        else:
            logger.error(f"{coachid} does not have any active GD teams!")
    
        with open("./config.ini", 'w') as file:
            config.write(file)
    elif coach_profile_page.status_code == 503:
        logger.error(f"Request to grab {coachid} profile page was NOT successful. Please check coach ID.")


class TableModel(QSqlTableModel):
    def __init__(self, *args, **kwargs):
        super(TableModel, self).__init__(*args, **kwargs)
        logger.debug("-> TableModel.__init__:")
        self.setTable('recruits')
        # model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.select()
        
        # Dict to map column headers to column ID
        col_head = {
            'ID': 0,
            'Name': 1,
            'Pos': 2,
            'Height': 3,
            'Weight': 4,
            'Rating': 5,
            'Rank': 6,
            'Hometown': 7,
            'Miles': 8,
            'Considering': 9,
            'ATH': 10,
            'SPD': 11,
            'DUR': 12,
            'WE': 13,
            'STA': 14,
            'STR': 15,
            'BLK': 16,
            'TKL': 17,
            'HAN': 18,
            'GI': 19,
            'ELU': 20,
            'TEC': 21,
            'R1': 22,
            'R2': 23,
            'R3': 24,
            'R4': 25,
            'R5': 26,
            'R6': 27,
            'GPA': 28,
            'Pot': 29,
            'Signed': 30,
            'Watched': 31
        }
        
        self.setHeaderData(col_head['ID'], Qt.Horizontal, "ID")
        self.setHeaderData(col_head['Name'], Qt.Horizontal, "Name")
        self.setHeaderData(col_head['Pos'], Qt.Horizontal, "Pos")
        self.setHeaderData(col_head['Height'], Qt.Horizontal, "Height")
        self.setHeaderData(col_head['Weight'], Qt.Horizontal, "Weight")
        self.setHeaderData(col_head['Rating'], Qt.Horizontal, "Rating")
        self.setHeaderData(col_head['Rank'], Qt.Horizontal, "Rank")
        self.setHeaderData(col_head['Hometown'], Qt.Horizontal, "Hometown")
        self.setHeaderData(col_head['Miles'], Qt.Horizontal, "Miles")
        self.setHeaderData(col_head['Considering'], Qt.Horizontal, "Considering")
        self.setHeaderData(col_head['ATH'], Qt.Horizontal, "ATH")
        self.setHeaderData(col_head['SPD'], Qt.Horizontal, "SPD")
        self.setHeaderData(col_head['DUR'], Qt.Horizontal, "DUR")
        self.setHeaderData(col_head['WE'], Qt.Horizontal, "WE")
        self.setHeaderData(col_head['STA'], Qt.Horizontal, "STA")
        self.setHeaderData(col_head['STR'], Qt.Horizontal, "STR")
        self.setHeaderData(col_head['BLK'], Qt.Horizontal, "BLK")
        self.setHeaderData(col_head['TKL'], Qt.Horizontal, "TKL")
        self.setHeaderData(col_head['HAN'], Qt.Horizontal, "HAN")
        self.setHeaderData(col_head['GI'], Qt.Horizontal, "GI")
        self.setHeaderData(col_head['ELU'], Qt.Horizontal, "ELU")
        self.setHeaderData(col_head['TEC'], Qt.Horizontal, "TEC")
        self.setHeaderData(col_head['R1'], Qt.Horizontal, "R1")
        self.setHeaderData(col_head['R2'], Qt.Horizontal, "R2")
        self.setHeaderData(col_head['R3'], Qt.Horizontal, "R3")
        self.setHeaderData(col_head['R4'], Qt.Horizontal, "R4")
        self.setHeaderData(col_head['R5'], Qt.Horizontal, "R5")
        self.setHeaderData(col_head['R6'], Qt.Horizontal, "R6")
        self.setHeaderData(col_head['GPA'], Qt.Horizontal, "GPA")
        self.setHeaderData(col_head['Pot'], Qt.Horizontal, "Pot")
        self.setHeaderData(col_head['Signed'], Qt.Horizontal, "Signed")
        self.setHeaderData(col_head['Watched'], Qt.Horizontal, "Watched")
        self.info()
        logger.debug("<- TableModel.__init__")

        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            self.checkmarkicon = f"{Path(sys._MEIPASS) / 'images' / 'checkmark_1.png'}"
            self.x_icon = f"{Path(sys._MEIPASS) / 'images' / 'x_icon.png'}"
        #checkmarkicon = f"{sys._MEIPASS}/images/checkmark_1.png"
        else:
            self.checkmarkicon = f"./images/checkmark_1.png"
            self.x_icon = f"./images/x_icon.png"

        # Dataframe to be used with Bold Attributes
        data = [[col_head['ATH'], col_head['SPD'], col_head['DUR'], col_head['WE'],
                col_head['STA'], col_head['STR'], col_head['BLK'], col_head['TKL'],
                col_head['HAN'], col_head['GI'], col_head['ELU'], col_head['TEC']]
                ]
        index_names = ['qb', 'rb', 'wr', 'te', 'ol', 'dl', 'lb', 'db', 'k', 'p']
        column_headers = ['ath', 'spd', 'dur', 'we', 'sta', 'str', 'blk', 'tkl', 'han', 'gi', 'elu', 'tec']
        column_mapping_df = pd.DataFrame(data, columns=column_headers, index=index_names)

        # Multiple bold attributes dataframe with column mapping dataframe
        # End result should be which column IDs to include in a list
        # which can then be used to make conditional formatting
        bold_mapping = bold_attributes_df.mul(column_mapping_df)
        self.qb_bold = set(bold_mapping.loc['qb'])
        self.qb_bold.discard(0)
        self.rb_bold = set(bold_mapping.loc['rb'])
        self.rb_bold.discard(0)
        self.wr_bold = set(bold_mapping.loc['wr'])
        self.wr_bold.discard(0)
        self.te_bold = set(bold_mapping.loc['te'])
        self.te_bold.discard(0)
        self.ol_bold = set(bold_mapping.loc['ol'])
        self.ol_bold.discard(0)
        self.dl_bold = set(bold_mapping.loc['dl'])
        self.dl_bold.discard(0)
        self.lb_bold = set(bold_mapping.loc['lb'])
        self.lb_bold.discard(0)
        self.db_bold = set(bold_mapping.loc['db'])
        self.db_bold.discard(0)
        self.k_bold = set(bold_mapping.loc['k'])
        self.k_bold.discard(0)
        self.p_bold = set(bold_mapping.loc['p'])
        self.p_bold.discard(0)

    def info(self):
        logger.debug("     -> info")
        logger.debug(f"         TableModel tables inside : {self.database().tables()}")
        logger.debug(f"         TableModel self.db       : {self.database()}")
        logger.debug(f"         TableModel self.Table    : {self.tableName()}")
        logger.debug(f"         TableModel self.rowCount : {self.rowCount()}")
        logger.debug(f"         TableModel self.lastEror : {self.lastError().text()}")
        logger.debug("     <- info")

    def data(self, index, role):
        if role == Qt.ForegroundRole:
            # Format blue text for Recruit ID and Hometown columns to indicate hyperlinks
            if index.column() in [0,7]:
                return QColor('darkblue')

            # Format potential in different colors
            if index.column() == 29:
                value = super(TableModel, self).data(index)
                if value == '0-VL':
                    return QColor('darkred')
                elif value == '1-L':
                    return QColor('peru')
                elif value == '2-A' or value == '?':
                    return QColor('black')
                elif value == '3-H':
                    return QColor('blue')
                elif value == '4-VH':
                    return QColor('darkgreen')

        # Right Align most columns
        if role == Qt.TextAlignmentRole:
            if index.column() in [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31]:
                return Qt.AlignRight

        # Format columns with float data to 1 decimal point
        if role == Qt.DisplayRole:
            if index.column() in [22, 23, 24, 25, 26, 27, 28]:
                value = super(TableModel, self).data(index)
                return "%.1f" % value

        # Add a checkmark icon if a player is watched
        if role == Qt.DecorationRole:
            if index.column() in [31]:
                value = super(TableModel, self).data(index)
                if value == 1:
                    return QIcon(self.checkmarkicon)

        # Format background of the entire row to light gray if a player is signed
        if role == Qt.BackgroundRole:
            if super(TableModel, self).data(self.index(index.row(), 30), Qt.DisplayRole) == 1:
                return QBrush(Qt.lightGray)

        # Section to Bold the text for the critical attributes for each position
        if role == Qt.FontRole:
            position = super(TableModel, self).data(self.index(index.row(), 2), Qt.DisplayRole)
            font = QFont()
            font.setBold(True)
            font.setPointSize(11)
            if position == "QB":
                if index.column() in self.qb_bold:
                    return font
            if position == "RB":
                if index.column() in self.rb_bold:
                    return font
            if position == "WR":
                if index.column() in self.wr_bold:
                    return font
            if position == "TE":
                if index.column() in self.te_bold:
                    return font
            if position == "OL":
                if index.column() in self.ol_bold:
                    return font
            if position == "DL":
                if index.column() in self.dl_bold:
                    return font
            if position == "LB":
                if index.column() in self.lb_bold:
                    return font
            if position == "DB":
                if index.column() in self.db_bold:
                    return font
            if position == "K":
                if index.column() in self.k_bold:
                    return font
            if position == "P":
                if index.column() in self.p_bold:
                    return font


        return QSqlTableModel.data(self, index, role)
    
    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False
        else:
            return QSqlTableModel.setData(self, index, value, role)


    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        else:
            return QSqlTableModel.flags(self, index)


if __name__ == "__main__":
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        logger.info('running in a PyInstaller bundle')
    else:
        logger.info('running in a normal Python process')
    print(f"Running {window_title} . . . ")
    logger.info(f"{window_title}")
    logger.info(f"Platform System = {platform.system()}")
    logger.info(f"Platform System Alias= {platform.system_alias(platform.system(),platform.release(),platform.version())}")
    logger.info(f"Platform Win32 Version = {platform.win32_ver()}")
    logger.info(f"Platform Win32 Edition = {platform.win32_edition()}")
    logger.info(f"Platform Architecture = {platform.architecture()}")
    logger.info(f"Platform Machine = {platform.machine()}")
    logger.info(f"Platform Processor = {platform.processor()}")
    
    # Bold Attributes Config
    bold_attributes_csv = "./bold_attributes.csv" 
    if path.exists(bold_attributes_csv):
        logger.debug("bold_attributes_csv file path found.")
        try:
            bold_attributes_df = pd.read_csv(bold_attributes_csv, header = 0, index_col=0)
        except Exception as e:
            logger.error(f"Exception ({e}) reading bold_attributes.csv file.")
    else:
        logger.debug("bold_attributes_csv file path NOT found.")
        logger.debug("Creating bold_attributes.csv file...")

        data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        index_names = ['qb', 'rb', 'wr', 'te', 'ol', 'dl', 'lb', 'db', 'k', 'p']
        column_headers = ['ath', 'spd', 'dur', 'we', 'sta', 'str', 'blk', 'tkl', 'han', 'gi', 'elu', 'tec']
        bold_attributes_df = pd.DataFrame(data, columns=column_headers, index=index_names)
        bold_attributes_df.to_csv(bold_attributes_csv)

    # Configure for High DPI
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    app = QApplication(sys.argv)
    
        
    # Default database connection
    db = QSqlDatabase.addDatabase('QSQLITE')
    # Database connection to be used by thread
    db_t = QSqlDatabase.addDatabase('QSQLITE', connectionName='worker_connection')
    mw = MainWindow()
    mw.setWindowTitle(window_title)
    mw.show() 
    sys.exit(app.exec_())