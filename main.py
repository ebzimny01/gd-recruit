version = "0.2.1"
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

from mypackages.grab_season_data_widget import Ui_WidgetGrabSeasonData
import os
import datetime, time
import requests
from playwright.async_api import async_playwright
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *
from mypackages.mainwindow_ui import Ui_MainWindow
from mypackages.wis_cred_dialog import Ui_WISCredentialDialog
from mypackages.new_season_dialog import Ui_DialogNewSeason
from mypackages.load_season_dialog import Ui_DialogLoadSeason
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
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    gdr_csv = f"{Path(sys._MEIPASS) / 'data' / 'gdr.csv'}"
else:
    gdr_csv = f"./data/gdr.csv"
logger.info(f"gdr.csv path is = {gdr_csv}")
wis_gd_df = pd.read_csv(gdr_csv, header=0, index_col=0)



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
            # After grabbing all Recruit IDs and storing in DB
            # Now need to grab all static data
            logger.info("Running query_Recruit_IDs after wis_browser...")
            rids = query_Recruit_IDs("all", db_t)
            rids_length = len(rids)
            logger.info(f"Number of recruits to process = {rids_length}")
            print(f"Number of recruits to process = {rids_length}")
            openDB(db_t)
            queryUpdate = QSqlQuery(db_t)
            queryUpdate.prepare("UPDATE recruits "
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
            
            #Thread progress signaling that Grab Recruit Static Data is starting
            i = 1000
            logger.info(f"before emit {i}...")
            self.progress.emit(i, rids_length)

            with Bar('Initializing Recruit Static Data...', max=rids_length) as bar:
                for rid in rids:
                    r = rid[0]
                    position = rid[1]
                    recruitpage = requests_session.get(f"https://www.whatifsports.com/gd/RecruitProfile/Ratings.aspx?rid={r}")
                    recruitpage_soup = BeautifulSoup(recruitpage.content, "lxml")
                    recruit_ratings_section = recruitpage_soup.find(class_="ratingsDisplayCtl")
                    recruit_ratings_values = recruit_ratings_section.find_all(class_="value")
                    gpa_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_gpa")
                    gpa = float(gpa_section.text)
                    ath = int(recruit_ratings_values[0].text)
                    spd = int(recruit_ratings_values[1].text)
                    dur = int(recruit_ratings_values[2].text)
                    we = int(recruit_ratings_values[3].text)
                    sta = int(recruit_ratings_values[4].text)
                    strength = int(recruit_ratings_values[5].text)
                    blk = int(recruit_ratings_values[6].text)
                    tkl = int(recruit_ratings_values[7].text)
                    han = int(recruit_ratings_values[8].text)
                    gi = int(recruit_ratings_values[9].text)
                    elu = int(recruit_ratings_values[10].text)
                    tec = int(recruit_ratings_values[11].text)
                    r_ratings = [ath, spd, dur, we, sta, strength, blk, tkl, han, gi, elu, tec]
                    role_rating = self.calculate_role_rating(position, r_ratings)
                    queryUpdate.bindValue(":ath", ath)
                    queryUpdate.bindValue(":spd", spd)
                    queryUpdate.bindValue(":dur", dur)
                    queryUpdate.bindValue(":we", we)
                    queryUpdate.bindValue(":sta", sta)
                    queryUpdate.bindValue(":str", strength)
                    queryUpdate.bindValue(":blk", blk)
                    queryUpdate.bindValue(":tkl", tkl)
                    queryUpdate.bindValue(":han", han)
                    queryUpdate.bindValue(":gi", gi)
                    queryUpdate.bindValue(":elu", elu)
                    queryUpdate.bindValue(":tec", tec)
                    queryUpdate.bindValue(":r1", float(role_rating['r1']))
                    queryUpdate.bindValue(":r2", float(role_rating['r2']))
                    queryUpdate.bindValue(":r3", float(role_rating['r3']))
                    queryUpdate.bindValue(":r4", float(role_rating['r4']))
                    queryUpdate.bindValue(":r5", float(role_rating['r5']))
                    queryUpdate.bindValue(":r6", float(role_rating['r6']))
                    queryUpdate.bindValue(":gpa", gpa)
                    queryUpdate.bindValue(":id", r)
                    
                    if not queryUpdate.exec_():
                        logQueryError(queryUpdate)
                                        
                    # Thread progress signal for Grab Recruit Static Data
                    i += 1
                    self.progress.emit(i, rids_length)
                    bar.next()

            queryUpdate.finish()
            db_t.close()
        else:
            # Implies there was an error authenticating to WIS
            self.progress.emit(999999,1)

        self.finished.emit()


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

        recruit_role_ratings = {
            'r1': round(np.dot(rating_formulas[pos]['r1'], ratings)/100,1),
            'r2': round(np.dot(rating_formulas[pos]['r2'], ratings)/100,1),
            'r3': round(np.dot(rating_formulas[pos]['r3'], ratings)/100,1),
            'r4': round(np.dot(rating_formulas[pos]['r4'], ratings)/100,1),
            'r5': round(np.dot(rating_formulas[pos]['r5'], ratings)/100,1),
            'r6': round(np.dot(rating_formulas[pos]['r6'], ratings)/100,1)
        }

        return recruit_role_ratings


class UpdateConsideringWorker(QObject):
    finished = Signal()
    progress = Signal(int, int)
        
    def run(self):
        """Long-running Initialize Recruit task goes here."""
        logger.info("Started UpdateConsideringWorker.run function")
        # Thread signaling start
        self.progress.emit(0,1)

        i = 0
        db_t.setDatabaseName(db.databaseName())
        rids_unsigned = query_Recruit_IDs("unsigned", db_t)
        rids_unsigned_length = len(rids_unsigned)
        
        openDB(db_t)
        queryUpdateConsidering = QSqlQuery(db_t)
        queryUpdateConsidering.prepare("UPDATE recruits "
                                        "SET considering = :considering, "
                                        "signed = :signed "
                                        "WHERE id = :id")

        requests_session = requests.Session()
        with Bar('Update Recruits Considering...', max=rids_unsigned_length) as bar:            
            logger.info(f"Updating {rids_unsigned_length} unsigned recruits . . . ")
            for rid in rids_unsigned:
                recruitpage = requests_session.get(f"https://www.whatifsports.com/gd/RecruitProfile/Considering.aspx?rid={rid}")
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
                        # print(considering)
                queryUpdateConsidering.bindValue(":considering", considering[:-1]) # remove newline at end
                queryUpdateConsidering.bindValue(":signed", signed)
                queryUpdateConsidering.bindValue(":id", rid)
                if not queryUpdateConsidering.exec_():
                    logQueryError(queryUpdateConsidering)
                                    
                # Increment counter and progress bar
                i += 1
                self.progress.emit(i, rids_unsigned_length)
                bar.next()

        logger.info(f"Finished updating {rids_unsigned_length} unsigned recruits.")
        queryUpdateConsidering.finish()
        db_t.close()
        self.finished.emit()


class MarkRecruitsWorker(QObject):
    finished = Signal()
    progress = Signal(int)
    
    def run(self):
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
                    potential = columns[9].text
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
                    potential = columns[9].text
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
        self.rids_all = query_Recruit_IDs("all", db)
        self.rids_all_length = len(self.rids_all)
        if self.rids_all_length == 0:
            self.pushButtonInitializeRecruits.setText(QCoreApplication.translate("MainWindow", u"&Initialize Recruits", None))
            self.pushButtonUpdateConsideringSigned.setVisible(False)
            self.pushButtonMarkRecruitsFromWatchlist.setVisible(False)
        else:
            self.pushButtonMarkRecruitsFromWatchlist.setEnabled(True)
            self.labelRecruitsInitialized.setText(f"Recruits Initialized = {self.rids_all_length}")
            self.labelRecruitsInitialized.setStyleSheet(u"color: rgb(0, 0, 255);")
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
        self.pushButtonUpdateConsideringSigned.clicked.connect(self.runUpdateConsideringJob)
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
        self.thread.finished.connect(
            lambda: self.pushButtonInitializeRecruits.setEnabled(True)
        )

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
    

    def runUpdateConsideringJob(self):
        logger.info("Button Pressed: Update Considering / Signed")
        # Step 1: Create a QThread object
        self.thread = QThread()
        # Step 2: Create a worker object
        self.worker = UpdateConsideringWorker()
        # Step 3: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 4: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportUpdateConsideringProgress)
        # Step 6: Start the thread
        self.thread.start()
        # Final resets
        self.pushButtonInitializeRecruits.setEnabled(False)
        self.pushButtonMarkRecruitsFromWatchlist.setEnabled(False)
        self.pushButtonUpdateConsideringSigned.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.pushButtonUpdateConsideringSigned.setEnabled(True)
        )


    def reportUpdateConsideringProgress(self, n, m):
        # print(f"n = {n}\nm = {m}")
        if n == 0:
            self.progressBarMarkWatchlist.setVisible(False)
            mw.statusbar.showMessage(f"Updating {m} recruits . . . ")
            self.progressBarUpdateConsidering.setVisible(True)
        if n > 0 and n <= m:
            self.labelUpdateProgressBarMax.setVisible(True)
            self.labelUpdateProgressBarMax.setText(f"of {m}")
            self.progressBarUpdateConsidering.setRange(0, m)
            self.progressBarUpdateConsidering.setValue(n)
            # self.progressBarUpdateConsidering.value()
        if n == m:
            self.pushButtonInitializeRecruits.setEnabled(True)
            self.pushButtonUpdateConsideringSigned.setEnabled(True)
            self.pushButtonMarkRecruitsFromWatchlist.setEnabled(True)
            mw.statusbar.showMessage(f"Finished updating {m} recruits.")


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
        self.actionNew_Season.setText(QCoreApplication.translate("MainWindow", u"&New Season", None))
        self.actionLoad_Season.setText(QCoreApplication.translate("MainWindow", u"&Load Season", None))
        self.actionGrabSeasonData.setText(QCoreApplication.translate("MainWindow", u"&Grab Recruit Data", None))
        self.actionWIS_Credentials.setText(QCoreApplication.translate("MainWindow", u"&WIS Credentials", None))
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
                    self.string_filter[k] = f"{k} > {float(v)}"
                else:
                    self.string_filter[k] = f"{k} > {int(v)}"
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
        self.model = QSqlTableModel()
        initializeModel(self.model)
        self.recruit_tableView.setModel(self.model)
        self.recruit_tableView.setEnabled(True)
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


def initializeModel(model):
   model.setTable('recruits')
   # model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
   model.select()
   model.setHeaderData(0, Qt.Horizontal, "ID")
   model.setHeaderData(1, Qt.Horizontal, "Name")
   model.setHeaderData(2, Qt.Horizontal, "Pos")
   model.setHeaderData(3, Qt.Horizontal, "Height")
   model.setHeaderData(4, Qt.Horizontal, "Weight")
   model.setHeaderData(5, Qt.Horizontal, "Rating")
   model.setHeaderData(6, Qt.Horizontal, "Rank")
   model.setHeaderData(7, Qt.Horizontal, "Hometown")
   model.setHeaderData(8, Qt.Horizontal, "Miles")
   model.setHeaderData(9, Qt.Horizontal, "Considering")
   model.setHeaderData(10, Qt.Horizontal, "ATH")
   model.setHeaderData(11, Qt.Horizontal, "SPD")
   model.setHeaderData(12, Qt.Horizontal, "DUR")
   model.setHeaderData(13, Qt.Horizontal, "WE")
   model.setHeaderData(14, Qt.Horizontal, "STA")
   model.setHeaderData(15, Qt.Horizontal, "STR")
   model.setHeaderData(16, Qt.Horizontal, "BLK")
   model.setHeaderData(17, Qt.Horizontal, "TKL")
   model.setHeaderData(18, Qt.Horizontal, "HAN")
   model.setHeaderData(19, Qt.Horizontal, "GI")
   model.setHeaderData(20, Qt.Horizontal, "ELU")
   model.setHeaderData(21, Qt.Horizontal, "TEC")
   model.setHeaderData(22, Qt.Horizontal, "R1")
   model.setHeaderData(23, Qt.Horizontal, "R2")
   model.setHeaderData(24, Qt.Horizontal, "R3")
   model.setHeaderData(25, Qt.Horizontal, "R4")
   model.setHeaderData(26, Qt.Horizontal, "R5")
   model.setHeaderData(27, Qt.Horizontal, "R6")
   model.setHeaderData(28, Qt.Horizontal, "GPA")
   model.setHeaderData(29, Qt.Horizontal, "Pot")
   model.setHeaderData(30, Qt.Horizontal, "Signed")
   model.setHeaderData(31, Qt.Horizontal, "Watched")


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