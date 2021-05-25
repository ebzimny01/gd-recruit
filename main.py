version = "0.5.1"
window_title = f"GD Recruit Assistant Beta ({version})"
from asyncio.windows_events import NULL
import sys
import platform
from loguru import logger
import os, os.path
from os import path
from queue import Queue
import datetime, time
import requests
import traceback
import sqlite3
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
from mypackages.role_ratings_dialog import Ui_DialogRoleRatings
from mypackages.role_ratings_update_db import Ui_DialogRoleRatingUpdateDB_Progress
from mypackages.advanced_config_options import Ui_DialogAdvancedConfigOptions
from mypackages.mark_watchlist_potential_dialog import Ui_DialogMarkWatchlistPotential
from mypackages.update_considering_dialog import Ui_DialogUpdateConsidering
from mypackages.show_columns import Ui_DialogShowColumns
from mypackages.world_lookup import wid_world_list
from mypackages.browser import *
import mypackages.config as myconfig
import configparser
from progress.bar import Bar
import pandas as pd
import numpy as np
from pathlib import Path



# https://stackoverflow.com/questions/61316258/how-to-overwrite-qdialog-accept




def logQueryError(query):
    logger.error(f"{datetime.datetime.now()}: query: last error: {query.lastError()}")
    logger.error(f"{datetime.datetime.now()}: query: last query: {query.lastQuery()}")


def query_Recruit_IDs(type, dbconn):
    openDB(dbconn)
    logger.info(f"query_Recruit_IDs: Database name = {dbconn.databaseName()} Connection name = {dbconn.connectionName()} Tables = {dbconn.tables()}")
    rids = []
    if 'recruits' in dbconn.tables():
        logger.debug("Found table 'recruits' in database")
        queryRecruitIDs = QSqlQuery(dbconn)
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
        elif type == "update_role_ratings":
            if not queryRecruitIDs.exec_("Select id,pos,ath,spd,dur,we,sta,str,blk,tkl,han,gi,elu,tec FROM recruits"):
                logQueryError(queryRecruitIDs)
            while queryRecruitIDs.next():
                r = queryRecruitIDs.value('id')
                pos = queryRecruitIDs.value('pos')
                ath = queryRecruitIDs.value('ath')
                spd = queryRecruitIDs.value('spd')
                dur = queryRecruitIDs.value('dur')
                we = queryRecruitIDs.value('we')
                sta = queryRecruitIDs.value('sta')
                strength = queryRecruitIDs.value('str')
                blk = queryRecruitIDs.value('blk')
                tkl = queryRecruitIDs.value('tkl')
                han = queryRecruitIDs.value('han')
                gi = queryRecruitIDs.value('gi')
                elu = queryRecruitIDs.value('elu')
                tec = queryRecruitIDs.value('tec')
                rids.append([r, pos, ath, spd, dur, we, sta, strength, blk, tkl, han, gi, elu, tec])
        queryRecruitIDs.finish()
        logger.info(f"Closing {dbconn.databaseName()}...")
        dbconn.close()
    else:
        logger.debug("Table 'recruits' does not exist in database")
    logger.info("End of query_Recruit_IDs function")
    return rids


def queue_rid_urls(q=Queue(), t=str()):
        rids = query_Recruit_IDs(t, db)
        if t == "all":
            myconfig.rids_all_length = len(rids)
            logger.info(f"All recruits = {myconfig.rids_unsigned_length}")
            url_base = "https://www.whatifsports.com/gd/RecruitProfile/Ratings.aspx?rid="
            for each in rids:
                rid = each[0]
                position = each[1]
                recruit = (rid, position, f"{url_base}{rid}")
                logger.debug(f"Queuing ({t}): {recruit}")
                q.put(recruit)
        elif t == "unsigned":
            myconfig.rids_unsigned_length = len(rids)
            logger.info(f"Unsigned recruits = {myconfig.rids_unsigned_length}")
            url_base = "https://www.whatifsports.com/gd/RecruitProfile/Considering.aspx?rid="
            for rid in rids:
                recruit = (rid, f"{url_base}{rid}")
                logger.debug(f"Queuing ({t}): {recruit}")
                q.put(recruit)
            


def calculate_role_rating(ratings):
        attributes = ['ath', 'spd', 'dur', 'we', 'sta', 'str', 'blk', 'tkl', 'han', 'gi', 'elu', 'tec']
        rating_formulas = {
            'QB': {
                'r1': list(myconfig.role_ratings_df.loc['qbr1'][attributes]),
                'r2': list(myconfig.role_ratings_df.loc['qbr2'][attributes]),
                'r3': list(myconfig.role_ratings_df.loc['qbr3'][attributes]),
                'r4': list(myconfig.role_ratings_df.loc['qbr4'][attributes]),
                'r5': list(myconfig.role_ratings_df.loc['qbr5'][attributes]),
                'r6': list(myconfig.role_ratings_df.loc['qbr6'][attributes])
            },
            'RB': {
                'r1': list(myconfig.role_ratings_df.loc['rbr1'][attributes]),
                'r2': list(myconfig.role_ratings_df.loc['rbr2'][attributes]),
                'r3': list(myconfig.role_ratings_df.loc['rbr3'][attributes]),
                'r4': list(myconfig.role_ratings_df.loc['rbr4'][attributes]),
                'r5': list(myconfig.role_ratings_df.loc['rbr5'][attributes]),
                'r6': list(myconfig.role_ratings_df.loc['rbr6'][attributes])
            },
            'WR': {
                'r1': list(myconfig.role_ratings_df.loc['wrr1'][attributes]),
                'r2': list(myconfig.role_ratings_df.loc['wrr2'][attributes]),
                'r3': list(myconfig.role_ratings_df.loc['wrr3'][attributes]),
                'r4': list(myconfig.role_ratings_df.loc['wrr4'][attributes]),
                'r5': list(myconfig.role_ratings_df.loc['wrr5'][attributes]),
                'r6': list(myconfig.role_ratings_df.loc['wrr6'][attributes])
            },
            'TE': {
                'r1': list(myconfig.role_ratings_df.loc['ter1'][attributes]),
                'r2': list(myconfig.role_ratings_df.loc['ter2'][attributes]),
                'r3': list(myconfig.role_ratings_df.loc['ter3'][attributes]),
                'r4': list(myconfig.role_ratings_df.loc['ter4'][attributes]),
                'r5': list(myconfig.role_ratings_df.loc['ter5'][attributes]),
                'r6': list(myconfig.role_ratings_df.loc['ter6'][attributes])
            },
            'OL': {
                'r1': list(myconfig.role_ratings_df.loc['olr1'][attributes]),
                'r2': list(myconfig.role_ratings_df.loc['olr2'][attributes]),
                'r3': list(myconfig.role_ratings_df.loc['olr3'][attributes]),
                'r4': list(myconfig.role_ratings_df.loc['olr4'][attributes]),
                'r5': list(myconfig.role_ratings_df.loc['olr5'][attributes]),
                'r6': list(myconfig.role_ratings_df.loc['olr6'][attributes])
            },
            'DL': {
                'r1': list(myconfig.role_ratings_df.loc['dlr1'][attributes]),
                'r2': list(myconfig.role_ratings_df.loc['dlr2'][attributes]),
                'r3': list(myconfig.role_ratings_df.loc['dlr3'][attributes]),
                'r4': list(myconfig.role_ratings_df.loc['dlr4'][attributes]),
                'r5': list(myconfig.role_ratings_df.loc['dlr5'][attributes]),
                'r6': list(myconfig.role_ratings_df.loc['dlr6'][attributes])
            },
            'LB': {
                'r1': list(myconfig.role_ratings_df.loc['lbr1'][attributes]),
                'r2': list(myconfig.role_ratings_df.loc['lbr2'][attributes]),
                'r3': list(myconfig.role_ratings_df.loc['lbr3'][attributes]),
                'r4': list(myconfig.role_ratings_df.loc['lbr4'][attributes]),
                'r5': list(myconfig.role_ratings_df.loc['lbr5'][attributes]),
                'r6': list(myconfig.role_ratings_df.loc['lbr6'][attributes])
            },
            'DB': {
                'r1': list(myconfig.role_ratings_df.loc['dbr1'][attributes]),
                'r2': list(myconfig.role_ratings_df.loc['dbr2'][attributes]),
                'r3': list(myconfig.role_ratings_df.loc['dbr3'][attributes]),
                'r4': list(myconfig.role_ratings_df.loc['dbr4'][attributes]),
                'r5': list(myconfig.role_ratings_df.loc['dbr5'][attributes]),
                'r6': list(myconfig.role_ratings_df.loc['dbr6'][attributes])
            },
            'K': {
                'r1': list(myconfig.role_ratings_df.loc['kr1'][attributes]),
                'r2': list(myconfig.role_ratings_df.loc['kr2'][attributes]),
                'r3': list(myconfig.role_ratings_df.loc['kr3'][attributes]),
                'r4': list(myconfig.role_ratings_df.loc['kr4'][attributes]),
                'r5': list(myconfig.role_ratings_df.loc['kr5'][attributes]),
                'r6': list(myconfig.role_ratings_df.loc['kr6'][attributes])
            },
            'P': {
                'r1': list(myconfig.role_ratings_df.loc['pr1'][attributes]),
                'r2': list(myconfig.role_ratings_df.loc['pr2'][attributes]),
                'r3': list(myconfig.role_ratings_df.loc['pr3'][attributes]),
                'r4': list(myconfig.role_ratings_df.loc['pr4'][attributes]),
                'r5': list(myconfig.role_ratings_df.loc['pr5'][attributes]),
                'r6': list(myconfig.role_ratings_df.loc['pr6'][attributes])
            }
        }

        recruit = [
            ratings['ath'],
            ratings['spd'],
            ratings['dur'],
            ratings['we'],
            ratings['sta'],
            ratings['str'],
            ratings['blk'],
            ratings['tkl'],
            ratings['han'],
            ratings['gi'],
            ratings['elu'],
            ratings['tec']
        ]
        pos = ratings['pos']
        recruit_role_ratings = {
            'r1': round(np.dot(rating_formulas[pos]['r1'], recruit)/100, 1),
            'r2': round(np.dot(rating_formulas[pos]['r2'], recruit)/100, 1),
            'r3': round(np.dot(rating_formulas[pos]['r3'], recruit)/100, 1),
            'r4': round(np.dot(rating_formulas[pos]['r4'], recruit)/100, 1),
            'r5': round(np.dot(rating_formulas[pos]['r5'], recruit)/100, 1),
            'r6': round(np.dot(rating_formulas[pos]['r6'], recruit)/100, 1)
        }

        return recruit_role_ratings


class RoleRatingDBWorker(QObject):
    finished = Signal()
    progress = Signal(int)
    
       
    def run(self):
        """Long-running Initialize Recruit task goes here."""
        logger.info("Started RoleRatingDBWorker.run function")
        # Thread signaling start
        self.progress.emit(0)
        # Update role ratings for all recruits in DB
        if db.databaseName() != "":
            # Returned list of lists should contain this data:
            # [r, pos, ath, spd, dur, we, sta, strength, blk, tkl, han, gi, elu, tec]
            ratings_keys = ['ath', 'spd', 'dur', 'we', 'sta', 'strength', 'blk', 'tkl', 'han', 'gi', 'elu', 'tec']
            recruits = query_Recruit_IDs("update_role_ratings", db)
            openDB(db)
            query = QSqlQuery(db)
            query.prepare("UPDATE recruits "
                            "SET r1 = :r1, "
                                "r2 = :r2, "
                                "r3 = :r3, "
                                "r4 = :r4, "
                                "r5 = :r5, "
                                "r6 = :r6 "
                            "WHERE id = :id")
            with Bar('Updating recruit role ratings in DB...', max=len(recruits)) as bar:
                logger.info(f"Updating recruit role ratings in database...")
                for r in recruits:
                    rid = r[0]
                    pos = r[1]
                    rating_values = r[2:]
                    ratings = dict(zip(ratings_keys, rating_values))
                    role_ratings = calculate_role_rating(pos, ratings)
                    query.bindValue(":r1", float(role_ratings['r1']))
                    query.bindValue(":r2", float(role_ratings['r2']))
                    query.bindValue(":r3", float(role_ratings['r3']))
                    query.bindValue(":r4", float(role_ratings['r4']))
                    query.bindValue(":r5", float(role_ratings['r5']))
                    query.bindValue(":r6", float(role_ratings['r6']))
                    query.bindValue(":id", rid)
                    if not query.exec_():
                        logQueryError(query)
                    bar.next()
                    self.progress.emit(round(bar.index / bar.max * 100))
        query.finish()
        db.close()
        self.finished.emit()



class InitializeWorker(QObject):
    finished = Signal()
    progress = Signal(int, int)
    
    
    
    def run(self):
        """Long-running Initialize Recruit task goes here."""
        logger.info("Started InitializeWorker.run function")
        # Thread signaling start
        self.progress.emit(0, 1)

        
        #c = load_config()
        #config = c['config']
        #requests_session = requests.Session()
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
                rank INTEGER,
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
                watched INTEGER,
                division TEXT
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
        result = wis_browser("scrape_recruit_IDs", db_t, self.progress)
        if result:
            # After grabbing all Recruit IDs and storing in DB.
            # This thread is finished and now need to signal 
            # creation of new threads for grabbing static attributes of recruits.
            self.finished.emit()
        else:
            # Implies there was an error authenticating to WIS
            self.progress.emit(999999,1)
            self.finished.emit()


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

# This class is no longer needed as-is when using the new Advanced Search page to gather recruits
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
                emit_progress = 1000000
                self.progress.emit(emit_progress)
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
                    emit_progress += 1
                    self.progress.emit(emit_progress)
        query.finish()
        db_t.close()
        self.finished.emit()


class BrowserAuthWorker(QObject):
    finished = Signal()
    progress = Signal(int)
    
    
    def run(self):
        """Long-running Initialize Recruit task goes here."""

        # Thread signaling start
        logger.debug("progress.emit(0)")
        self.progress.emit(0)
        
        page = wis_browser("auth_to_store_cookies", db_t, self.progress)

        if not page:
            logger.debug("progress.emit(999999)")
            self.progress.emit(999999)

        logger.debug("finished.emit()")
        self.finished.emit()

# This class is no longer needed as-is when using the new Advanced Search page to gather recruits
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
        #c = load_config()
        #config = c['config']
        
        db_m.setDatabaseName(db.databaseName())
        page = wis_browser("grab_watched_recruits", db_m, self.progress)
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
            myconfig.watchlist_length = len(watchlist)
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

            myconfig.watchlist_length = len(watchlist)
            logger.info(f"Length of watchlist = {myconfig.watchlist_length}")

            # First we clear all watched recruits from the db
            if db.isOpen():
                logger.debug("closing 'db' connection...")
                db.close()
            if db_t.isOpen():
                logger.debug("closing 'db_t' connection...")
                db_t.close()
            openDB(db_m)
            queryUpdate = QSqlQuery(db_m)
            if not queryUpdate.exec_(
                """
                UPDATE recruits SET watched = 0
                """
            ):
                logQueryError(queryUpdate)
            queryUpdate.finish()

            # Now we set watched = 1 for the rids in watchlist
            query_watched_update = QSqlQuery(db_m)
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

            db_m.close()

            # Report done
            self.progress.emit(1000)
            mw.statusbar.showMessage(f"{len(watchlist)} recruits marked from watchlist.")
        self.finished.emit()


class GrabSeasonData(QDialog, Ui_WidgetGrabSeasonData):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = QSettings()
        geometry = self.settings.value('GrabSeasonDataGeometry', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)
        # Queue to process recruit IDs
        self.rid_queue = Queue()
        self.threadpool = QThreadPool()
        self.threadCount = QThreadPool.globalInstance().maxThreadCount()
        self.requests_session = requests.Session()
        self.recruit_initialize_list = []
        self.rids_all = query_Recruit_IDs("all", db)
        myconfig.rids_all_length = len(self.rids_all)
        if myconfig.rids_all_length == 0:
            self.pushButtonInitializeRecruits.setText(QCoreApplication.translate("MainWindow", u"&Initialize Recruits", None))
        else:
            self.labelRecruitsInitialized.setText(f"Recruits Initialized = {myconfig.rids_all_length}")
            self.labelRecruitsInitialized.setStyleSheet(u"color: rgb(0, 128, 0);")
            self.pushButtonInitializeRecruits.setText(QCoreApplication.translate("MainWindow", u"&Re-Initialize Recruits", None))

        self.checkBoxGrabHigherRecruits.setChecked(myconfig.higher_division_recruits)

        # Hide all progress check marks and text until button is pressed
        self.labelCheckMarkAuthWIS_Error.setVisible(False)
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
        self.pushButtonInitializeRecruits.clicked.connect(self.runInitializeJob)
        self.checkBoxGrabHigherRecruits.stateChanged.connect(self.save_higher_recruit_config)
        self.buttonBox.button(QDialogButtonBox.Close).clicked.connect(self.accept)

    def accept(self):
        geometry = self.saveGeometry()
        self.settings.setValue('GrabSeasonDataGeometry', geometry)
        super().close()


    def save_higher_recruit_config(self):
        data = {0: False, 2: True}
        myconfig.higher_division_recruits = data[self.checkBoxGrabHigherRecruits.checkState()]
        logger.debug(f"myconfig.higher_division_recruits = {myconfig.higher_division_recruits}")

    
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
        self.buttonBox.button(QDialogButtonBox.Close).setEnabled(False)
        self.labelRecruitsInitialized.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.labelRecruitsInitialized.setText(f"Recruits Initialized = 0")
        self.pushButtonInitializeRecruits.setEnabled(False)
        self.labelCheckMarkCreateDB.setVisible(False)
        self.labelCheckMarkAuthWIS.setVisible(False)
        self.labelCheckMarkAuthWIS_Error.setVisible(False)
        self.labelCheckMarkGrabUnsigned.setVisible(False)
        self.labelCheckMarkGrabSigned.setVisible(False)
        self.labelCheckMarkGrabStaticData.setVisible(False)
        self.checkBoxGrabHigherRecruits.setEnabled(False)
        self.thread.finished.connect(self.initialize_finished)

    
    def reportInitializeProgress(self, n, m):
        divisions = {1: 'D-IA', 2: 'D-IAA', 3: 'D-II', 4: 'D-III'}
        if n == 0:
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
            self.progressBarInitializeRecruits.setValue(0)
            self.progressBarInitializeRecruits.setVisible(True)
            self.labelGrabUnsigned.setText(f"Grab Unsigned Recruits for {divisions[m]}")
            self.labelGrabSigned.setText(f"Grab Signed Recruits for {divisions[m]}")
            self.labelCheckMarkGrabUnsigned.setVisible(False)
            self.labelCheckMarkGrabSigned.setVisible(False)
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
            self.checkBoxGrabHigherRecruits.setEnabled(True)
        if n == 999999:
            self.labelCheckMarkAuthWIS_Error.setVisible(True)
            mw.statusbar.showMessage("ERROR: There was a problem authenticating to WIS.")
            self.progressBarInitializeRecruits.setVisible(False)

    
    # This function is no longer needed as-is when using the new Advanced Search page to gather recruits
    def queue_run_initialize_attributes(self):
        logger.info(f"Running queue_run_initialize_attributes function")
        queue_rid_urls(self.rid_queue, "all")
        self.labelRecruitsInitialized.setText(f"Initializing {myconfig.rids_all_length} Recruits...")
        self.progressBarInitializeRecruits.setRange(0, myconfig.rids_all_length)
        self.progressBarInitializeRecruits.setValue(0)
        self.progressBarInitializeRecruits.value()
        self.stopped = False
        self.run_threads(self.recruit_initialize, self.completed)

    # This function is no longer needed as-is when using the new Advanced Search page to gather recruits
    def run_threads(self, process, on_complete):
        # Step 1: Create thread object to monitor queue
        self.thread = QThread()
        # Step 2: Create a worker object
        if process.__func__.__name__ == "recruit_initialize":
            logger.debug("run_threads function -> recruit_initialize conditional statement")
            self.worker = QueueMonitorWorker(self.rid_queue, self.recruit_initialize_list, myconfig.rids_all_length, "initialize")
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

    # This function is no longer needed as-is when using the new Advanced Search page to gather recruits
    def recruit_initialize(self, progress_callback):
        while self.rid_queue.qsize() > 0:
            logger.debug(f"Looking for the next Recruit ID...")
            rid = self.rid_queue.get()
            logger.debug(f"Processing {rid}")
            r = rid[0]
            position = rid[1]
            page = rid[2]
            headers = {'User-Agent': 'gdrecruit-recruit-initialize/0.5.1 python-requests/2.25.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
            recruitpage = self.requests_session.get(page, headers=headers)
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

            recruit['role_rating'] = calculate_role_rating(position, recruit)

            self.recruit_initialize_list.append(recruit)
            self.rid_queue.task_done()
            progress_callback.emit(self.rid_queue.qsize())
            if self.stopped == True:
                return
        return


    def completed(self):
        logger.debug(f"Running threading completed function")
        return

        
    def progress_fn(self, msg):
        #self.info.append(str(msg))
        logger.debug("Running progress_fn function")
        return

       
    def initialize_finished(self):
        logger.debug("Running initialized_finished function")
        self.labelRecruitsInitialized.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.labelRecruitsInitialized.setText(f"Initialized {myconfig.rids_all_length} Recruits...")
        self.buttonBox.button(QDialogButtonBox.Close).setEnabled(True)

    
    def queue_monitor_initialize_progress(self, n):
        if n == 0:
            logger.debug("Queue is empty.")
            completed = myconfig.rids_all_length - n
            self.progressBarInitializeRecruits.setValue(completed)
            self.labelCheckMarkGrabStaticData.setVisible(True)
        elif n > 0 and n < 1000000:
            completed = myconfig.rids_all_length - n
            self.progressBarInitializeRecruits.setValue(completed)
        elif n == 1000000:
            self.progressBarInitializeRecruits.setValue(0)
        elif n > 1000000:
            self.progressBarInitializeRecruits.setValue(n - 1000000)

    
    def closeEvent(self, event):
        # Now we define the closeEvent
        # This is called whenever a window is closed.
        # It is passed an event which we can choose to accept or reject, but in this case we'll just pass it on after we're done.
        
        # First we need to get the current size and position of the window.
        # This can be fetchesd using the built in saveGeometry() method. 
        # This is got back as a byte array. It won't really make sense to a human directly, but it makes sense to Qt.
        geometry = self.saveGeometry()

        # Once we know the geometry we can save it in our settings under geometry
        self.settings.setValue('GrabSeasonDataGeometry', geometry)
        
        # Finally we pass the event to the class we inherit from. It can choose to accept or reject the event, but we don't need to deal with it ourselves
        super(GrabSeasonData, self).closeEvent(event)


class UpdateConsidering(QDialog, Ui_DialogUpdateConsidering):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = QSettings()
        geometry = self.settings.value('UpdateConsideringGeometry', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)
        self.buttonBox.button(QDialogButtonBox.Close).setEnabled(False)
        self.labelCheckmarkUpdateConsidering.setVisible(False)
        self.rid_queue = Queue()
        self.threadpool = QThreadPool()
        self.threadCount = QThreadPool.globalInstance().maxThreadCount()
        self.requests_session = requests.Session()
        self.recruit_considering = []
        self.queue_run_update_considering()
        self.buttonBox.button(QDialogButtonBox.Close).clicked.connect(self.accept)

    
    def accept(self):
        geometry = self.saveGeometry()
        self.settings.setValue('UpdateConsideringGeometry', geometry)
        super().accept()


    def closeEvent(self, event):
        # Now we define the closeEvent
        # This is called whenever a window is closed.
        # It is passed an event which we can choose to accept or reject, but in this case we'll just pass it on after we're done.
        
        # First we need to get the current size and position of the window.
        # This can be fetchesd using the built in saveGeometry() method. 
        # This is got back as a byte array. It won't really make sense to a human directly, but it makes sense to Qt.
        geometry = self.saveGeometry()

        # Once we know the geometry we can save it in our settings under geometry
        self.settings.setValue('UpdateConsideringGeometry', geometry)
        
        # Finally we pass the event to the class we inherit from. It can choose to accept or reject the event, but we don't need to deal with it ourselves
        super(UpdateConsidering, self).closeEvent(event)

    
    def queue_run_update_considering(self):
        self.progressBarUpdateConsidering.setVisible(True)
        queue_rid_urls(self.rid_queue, "unsigned")
        self.progressBarUpdateConsidering.setRange(0, myconfig.rids_unsigned_length)
        self.stopped = False
        self.run_threads(self.recruit_update, self.completed)

    
    def run_threads(self, process, on_complete):
        # Step 1: Create thread object to monitor queue
        self.thread = QThread()
        # Step 2: Create a worker object
        if process.__func__.__name__ == "recruit_update":
            logger.debug("run_threads function -> recruit_update conditional statement")
            self.worker = QueueMonitorWorker(self.rid_queue, self.recruit_considering, myconfig.rids_unsigned_length, "update")
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
            self.labelUpdateStatusText.setText(f"Grabbing updates for {myconfig.rids_unsigned_length} recruits...")
            self.labelUpdateStatusText.setVisible(True)
            self.thread.finished.connect(self.update_finished)
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


    def update_finished(self):
        logger.debug("Running update_finished function")
        self.buttonBox.button(QDialogButtonBox.Close).setEnabled(True)
        self.labelUpdateStatusText.setText("Update Considering action completed.")
        self.labelCheckmarkUpdateConsidering.setVisible(True)

    
    def recruit_update(self, progress_callback):
        while self.rid_queue.qsize() > 0:
            logger.debug(f"Length of queue = {self.rid_queue.qsize()}")
            logger.debug(f"Looking for the next Recruit ID...")
            rid = self.rid_queue.get()
            logger.debug(f"Processing {rid}")
            headers = {'User-Agent': 'gdrecruit-recruit-update/0.5.1 python-requests/2.25.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
            recruitpage = self.requests_session.get(rid[1], headers=headers)
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
                    considering = f"{myconfig.wis_gd_df.school_short[team_id]}\n"
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

    
    def stop(self):
        self.stopped=True
        return

    def completed(self):
        logger.debug(f"Running threading completed function")
        return


    def progress_fn(self, msg):
        #self.info.append(str(msg))
        logger.debug("Running progress_fn function")
        return


    def queue_monitor_update_progress(self, n):
        if n == 0:
            logger.debug("Queue is empty.")
            completed = myconfig.rids_unsigned_length - n
            self.progressBarUpdateConsidering.setValue(completed)
        elif n > 0 and n <= myconfig.rids_unsigned_length:
            completed = myconfig.rids_unsigned_length - n
            self.progressBarUpdateConsidering.setValue(completed)
        elif n >= 1000000:
            if n == 1000000:
                self.labelUpdateStatusText.setText(f"Saving {myconfig.rids_unsigned_length} updates to database...")
            completed = n - 1000000
            self.progressBarUpdateConsidering.setValue(completed)
            if completed == myconfig.rids_unsigned_length:
                self.labelCheckmarkUpdateConsidering.setVisible(True)


class MarkWatchlistPotential(QDialog, Ui_DialogMarkWatchlistPotential):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = QSettings()
        geometry = self.settings.value('MarkWatchlistPotentialGeometry', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)
        self.buttonBox.button(QDialogButtonBox.Close).setEnabled(False)
        self.runMarkRecruitsJob()
        self.buttonBox.button(QDialogButtonBox.Close).clicked.connect(self.accept)

    
    def accept(self):
        geometry = self.saveGeometry()
        self.settings.setValue('MarkWatchlistPotentialGeometry', geometry)
        super().accept()


    def closeEvent(self, event):
        # Now we define the closeEvent
        # This is called whenever a window is closed.
        # It is passed an event which we can choose to accept or reject, but in this case we'll just pass it on after we're done.
        
        # First we need to get the current size and position of the window.
        # This can be fetchesd using the built in saveGeometry() method. 
        # This is got back as a byte array. It won't really make sense to a human directly, but it makes sense to Qt.
        geometry = self.saveGeometry()

        # Once we know the geometry we can save it in our settings under geometry
        self.settings.setValue('MarkWatchlistPotentialGeometry', geometry)
        
        # Finally we pass the event to the class we inherit from. It can choose to accept or reject the event, but we don't need to deal with it ourselves
        super(MarkWatchlistPotential, self).closeEvent(event)


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
        self.thread.finished.connect(
            lambda: self.buttonBox.button(QDialogButtonBox.Close).setEnabled(True)
        )

    
    def reportMarkRecruitsProgress(self, n):
        if n == 0:
            self.progressBarMarkWatchlist.setStyleSheet("color: blue")
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
            self.labelAuthWIS_MarkRecruits.setText(f"Processed {myconfig.watchlist_length} recruits from Watchlist.")
        if n == 2000:
            mw.statusbar.showMessage("ERROR: There was a problem loading Recruit Summary Page.")
        if n == 6:
            pass
        if n == 999999:
            self.labelCheckMarkAuthWIS_Error_MarkRecruits.setVisible(True)
            self.progressBarMarkWatchlist.setVisible(False)
            mw.statusbar.showMessage("ERROR: There was a problem authenticating to WIS.")

        
class LoadSeason(QDialog, Ui_DialogLoadSeason):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = QSettings()
        geometry = self.settings.value('LoadSeasonGeometry', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)
        db_files = [x for x in os.listdir(myconfig.seasons_directory_path) if x.endswith(".db")]
        logger.debug(f"db_files = {db_files}")
        c = load_config()
        config = c['config']
        if config.has_option('WISCreds', 'coachid'):
            coachid = config.get('WISCreds', 'coachid')
            logger.debug(f"LoadSeason coachid = {coachid}")
            if coachid != "":
                filtered_db_files = [k for k in db_files if coachid in k]
            else:
                filtered_db_files = []
        logger.debug(f"filtered_db_files = {filtered_db_files}")
        if len(filtered_db_files) > 0:
            self.comboBoxSelectSeason.addItems(filtered_db_files)
        else:
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

    def accept(self):
        myconfig.season_filename = os.path.join(myconfig.seasons_directory_path, self.comboBoxSelectSeason.currentText())
        
        myconfig.clear_model = True
        geometry = self.saveGeometry()
        self.settings.setValue('LoadSeasonGeometry', geometry)
        super().accept()


    def closeEvent(self, event):
        # Now we define the closeEvent
        # This is called whenever a window is closed.
        # It is passed an event which we can choose to accept or reject, but in this case we'll just pass it on after we're done.
        
        # First we need to get the current size and position of the window.
        # This can be fetchesd using the built in saveGeometry() method. 
        # This is got back as a byte array. It won't really make sense to a human directly, but it makes sense to Qt.
        geometry = self.saveGeometry()

        # Once we know the geometry we can save it in our settings under geometry
        self.settings.setValue('LoadSeasonGeometry', geometry)
        
        # Finally we pass the event to the class we inherit from. It can choose to accept or reject the event, but we don't need to deal with it ourselves
        super(LoadSeason, self).closeEvent(event)


class NewSeason(QDialog, Ui_DialogNewSeason):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = QSettings()
        geometry = self.settings.value('NewSeasonGeometry', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)
        config = configparser.ConfigParser()
        config.read(myconfig.config_file)
        if config.has_option('WISCreds', 'coachid'):
            self.coachid = config.get('WISCreds', 'coachid')
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
        myconfig.season_filename = os.path.join(myconfig.seasons_directory_path, f"{self.coachid} - {seasonnum} - {selected}.db")
        logger.debug(f"Storing database name as: {myconfig.season_filename}")
        myconfig.clear_model = True
        geometry = self.saveGeometry()
        self.settings.setValue('NewSeasonGeometry', geometry)
        super().accept()


    def closeEvent(self, event):
        # Now we define the closeEvent
        # This is called whenever a window is closed.
        # It is passed an event which we can choose to accept or reject, but in this case we'll just pass it on after we're done.
        
        # First we need to get the current size and position of the window.
        # This can be fetchesd using the built in saveGeometry() method. 
        # This is got back as a byte array. It won't really make sense to a human directly, but it makes sense to Qt.
        geometry = self.saveGeometry()

        # Once we know the geometry we can save it in our settings under geometry
        self.settings.setValue('NewSeasonGeometry', geometry)
        
        # Finally we pass the event to the class we inherit from. It can choose to accept or reject the event, but we don't need to deal with it ourselves
        super(NewSeason, self).closeEvent(event)


class WISCred(QDialog, Ui_WISCredentialDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        logger.debug("Entering WISCred class section...")
        self.c = load_config()
        self.coachid = self.c['coachid']
        logger.info(f"WISCred section: coachid = {self.coachid}")
        self.setupUi(self, self.coachid)
        self.settings = QSettings()
        geometry = self.settings.value('WISCredGeometry', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)
        self.labelCheckMarkcoachIDValidated.setVisible(False)
        self.labelCheckMarkcoachIDValidationError.setVisible(False)
        self.labelCheckMarkCookieStored.setVisible(False)
        self.labelCookieStored.setVisible(False)
        self.labelCookieStoredError.setVisible(False)
        self.progressBarLoginStoreCookies.setVisible(False)
        self.pushButton_LoginStoreCookie.setEnabled(False)
        self.pushButton_LoginStoreCookie.setVisible(False)
        self.buttonBox.button(QDialogButtonBox.Close).setEnabled(False)
        
        # Validate coachid from config file is proper
        if self.coachid != "":
            self.validate_coach_profile()
        self.lineEditWISCoachID.editingFinished.connect(self.validate_coach_profile)
        self.pushButton_LoginStoreCookie.clicked.connect(self.browser_auth)
        self.buttonBox.button(QDialogButtonBox.Close).clicked.connect(self.accept)

    
    def validate_coach_profile(self):
        requests_session = requests.Session()
        coachid = self.lineEditWISCoachID.text()
        if coachid == "":
            self.labelCookieStored.setVisible(False)
            self.labelCheckMarkcoachIDValidationError.setVisible(False)
            self.labelCheckMarkcoachIDValidated.setVisible(False)
            self.labelCheckMarkCookieStored.setVisible(False)
            self.labelCookieStoredError.setVisible(False)
            self.pushButton_LoginStoreCookie.setVisible(False)
        else:
            headers = {'User-Agent': 'gdrecruit-validate-coach-profile/0.5.1 python-requests/2.25.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
            
            coach_profile_page = requests_session.get(f"https://wis-dev.shub.dog/account/UserProfile/Games/GridironDynasty/?user={coachid}", headers=headers)
            #coach_profile_page = requests_session.get(f"https://www.whatifsports.com/account/UserProfile/Games/GridironDynasty/?user={coachid}", headers=headers)
            if coach_profile_page.status_code == 200:
                logger.info(f"Validated coach ID: {coachid} (status code = {coach_profile_page.status_code})")
                config = self.c['config']
                self.coachid = coachid
                if config['WISCreds']['coachid'] != coachid:
                    logger.info("CoachID was changed. Clearing cookies from storage_state.")
                    config.set('WISCreds', 'coachid', coachid)
                    write_config(config)
                    # If coachid changes then assume auth changes.
                    # Therefore have to clear the browser storage state.
                    global storage_state
                    storage_state = ""
                    myconfig.clear_model = True
                self.labelCheckMarkcoachIDValidationError.setVisible(False)
                self.labelCheckMarkcoachIDValidated.setVisible(True)
                self.pushButton_LoginStoreCookie.setVisible(True)
                self.pushButton_LoginStoreCookie.setEnabled(True)
                self.check_stored_cookie(coachid)
            else:
                logger.info(f"Error validating coach ID: {coachid} (status code = {coach_profile_page.status_code})")
                self.labelCheckMarkcoachIDValidationError.setVisible(True)
                self.labelCheckMarkcoachIDValidated.setVisible(False)
                self.pushButton_LoginStoreCookie.setVisible(False)
                self.labelCookieStored.setVisible(False)
                self.labelCheckMarkCookieStored.setVisible(False)
                self.labelCookieStoredError.setVisible(False)
                self.buttonBox.button(QDialogButtonBox.Close).setEnabled(False)

    
    def check_stored_cookie(self, coachid):
        file = os.path.join(myconfig.cookies_directory_path, f"browser_cookie_{coachid}.json")
        self.labelCookieStored.setVisible(True)
        self.labelCheckMarkCookieStored.setVisible(False)
        self.labelCookieStoredError.setVisible(False)
        if path.exists(file):
            self.labelCheckMarkCookieStored.setVisible(True)
            self.pushButton_LoginStoreCookie.setEnabled(True)
            self.buttonBox.button(QDialogButtonBox.Close).setEnabled(True)
        else:
            logger.info(f"Path to {file} does not exist!")
            self.labelCheckMarkCookieStored.setVisible(False)
            self.labelCookieStoredError.setVisible(True)



    def browser_auth(self):
        logger.info("Button Pressed: Login To Store Cookies")
        # Step 1: Create a QThread object
        self.thread = QThread()
        # Step 2: Create a worker object
        self.worker = BrowserAuthWorker()
        # Step 3: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 4: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.browser_auth_Progress)
        # Step 6: Start the thread
        self.thread.start()
        # Final resets
        self.progressBarLoginStoreCookies.setVisible(True)
        self.lineEditWISCoachID.setEnabled(False)
        self.pushButton_LoginStoreCookie.setEnabled(False)
        self.labelCheckMarkCookieStored.setVisible(False)
        self.labelCookieStoredError.setVisible(False)
        self.buttonBox.button(QDialogButtonBox.Close).setEnabled(False)
        self.thread.finished.connect(
            lambda: self.check_stored_cookie(self.coachid)
        )


    def browser_auth_Progress(self, n):
        if n == 0:
            logger.debug("browser auth received emit signal 0")
            logger.info("Thread started for WIS Auth and storing cookies.")
        if n == 1:
            logger.debug("browser auth received emit signal 1")
            logger.info("WIS auth through playwright browser completed.")
            self.progressBarLoginStoreCookies.setVisible(False)
            self.lineEditWISCoachID.setEnabled(True)
            self.pushButton_LoginStoreCookie.setEnabled(True)
            self.labelCheckMarkCookieStored.setVisible(True)
            self.buttonBox.button(QDialogButtonBox.Close).setEnabled(True)
        if n == 999999:
            logger.debug("browser auth received emit signal 999999")
            self.labelCookieStoredError.setVisible(True)
            self.progressBarLoginStoreCookies.setVisible(False)
            self.pushButton_LoginStoreCookie.setEnabled(True)
            self.buttonBox.button(QDialogButtonBox.Close).setEnabled(True)
            logger.error("There was a problem authenticating to WIS.")
            mw.statusbar.showMessage("ERROR: There was a problem authenticating to WIS.")
    

    def accept(self):
        update_active_teams(self.lineEditWISCoachID.text())
        geometry = self.saveGeometry()
        self.settings.setValue('WISCredGeometry', geometry)
        super().accept()

    
    def closeEvent(self, event):
        # Now we define the closeEvent
        # This is called whenever a window is closed.
        # It is passed an event which we can choose to accept or reject, but in this case we'll just pass it on after we're done.
        
        # First we need to get the current size and position of the window.
        # This can be fetchesd using the built in saveGeometry() method. 
        # This is got back as a byte array. It won't really make sense to a human directly, but it makes sense to Qt.
        geometry = self.saveGeometry()

        # Once we know the geometry we can save it in our settings under geometry
        self.settings.setValue('WISCredGeometry', geometry)
        
        # Finally we pass the event to the class we inherit from. It can choose to accept or reject the event, but we don't need to deal with it ourselves
        super(WISCred, self).closeEvent(event)


class ShowColumns(QDialog, Ui_DialogShowColumns):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = QSettings()
        geometry = self.settings.value('ShowColumnsGeometry', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)
        hide_columns = self.settings.value('HideColumns', [])
        columns = {
                    0: self.checkBoxID.setChecked,
                    1: self.checkBoxName.setChecked,
                    2: self.checkBoxPos.setChecked,
                    3: self.checkBoxHeight.setChecked,
                    4: self.checkBoxWeight.setChecked,
                    5: self.checkBoxRating.setChecked,
                    6: self.checkBoxRank.setChecked,
                    7: self.checkBoxHometown.setChecked,
                    8: self.checkBoxMiles.setChecked,
                    9: self.checkBoxConsidering.setChecked,
                    10: self.checkBoxATH.setChecked,
                    11: self.checkBoxSPD.setChecked,
                    12: self.checkBoxDUR.setChecked,
                    13: self.checkBoxWE.setChecked,
                    14: self.checkBoxSTA.setChecked,
                    15: self.checkBoxSTR.setChecked,
                    16: self.checkBoxBLK.setChecked,
                    17: self.checkBoxTKL.setChecked,
                    18: self.checkBoxHAN.setChecked,
                    19: self.checkBoxGI.setChecked,
                    20: self.checkBoxELU.setChecked,
                    21: self.checkBoxTEC.setChecked,
                    22: self.checkBoxR1.setChecked,
                    23: self.checkBoxR2.setChecked,
                    24: self.checkBoxR3.setChecked,
                    25: self.checkBoxR4.setChecked,
                    26: self.checkBoxR5.setChecked,
                    27: self.checkBoxR6.setChecked,
                    28: self.checkBoxGPA.setChecked,
                    29: self.checkBoxPot.setChecked,
                    30: self.checkBoxSigned.setChecked,
                    31: self.checkBoxWatched.setChecked,
                    32: self.checkBoxDivision.setChecked
        }
        if hide_columns != '':
            for col in hide_columns:
                c = int(col)
                columns[c].__call__(False)
                logger.info(f"Setting UI checkbox for column {c} to unchecked")
        
        
    def accept(self):
        columns = {
                    0: self.checkBoxID.isChecked(),
                    1: self.checkBoxName.isChecked(),
                    2: self.checkBoxPos.isChecked(),
                    3: self.checkBoxHeight.isChecked(),
                    4: self.checkBoxWeight.isChecked(),
                    5: self.checkBoxRating.isChecked(),
                    6: self.checkBoxRank.isChecked(),
                    7: self.checkBoxHometown.isChecked(),
                    8: self.checkBoxMiles.isChecked(),
                    9: self.checkBoxConsidering.isChecked(),
                    10: self.checkBoxATH.isChecked(),
                    11: self.checkBoxSPD.isChecked(),
                    12: self.checkBoxDUR.isChecked(),
                    13: self.checkBoxWE.isChecked(),
                    14: self.checkBoxSTA.isChecked(),
                    15: self.checkBoxSTR.isChecked(),
                    16: self.checkBoxBLK.isChecked(),
                    17: self.checkBoxTKL.isChecked(),
                    18: self.checkBoxHAN.isChecked(),
                    19: self.checkBoxGI.isChecked(),
                    20: self.checkBoxELU.isChecked(),
                    21: self.checkBoxTEC.isChecked(),
                    22: self.checkBoxR1.isChecked(),
                    23: self.checkBoxR2.isChecked(),
                    24: self.checkBoxR3.isChecked(),
                    25: self.checkBoxR4.isChecked(),
                    26: self.checkBoxR5.isChecked(),
                    27: self.checkBoxR6.isChecked(),
                    28: self.checkBoxGPA.isChecked(),
                    29: self.checkBoxPot.isChecked(),
                    30: self.checkBoxSigned.isChecked(),
                    31: self.checkBoxWatched.isChecked(),
                    32: self.checkBoxDivision.isChecked()
        }
        logger.debug(f"Column checkbox states = {columns}")
        columns_to_hide = []
        for k, v in columns.items():
            if v == False:
                columns_to_hide.append(k)
        logger.info(f"Saving columns to hide in registry = {columns_to_hide}")
        self.settings.setValue('HideColumns', columns_to_hide)

        # Save Windows geometry to registry
        geometry = self.saveGeometry()
        self.settings.setValue('ShowColumnsGeometry', geometry)
        super().accept()


    def closeEvent(self, event):
        # Now we define the closeEvent
        # This is called whenever a window is closed.
        # It is passed an event which we can choose to accept or reject, but in this case we'll just pass it on after we're done.
        
        # First we need to get the current size and position of the window.
        # This can be fetchesd using the built in saveGeometry() method. 
        # This is got back as a byte array. It won't really make sense to a human directly, but it makes sense to Qt.
        geometry = self.saveGeometry()

        # Once we know the geometry we can save it in our settings under geometry
        self.settings.setValue('ShowColumnsGeometry', geometry)
        
        # Finally we pass the event to the class we inherit from. It can choose to accept or reject the event, but we don't need to deal with it ourselves
        super(ShowColumns, self).closeEvent(event)


class RoleRatings(QDialog, Ui_DialogRoleRatings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = QSettings()
        geometry = self.settings.value('RoleRatingsGeometry', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)
        
        # QB Section
        self.lineEdit_R1_QB.setText(myconfig.role_ratings_df['label']['qbr1'])
        self.spinBox_R1_ATH_QB.setValue(myconfig.role_ratings_df['ath']['qbr1'])
        self.spinBox_R1_SPD_QB.setValue(myconfig.role_ratings_df['spd']['qbr1'])
        self.spinBox_R1_DUR_QB.setValue(myconfig.role_ratings_df['dur']['qbr1'])
        self.spinBox_R1_WE_QB.setValue(myconfig.role_ratings_df['we']['qbr1'])
        self.spinBox_R1_STA_QB.setValue(myconfig.role_ratings_df['sta']['qbr1'])
        self.spinBox_R1_STR_QB.setValue(myconfig.role_ratings_df['str']['qbr1'])
        self.spinBox_R1_BLK_QB.setValue(myconfig.role_ratings_df['blk']['qbr1'])
        self.spinBox_R1_TKL_QB.setValue(myconfig.role_ratings_df['tkl']['qbr1'])
        self.spinBox_R1_HAN_QB.setValue(myconfig.role_ratings_df['han']['qbr1'])
        self.spinBox_R1_GI_QB.setValue(myconfig.role_ratings_df['gi']['qbr1'])
        self.spinBox_R1_ELU_QB.setValue(myconfig.role_ratings_df['elu']['qbr1'])
        self.spinBox_R1_TEC_QB.setValue(myconfig.role_ratings_df['tec']['qbr1'])
        self.lcdNumber_R1_QB.display(myconfig.role_ratings_df['total']['qbr1'])
        self.spinBox_R1_ATH_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_SPD_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_DUR_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_WE_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STA_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STR_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_BLK_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TKL_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_HAN_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_GI_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_ELU_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TEC_QB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R2_QB.setText(myconfig.role_ratings_df['label']['qbr2'])
        self.spinBox_R2_ATH_QB.setValue(myconfig.role_ratings_df['ath']['qbr2'])
        self.spinBox_R2_SPD_QB.setValue(myconfig.role_ratings_df['spd']['qbr2'])
        self.spinBox_R2_DUR_QB.setValue(myconfig.role_ratings_df['dur']['qbr2'])
        self.spinBox_R2_WE_QB.setValue(myconfig.role_ratings_df['we']['qbr2'])
        self.spinBox_R2_STA_QB.setValue(myconfig.role_ratings_df['sta']['qbr2'])
        self.spinBox_R2_STR_QB.setValue(myconfig.role_ratings_df['str']['qbr2'])
        self.spinBox_R2_BLK_QB.setValue(myconfig.role_ratings_df['blk']['qbr2'])
        self.spinBox_R2_TKL_QB.setValue(myconfig.role_ratings_df['tkl']['qbr2'])
        self.spinBox_R2_HAN_QB.setValue(myconfig.role_ratings_df['han']['qbr2'])
        self.spinBox_R2_GI_QB.setValue(myconfig.role_ratings_df['gi']['qbr2'])
        self.spinBox_R2_ELU_QB.setValue(myconfig.role_ratings_df['elu']['qbr2'])
        self.spinBox_R2_TEC_QB.setValue(myconfig.role_ratings_df['tec']['qbr2'])
        self.lcdNumber_R2_QB.display(myconfig.role_ratings_df['total']['qbr2'])
        self.spinBox_R2_ATH_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_SPD_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_DUR_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_WE_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STA_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STR_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_BLK_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TKL_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_HAN_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_GI_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_ELU_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TEC_QB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R3_QB.setText(myconfig.role_ratings_df['label']['qbr3'])
        self.spinBox_R3_ATH_QB.setValue(myconfig.role_ratings_df['ath']['qbr3'])
        self.spinBox_R3_SPD_QB.setValue(myconfig.role_ratings_df['spd']['qbr3'])
        self.spinBox_R3_DUR_QB.setValue(myconfig.role_ratings_df['dur']['qbr3'])
        self.spinBox_R3_WE_QB.setValue(myconfig.role_ratings_df['we']['qbr3'])
        self.spinBox_R3_STA_QB.setValue(myconfig.role_ratings_df['sta']['qbr3'])
        self.spinBox_R3_STR_QB.setValue(myconfig.role_ratings_df['str']['qbr3'])
        self.spinBox_R3_BLK_QB.setValue(myconfig.role_ratings_df['blk']['qbr3'])
        self.spinBox_R3_TKL_QB.setValue(myconfig.role_ratings_df['tkl']['qbr3'])
        self.spinBox_R3_HAN_QB.setValue(myconfig.role_ratings_df['han']['qbr3'])
        self.spinBox_R3_GI_QB.setValue(myconfig.role_ratings_df['gi']['qbr3'])
        self.spinBox_R3_ELU_QB.setValue(myconfig.role_ratings_df['elu']['qbr3'])
        self.spinBox_R3_TEC_QB.setValue(myconfig.role_ratings_df['tec']['qbr3'])
        self.lcdNumber_R3_QB.display(myconfig.role_ratings_df['total']['qbr3'])
        self.spinBox_R3_ATH_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_SPD_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_DUR_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_WE_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STA_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STR_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_BLK_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TKL_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_HAN_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_GI_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_ELU_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TEC_QB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R4_QB.setText(myconfig.role_ratings_df['label']['qbr4'])
        self.spinBox_R4_ATH_QB.setValue(myconfig.role_ratings_df['ath']['qbr4'])
        self.spinBox_R4_SPD_QB.setValue(myconfig.role_ratings_df['spd']['qbr4'])
        self.spinBox_R4_DUR_QB.setValue(myconfig.role_ratings_df['dur']['qbr4'])
        self.spinBox_R4_WE_QB.setValue(myconfig.role_ratings_df['we']['qbr4'])
        self.spinBox_R4_STA_QB.setValue(myconfig.role_ratings_df['sta']['qbr4'])
        self.spinBox_R4_STR_QB.setValue(myconfig.role_ratings_df['str']['qbr4'])
        self.spinBox_R4_BLK_QB.setValue(myconfig.role_ratings_df['blk']['qbr4'])
        self.spinBox_R4_TKL_QB.setValue(myconfig.role_ratings_df['tkl']['qbr4'])
        self.spinBox_R4_HAN_QB.setValue(myconfig.role_ratings_df['han']['qbr4'])
        self.spinBox_R4_GI_QB.setValue(myconfig.role_ratings_df['gi']['qbr4'])
        self.spinBox_R4_ELU_QB.setValue(myconfig.role_ratings_df['elu']['qbr4'])
        self.spinBox_R4_TEC_QB.setValue(myconfig.role_ratings_df['tec']['qbr4'])
        self.lcdNumber_R4_QB.display(myconfig.role_ratings_df['total']['qbr4'])
        self.spinBox_R4_ATH_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_SPD_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_DUR_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_WE_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STA_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STR_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_BLK_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TKL_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_HAN_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_GI_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_ELU_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TEC_QB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R5_QB.setText(myconfig.role_ratings_df['label']['qbr5'])
        self.spinBox_R5_ATH_QB.setValue(myconfig.role_ratings_df['ath']['qbr5'])
        self.spinBox_R5_SPD_QB.setValue(myconfig.role_ratings_df['spd']['qbr5'])
        self.spinBox_R5_DUR_QB.setValue(myconfig.role_ratings_df['dur']['qbr5'])
        self.spinBox_R5_WE_QB.setValue(myconfig.role_ratings_df['we']['qbr5'])
        self.spinBox_R5_STA_QB.setValue(myconfig.role_ratings_df['sta']['qbr5'])
        self.spinBox_R5_STR_QB.setValue(myconfig.role_ratings_df['str']['qbr5'])
        self.spinBox_R5_BLK_QB.setValue(myconfig.role_ratings_df['blk']['qbr5'])
        self.spinBox_R5_TKL_QB.setValue(myconfig.role_ratings_df['tkl']['qbr5'])
        self.spinBox_R5_HAN_QB.setValue(myconfig.role_ratings_df['han']['qbr5'])
        self.spinBox_R5_GI_QB.setValue(myconfig.role_ratings_df['gi']['qbr5'])
        self.spinBox_R5_ELU_QB.setValue(myconfig.role_ratings_df['elu']['qbr5'])
        self.spinBox_R5_TEC_QB.setValue(myconfig.role_ratings_df['tec']['qbr5'])
        self.lcdNumber_R5_QB.display(myconfig.role_ratings_df['total']['qbr5'])
        self.spinBox_R5_ATH_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_SPD_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_DUR_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_WE_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STA_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STR_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_BLK_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TKL_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_HAN_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_GI_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_ELU_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TEC_QB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R6_QB.setText(myconfig.role_ratings_df['label']['qbr6'])
        self.spinBox_R6_ATH_QB.setValue(myconfig.role_ratings_df['ath']['qbr6'])
        self.spinBox_R6_SPD_QB.setValue(myconfig.role_ratings_df['spd']['qbr6'])
        self.spinBox_R6_DUR_QB.setValue(myconfig.role_ratings_df['dur']['qbr6'])
        self.spinBox_R6_WE_QB.setValue(myconfig.role_ratings_df['we']['qbr6'])
        self.spinBox_R6_STA_QB.setValue(myconfig.role_ratings_df['sta']['qbr6'])
        self.spinBox_R6_STR_QB.setValue(myconfig.role_ratings_df['str']['qbr6'])
        self.spinBox_R6_BLK_QB.setValue(myconfig.role_ratings_df['blk']['qbr6'])
        self.spinBox_R6_TKL_QB.setValue(myconfig.role_ratings_df['tkl']['qbr6'])
        self.spinBox_R6_HAN_QB.setValue(myconfig.role_ratings_df['han']['qbr6'])
        self.spinBox_R6_GI_QB.setValue(myconfig.role_ratings_df['gi']['qbr6'])
        self.spinBox_R6_ELU_QB.setValue(myconfig.role_ratings_df['elu']['qbr6'])
        self.spinBox_R6_TEC_QB.setValue(myconfig.role_ratings_df['tec']['qbr6'])
        self.lcdNumber_R6_QB.display(myconfig.role_ratings_df['total']['qbr6'])
        self.spinBox_R6_ATH_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_SPD_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_DUR_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_WE_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STA_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STR_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_BLK_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TKL_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_HAN_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_GI_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_ELU_QB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TEC_QB.valueChanged.connect(self.update_row_total)

        # RB Section
        self.lineEdit_R1_RB.setText(myconfig.role_ratings_df['label']['rbr1'])
        self.spinBox_R1_ATH_RB.setValue(myconfig.role_ratings_df['ath']['rbr1'])
        self.spinBox_R1_SPD_RB.setValue(myconfig.role_ratings_df['spd']['rbr1'])
        self.spinBox_R1_DUR_RB.setValue(myconfig.role_ratings_df['dur']['rbr1'])
        self.spinBox_R1_WE_RB.setValue(myconfig.role_ratings_df['we']['rbr1'])
        self.spinBox_R1_STA_RB.setValue(myconfig.role_ratings_df['sta']['rbr1'])
        self.spinBox_R1_STR_RB.setValue(myconfig.role_ratings_df['str']['rbr1'])
        self.spinBox_R1_BLK_RB.setValue(myconfig.role_ratings_df['blk']['rbr1'])
        self.spinBox_R1_TKL_RB.setValue(myconfig.role_ratings_df['tkl']['rbr1'])
        self.spinBox_R1_HAN_RB.setValue(myconfig.role_ratings_df['han']['rbr1'])
        self.spinBox_R1_GI_RB.setValue(myconfig.role_ratings_df['gi']['rbr1'])
        self.spinBox_R1_ELU_RB.setValue(myconfig.role_ratings_df['elu']['rbr1'])
        self.spinBox_R1_TEC_RB.setValue(myconfig.role_ratings_df['tec']['rbr1'])
        self.lcdNumber_R1_RB.display(myconfig.role_ratings_df['total']['rbr1'])
        self.spinBox_R1_ATH_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_SPD_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_DUR_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_WE_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STA_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STR_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_BLK_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TKL_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_HAN_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_GI_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_ELU_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TEC_RB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R2_RB.setText(myconfig.role_ratings_df['label']['rbr2'])
        self.spinBox_R2_ATH_RB.setValue(myconfig.role_ratings_df['ath']['rbr2'])
        self.spinBox_R2_SPD_RB.setValue(myconfig.role_ratings_df['spd']['rbr2'])
        self.spinBox_R2_DUR_RB.setValue(myconfig.role_ratings_df['dur']['rbr2'])
        self.spinBox_R2_WE_RB.setValue(myconfig.role_ratings_df['we']['rbr2'])
        self.spinBox_R2_STA_RB.setValue(myconfig.role_ratings_df['sta']['rbr2'])
        self.spinBox_R2_STR_RB.setValue(myconfig.role_ratings_df['str']['rbr2'])
        self.spinBox_R2_BLK_RB.setValue(myconfig.role_ratings_df['blk']['rbr2'])
        self.spinBox_R2_TKL_RB.setValue(myconfig.role_ratings_df['tkl']['rbr2'])
        self.spinBox_R2_HAN_RB.setValue(myconfig.role_ratings_df['han']['rbr2'])
        self.spinBox_R2_GI_RB.setValue(myconfig.role_ratings_df['gi']['rbr2'])
        self.spinBox_R2_ELU_RB.setValue(myconfig.role_ratings_df['elu']['rbr2'])
        self.spinBox_R2_TEC_RB.setValue(myconfig.role_ratings_df['tec']['rbr2'])
        self.lcdNumber_R2_RB.display(myconfig.role_ratings_df['total']['rbr2'])
        self.spinBox_R2_ATH_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_SPD_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_DUR_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_WE_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STA_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STR_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_BLK_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TKL_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_HAN_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_GI_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_ELU_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TEC_RB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R3_RB.setText(myconfig.role_ratings_df['label']['rbr3'])
        self.spinBox_R3_ATH_RB.setValue(myconfig.role_ratings_df['ath']['rbr3'])
        self.spinBox_R3_SPD_RB.setValue(myconfig.role_ratings_df['spd']['rbr3'])
        self.spinBox_R3_DUR_RB.setValue(myconfig.role_ratings_df['dur']['rbr3'])
        self.spinBox_R3_WE_RB.setValue(myconfig.role_ratings_df['we']['rbr3'])
        self.spinBox_R3_STA_RB.setValue(myconfig.role_ratings_df['sta']['rbr3'])
        self.spinBox_R3_STR_RB.setValue(myconfig.role_ratings_df['str']['rbr3'])
        self.spinBox_R3_BLK_RB.setValue(myconfig.role_ratings_df['blk']['rbr3'])
        self.spinBox_R3_TKL_RB.setValue(myconfig.role_ratings_df['tkl']['rbr3'])
        self.spinBox_R3_HAN_RB.setValue(myconfig.role_ratings_df['han']['rbr3'])
        self.spinBox_R3_GI_RB.setValue(myconfig.role_ratings_df['gi']['rbr3'])
        self.spinBox_R3_ELU_RB.setValue(myconfig.role_ratings_df['elu']['rbr3'])
        self.spinBox_R3_TEC_RB.setValue(myconfig.role_ratings_df['tec']['rbr3'])
        self.lcdNumber_R3_RB.display(myconfig.role_ratings_df['total']['rbr3'])
        self.spinBox_R3_ATH_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_SPD_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_DUR_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_WE_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STA_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STR_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_BLK_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TKL_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_HAN_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_GI_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_ELU_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TEC_RB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R4_RB.setText(myconfig.role_ratings_df['label']['rbr4'])
        self.spinBox_R4_ATH_RB.setValue(myconfig.role_ratings_df['ath']['rbr4'])
        self.spinBox_R4_SPD_RB.setValue(myconfig.role_ratings_df['spd']['rbr4'])
        self.spinBox_R4_DUR_RB.setValue(myconfig.role_ratings_df['dur']['rbr4'])
        self.spinBox_R4_WE_RB.setValue(myconfig.role_ratings_df['we']['rbr4'])
        self.spinBox_R4_STA_RB.setValue(myconfig.role_ratings_df['sta']['rbr4'])
        self.spinBox_R4_STR_RB.setValue(myconfig.role_ratings_df['str']['rbr4'])
        self.spinBox_R4_BLK_RB.setValue(myconfig.role_ratings_df['blk']['rbr4'])
        self.spinBox_R4_TKL_RB.setValue(myconfig.role_ratings_df['tkl']['rbr4'])
        self.spinBox_R4_HAN_RB.setValue(myconfig.role_ratings_df['han']['rbr4'])
        self.spinBox_R4_GI_RB.setValue(myconfig.role_ratings_df['gi']['rbr4'])
        self.spinBox_R4_ELU_RB.setValue(myconfig.role_ratings_df['elu']['rbr4'])
        self.spinBox_R4_TEC_RB.setValue(myconfig.role_ratings_df['tec']['rbr4'])
        self.lcdNumber_R4_RB.display(myconfig.role_ratings_df['total']['rbr4'])
        self.spinBox_R4_ATH_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_SPD_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_DUR_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_WE_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STA_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STR_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_BLK_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TKL_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_HAN_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_GI_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_ELU_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TEC_RB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R5_RB.setText(myconfig.role_ratings_df['label']['rbr5'])
        self.spinBox_R5_ATH_RB.setValue(myconfig.role_ratings_df['ath']['rbr5'])
        self.spinBox_R5_SPD_RB.setValue(myconfig.role_ratings_df['spd']['rbr5'])
        self.spinBox_R5_DUR_RB.setValue(myconfig.role_ratings_df['dur']['rbr5'])
        self.spinBox_R5_WE_RB.setValue(myconfig.role_ratings_df['we']['rbr5'])
        self.spinBox_R5_STA_RB.setValue(myconfig.role_ratings_df['sta']['rbr5'])
        self.spinBox_R5_STR_RB.setValue(myconfig.role_ratings_df['str']['rbr5'])
        self.spinBox_R5_BLK_RB.setValue(myconfig.role_ratings_df['blk']['rbr5'])
        self.spinBox_R5_TKL_RB.setValue(myconfig.role_ratings_df['tkl']['rbr5'])
        self.spinBox_R5_HAN_RB.setValue(myconfig.role_ratings_df['han']['rbr5'])
        self.spinBox_R5_GI_RB.setValue(myconfig.role_ratings_df['gi']['rbr5'])
        self.spinBox_R5_ELU_RB.setValue(myconfig.role_ratings_df['elu']['rbr5'])
        self.spinBox_R5_TEC_RB.setValue(myconfig.role_ratings_df['tec']['rbr5'])
        self.lcdNumber_R5_RB.display(myconfig.role_ratings_df['total']['rbr5'])
        self.spinBox_R5_ATH_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_SPD_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_DUR_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_WE_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STA_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STR_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_BLK_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TKL_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_HAN_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_GI_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_ELU_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TEC_RB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R6_RB.setText(myconfig.role_ratings_df['label']['rbr6'])
        self.spinBox_R6_ATH_RB.setValue(myconfig.role_ratings_df['ath']['rbr6'])
        self.spinBox_R6_SPD_RB.setValue(myconfig.role_ratings_df['spd']['rbr6'])
        self.spinBox_R6_DUR_RB.setValue(myconfig.role_ratings_df['dur']['rbr6'])
        self.spinBox_R6_WE_RB.setValue(myconfig.role_ratings_df['we']['rbr6'])
        self.spinBox_R6_STA_RB.setValue(myconfig.role_ratings_df['sta']['rbr6'])
        self.spinBox_R6_STR_RB.setValue(myconfig.role_ratings_df['str']['rbr6'])
        self.spinBox_R6_BLK_RB.setValue(myconfig.role_ratings_df['blk']['rbr6'])
        self.spinBox_R6_TKL_RB.setValue(myconfig.role_ratings_df['tkl']['rbr6'])
        self.spinBox_R6_HAN_RB.setValue(myconfig.role_ratings_df['han']['rbr6'])
        self.spinBox_R6_GI_RB.setValue(myconfig.role_ratings_df['gi']['rbr6'])
        self.spinBox_R6_ELU_RB.setValue(myconfig.role_ratings_df['elu']['rbr6'])
        self.spinBox_R6_TEC_RB.setValue(myconfig.role_ratings_df['tec']['rbr6'])
        self.lcdNumber_R6_RB.display(myconfig.role_ratings_df['total']['rbr6'])
        self.spinBox_R6_ATH_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_SPD_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_DUR_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_WE_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STA_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STR_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_BLK_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TKL_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_HAN_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_GI_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_ELU_RB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TEC_RB.valueChanged.connect(self.update_row_total)

        # WR Section
        self.lineEdit_R1_WR.setText(myconfig.role_ratings_df['label']['wrr1'])
        self.spinBox_R1_ATH_WR.setValue(myconfig.role_ratings_df['ath']['wrr1'])
        self.spinBox_R1_SPD_WR.setValue(myconfig.role_ratings_df['spd']['wrr1'])
        self.spinBox_R1_DUR_WR.setValue(myconfig.role_ratings_df['dur']['wrr1'])
        self.spinBox_R1_WE_WR.setValue(myconfig.role_ratings_df['we']['wrr1'])
        self.spinBox_R1_STA_WR.setValue(myconfig.role_ratings_df['sta']['wrr1'])
        self.spinBox_R1_STR_WR.setValue(myconfig.role_ratings_df['str']['wrr1'])
        self.spinBox_R1_BLK_WR.setValue(myconfig.role_ratings_df['blk']['wrr1'])
        self.spinBox_R1_TKL_WR.setValue(myconfig.role_ratings_df['tkl']['wrr1'])
        self.spinBox_R1_HAN_WR.setValue(myconfig.role_ratings_df['han']['wrr1'])
        self.spinBox_R1_GI_WR.setValue(myconfig.role_ratings_df['gi']['wrr1'])
        self.spinBox_R1_ELU_WR.setValue(myconfig.role_ratings_df['elu']['wrr1'])
        self.spinBox_R1_TEC_WR.setValue(myconfig.role_ratings_df['tec']['wrr1'])
        self.lcdNumber_R1_WR.display(myconfig.role_ratings_df['total']['wrr1'])
        self.spinBox_R1_ATH_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_SPD_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_DUR_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_WE_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STA_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STR_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_BLK_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TKL_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_HAN_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_GI_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_ELU_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TEC_WR.valueChanged.connect(self.update_row_total)

        self.lineEdit_R2_WR.setText(myconfig.role_ratings_df['label']['wrr2'])
        self.spinBox_R2_ATH_WR.setValue(myconfig.role_ratings_df['ath']['wrr2'])
        self.spinBox_R2_SPD_WR.setValue(myconfig.role_ratings_df['spd']['wrr2'])
        self.spinBox_R2_DUR_WR.setValue(myconfig.role_ratings_df['dur']['wrr2'])
        self.spinBox_R2_WE_WR.setValue(myconfig.role_ratings_df['we']['wrr2'])
        self.spinBox_R2_STA_WR.setValue(myconfig.role_ratings_df['sta']['wrr2'])
        self.spinBox_R2_STR_WR.setValue(myconfig.role_ratings_df['str']['wrr2'])
        self.spinBox_R2_BLK_WR.setValue(myconfig.role_ratings_df['blk']['wrr2'])
        self.spinBox_R2_TKL_WR.setValue(myconfig.role_ratings_df['tkl']['wrr2'])
        self.spinBox_R2_HAN_WR.setValue(myconfig.role_ratings_df['han']['wrr2'])
        self.spinBox_R2_GI_WR.setValue(myconfig.role_ratings_df['gi']['wrr2'])
        self.spinBox_R2_ELU_WR.setValue(myconfig.role_ratings_df['elu']['wrr2'])
        self.spinBox_R2_TEC_WR.setValue(myconfig.role_ratings_df['tec']['wrr2'])
        self.lcdNumber_R2_WR.display(myconfig.role_ratings_df['total']['wrr2'])
        self.spinBox_R2_ATH_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_SPD_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_DUR_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_WE_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STA_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STR_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_BLK_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TKL_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_HAN_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_GI_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_ELU_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TEC_WR.valueChanged.connect(self.update_row_total)

        self.lineEdit_R3_WR.setText(myconfig.role_ratings_df['label']['wrr3'])
        self.spinBox_R3_ATH_WR.setValue(myconfig.role_ratings_df['ath']['wrr3'])
        self.spinBox_R3_SPD_WR.setValue(myconfig.role_ratings_df['spd']['wrr3'])
        self.spinBox_R3_DUR_WR.setValue(myconfig.role_ratings_df['dur']['wrr3'])
        self.spinBox_R3_WE_WR.setValue(myconfig.role_ratings_df['we']['wrr3'])
        self.spinBox_R3_STA_WR.setValue(myconfig.role_ratings_df['sta']['wrr3'])
        self.spinBox_R3_STR_WR.setValue(myconfig.role_ratings_df['str']['wrr3'])
        self.spinBox_R3_BLK_WR.setValue(myconfig.role_ratings_df['blk']['wrr3'])
        self.spinBox_R3_TKL_WR.setValue(myconfig.role_ratings_df['tkl']['wrr3'])
        self.spinBox_R3_HAN_WR.setValue(myconfig.role_ratings_df['han']['wrr3'])
        self.spinBox_R3_GI_WR.setValue(myconfig.role_ratings_df['gi']['wrr3'])
        self.spinBox_R3_ELU_WR.setValue(myconfig.role_ratings_df['elu']['wrr3'])
        self.spinBox_R3_TEC_WR.setValue(myconfig.role_ratings_df['tec']['wrr3'])
        self.lcdNumber_R3_WR.display(myconfig.role_ratings_df['total']['wrr3'])
        self.spinBox_R3_ATH_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_SPD_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_DUR_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_WE_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STA_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STR_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_BLK_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TKL_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_HAN_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_GI_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_ELU_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TEC_WR.valueChanged.connect(self.update_row_total)

        self.lineEdit_R4_WR.setText(myconfig.role_ratings_df['label']['wrr4'])
        self.spinBox_R4_ATH_WR.setValue(myconfig.role_ratings_df['ath']['wrr4'])
        self.spinBox_R4_SPD_WR.setValue(myconfig.role_ratings_df['spd']['wrr4'])
        self.spinBox_R4_DUR_WR.setValue(myconfig.role_ratings_df['dur']['wrr4'])
        self.spinBox_R4_WE_WR.setValue(myconfig.role_ratings_df['we']['wrr4'])
        self.spinBox_R4_STA_WR.setValue(myconfig.role_ratings_df['sta']['wrr4'])
        self.spinBox_R4_STR_WR.setValue(myconfig.role_ratings_df['str']['wrr4'])
        self.spinBox_R4_BLK_WR.setValue(myconfig.role_ratings_df['blk']['wrr4'])
        self.spinBox_R4_TKL_WR.setValue(myconfig.role_ratings_df['tkl']['wrr4'])
        self.spinBox_R4_HAN_WR.setValue(myconfig.role_ratings_df['han']['wrr4'])
        self.spinBox_R4_GI_WR.setValue(myconfig.role_ratings_df['gi']['wrr4'])
        self.spinBox_R4_ELU_WR.setValue(myconfig.role_ratings_df['elu']['wrr4'])
        self.spinBox_R4_TEC_WR.setValue(myconfig.role_ratings_df['tec']['wrr4'])
        self.lcdNumber_R4_WR.display(myconfig.role_ratings_df['total']['wrr4'])
        self.spinBox_R4_ATH_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_SPD_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_DUR_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_WE_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STA_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STR_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_BLK_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TKL_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_HAN_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_GI_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_ELU_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TEC_WR.valueChanged.connect(self.update_row_total)

        self.lineEdit_R5_WR.setText(myconfig.role_ratings_df['label']['wrr5'])
        self.spinBox_R5_ATH_WR.setValue(myconfig.role_ratings_df['ath']['wrr5'])
        self.spinBox_R5_SPD_WR.setValue(myconfig.role_ratings_df['spd']['wrr5'])
        self.spinBox_R5_DUR_WR.setValue(myconfig.role_ratings_df['dur']['wrr5'])
        self.spinBox_R5_WE_WR.setValue(myconfig.role_ratings_df['we']['wrr5'])
        self.spinBox_R5_STA_WR.setValue(myconfig.role_ratings_df['sta']['wrr5'])
        self.spinBox_R5_STR_WR.setValue(myconfig.role_ratings_df['str']['wrr5'])
        self.spinBox_R5_BLK_WR.setValue(myconfig.role_ratings_df['blk']['wrr5'])
        self.spinBox_R5_TKL_WR.setValue(myconfig.role_ratings_df['tkl']['wrr5'])
        self.spinBox_R5_HAN_WR.setValue(myconfig.role_ratings_df['han']['wrr5'])
        self.spinBox_R5_GI_WR.setValue(myconfig.role_ratings_df['gi']['wrr5'])
        self.spinBox_R5_ELU_WR.setValue(myconfig.role_ratings_df['elu']['wrr5'])
        self.spinBox_R5_TEC_WR.setValue(myconfig.role_ratings_df['tec']['wrr5'])
        self.lcdNumber_R5_WR.display(myconfig.role_ratings_df['total']['wrr5'])
        self.spinBox_R5_ATH_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_SPD_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_DUR_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_WE_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STA_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STR_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_BLK_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TKL_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_HAN_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_GI_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_ELU_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TEC_WR.valueChanged.connect(self.update_row_total)

        self.lineEdit_R6_WR.setText(myconfig.role_ratings_df['label']['wrr6'])
        self.spinBox_R6_ATH_WR.setValue(myconfig.role_ratings_df['ath']['wrr6'])
        self.spinBox_R6_SPD_WR.setValue(myconfig.role_ratings_df['spd']['wrr6'])
        self.spinBox_R6_DUR_WR.setValue(myconfig.role_ratings_df['dur']['wrr6'])
        self.spinBox_R6_WE_WR.setValue(myconfig.role_ratings_df['we']['wrr6'])
        self.spinBox_R6_STA_WR.setValue(myconfig.role_ratings_df['sta']['wrr6'])
        self.spinBox_R6_STR_WR.setValue(myconfig.role_ratings_df['str']['wrr6'])
        self.spinBox_R6_BLK_WR.setValue(myconfig.role_ratings_df['blk']['wrr6'])
        self.spinBox_R6_TKL_WR.setValue(myconfig.role_ratings_df['tkl']['wrr6'])
        self.spinBox_R6_HAN_WR.setValue(myconfig.role_ratings_df['han']['wrr6'])
        self.spinBox_R6_GI_WR.setValue(myconfig.role_ratings_df['gi']['wrr6'])
        self.spinBox_R6_ELU_WR.setValue(myconfig.role_ratings_df['elu']['wrr6'])
        self.spinBox_R6_TEC_WR.setValue(myconfig.role_ratings_df['tec']['wrr6'])
        self.lcdNumber_R6_WR.display(myconfig.role_ratings_df['total']['wrr6'])
        self.spinBox_R6_ATH_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_SPD_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_DUR_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_WE_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STA_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STR_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_BLK_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TKL_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_HAN_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_GI_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_ELU_WR.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TEC_WR.valueChanged.connect(self.update_row_total)

        # TE Section
        self.lineEdit_R1_TE.setText(myconfig.role_ratings_df['label']['ter1'])
        self.spinBox_R1_ATH_TE.setValue(myconfig.role_ratings_df['ath']['ter1'])
        self.spinBox_R1_SPD_TE.setValue(myconfig.role_ratings_df['spd']['ter1'])
        self.spinBox_R1_DUR_TE.setValue(myconfig.role_ratings_df['dur']['ter1'])
        self.spinBox_R1_WE_TE.setValue(myconfig.role_ratings_df['we']['ter1'])
        self.spinBox_R1_STA_TE.setValue(myconfig.role_ratings_df['sta']['ter1'])
        self.spinBox_R1_STR_TE.setValue(myconfig.role_ratings_df['str']['ter1'])
        self.spinBox_R1_BLK_TE.setValue(myconfig.role_ratings_df['blk']['ter1'])
        self.spinBox_R1_TKL_TE.setValue(myconfig.role_ratings_df['tkl']['ter1'])
        self.spinBox_R1_HAN_TE.setValue(myconfig.role_ratings_df['han']['ter1'])
        self.spinBox_R1_GI_TE.setValue(myconfig.role_ratings_df['gi']['ter1'])
        self.spinBox_R1_ELU_TE.setValue(myconfig.role_ratings_df['elu']['ter1'])
        self.spinBox_R1_TEC_TE.setValue(myconfig.role_ratings_df['tec']['ter1'])
        self.lcdNumber_R1_TE.display(myconfig.role_ratings_df['total']['ter1'])
        self.spinBox_R1_ATH_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_SPD_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_DUR_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_WE_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STA_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STR_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_BLK_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TKL_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_HAN_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_GI_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_ELU_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TEC_TE.valueChanged.connect(self.update_row_total)

        self.lineEdit_R2_TE.setText(myconfig.role_ratings_df['label']['ter2'])
        self.spinBox_R2_ATH_TE.setValue(myconfig.role_ratings_df['ath']['ter2'])
        self.spinBox_R2_SPD_TE.setValue(myconfig.role_ratings_df['spd']['ter2'])
        self.spinBox_R2_DUR_TE.setValue(myconfig.role_ratings_df['dur']['ter2'])
        self.spinBox_R2_WE_TE.setValue(myconfig.role_ratings_df['we']['ter2'])
        self.spinBox_R2_STA_TE.setValue(myconfig.role_ratings_df['sta']['ter2'])
        self.spinBox_R2_STR_TE.setValue(myconfig.role_ratings_df['str']['ter2'])
        self.spinBox_R2_BLK_TE.setValue(myconfig.role_ratings_df['blk']['ter2'])
        self.spinBox_R2_TKL_TE.setValue(myconfig.role_ratings_df['tkl']['ter2'])
        self.spinBox_R2_HAN_TE.setValue(myconfig.role_ratings_df['han']['ter2'])
        self.spinBox_R2_GI_TE.setValue(myconfig.role_ratings_df['gi']['ter2'])
        self.spinBox_R2_ELU_TE.setValue(myconfig.role_ratings_df['elu']['ter2'])
        self.spinBox_R2_TEC_TE.setValue(myconfig.role_ratings_df['tec']['ter2'])
        self.lcdNumber_R2_TE.display(myconfig.role_ratings_df['total']['ter2'])
        self.spinBox_R2_ATH_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_SPD_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_DUR_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_WE_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STA_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STR_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_BLK_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TKL_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_HAN_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_GI_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_ELU_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TEC_TE.valueChanged.connect(self.update_row_total)

        self.lineEdit_R3_TE.setText(myconfig.role_ratings_df['label']['ter3'])
        self.spinBox_R3_ATH_TE.setValue(myconfig.role_ratings_df['ath']['ter3'])
        self.spinBox_R3_SPD_TE.setValue(myconfig.role_ratings_df['spd']['ter3'])
        self.spinBox_R3_DUR_TE.setValue(myconfig.role_ratings_df['dur']['ter3'])
        self.spinBox_R3_WE_TE.setValue(myconfig.role_ratings_df['we']['ter3'])
        self.spinBox_R3_STA_TE.setValue(myconfig.role_ratings_df['sta']['ter3'])
        self.spinBox_R3_STR_TE.setValue(myconfig.role_ratings_df['str']['ter3'])
        self.spinBox_R3_BLK_TE.setValue(myconfig.role_ratings_df['blk']['ter3'])
        self.spinBox_R3_TKL_TE.setValue(myconfig.role_ratings_df['tkl']['ter3'])
        self.spinBox_R3_HAN_TE.setValue(myconfig.role_ratings_df['han']['ter3'])
        self.spinBox_R3_GI_TE.setValue(myconfig.role_ratings_df['gi']['ter3'])
        self.spinBox_R3_ELU_TE.setValue(myconfig.role_ratings_df['elu']['ter3'])
        self.spinBox_R3_TEC_TE.setValue(myconfig.role_ratings_df['tec']['ter3'])
        self.lcdNumber_R3_TE.display(myconfig.role_ratings_df['total']['ter3'])
        self.spinBox_R3_ATH_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_SPD_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_DUR_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_WE_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STA_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STR_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_BLK_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TKL_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_HAN_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_GI_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_ELU_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TEC_TE.valueChanged.connect(self.update_row_total)

        self.lineEdit_R4_TE.setText(myconfig.role_ratings_df['label']['ter4'])
        self.spinBox_R4_ATH_TE.setValue(myconfig.role_ratings_df['ath']['ter4'])
        self.spinBox_R4_SPD_TE.setValue(myconfig.role_ratings_df['spd']['ter4'])
        self.spinBox_R4_DUR_TE.setValue(myconfig.role_ratings_df['dur']['ter4'])
        self.spinBox_R4_WE_TE.setValue(myconfig.role_ratings_df['we']['ter4'])
        self.spinBox_R4_STA_TE.setValue(myconfig.role_ratings_df['sta']['ter4'])
        self.spinBox_R4_STR_TE.setValue(myconfig.role_ratings_df['str']['ter4'])
        self.spinBox_R4_BLK_TE.setValue(myconfig.role_ratings_df['blk']['ter4'])
        self.spinBox_R4_TKL_TE.setValue(myconfig.role_ratings_df['tkl']['ter4'])
        self.spinBox_R4_HAN_TE.setValue(myconfig.role_ratings_df['han']['ter4'])
        self.spinBox_R4_GI_TE.setValue(myconfig.role_ratings_df['gi']['ter4'])
        self.spinBox_R4_ELU_TE.setValue(myconfig.role_ratings_df['elu']['ter4'])
        self.spinBox_R4_TEC_TE.setValue(myconfig.role_ratings_df['tec']['ter4'])
        self.lcdNumber_R4_TE.display(myconfig.role_ratings_df['total']['ter4'])
        self.spinBox_R4_ATH_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_SPD_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_DUR_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_WE_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STA_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STR_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_BLK_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TKL_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_HAN_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_GI_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_ELU_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TEC_TE.valueChanged.connect(self.update_row_total)

        self.lineEdit_R5_TE.setText(myconfig.role_ratings_df['label']['ter5'])
        self.spinBox_R5_ATH_TE.setValue(myconfig.role_ratings_df['ath']['ter5'])
        self.spinBox_R5_SPD_TE.setValue(myconfig.role_ratings_df['spd']['ter5'])
        self.spinBox_R5_DUR_TE.setValue(myconfig.role_ratings_df['dur']['ter5'])
        self.spinBox_R5_WE_TE.setValue(myconfig.role_ratings_df['we']['ter5'])
        self.spinBox_R5_STA_TE.setValue(myconfig.role_ratings_df['sta']['ter5'])
        self.spinBox_R5_STR_TE.setValue(myconfig.role_ratings_df['str']['ter5'])
        self.spinBox_R5_BLK_TE.setValue(myconfig.role_ratings_df['blk']['ter5'])
        self.spinBox_R5_TKL_TE.setValue(myconfig.role_ratings_df['tkl']['ter5'])
        self.spinBox_R5_HAN_TE.setValue(myconfig.role_ratings_df['han']['ter5'])
        self.spinBox_R5_GI_TE.setValue(myconfig.role_ratings_df['gi']['ter5'])
        self.spinBox_R5_ELU_TE.setValue(myconfig.role_ratings_df['elu']['ter5'])
        self.spinBox_R5_TEC_TE.setValue(myconfig.role_ratings_df['tec']['ter5'])
        self.lcdNumber_R5_TE.display(myconfig.role_ratings_df['total']['ter5'])
        self.spinBox_R5_ATH_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_SPD_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_DUR_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_WE_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STA_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STR_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_BLK_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TKL_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_HAN_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_GI_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_ELU_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TEC_TE.valueChanged.connect(self.update_row_total)

        self.lineEdit_R6_TE.setText(myconfig.role_ratings_df['label']['ter6'])
        self.spinBox_R6_ATH_TE.setValue(myconfig.role_ratings_df['ath']['ter6'])
        self.spinBox_R6_SPD_TE.setValue(myconfig.role_ratings_df['spd']['ter6'])
        self.spinBox_R6_DUR_TE.setValue(myconfig.role_ratings_df['dur']['ter6'])
        self.spinBox_R6_WE_TE.setValue(myconfig.role_ratings_df['we']['ter6'])
        self.spinBox_R6_STA_TE.setValue(myconfig.role_ratings_df['sta']['ter6'])
        self.spinBox_R6_STR_TE.setValue(myconfig.role_ratings_df['str']['ter6'])
        self.spinBox_R6_BLK_TE.setValue(myconfig.role_ratings_df['blk']['ter6'])
        self.spinBox_R6_TKL_TE.setValue(myconfig.role_ratings_df['tkl']['ter6'])
        self.spinBox_R6_HAN_TE.setValue(myconfig.role_ratings_df['han']['ter6'])
        self.spinBox_R6_GI_TE.setValue(myconfig.role_ratings_df['gi']['ter6'])
        self.spinBox_R6_ELU_TE.setValue(myconfig.role_ratings_df['elu']['ter6'])
        self.spinBox_R6_TEC_TE.setValue(myconfig.role_ratings_df['tec']['ter6'])
        self.lcdNumber_R6_TE.display(myconfig.role_ratings_df['total']['ter6'])
        self.spinBox_R6_ATH_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_SPD_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_DUR_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_WE_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STA_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STR_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_BLK_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TKL_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_HAN_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_GI_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_ELU_TE.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TEC_TE.valueChanged.connect(self.update_row_total)

        # OL Section
        self.lineEdit_R1_OL.setText(myconfig.role_ratings_df['label']['olr1'])
        self.spinBox_R1_ATH_OL.setValue(myconfig.role_ratings_df['ath']['olr1'])
        self.spinBox_R1_SPD_OL.setValue(myconfig.role_ratings_df['spd']['olr1'])
        self.spinBox_R1_DUR_OL.setValue(myconfig.role_ratings_df['dur']['olr1'])
        self.spinBox_R1_WE_OL.setValue(myconfig.role_ratings_df['we']['olr1'])
        self.spinBox_R1_STA_OL.setValue(myconfig.role_ratings_df['sta']['olr1'])
        self.spinBox_R1_STR_OL.setValue(myconfig.role_ratings_df['str']['olr1'])
        self.spinBox_R1_BLK_OL.setValue(myconfig.role_ratings_df['blk']['olr1'])
        self.spinBox_R1_TKL_OL.setValue(myconfig.role_ratings_df['tkl']['olr1'])
        self.spinBox_R1_HAN_OL.setValue(myconfig.role_ratings_df['han']['olr1'])
        self.spinBox_R1_GI_OL.setValue(myconfig.role_ratings_df['gi']['olr1'])
        self.spinBox_R1_ELU_OL.setValue(myconfig.role_ratings_df['elu']['olr1'])
        self.spinBox_R1_TEC_OL.setValue(myconfig.role_ratings_df['tec']['olr1'])
        self.lcdNumber_R1_OL.display(myconfig.role_ratings_df['total']['olr1'])
        self.spinBox_R1_ATH_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_SPD_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_DUR_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_WE_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STA_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STR_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_BLK_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TKL_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_HAN_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_GI_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_ELU_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TEC_OL.valueChanged.connect(self.update_row_total)

        self.lineEdit_R2_OL.setText(myconfig.role_ratings_df['label']['olr2'])
        self.spinBox_R2_ATH_OL.setValue(myconfig.role_ratings_df['ath']['olr2'])
        self.spinBox_R2_SPD_OL.setValue(myconfig.role_ratings_df['spd']['olr2'])
        self.spinBox_R2_DUR_OL.setValue(myconfig.role_ratings_df['dur']['olr2'])
        self.spinBox_R2_WE_OL.setValue(myconfig.role_ratings_df['we']['olr2'])
        self.spinBox_R2_STA_OL.setValue(myconfig.role_ratings_df['sta']['olr2'])
        self.spinBox_R2_STR_OL.setValue(myconfig.role_ratings_df['str']['olr2'])
        self.spinBox_R2_BLK_OL.setValue(myconfig.role_ratings_df['blk']['olr2'])
        self.spinBox_R2_TKL_OL.setValue(myconfig.role_ratings_df['tkl']['olr2'])
        self.spinBox_R2_HAN_OL.setValue(myconfig.role_ratings_df['han']['olr2'])
        self.spinBox_R2_GI_OL.setValue(myconfig.role_ratings_df['gi']['olr2'])
        self.spinBox_R2_ELU_OL.setValue(myconfig.role_ratings_df['elu']['olr2'])
        self.spinBox_R2_TEC_OL.setValue(myconfig.role_ratings_df['tec']['olr2'])
        self.lcdNumber_R2_OL.display(myconfig.role_ratings_df['total']['olr2'])
        self.spinBox_R2_ATH_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_SPD_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_DUR_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_WE_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STA_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STR_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_BLK_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TKL_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_HAN_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_GI_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_ELU_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TEC_OL.valueChanged.connect(self.update_row_total)

        self.lineEdit_R3_OL.setText(myconfig.role_ratings_df['label']['olr3'])
        self.spinBox_R3_ATH_OL.setValue(myconfig.role_ratings_df['ath']['olr3'])
        self.spinBox_R3_SPD_OL.setValue(myconfig.role_ratings_df['spd']['olr3'])
        self.spinBox_R3_DUR_OL.setValue(myconfig.role_ratings_df['dur']['olr3'])
        self.spinBox_R3_WE_OL.setValue(myconfig.role_ratings_df['we']['olr3'])
        self.spinBox_R3_STA_OL.setValue(myconfig.role_ratings_df['sta']['olr3'])
        self.spinBox_R3_STR_OL.setValue(myconfig.role_ratings_df['str']['olr3'])
        self.spinBox_R3_BLK_OL.setValue(myconfig.role_ratings_df['blk']['olr3'])
        self.spinBox_R3_TKL_OL.setValue(myconfig.role_ratings_df['tkl']['olr3'])
        self.spinBox_R3_HAN_OL.setValue(myconfig.role_ratings_df['han']['olr3'])
        self.spinBox_R3_GI_OL.setValue(myconfig.role_ratings_df['gi']['olr3'])
        self.spinBox_R3_ELU_OL.setValue(myconfig.role_ratings_df['elu']['olr3'])
        self.spinBox_R3_TEC_OL.setValue(myconfig.role_ratings_df['tec']['olr3'])
        self.lcdNumber_R3_OL.display(myconfig.role_ratings_df['total']['olr3'])
        self.spinBox_R3_ATH_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_SPD_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_DUR_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_WE_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STA_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STR_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_BLK_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TKL_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_HAN_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_GI_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_ELU_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TEC_OL.valueChanged.connect(self.update_row_total)

        self.lineEdit_R4_OL.setText(myconfig.role_ratings_df['label']['olr4'])
        self.spinBox_R4_ATH_OL.setValue(myconfig.role_ratings_df['ath']['olr4'])
        self.spinBox_R4_SPD_OL.setValue(myconfig.role_ratings_df['spd']['olr4'])
        self.spinBox_R4_DUR_OL.setValue(myconfig.role_ratings_df['dur']['olr4'])
        self.spinBox_R4_WE_OL.setValue(myconfig.role_ratings_df['we']['olr4'])
        self.spinBox_R4_STA_OL.setValue(myconfig.role_ratings_df['sta']['olr4'])
        self.spinBox_R4_STR_OL.setValue(myconfig.role_ratings_df['str']['olr4'])
        self.spinBox_R4_BLK_OL.setValue(myconfig.role_ratings_df['blk']['olr4'])
        self.spinBox_R4_TKL_OL.setValue(myconfig.role_ratings_df['tkl']['olr4'])
        self.spinBox_R4_HAN_OL.setValue(myconfig.role_ratings_df['han']['olr4'])
        self.spinBox_R4_GI_OL.setValue(myconfig.role_ratings_df['gi']['olr4'])
        self.spinBox_R4_ELU_OL.setValue(myconfig.role_ratings_df['elu']['olr4'])
        self.spinBox_R4_TEC_OL.setValue(myconfig.role_ratings_df['tec']['olr4'])
        self.lcdNumber_R4_OL.display(myconfig.role_ratings_df['total']['olr4'])
        self.spinBox_R4_ATH_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_SPD_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_DUR_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_WE_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STA_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STR_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_BLK_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TKL_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_HAN_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_GI_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_ELU_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TEC_OL.valueChanged.connect(self.update_row_total)

        self.lineEdit_R5_OL.setText(myconfig.role_ratings_df['label']['olr5'])
        self.spinBox_R5_ATH_OL.setValue(myconfig.role_ratings_df['ath']['olr5'])
        self.spinBox_R5_SPD_OL.setValue(myconfig.role_ratings_df['spd']['olr5'])
        self.spinBox_R5_DUR_OL.setValue(myconfig.role_ratings_df['dur']['olr5'])
        self.spinBox_R5_WE_OL.setValue(myconfig.role_ratings_df['we']['olr5'])
        self.spinBox_R5_STA_OL.setValue(myconfig.role_ratings_df['sta']['olr5'])
        self.spinBox_R5_STR_OL.setValue(myconfig.role_ratings_df['str']['olr5'])
        self.spinBox_R5_BLK_OL.setValue(myconfig.role_ratings_df['blk']['olr5'])
        self.spinBox_R5_TKL_OL.setValue(myconfig.role_ratings_df['tkl']['olr5'])
        self.spinBox_R5_HAN_OL.setValue(myconfig.role_ratings_df['han']['olr5'])
        self.spinBox_R5_GI_OL.setValue(myconfig.role_ratings_df['gi']['olr5'])
        self.spinBox_R5_ELU_OL.setValue(myconfig.role_ratings_df['elu']['olr5'])
        self.spinBox_R5_TEC_OL.setValue(myconfig.role_ratings_df['tec']['olr5'])
        self.lcdNumber_R5_OL.display(myconfig.role_ratings_df['total']['olr5'])
        self.spinBox_R5_ATH_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_SPD_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_DUR_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_WE_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STA_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STR_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_BLK_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TKL_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_HAN_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_GI_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_ELU_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TEC_OL.valueChanged.connect(self.update_row_total)

        self.lineEdit_R6_OL.setText(myconfig.role_ratings_df['label']['olr6'])
        self.spinBox_R6_ATH_OL.setValue(myconfig.role_ratings_df['ath']['olr6'])
        self.spinBox_R6_SPD_OL.setValue(myconfig.role_ratings_df['spd']['olr6'])
        self.spinBox_R6_DUR_OL.setValue(myconfig.role_ratings_df['dur']['olr6'])
        self.spinBox_R6_WE_OL.setValue(myconfig.role_ratings_df['we']['olr6'])
        self.spinBox_R6_STA_OL.setValue(myconfig.role_ratings_df['sta']['olr6'])
        self.spinBox_R6_STR_OL.setValue(myconfig.role_ratings_df['str']['olr6'])
        self.spinBox_R6_BLK_OL.setValue(myconfig.role_ratings_df['blk']['olr6'])
        self.spinBox_R6_TKL_OL.setValue(myconfig.role_ratings_df['tkl']['olr6'])
        self.spinBox_R6_HAN_OL.setValue(myconfig.role_ratings_df['han']['olr6'])
        self.spinBox_R6_GI_OL.setValue(myconfig.role_ratings_df['gi']['olr6'])
        self.spinBox_R6_ELU_OL.setValue(myconfig.role_ratings_df['elu']['olr6'])
        self.spinBox_R6_TEC_OL.setValue(myconfig.role_ratings_df['tec']['olr6'])
        self.lcdNumber_R6_OL.display(myconfig.role_ratings_df['total']['olr6'])
        self.spinBox_R6_ATH_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_SPD_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_DUR_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_WE_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STA_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STR_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_BLK_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TKL_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_HAN_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_GI_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_ELU_OL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TEC_OL.valueChanged.connect(self.update_row_total)

        # DL Section
        self.lineEdit_R1_DL.setText(myconfig.role_ratings_df['label']['dlr1'])
        self.spinBox_R1_ATH_DL.setValue(myconfig.role_ratings_df['ath']['dlr1'])
        self.spinBox_R1_SPD_DL.setValue(myconfig.role_ratings_df['spd']['dlr1'])
        self.spinBox_R1_DUR_DL.setValue(myconfig.role_ratings_df['dur']['dlr1'])
        self.spinBox_R1_WE_DL.setValue(myconfig.role_ratings_df['we']['dlr1'])
        self.spinBox_R1_STA_DL.setValue(myconfig.role_ratings_df['sta']['dlr1'])
        self.spinBox_R1_STR_DL.setValue(myconfig.role_ratings_df['str']['dlr1'])
        self.spinBox_R1_BLK_DL.setValue(myconfig.role_ratings_df['blk']['dlr1'])
        self.spinBox_R1_TKL_DL.setValue(myconfig.role_ratings_df['tkl']['dlr1'])
        self.spinBox_R1_HAN_DL.setValue(myconfig.role_ratings_df['han']['dlr1'])
        self.spinBox_R1_GI_DL.setValue(myconfig.role_ratings_df['gi']['dlr1'])
        self.spinBox_R1_ELU_DL.setValue(myconfig.role_ratings_df['elu']['dlr1'])
        self.spinBox_R1_TEC_DL.setValue(myconfig.role_ratings_df['tec']['dlr1'])
        self.lcdNumber_R1_DL.display(myconfig.role_ratings_df['total']['dlr1'])
        self.spinBox_R1_ATH_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_SPD_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_DUR_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_WE_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STA_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STR_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_BLK_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TKL_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_HAN_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_GI_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_ELU_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TEC_DL.valueChanged.connect(self.update_row_total)

        self.lineEdit_R2_DL.setText(myconfig.role_ratings_df['label']['dlr2'])
        self.spinBox_R2_ATH_DL.setValue(myconfig.role_ratings_df['ath']['dlr2'])
        self.spinBox_R2_SPD_DL.setValue(myconfig.role_ratings_df['spd']['dlr2'])
        self.spinBox_R2_DUR_DL.setValue(myconfig.role_ratings_df['dur']['dlr2'])
        self.spinBox_R2_WE_DL.setValue(myconfig.role_ratings_df['we']['dlr2'])
        self.spinBox_R2_STA_DL.setValue(myconfig.role_ratings_df['sta']['dlr2'])
        self.spinBox_R2_STR_DL.setValue(myconfig.role_ratings_df['str']['dlr2'])
        self.spinBox_R2_BLK_DL.setValue(myconfig.role_ratings_df['blk']['dlr2'])
        self.spinBox_R2_TKL_DL.setValue(myconfig.role_ratings_df['tkl']['dlr2'])
        self.spinBox_R2_HAN_DL.setValue(myconfig.role_ratings_df['han']['dlr2'])
        self.spinBox_R2_GI_DL.setValue(myconfig.role_ratings_df['gi']['dlr2'])
        self.spinBox_R2_ELU_DL.setValue(myconfig.role_ratings_df['elu']['dlr2'])
        self.spinBox_R2_TEC_DL.setValue(myconfig.role_ratings_df['tec']['dlr2'])
        self.lcdNumber_R2_DL.display(myconfig.role_ratings_df['total']['dlr2'])
        self.spinBox_R2_ATH_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_SPD_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_DUR_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_WE_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STA_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STR_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_BLK_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TKL_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_HAN_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_GI_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_ELU_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TEC_DL.valueChanged.connect(self.update_row_total)

        self.lineEdit_R3_DL.setText(myconfig.role_ratings_df['label']['dlr3'])
        self.spinBox_R3_ATH_DL.setValue(myconfig.role_ratings_df['ath']['dlr3'])
        self.spinBox_R3_SPD_DL.setValue(myconfig.role_ratings_df['spd']['dlr3'])
        self.spinBox_R3_DUR_DL.setValue(myconfig.role_ratings_df['dur']['dlr3'])
        self.spinBox_R3_WE_DL.setValue(myconfig.role_ratings_df['we']['dlr3'])
        self.spinBox_R3_STA_DL.setValue(myconfig.role_ratings_df['sta']['dlr3'])
        self.spinBox_R3_STR_DL.setValue(myconfig.role_ratings_df['str']['dlr3'])
        self.spinBox_R3_BLK_DL.setValue(myconfig.role_ratings_df['blk']['dlr3'])
        self.spinBox_R3_TKL_DL.setValue(myconfig.role_ratings_df['tkl']['dlr3'])
        self.spinBox_R3_HAN_DL.setValue(myconfig.role_ratings_df['han']['dlr3'])
        self.spinBox_R3_GI_DL.setValue(myconfig.role_ratings_df['gi']['dlr3'])
        self.spinBox_R3_ELU_DL.setValue(myconfig.role_ratings_df['elu']['dlr3'])
        self.spinBox_R3_TEC_DL.setValue(myconfig.role_ratings_df['tec']['dlr3'])
        self.lcdNumber_R3_DL.display(myconfig.role_ratings_df['total']['dlr3'])
        self.spinBox_R3_ATH_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_SPD_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_DUR_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_WE_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STA_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STR_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_BLK_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TKL_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_HAN_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_GI_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_ELU_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TEC_DL.valueChanged.connect(self.update_row_total)

        self.lineEdit_R4_DL.setText(myconfig.role_ratings_df['label']['dlr4'])
        self.spinBox_R4_ATH_DL.setValue(myconfig.role_ratings_df['ath']['dlr4'])
        self.spinBox_R4_SPD_DL.setValue(myconfig.role_ratings_df['spd']['dlr4'])
        self.spinBox_R4_DUR_DL.setValue(myconfig.role_ratings_df['dur']['dlr4'])
        self.spinBox_R4_WE_DL.setValue(myconfig.role_ratings_df['we']['dlr4'])
        self.spinBox_R4_STA_DL.setValue(myconfig.role_ratings_df['sta']['dlr4'])
        self.spinBox_R4_STR_DL.setValue(myconfig.role_ratings_df['str']['dlr4'])
        self.spinBox_R4_BLK_DL.setValue(myconfig.role_ratings_df['blk']['dlr4'])
        self.spinBox_R4_TKL_DL.setValue(myconfig.role_ratings_df['tkl']['dlr4'])
        self.spinBox_R4_HAN_DL.setValue(myconfig.role_ratings_df['han']['dlr4'])
        self.spinBox_R4_GI_DL.setValue(myconfig.role_ratings_df['gi']['dlr4'])
        self.spinBox_R4_ELU_DL.setValue(myconfig.role_ratings_df['elu']['dlr4'])
        self.spinBox_R4_TEC_DL.setValue(myconfig.role_ratings_df['tec']['dlr4'])
        self.lcdNumber_R4_DL.display(myconfig.role_ratings_df['total']['dlr4'])
        self.spinBox_R4_ATH_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_SPD_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_DUR_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_WE_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STA_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STR_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_BLK_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TKL_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_HAN_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_GI_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_ELU_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TEC_DL.valueChanged.connect(self.update_row_total)

        self.lineEdit_R5_DL.setText(myconfig.role_ratings_df['label']['dlr5'])
        self.spinBox_R5_ATH_DL.setValue(myconfig.role_ratings_df['ath']['dlr5'])
        self.spinBox_R5_SPD_DL.setValue(myconfig.role_ratings_df['spd']['dlr5'])
        self.spinBox_R5_DUR_DL.setValue(myconfig.role_ratings_df['dur']['dlr5'])
        self.spinBox_R5_WE_DL.setValue(myconfig.role_ratings_df['we']['dlr5'])
        self.spinBox_R5_STA_DL.setValue(myconfig.role_ratings_df['sta']['dlr5'])
        self.spinBox_R5_STR_DL.setValue(myconfig.role_ratings_df['str']['dlr5'])
        self.spinBox_R5_BLK_DL.setValue(myconfig.role_ratings_df['blk']['dlr5'])
        self.spinBox_R5_TKL_DL.setValue(myconfig.role_ratings_df['tkl']['dlr5'])
        self.spinBox_R5_HAN_DL.setValue(myconfig.role_ratings_df['han']['dlr5'])
        self.spinBox_R5_GI_DL.setValue(myconfig.role_ratings_df['gi']['dlr5'])
        self.spinBox_R5_ELU_DL.setValue(myconfig.role_ratings_df['elu']['dlr5'])
        self.spinBox_R5_TEC_DL.setValue(myconfig.role_ratings_df['tec']['dlr5'])
        self.lcdNumber_R5_DL.display(myconfig.role_ratings_df['total']['dlr5'])
        self.spinBox_R5_ATH_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_SPD_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_DUR_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_WE_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STA_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STR_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_BLK_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TKL_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_HAN_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_GI_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_ELU_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TEC_DL.valueChanged.connect(self.update_row_total)

        self.lineEdit_R6_DL.setText(myconfig.role_ratings_df['label']['dlr6'])
        self.spinBox_R6_ATH_DL.setValue(myconfig.role_ratings_df['ath']['dlr6'])
        self.spinBox_R6_SPD_DL.setValue(myconfig.role_ratings_df['spd']['dlr6'])
        self.spinBox_R6_DUR_DL.setValue(myconfig.role_ratings_df['dur']['dlr6'])
        self.spinBox_R6_WE_DL.setValue(myconfig.role_ratings_df['we']['dlr6'])
        self.spinBox_R6_STA_DL.setValue(myconfig.role_ratings_df['sta']['dlr6'])
        self.spinBox_R6_STR_DL.setValue(myconfig.role_ratings_df['str']['dlr6'])
        self.spinBox_R6_BLK_DL.setValue(myconfig.role_ratings_df['blk']['dlr6'])
        self.spinBox_R6_TKL_DL.setValue(myconfig.role_ratings_df['tkl']['dlr6'])
        self.spinBox_R6_HAN_DL.setValue(myconfig.role_ratings_df['han']['dlr6'])
        self.spinBox_R6_GI_DL.setValue(myconfig.role_ratings_df['gi']['dlr6'])
        self.spinBox_R6_ELU_DL.setValue(myconfig.role_ratings_df['elu']['dlr6'])
        self.spinBox_R6_TEC_DL.setValue(myconfig.role_ratings_df['tec']['dlr6'])
        self.lcdNumber_R6_DL.display(myconfig.role_ratings_df['total']['dlr6'])
        self.spinBox_R6_ATH_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_SPD_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_DUR_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_WE_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STA_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STR_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_BLK_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TKL_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_HAN_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_GI_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_ELU_DL.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TEC_DL.valueChanged.connect(self.update_row_total)

        # LB Section
        self.lineEdit_R1_LB.setText(myconfig.role_ratings_df['label']['lbr1'])
        self.spinBox_R1_ATH_LB.setValue(myconfig.role_ratings_df['ath']['lbr1'])
        self.spinBox_R1_SPD_LB.setValue(myconfig.role_ratings_df['spd']['lbr1'])
        self.spinBox_R1_DUR_LB.setValue(myconfig.role_ratings_df['dur']['lbr1'])
        self.spinBox_R1_WE_LB.setValue(myconfig.role_ratings_df['we']['lbr1'])
        self.spinBox_R1_STA_LB.setValue(myconfig.role_ratings_df['sta']['lbr1'])
        self.spinBox_R1_STR_LB.setValue(myconfig.role_ratings_df['str']['lbr1'])
        self.spinBox_R1_BLK_LB.setValue(myconfig.role_ratings_df['blk']['lbr1'])
        self.spinBox_R1_TKL_LB.setValue(myconfig.role_ratings_df['tkl']['lbr1'])
        self.spinBox_R1_HAN_LB.setValue(myconfig.role_ratings_df['han']['lbr1'])
        self.spinBox_R1_GI_LB.setValue(myconfig.role_ratings_df['gi']['lbr1'])
        self.spinBox_R1_ELU_LB.setValue(myconfig.role_ratings_df['elu']['lbr1'])
        self.spinBox_R1_TEC_LB.setValue(myconfig.role_ratings_df['tec']['lbr1'])
        self.lcdNumber_R1_LB.display(myconfig.role_ratings_df['total']['lbr1'])
        self.spinBox_R1_ATH_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_SPD_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_DUR_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_WE_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STA_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STR_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_BLK_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TKL_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_HAN_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_GI_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_ELU_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TEC_LB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R2_LB.setText(myconfig.role_ratings_df['label']['lbr2'])
        self.spinBox_R2_ATH_LB.setValue(myconfig.role_ratings_df['ath']['lbr2'])
        self.spinBox_R2_SPD_LB.setValue(myconfig.role_ratings_df['spd']['lbr2'])
        self.spinBox_R2_DUR_LB.setValue(myconfig.role_ratings_df['dur']['lbr2'])
        self.spinBox_R2_WE_LB.setValue(myconfig.role_ratings_df['we']['lbr2'])
        self.spinBox_R2_STA_LB.setValue(myconfig.role_ratings_df['sta']['lbr2'])
        self.spinBox_R2_STR_LB.setValue(myconfig.role_ratings_df['str']['lbr2'])
        self.spinBox_R2_BLK_LB.setValue(myconfig.role_ratings_df['blk']['lbr2'])
        self.spinBox_R2_TKL_LB.setValue(myconfig.role_ratings_df['tkl']['lbr2'])
        self.spinBox_R2_HAN_LB.setValue(myconfig.role_ratings_df['han']['lbr2'])
        self.spinBox_R2_GI_LB.setValue(myconfig.role_ratings_df['gi']['lbr2'])
        self.spinBox_R2_ELU_LB.setValue(myconfig.role_ratings_df['elu']['lbr2'])
        self.spinBox_R2_TEC_LB.setValue(myconfig.role_ratings_df['tec']['lbr2'])
        self.lcdNumber_R2_LB.display(myconfig.role_ratings_df['total']['lbr2'])
        self.spinBox_R2_ATH_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_SPD_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_DUR_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_WE_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STA_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STR_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_BLK_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TKL_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_HAN_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_GI_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_ELU_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TEC_LB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R3_LB.setText(myconfig.role_ratings_df['label']['lbr3'])
        self.spinBox_R3_ATH_LB.setValue(myconfig.role_ratings_df['ath']['lbr3'])
        self.spinBox_R3_SPD_LB.setValue(myconfig.role_ratings_df['spd']['lbr3'])
        self.spinBox_R3_DUR_LB.setValue(myconfig.role_ratings_df['dur']['lbr3'])
        self.spinBox_R3_WE_LB.setValue(myconfig.role_ratings_df['we']['lbr3'])
        self.spinBox_R3_STA_LB.setValue(myconfig.role_ratings_df['sta']['lbr3'])
        self.spinBox_R3_STR_LB.setValue(myconfig.role_ratings_df['str']['lbr3'])
        self.spinBox_R3_BLK_LB.setValue(myconfig.role_ratings_df['blk']['lbr3'])
        self.spinBox_R3_TKL_LB.setValue(myconfig.role_ratings_df['tkl']['lbr3'])
        self.spinBox_R3_HAN_LB.setValue(myconfig.role_ratings_df['han']['lbr3'])
        self.spinBox_R3_GI_LB.setValue(myconfig.role_ratings_df['gi']['lbr3'])
        self.spinBox_R3_ELU_LB.setValue(myconfig.role_ratings_df['elu']['lbr3'])
        self.spinBox_R3_TEC_LB.setValue(myconfig.role_ratings_df['tec']['lbr3'])
        self.lcdNumber_R3_LB.display(myconfig.role_ratings_df['total']['lbr3'])
        self.spinBox_R3_ATH_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_SPD_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_DUR_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_WE_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STA_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STR_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_BLK_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TKL_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_HAN_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_GI_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_ELU_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TEC_LB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R4_LB.setText(myconfig.role_ratings_df['label']['lbr4'])
        self.spinBox_R4_ATH_LB.setValue(myconfig.role_ratings_df['ath']['lbr4'])
        self.spinBox_R4_SPD_LB.setValue(myconfig.role_ratings_df['spd']['lbr4'])
        self.spinBox_R4_DUR_LB.setValue(myconfig.role_ratings_df['dur']['lbr4'])
        self.spinBox_R4_WE_LB.setValue(myconfig.role_ratings_df['we']['lbr4'])
        self.spinBox_R4_STA_LB.setValue(myconfig.role_ratings_df['sta']['lbr4'])
        self.spinBox_R4_STR_LB.setValue(myconfig.role_ratings_df['str']['lbr4'])
        self.spinBox_R4_BLK_LB.setValue(myconfig.role_ratings_df['blk']['lbr4'])
        self.spinBox_R4_TKL_LB.setValue(myconfig.role_ratings_df['tkl']['lbr4'])
        self.spinBox_R4_HAN_LB.setValue(myconfig.role_ratings_df['han']['lbr4'])
        self.spinBox_R4_GI_LB.setValue(myconfig.role_ratings_df['gi']['lbr4'])
        self.spinBox_R4_ELU_LB.setValue(myconfig.role_ratings_df['elu']['lbr4'])
        self.spinBox_R4_TEC_LB.setValue(myconfig.role_ratings_df['tec']['lbr4'])
        self.lcdNumber_R4_LB.display(myconfig.role_ratings_df['total']['lbr4'])
        self.spinBox_R4_ATH_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_SPD_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_DUR_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_WE_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STA_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STR_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_BLK_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TKL_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_HAN_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_GI_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_ELU_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TEC_LB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R5_LB.setText(myconfig.role_ratings_df['label']['lbr5'])
        self.spinBox_R5_ATH_LB.setValue(myconfig.role_ratings_df['ath']['lbr5'])
        self.spinBox_R5_SPD_LB.setValue(myconfig.role_ratings_df['spd']['lbr5'])
        self.spinBox_R5_DUR_LB.setValue(myconfig.role_ratings_df['dur']['lbr5'])
        self.spinBox_R5_WE_LB.setValue(myconfig.role_ratings_df['we']['lbr5'])
        self.spinBox_R5_STA_LB.setValue(myconfig.role_ratings_df['sta']['lbr5'])
        self.spinBox_R5_STR_LB.setValue(myconfig.role_ratings_df['str']['lbr5'])
        self.spinBox_R5_BLK_LB.setValue(myconfig.role_ratings_df['blk']['lbr5'])
        self.spinBox_R5_TKL_LB.setValue(myconfig.role_ratings_df['tkl']['lbr5'])
        self.spinBox_R5_HAN_LB.setValue(myconfig.role_ratings_df['han']['lbr5'])
        self.spinBox_R5_GI_LB.setValue(myconfig.role_ratings_df['gi']['lbr5'])
        self.spinBox_R5_ELU_LB.setValue(myconfig.role_ratings_df['elu']['lbr5'])
        self.spinBox_R5_TEC_LB.setValue(myconfig.role_ratings_df['tec']['lbr5'])
        self.lcdNumber_R5_LB.display(myconfig.role_ratings_df['total']['lbr5'])
        self.spinBox_R5_ATH_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_SPD_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_DUR_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_WE_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STA_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STR_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_BLK_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TKL_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_HAN_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_GI_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_ELU_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TEC_LB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R6_LB.setText(myconfig.role_ratings_df['label']['lbr6'])
        self.spinBox_R6_ATH_LB.setValue(myconfig.role_ratings_df['ath']['lbr6'])
        self.spinBox_R6_SPD_LB.setValue(myconfig.role_ratings_df['spd']['lbr6'])
        self.spinBox_R6_DUR_LB.setValue(myconfig.role_ratings_df['dur']['lbr6'])
        self.spinBox_R6_WE_LB.setValue(myconfig.role_ratings_df['we']['lbr6'])
        self.spinBox_R6_STA_LB.setValue(myconfig.role_ratings_df['sta']['lbr6'])
        self.spinBox_R6_STR_LB.setValue(myconfig.role_ratings_df['str']['lbr6'])
        self.spinBox_R6_BLK_LB.setValue(myconfig.role_ratings_df['blk']['lbr6'])
        self.spinBox_R6_TKL_LB.setValue(myconfig.role_ratings_df['tkl']['lbr6'])
        self.spinBox_R6_HAN_LB.setValue(myconfig.role_ratings_df['han']['lbr6'])
        self.spinBox_R6_GI_LB.setValue(myconfig.role_ratings_df['gi']['lbr6'])
        self.spinBox_R6_ELU_LB.setValue(myconfig.role_ratings_df['elu']['lbr6'])
        self.spinBox_R6_TEC_LB.setValue(myconfig.role_ratings_df['tec']['lbr6'])
        self.lcdNumber_R6_LB.display(myconfig.role_ratings_df['total']['lbr6'])
        self.spinBox_R6_ATH_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_SPD_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_DUR_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_WE_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STA_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STR_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_BLK_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TKL_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_HAN_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_GI_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_ELU_LB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TEC_LB.valueChanged.connect(self.update_row_total)

        # DB Section
        self.lineEdit_R1_DB.setText(myconfig.role_ratings_df['label']['dbr1'])
        self.spinBox_R1_ATH_DB.setValue(myconfig.role_ratings_df['ath']['dbr1'])
        self.spinBox_R1_SPD_DB.setValue(myconfig.role_ratings_df['spd']['dbr1'])
        self.spinBox_R1_DUR_DB.setValue(myconfig.role_ratings_df['dur']['dbr1'])
        self.spinBox_R1_WE_DB.setValue(myconfig.role_ratings_df['we']['dbr1'])
        self.spinBox_R1_STA_DB.setValue(myconfig.role_ratings_df['sta']['dbr1'])
        self.spinBox_R1_STR_DB.setValue(myconfig.role_ratings_df['str']['dbr1'])
        self.spinBox_R1_BLK_DB.setValue(myconfig.role_ratings_df['blk']['dbr1'])
        self.spinBox_R1_TKL_DB.setValue(myconfig.role_ratings_df['tkl']['dbr1'])
        self.spinBox_R1_HAN_DB.setValue(myconfig.role_ratings_df['han']['dbr1'])
        self.spinBox_R1_GI_DB.setValue(myconfig.role_ratings_df['gi']['dbr1'])
        self.spinBox_R1_ELU_DB.setValue(myconfig.role_ratings_df['elu']['dbr1'])
        self.spinBox_R1_TEC_DB.setValue(myconfig.role_ratings_df['tec']['dbr1'])
        self.lcdNumber_R1_DB.display(myconfig.role_ratings_df['total']['dbr1'])
        self.spinBox_R1_ATH_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_SPD_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_DUR_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_WE_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STA_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STR_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_BLK_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TKL_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_HAN_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_GI_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_ELU_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TEC_DB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R2_DB.setText(myconfig.role_ratings_df['label']['dbr2'])
        self.spinBox_R2_ATH_DB.setValue(myconfig.role_ratings_df['ath']['dbr2'])
        self.spinBox_R2_SPD_DB.setValue(myconfig.role_ratings_df['spd']['dbr2'])
        self.spinBox_R2_DUR_DB.setValue(myconfig.role_ratings_df['dur']['dbr2'])
        self.spinBox_R2_WE_DB.setValue(myconfig.role_ratings_df['we']['dbr2'])
        self.spinBox_R2_STA_DB.setValue(myconfig.role_ratings_df['sta']['dbr2'])
        self.spinBox_R2_STR_DB.setValue(myconfig.role_ratings_df['str']['dbr2'])
        self.spinBox_R2_BLK_DB.setValue(myconfig.role_ratings_df['blk']['dbr2'])
        self.spinBox_R2_TKL_DB.setValue(myconfig.role_ratings_df['tkl']['dbr2'])
        self.spinBox_R2_HAN_DB.setValue(myconfig.role_ratings_df['han']['dbr2'])
        self.spinBox_R2_GI_DB.setValue(myconfig.role_ratings_df['gi']['dbr2'])
        self.spinBox_R2_ELU_DB.setValue(myconfig.role_ratings_df['elu']['dbr2'])
        self.spinBox_R2_TEC_DB.setValue(myconfig.role_ratings_df['tec']['dbr2'])
        self.lcdNumber_R2_DB.display(myconfig.role_ratings_df['total']['dbr2'])
        self.spinBox_R2_ATH_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_SPD_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_DUR_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_WE_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STA_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STR_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_BLK_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TKL_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_HAN_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_GI_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_ELU_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TEC_DB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R3_DB.setText(myconfig.role_ratings_df['label']['dbr3'])
        self.spinBox_R3_ATH_DB.setValue(myconfig.role_ratings_df['ath']['dbr3'])
        self.spinBox_R3_SPD_DB.setValue(myconfig.role_ratings_df['spd']['dbr3'])
        self.spinBox_R3_DUR_DB.setValue(myconfig.role_ratings_df['dur']['dbr3'])
        self.spinBox_R3_WE_DB.setValue(myconfig.role_ratings_df['we']['dbr3'])
        self.spinBox_R3_STA_DB.setValue(myconfig.role_ratings_df['sta']['dbr3'])
        self.spinBox_R3_STR_DB.setValue(myconfig.role_ratings_df['str']['dbr3'])
        self.spinBox_R3_BLK_DB.setValue(myconfig.role_ratings_df['blk']['dbr3'])
        self.spinBox_R3_TKL_DB.setValue(myconfig.role_ratings_df['tkl']['dbr3'])
        self.spinBox_R3_HAN_DB.setValue(myconfig.role_ratings_df['han']['dbr3'])
        self.spinBox_R3_GI_DB.setValue(myconfig.role_ratings_df['gi']['dbr3'])
        self.spinBox_R3_ELU_DB.setValue(myconfig.role_ratings_df['elu']['dbr3'])
        self.spinBox_R3_TEC_DB.setValue(myconfig.role_ratings_df['tec']['dbr3'])
        self.lcdNumber_R3_DB.display(myconfig.role_ratings_df['total']['dbr3'])
        self.spinBox_R3_ATH_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_SPD_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_DUR_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_WE_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STA_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STR_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_BLK_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TKL_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_HAN_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_GI_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_ELU_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TEC_DB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R4_DB.setText(myconfig.role_ratings_df['label']['dbr4'])
        self.spinBox_R4_ATH_DB.setValue(myconfig.role_ratings_df['ath']['dbr4'])
        self.spinBox_R4_SPD_DB.setValue(myconfig.role_ratings_df['spd']['dbr4'])
        self.spinBox_R4_DUR_DB.setValue(myconfig.role_ratings_df['dur']['dbr4'])
        self.spinBox_R4_WE_DB.setValue(myconfig.role_ratings_df['we']['dbr4'])
        self.spinBox_R4_STA_DB.setValue(myconfig.role_ratings_df['sta']['dbr4'])
        self.spinBox_R4_STR_DB.setValue(myconfig.role_ratings_df['str']['dbr4'])
        self.spinBox_R4_BLK_DB.setValue(myconfig.role_ratings_df['blk']['dbr4'])
        self.spinBox_R4_TKL_DB.setValue(myconfig.role_ratings_df['tkl']['dbr4'])
        self.spinBox_R4_HAN_DB.setValue(myconfig.role_ratings_df['han']['dbr4'])
        self.spinBox_R4_GI_DB.setValue(myconfig.role_ratings_df['gi']['dbr4'])
        self.spinBox_R4_ELU_DB.setValue(myconfig.role_ratings_df['elu']['dbr4'])
        self.spinBox_R4_TEC_DB.setValue(myconfig.role_ratings_df['tec']['dbr4'])
        self.lcdNumber_R4_DB.display(myconfig.role_ratings_df['total']['dbr4'])
        self.spinBox_R4_ATH_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_SPD_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_DUR_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_WE_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STA_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STR_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_BLK_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TKL_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_HAN_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_GI_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_ELU_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TEC_DB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R5_DB.setText(myconfig.role_ratings_df['label']['dbr5'])
        self.spinBox_R5_ATH_DB.setValue(myconfig.role_ratings_df['ath']['dbr5'])
        self.spinBox_R5_SPD_DB.setValue(myconfig.role_ratings_df['spd']['dbr5'])
        self.spinBox_R5_DUR_DB.setValue(myconfig.role_ratings_df['dur']['dbr5'])
        self.spinBox_R5_WE_DB.setValue(myconfig.role_ratings_df['we']['dbr5'])
        self.spinBox_R5_STA_DB.setValue(myconfig.role_ratings_df['sta']['dbr5'])
        self.spinBox_R5_STR_DB.setValue(myconfig.role_ratings_df['str']['dbr5'])
        self.spinBox_R5_BLK_DB.setValue(myconfig.role_ratings_df['blk']['dbr5'])
        self.spinBox_R5_TKL_DB.setValue(myconfig.role_ratings_df['tkl']['dbr5'])
        self.spinBox_R5_HAN_DB.setValue(myconfig.role_ratings_df['han']['dbr5'])
        self.spinBox_R5_GI_DB.setValue(myconfig.role_ratings_df['gi']['dbr5'])
        self.spinBox_R5_ELU_DB.setValue(myconfig.role_ratings_df['elu']['dbr5'])
        self.spinBox_R5_TEC_DB.setValue(myconfig.role_ratings_df['tec']['dbr5'])
        self.lcdNumber_R5_DB.display(myconfig.role_ratings_df['total']['dbr5'])
        self.spinBox_R5_ATH_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_SPD_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_DUR_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_WE_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STA_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STR_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_BLK_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TKL_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_HAN_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_GI_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_ELU_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TEC_DB.valueChanged.connect(self.update_row_total)

        self.lineEdit_R6_DB.setText(myconfig.role_ratings_df['label']['dbr6'])
        self.spinBox_R6_ATH_DB.setValue(myconfig.role_ratings_df['ath']['dbr6'])
        self.spinBox_R6_SPD_DB.setValue(myconfig.role_ratings_df['spd']['dbr6'])
        self.spinBox_R6_DUR_DB.setValue(myconfig.role_ratings_df['dur']['dbr6'])
        self.spinBox_R6_WE_DB.setValue(myconfig.role_ratings_df['we']['dbr6'])
        self.spinBox_R6_STA_DB.setValue(myconfig.role_ratings_df['sta']['dbr6'])
        self.spinBox_R6_STR_DB.setValue(myconfig.role_ratings_df['str']['dbr6'])
        self.spinBox_R6_BLK_DB.setValue(myconfig.role_ratings_df['blk']['dbr6'])
        self.spinBox_R6_TKL_DB.setValue(myconfig.role_ratings_df['tkl']['dbr6'])
        self.spinBox_R6_HAN_DB.setValue(myconfig.role_ratings_df['han']['dbr6'])
        self.spinBox_R6_GI_DB.setValue(myconfig.role_ratings_df['gi']['dbr6'])
        self.spinBox_R6_ELU_DB.setValue(myconfig.role_ratings_df['elu']['dbr6'])
        self.spinBox_R6_TEC_DB.setValue(myconfig.role_ratings_df['tec']['dbr6'])
        self.lcdNumber_R6_DB.display(myconfig.role_ratings_df['total']['dbr6'])
        self.spinBox_R6_ATH_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_SPD_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_DUR_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_WE_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STA_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STR_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_BLK_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TKL_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_HAN_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_GI_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_ELU_DB.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TEC_DB.valueChanged.connect(self.update_row_total)

        # K Section
        self.lineEdit_R1_K.setText(myconfig.role_ratings_df['label']['kr1'])
        self.spinBox_R1_ATH_K.setValue(myconfig.role_ratings_df['ath']['kr1'])
        self.spinBox_R1_SPD_K.setValue(myconfig.role_ratings_df['spd']['kr1'])
        self.spinBox_R1_DUR_K.setValue(myconfig.role_ratings_df['dur']['kr1'])
        self.spinBox_R1_WE_K.setValue(myconfig.role_ratings_df['we']['kr1'])
        self.spinBox_R1_STA_K.setValue(myconfig.role_ratings_df['sta']['kr1'])
        self.spinBox_R1_STR_K.setValue(myconfig.role_ratings_df['str']['kr1'])
        self.spinBox_R1_BLK_K.setValue(myconfig.role_ratings_df['blk']['kr1'])
        self.spinBox_R1_TKL_K.setValue(myconfig.role_ratings_df['tkl']['kr1'])
        self.spinBox_R1_HAN_K.setValue(myconfig.role_ratings_df['han']['kr1'])
        self.spinBox_R1_GI_K.setValue(myconfig.role_ratings_df['gi']['kr1'])
        self.spinBox_R1_ELU_K.setValue(myconfig.role_ratings_df['elu']['kr1'])
        self.spinBox_R1_TEC_K.setValue(myconfig.role_ratings_df['tec']['kr1'])
        self.lcdNumber_R1_K.display(myconfig.role_ratings_df['total']['kr1'])
        self.spinBox_R1_ATH_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_SPD_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_DUR_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_WE_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STA_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STR_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_BLK_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TKL_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_HAN_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_GI_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_ELU_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TEC_K.valueChanged.connect(self.update_row_total)

        self.lineEdit_R2_K.setText(myconfig.role_ratings_df['label']['kr2'])
        self.spinBox_R2_ATH_K.setValue(myconfig.role_ratings_df['ath']['kr2'])
        self.spinBox_R2_SPD_K.setValue(myconfig.role_ratings_df['spd']['kr2'])
        self.spinBox_R2_DUR_K.setValue(myconfig.role_ratings_df['dur']['kr2'])
        self.spinBox_R2_WE_K.setValue(myconfig.role_ratings_df['we']['kr2'])
        self.spinBox_R2_STA_K.setValue(myconfig.role_ratings_df['sta']['kr2'])
        self.spinBox_R2_STR_K.setValue(myconfig.role_ratings_df['str']['kr2'])
        self.spinBox_R2_BLK_K.setValue(myconfig.role_ratings_df['blk']['kr2'])
        self.spinBox_R2_TKL_K.setValue(myconfig.role_ratings_df['tkl']['kr2'])
        self.spinBox_R2_HAN_K.setValue(myconfig.role_ratings_df['han']['kr2'])
        self.spinBox_R2_GI_K.setValue(myconfig.role_ratings_df['gi']['kr2'])
        self.spinBox_R2_ELU_K.setValue(myconfig.role_ratings_df['elu']['kr2'])
        self.spinBox_R2_TEC_K.setValue(myconfig.role_ratings_df['tec']['kr2'])
        self.lcdNumber_R2_K.display(myconfig.role_ratings_df['total']['kr2'])
        self.spinBox_R2_ATH_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_SPD_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_DUR_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_WE_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STA_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STR_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_BLK_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TKL_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_HAN_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_GI_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_ELU_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TEC_K.valueChanged.connect(self.update_row_total)

        self.lineEdit_R3_K.setText(myconfig.role_ratings_df['label']['kr3'])
        self.spinBox_R3_ATH_K.setValue(myconfig.role_ratings_df['ath']['kr3'])
        self.spinBox_R3_SPD_K.setValue(myconfig.role_ratings_df['spd']['kr3'])
        self.spinBox_R3_DUR_K.setValue(myconfig.role_ratings_df['dur']['kr3'])
        self.spinBox_R3_WE_K.setValue(myconfig.role_ratings_df['we']['kr3'])
        self.spinBox_R3_STA_K.setValue(myconfig.role_ratings_df['sta']['kr3'])
        self.spinBox_R3_STR_K.setValue(myconfig.role_ratings_df['str']['kr3'])
        self.spinBox_R3_BLK_K.setValue(myconfig.role_ratings_df['blk']['kr3'])
        self.spinBox_R3_TKL_K.setValue(myconfig.role_ratings_df['tkl']['kr3'])
        self.spinBox_R3_HAN_K.setValue(myconfig.role_ratings_df['han']['kr3'])
        self.spinBox_R3_GI_K.setValue(myconfig.role_ratings_df['gi']['kr3'])
        self.spinBox_R3_ELU_K.setValue(myconfig.role_ratings_df['elu']['kr3'])
        self.spinBox_R3_TEC_K.setValue(myconfig.role_ratings_df['tec']['kr3'])
        self.lcdNumber_R3_K.display(myconfig.role_ratings_df['total']['kr3'])
        self.spinBox_R3_ATH_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_SPD_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_DUR_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_WE_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STA_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STR_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_BLK_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TKL_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_HAN_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_GI_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_ELU_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TEC_K.valueChanged.connect(self.update_row_total)

        self.lineEdit_R4_K.setText(myconfig.role_ratings_df['label']['kr4'])
        self.spinBox_R4_ATH_K.setValue(myconfig.role_ratings_df['ath']['kr4'])
        self.spinBox_R4_SPD_K.setValue(myconfig.role_ratings_df['spd']['kr4'])
        self.spinBox_R4_DUR_K.setValue(myconfig.role_ratings_df['dur']['kr4'])
        self.spinBox_R4_WE_K.setValue(myconfig.role_ratings_df['we']['kr4'])
        self.spinBox_R4_STA_K.setValue(myconfig.role_ratings_df['sta']['kr4'])
        self.spinBox_R4_STR_K.setValue(myconfig.role_ratings_df['str']['kr4'])
        self.spinBox_R4_BLK_K.setValue(myconfig.role_ratings_df['blk']['kr4'])
        self.spinBox_R4_TKL_K.setValue(myconfig.role_ratings_df['tkl']['kr4'])
        self.spinBox_R4_HAN_K.setValue(myconfig.role_ratings_df['han']['kr4'])
        self.spinBox_R4_GI_K.setValue(myconfig.role_ratings_df['gi']['kr4'])
        self.spinBox_R4_ELU_K.setValue(myconfig.role_ratings_df['elu']['kr4'])
        self.spinBox_R4_TEC_K.setValue(myconfig.role_ratings_df['tec']['kr4'])
        self.lcdNumber_R4_K.display(myconfig.role_ratings_df['total']['kr4'])
        self.spinBox_R4_ATH_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_SPD_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_DUR_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_WE_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STA_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STR_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_BLK_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TKL_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_HAN_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_GI_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_ELU_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TEC_K.valueChanged.connect(self.update_row_total)

        self.lineEdit_R5_K.setText(myconfig.role_ratings_df['label']['kr5'])
        self.spinBox_R5_ATH_K.setValue(myconfig.role_ratings_df['ath']['kr5'])
        self.spinBox_R5_SPD_K.setValue(myconfig.role_ratings_df['spd']['kr5'])
        self.spinBox_R5_DUR_K.setValue(myconfig.role_ratings_df['dur']['kr5'])
        self.spinBox_R5_WE_K.setValue(myconfig.role_ratings_df['we']['kr5'])
        self.spinBox_R5_STA_K.setValue(myconfig.role_ratings_df['sta']['kr5'])
        self.spinBox_R5_STR_K.setValue(myconfig.role_ratings_df['str']['kr5'])
        self.spinBox_R5_BLK_K.setValue(myconfig.role_ratings_df['blk']['kr5'])
        self.spinBox_R5_TKL_K.setValue(myconfig.role_ratings_df['tkl']['kr5'])
        self.spinBox_R5_HAN_K.setValue(myconfig.role_ratings_df['han']['kr5'])
        self.spinBox_R5_GI_K.setValue(myconfig.role_ratings_df['gi']['kr5'])
        self.spinBox_R5_ELU_K.setValue(myconfig.role_ratings_df['elu']['kr5'])
        self.spinBox_R5_TEC_K.setValue(myconfig.role_ratings_df['tec']['kr5'])
        self.lcdNumber_R5_K.display(myconfig.role_ratings_df['total']['kr5'])
        self.spinBox_R5_ATH_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_SPD_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_DUR_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_WE_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STA_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STR_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_BLK_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TKL_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_HAN_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_GI_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_ELU_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TEC_K.valueChanged.connect(self.update_row_total)

        self.lineEdit_R6_K.setText(myconfig.role_ratings_df['label']['kr6'])
        self.spinBox_R6_ATH_K.setValue(myconfig.role_ratings_df['ath']['kr6'])
        self.spinBox_R6_SPD_K.setValue(myconfig.role_ratings_df['spd']['kr6'])
        self.spinBox_R6_DUR_K.setValue(myconfig.role_ratings_df['dur']['kr6'])
        self.spinBox_R6_WE_K.setValue(myconfig.role_ratings_df['we']['kr6'])
        self.spinBox_R6_STA_K.setValue(myconfig.role_ratings_df['sta']['kr6'])
        self.spinBox_R6_STR_K.setValue(myconfig.role_ratings_df['str']['kr6'])
        self.spinBox_R6_BLK_K.setValue(myconfig.role_ratings_df['blk']['kr6'])
        self.spinBox_R6_TKL_K.setValue(myconfig.role_ratings_df['tkl']['kr6'])
        self.spinBox_R6_HAN_K.setValue(myconfig.role_ratings_df['han']['kr6'])
        self.spinBox_R6_GI_K.setValue(myconfig.role_ratings_df['gi']['kr6'])
        self.spinBox_R6_ELU_K.setValue(myconfig.role_ratings_df['elu']['kr6'])
        self.spinBox_R6_TEC_K.setValue(myconfig.role_ratings_df['tec']['kr6'])
        self.lcdNumber_R6_K.display(myconfig.role_ratings_df['total']['kr6'])
        self.spinBox_R6_ATH_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_SPD_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_DUR_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_WE_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STA_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STR_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_BLK_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TKL_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_HAN_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_GI_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_ELU_K.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TEC_K.valueChanged.connect(self.update_row_total)

        # P Section
        self.lineEdit_R1_P.setText(myconfig.role_ratings_df['label']['pr1'])
        self.spinBox_R1_ATH_P.setValue(myconfig.role_ratings_df['ath']['pr1'])
        self.spinBox_R1_SPD_P.setValue(myconfig.role_ratings_df['spd']['pr1'])
        self.spinBox_R1_DUR_P.setValue(myconfig.role_ratings_df['dur']['pr1'])
        self.spinBox_R1_WE_P.setValue(myconfig.role_ratings_df['we']['pr1'])
        self.spinBox_R1_STA_P.setValue(myconfig.role_ratings_df['sta']['pr1'])
        self.spinBox_R1_STR_P.setValue(myconfig.role_ratings_df['str']['pr1'])
        self.spinBox_R1_BLK_P.setValue(myconfig.role_ratings_df['blk']['pr1'])
        self.spinBox_R1_TKL_P.setValue(myconfig.role_ratings_df['tkl']['pr1'])
        self.spinBox_R1_HAN_P.setValue(myconfig.role_ratings_df['han']['pr1'])
        self.spinBox_R1_GI_P.setValue(myconfig.role_ratings_df['gi']['pr1'])
        self.spinBox_R1_ELU_P.setValue(myconfig.role_ratings_df['elu']['pr1'])
        self.spinBox_R1_TEC_P.setValue(myconfig.role_ratings_df['tec']['pr1'])
        self.lcdNumber_R1_P.display(myconfig.role_ratings_df['total']['pr1'])
        self.spinBox_R1_ATH_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_SPD_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_DUR_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_WE_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STA_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_STR_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_BLK_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TKL_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_HAN_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_GI_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_ELU_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R1_TEC_P.valueChanged.connect(self.update_row_total)

        self.lineEdit_R2_P.setText(myconfig.role_ratings_df['label']['pr2'])
        self.spinBox_R2_ATH_P.setValue(myconfig.role_ratings_df['ath']['pr2'])
        self.spinBox_R2_SPD_P.setValue(myconfig.role_ratings_df['spd']['pr2'])
        self.spinBox_R2_DUR_P.setValue(myconfig.role_ratings_df['dur']['pr2'])
        self.spinBox_R2_WE_P.setValue(myconfig.role_ratings_df['we']['pr2'])
        self.spinBox_R2_STA_P.setValue(myconfig.role_ratings_df['sta']['pr2'])
        self.spinBox_R2_STR_P.setValue(myconfig.role_ratings_df['str']['pr2'])
        self.spinBox_R2_BLK_P.setValue(myconfig.role_ratings_df['blk']['pr2'])
        self.spinBox_R2_TKL_P.setValue(myconfig.role_ratings_df['tkl']['pr2'])
        self.spinBox_R2_HAN_P.setValue(myconfig.role_ratings_df['han']['pr2'])
        self.spinBox_R2_GI_P.setValue(myconfig.role_ratings_df['gi']['pr2'])
        self.spinBox_R2_ELU_P.setValue(myconfig.role_ratings_df['elu']['pr2'])
        self.spinBox_R2_TEC_P.setValue(myconfig.role_ratings_df['tec']['pr2'])
        self.lcdNumber_R2_P.display(myconfig.role_ratings_df['total']['pr2'])
        self.spinBox_R2_ATH_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_SPD_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_DUR_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_WE_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STA_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_STR_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_BLK_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TKL_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_HAN_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_GI_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_ELU_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R2_TEC_P.valueChanged.connect(self.update_row_total)

        self.lineEdit_R3_P.setText(myconfig.role_ratings_df['label']['pr3'])
        self.spinBox_R3_ATH_P.setValue(myconfig.role_ratings_df['ath']['pr3'])
        self.spinBox_R3_SPD_P.setValue(myconfig.role_ratings_df['spd']['pr3'])
        self.spinBox_R3_DUR_P.setValue(myconfig.role_ratings_df['dur']['pr3'])
        self.spinBox_R3_WE_P.setValue(myconfig.role_ratings_df['we']['pr3'])
        self.spinBox_R3_STA_P.setValue(myconfig.role_ratings_df['sta']['pr3'])
        self.spinBox_R3_STR_P.setValue(myconfig.role_ratings_df['str']['pr3'])
        self.spinBox_R3_BLK_P.setValue(myconfig.role_ratings_df['blk']['pr3'])
        self.spinBox_R3_TKL_P.setValue(myconfig.role_ratings_df['tkl']['pr3'])
        self.spinBox_R3_HAN_P.setValue(myconfig.role_ratings_df['han']['pr3'])
        self.spinBox_R3_GI_P.setValue(myconfig.role_ratings_df['gi']['pr3'])
        self.spinBox_R3_ELU_P.setValue(myconfig.role_ratings_df['elu']['pr3'])
        self.spinBox_R3_TEC_P.setValue(myconfig.role_ratings_df['tec']['pr3'])
        self.lcdNumber_R3_P.display(myconfig.role_ratings_df['total']['pr3'])
        self.spinBox_R3_ATH_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_SPD_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_DUR_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_WE_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STA_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_STR_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_BLK_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TKL_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_HAN_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_GI_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_ELU_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R3_TEC_P.valueChanged.connect(self.update_row_total)

        self.lineEdit_R4_P.setText(myconfig.role_ratings_df['label']['pr4'])
        self.spinBox_R4_ATH_P.setValue(myconfig.role_ratings_df['ath']['pr4'])
        self.spinBox_R4_SPD_P.setValue(myconfig.role_ratings_df['spd']['pr4'])
        self.spinBox_R4_DUR_P.setValue(myconfig.role_ratings_df['dur']['pr4'])
        self.spinBox_R4_WE_P.setValue(myconfig.role_ratings_df['we']['pr4'])
        self.spinBox_R4_STA_P.setValue(myconfig.role_ratings_df['sta']['pr4'])
        self.spinBox_R4_STR_P.setValue(myconfig.role_ratings_df['str']['pr4'])
        self.spinBox_R4_BLK_P.setValue(myconfig.role_ratings_df['blk']['pr4'])
        self.spinBox_R4_TKL_P.setValue(myconfig.role_ratings_df['tkl']['pr4'])
        self.spinBox_R4_HAN_P.setValue(myconfig.role_ratings_df['han']['pr4'])
        self.spinBox_R4_GI_P.setValue(myconfig.role_ratings_df['gi']['pr4'])
        self.spinBox_R4_ELU_P.setValue(myconfig.role_ratings_df['elu']['pr4'])
        self.spinBox_R4_TEC_P.setValue(myconfig.role_ratings_df['tec']['pr4'])
        self.lcdNumber_R4_P.display(myconfig.role_ratings_df['total']['pr4'])
        self.spinBox_R4_ATH_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_SPD_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_DUR_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_WE_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STA_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_STR_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_BLK_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TKL_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_HAN_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_GI_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_ELU_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R4_TEC_P.valueChanged.connect(self.update_row_total)

        self.lineEdit_R5_P.setText(myconfig.role_ratings_df['label']['pr5'])
        self.spinBox_R5_ATH_P.setValue(myconfig.role_ratings_df['ath']['pr5'])
        self.spinBox_R5_SPD_P.setValue(myconfig.role_ratings_df['spd']['pr5'])
        self.spinBox_R5_DUR_P.setValue(myconfig.role_ratings_df['dur']['pr5'])
        self.spinBox_R5_WE_P.setValue(myconfig.role_ratings_df['we']['pr5'])
        self.spinBox_R5_STA_P.setValue(myconfig.role_ratings_df['sta']['pr5'])
        self.spinBox_R5_STR_P.setValue(myconfig.role_ratings_df['str']['pr5'])
        self.spinBox_R5_BLK_P.setValue(myconfig.role_ratings_df['blk']['pr5'])
        self.spinBox_R5_TKL_P.setValue(myconfig.role_ratings_df['tkl']['pr5'])
        self.spinBox_R5_HAN_P.setValue(myconfig.role_ratings_df['han']['pr5'])
        self.spinBox_R5_GI_P.setValue(myconfig.role_ratings_df['gi']['pr5'])
        self.spinBox_R5_ELU_P.setValue(myconfig.role_ratings_df['elu']['pr5'])
        self.spinBox_R5_TEC_P.setValue(myconfig.role_ratings_df['tec']['pr5'])
        self.lcdNumber_R5_P.display(myconfig.role_ratings_df['total']['pr5'])
        self.spinBox_R5_ATH_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_SPD_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_DUR_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_WE_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STA_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_STR_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_BLK_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TKL_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_HAN_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_GI_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_ELU_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R5_TEC_P.valueChanged.connect(self.update_row_total)

        self.lineEdit_R6_P.setText(myconfig.role_ratings_df['label']['pr6'])
        self.spinBox_R6_ATH_P.setValue(myconfig.role_ratings_df['ath']['pr6'])
        self.spinBox_R6_SPD_P.setValue(myconfig.role_ratings_df['spd']['pr6'])
        self.spinBox_R6_DUR_P.setValue(myconfig.role_ratings_df['dur']['pr6'])
        self.spinBox_R6_WE_P.setValue(myconfig.role_ratings_df['we']['pr6'])
        self.spinBox_R6_STA_P.setValue(myconfig.role_ratings_df['sta']['pr6'])
        self.spinBox_R6_STR_P.setValue(myconfig.role_ratings_df['str']['pr6'])
        self.spinBox_R6_BLK_P.setValue(myconfig.role_ratings_df['blk']['pr6'])
        self.spinBox_R6_TKL_P.setValue(myconfig.role_ratings_df['tkl']['pr6'])
        self.spinBox_R6_HAN_P.setValue(myconfig.role_ratings_df['han']['pr6'])
        self.spinBox_R6_GI_P.setValue(myconfig.role_ratings_df['gi']['pr6'])
        self.spinBox_R6_ELU_P.setValue(myconfig.role_ratings_df['elu']['pr6'])
        self.spinBox_R6_TEC_P.setValue(myconfig.role_ratings_df['tec']['pr6'])
        self.lcdNumber_R6_P.display(myconfig.role_ratings_df['total']['pr6'])
        self.spinBox_R6_ATH_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_SPD_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_DUR_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_WE_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STA_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_STR_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_BLK_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TKL_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_HAN_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_GI_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_ELU_P.valueChanged.connect(self.update_row_total)
        self.spinBox_R6_TEC_P.valueChanged.connect(self.update_row_total)

    
    def update_row_total(self):
        # QB Section
        self.lcdNumber_R1_QB.display(
            sum([
                self.spinBox_R1_ATH_QB.value(),
                self.spinBox_R1_SPD_QB.value(),
                self.spinBox_R1_DUR_QB.value(),
                self.spinBox_R1_WE_QB.value(),
                self.spinBox_R1_STA_QB.value(),
                self.spinBox_R1_STR_QB.value(),
                self.spinBox_R1_BLK_QB.value(),
                self.spinBox_R1_TKL_QB.value(),
                self.spinBox_R1_HAN_QB.value(),
                self.spinBox_R1_GI_QB.value(),
                self.spinBox_R1_ELU_QB.value(),
                self.spinBox_R1_TEC_QB.value()
            ])
        )

        self.lcdNumber_R2_QB.display(
            sum([
                self.spinBox_R2_ATH_QB.value(),
                self.spinBox_R2_SPD_QB.value(),
                self.spinBox_R2_DUR_QB.value(),
                self.spinBox_R2_WE_QB.value(),
                self.spinBox_R2_STA_QB.value(),
                self.spinBox_R2_STR_QB.value(),
                self.spinBox_R2_BLK_QB.value(),
                self.spinBox_R2_TKL_QB.value(),
                self.spinBox_R2_HAN_QB.value(),
                self.spinBox_R2_GI_QB.value(),
                self.spinBox_R2_ELU_QB.value(),
                self.spinBox_R2_TEC_QB.value()
            ])
        )

        self.lcdNumber_R3_QB.display(
            sum([
                self.spinBox_R3_ATH_QB.value(),
                self.spinBox_R3_SPD_QB.value(),
                self.spinBox_R3_DUR_QB.value(),
                self.spinBox_R3_WE_QB.value(),
                self.spinBox_R3_STA_QB.value(),
                self.spinBox_R3_STR_QB.value(),
                self.spinBox_R3_BLK_QB.value(),
                self.spinBox_R3_TKL_QB.value(),
                self.spinBox_R3_HAN_QB.value(),
                self.spinBox_R3_GI_QB.value(),
                self.spinBox_R3_ELU_QB.value(),
                self.spinBox_R3_TEC_QB.value()
            ])
        )

        self.lcdNumber_R4_QB.display(
            sum([
                self.spinBox_R4_ATH_QB.value(),
                self.spinBox_R4_SPD_QB.value(),
                self.spinBox_R4_DUR_QB.value(),
                self.spinBox_R4_WE_QB.value(),
                self.spinBox_R4_STA_QB.value(),
                self.spinBox_R4_STR_QB.value(),
                self.spinBox_R4_BLK_QB.value(),
                self.spinBox_R4_TKL_QB.value(),
                self.spinBox_R4_HAN_QB.value(),
                self.spinBox_R4_GI_QB.value(),
                self.spinBox_R4_ELU_QB.value(),
                self.spinBox_R4_TEC_QB.value()
            ])
        )

        self.lcdNumber_R5_QB.display(
            sum([
                self.spinBox_R5_ATH_QB.value(),
                self.spinBox_R5_SPD_QB.value(),
                self.spinBox_R5_DUR_QB.value(),
                self.spinBox_R5_WE_QB.value(),
                self.spinBox_R5_STA_QB.value(),
                self.spinBox_R5_STR_QB.value(),
                self.spinBox_R5_BLK_QB.value(),
                self.spinBox_R5_TKL_QB.value(),
                self.spinBox_R5_HAN_QB.value(),
                self.spinBox_R5_GI_QB.value(),
                self.spinBox_R5_ELU_QB.value(),
                self.spinBox_R5_TEC_QB.value()
            ])
        )

        self.lcdNumber_R6_QB.display(
            sum([
                self.spinBox_R6_ATH_QB.value(),
                self.spinBox_R6_SPD_QB.value(),
                self.spinBox_R6_DUR_QB.value(),
                self.spinBox_R6_WE_QB.value(),
                self.spinBox_R6_STA_QB.value(),
                self.spinBox_R6_STR_QB.value(),
                self.spinBox_R6_BLK_QB.value(),
                self.spinBox_R6_TKL_QB.value(),
                self.spinBox_R6_HAN_QB.value(),
                self.spinBox_R6_GI_QB.value(),
                self.spinBox_R6_ELU_QB.value(),
                self.spinBox_R6_TEC_QB.value()
            ])
        )

        # RB Section
        self.lcdNumber_R1_RB.display(
            sum([
                self.spinBox_R1_ATH_RB.value(),
                self.spinBox_R1_SPD_RB.value(),
                self.spinBox_R1_DUR_RB.value(),
                self.spinBox_R1_WE_RB.value(),
                self.spinBox_R1_STA_RB.value(),
                self.spinBox_R1_STR_RB.value(),
                self.spinBox_R1_BLK_RB.value(),
                self.spinBox_R1_TKL_RB.value(),
                self.spinBox_R1_HAN_RB.value(),
                self.spinBox_R1_GI_RB.value(),
                self.spinBox_R1_ELU_RB.value(),
                self.spinBox_R1_TEC_RB.value()
            ])
        )

        self.lcdNumber_R2_RB.display(
            sum([
                self.spinBox_R2_ATH_RB.value(),
                self.spinBox_R2_SPD_RB.value(),
                self.spinBox_R2_DUR_RB.value(),
                self.spinBox_R2_WE_RB.value(),
                self.spinBox_R2_STA_RB.value(),
                self.spinBox_R2_STR_RB.value(),
                self.spinBox_R2_BLK_RB.value(),
                self.spinBox_R2_TKL_RB.value(),
                self.spinBox_R2_HAN_RB.value(),
                self.spinBox_R2_GI_RB.value(),
                self.spinBox_R2_ELU_RB.value(),
                self.spinBox_R2_TEC_RB.value()
            ])
        )

        self.lcdNumber_R3_RB.display(
            sum([
                self.spinBox_R3_ATH_RB.value(),
                self.spinBox_R3_SPD_RB.value(),
                self.spinBox_R3_DUR_RB.value(),
                self.spinBox_R3_WE_RB.value(),
                self.spinBox_R3_STA_RB.value(),
                self.spinBox_R3_STR_RB.value(),
                self.spinBox_R3_BLK_RB.value(),
                self.spinBox_R3_TKL_RB.value(),
                self.spinBox_R3_HAN_RB.value(),
                self.spinBox_R3_GI_RB.value(),
                self.spinBox_R3_ELU_RB.value(),
                self.spinBox_R3_TEC_RB.value()
            ])
        )

        self.lcdNumber_R4_RB.display(
            sum([
                self.spinBox_R4_ATH_RB.value(),
                self.spinBox_R4_SPD_RB.value(),
                self.spinBox_R4_DUR_RB.value(),
                self.spinBox_R4_WE_RB.value(),
                self.spinBox_R4_STA_RB.value(),
                self.spinBox_R4_STR_RB.value(),
                self.spinBox_R4_BLK_RB.value(),
                self.spinBox_R4_TKL_RB.value(),
                self.spinBox_R4_HAN_RB.value(),
                self.spinBox_R4_GI_RB.value(),
                self.spinBox_R4_ELU_RB.value(),
                self.spinBox_R4_TEC_RB.value()
            ])
        )

        self.lcdNumber_R5_RB.display(
            sum([
                self.spinBox_R5_ATH_RB.value(),
                self.spinBox_R5_SPD_RB.value(),
                self.spinBox_R5_DUR_RB.value(),
                self.spinBox_R5_WE_RB.value(),
                self.spinBox_R5_STA_RB.value(),
                self.spinBox_R5_STR_RB.value(),
                self.spinBox_R5_BLK_RB.value(),
                self.spinBox_R5_TKL_RB.value(),
                self.spinBox_R5_HAN_RB.value(),
                self.spinBox_R5_GI_RB.value(),
                self.spinBox_R5_ELU_RB.value(),
                self.spinBox_R5_TEC_RB.value()
            ])
        )

        self.lcdNumber_R6_RB.display(
            sum([
                self.spinBox_R6_ATH_RB.value(),
                self.spinBox_R6_SPD_RB.value(),
                self.spinBox_R6_DUR_RB.value(),
                self.spinBox_R6_WE_RB.value(),
                self.spinBox_R6_STA_RB.value(),
                self.spinBox_R6_STR_RB.value(),
                self.spinBox_R6_BLK_RB.value(),
                self.spinBox_R6_TKL_RB.value(),
                self.spinBox_R6_HAN_RB.value(),
                self.spinBox_R6_GI_RB.value(),
                self.spinBox_R6_ELU_RB.value(),
                self.spinBox_R6_TEC_RB.value()
            ])
        )
        
        # WR Section
        self.lcdNumber_R1_WR.display(
            sum([
                self.spinBox_R1_ATH_WR.value(),
                self.spinBox_R1_SPD_WR.value(),
                self.spinBox_R1_DUR_WR.value(),
                self.spinBox_R1_WE_WR.value(),
                self.spinBox_R1_STA_WR.value(),
                self.spinBox_R1_STR_WR.value(),
                self.spinBox_R1_BLK_WR.value(),
                self.spinBox_R1_TKL_WR.value(),
                self.spinBox_R1_HAN_WR.value(),
                self.spinBox_R1_GI_WR.value(),
                self.spinBox_R1_ELU_WR.value(),
                self.spinBox_R1_TEC_WR.value()
            ])
        )

        self.lcdNumber_R2_WR.display(
            sum([
                self.spinBox_R2_ATH_WR.value(),
                self.spinBox_R2_SPD_WR.value(),
                self.spinBox_R2_DUR_WR.value(),
                self.spinBox_R2_WE_WR.value(),
                self.spinBox_R2_STA_WR.value(),
                self.spinBox_R2_STR_WR.value(),
                self.spinBox_R2_BLK_WR.value(),
                self.spinBox_R2_TKL_WR.value(),
                self.spinBox_R2_HAN_WR.value(),
                self.spinBox_R2_GI_WR.value(),
                self.spinBox_R2_ELU_WR.value(),
                self.spinBox_R2_TEC_WR.value()
            ])
        )

        self.lcdNumber_R3_WR.display(
            sum([
                self.spinBox_R3_ATH_WR.value(),
                self.spinBox_R3_SPD_WR.value(),
                self.spinBox_R3_DUR_WR.value(),
                self.spinBox_R3_WE_WR.value(),
                self.spinBox_R3_STA_WR.value(),
                self.spinBox_R3_STR_WR.value(),
                self.spinBox_R3_BLK_WR.value(),
                self.spinBox_R3_TKL_WR.value(),
                self.spinBox_R3_HAN_WR.value(),
                self.spinBox_R3_GI_WR.value(),
                self.spinBox_R3_ELU_WR.value(),
                self.spinBox_R3_TEC_WR.value()
            ])
        )

        self.lcdNumber_R4_WR.display(
            sum([
                self.spinBox_R4_ATH_WR.value(),
                self.spinBox_R4_SPD_WR.value(),
                self.spinBox_R4_DUR_WR.value(),
                self.spinBox_R4_WE_WR.value(),
                self.spinBox_R4_STA_WR.value(),
                self.spinBox_R4_STR_WR.value(),
                self.spinBox_R4_BLK_WR.value(),
                self.spinBox_R4_TKL_WR.value(),
                self.spinBox_R4_HAN_WR.value(),
                self.spinBox_R4_GI_WR.value(),
                self.spinBox_R4_ELU_WR.value(),
                self.spinBox_R4_TEC_WR.value()
            ])
        )

        self.lcdNumber_R5_WR.display(
            sum([
                self.spinBox_R5_ATH_WR.value(),
                self.spinBox_R5_SPD_WR.value(),
                self.spinBox_R5_DUR_WR.value(),
                self.spinBox_R5_WE_WR.value(),
                self.spinBox_R5_STA_WR.value(),
                self.spinBox_R5_STR_WR.value(),
                self.spinBox_R5_BLK_WR.value(),
                self.spinBox_R5_TKL_WR.value(),
                self.spinBox_R5_HAN_WR.value(),
                self.spinBox_R5_GI_WR.value(),
                self.spinBox_R5_ELU_WR.value(),
                self.spinBox_R5_TEC_WR.value()
            ])
        )

        self.lcdNumber_R6_WR.display(
            sum([
                self.spinBox_R6_ATH_WR.value(),
                self.spinBox_R6_SPD_WR.value(),
                self.spinBox_R6_DUR_WR.value(),
                self.spinBox_R6_WE_WR.value(),
                self.spinBox_R6_STA_WR.value(),
                self.spinBox_R6_STR_WR.value(),
                self.spinBox_R6_BLK_WR.value(),
                self.spinBox_R6_TKL_WR.value(),
                self.spinBox_R6_HAN_WR.value(),
                self.spinBox_R6_GI_WR.value(),
                self.spinBox_R6_ELU_WR.value(),
                self.spinBox_R6_TEC_WR.value()
            ])
        )

        # TE Section
        self.lcdNumber_R1_TE.display(
            sum([
                self.spinBox_R1_ATH_TE.value(),
                self.spinBox_R1_SPD_TE.value(),
                self.spinBox_R1_DUR_TE.value(),
                self.spinBox_R1_WE_TE.value(),
                self.spinBox_R1_STA_TE.value(),
                self.spinBox_R1_STR_TE.value(),
                self.spinBox_R1_BLK_TE.value(),
                self.spinBox_R1_TKL_TE.value(),
                self.spinBox_R1_HAN_TE.value(),
                self.spinBox_R1_GI_TE.value(),
                self.spinBox_R1_ELU_TE.value(),
                self.spinBox_R1_TEC_TE.value()
            ])
        )

        self.lcdNumber_R2_TE.display(
            sum([
                self.spinBox_R2_ATH_TE.value(),
                self.spinBox_R2_SPD_TE.value(),
                self.spinBox_R2_DUR_TE.value(),
                self.spinBox_R2_WE_TE.value(),
                self.spinBox_R2_STA_TE.value(),
                self.spinBox_R2_STR_TE.value(),
                self.spinBox_R2_BLK_TE.value(),
                self.spinBox_R2_TKL_TE.value(),
                self.spinBox_R2_HAN_TE.value(),
                self.spinBox_R2_GI_TE.value(),
                self.spinBox_R2_ELU_TE.value(),
                self.spinBox_R2_TEC_TE.value()
            ])
        )

        self.lcdNumber_R3_TE.display(
            sum([
                self.spinBox_R3_ATH_TE.value(),
                self.spinBox_R3_SPD_TE.value(),
                self.spinBox_R3_DUR_TE.value(),
                self.spinBox_R3_WE_TE.value(),
                self.spinBox_R3_STA_TE.value(),
                self.spinBox_R3_STR_TE.value(),
                self.spinBox_R3_BLK_TE.value(),
                self.spinBox_R3_TKL_TE.value(),
                self.spinBox_R3_HAN_TE.value(),
                self.spinBox_R3_GI_TE.value(),
                self.spinBox_R3_ELU_TE.value(),
                self.spinBox_R3_TEC_TE.value()
            ])
        )

        self.lcdNumber_R4_TE.display(
            sum([
                self.spinBox_R4_ATH_TE.value(),
                self.spinBox_R4_SPD_TE.value(),
                self.spinBox_R4_DUR_TE.value(),
                self.spinBox_R4_WE_TE.value(),
                self.spinBox_R4_STA_TE.value(),
                self.spinBox_R4_STR_TE.value(),
                self.spinBox_R4_BLK_TE.value(),
                self.spinBox_R4_TKL_TE.value(),
                self.spinBox_R4_HAN_TE.value(),
                self.spinBox_R4_GI_TE.value(),
                self.spinBox_R4_ELU_TE.value(),
                self.spinBox_R4_TEC_TE.value()
            ])
        )

        self.lcdNumber_R5_TE.display(
            sum([
                self.spinBox_R5_ATH_TE.value(),
                self.spinBox_R5_SPD_TE.value(),
                self.spinBox_R5_DUR_TE.value(),
                self.spinBox_R5_WE_TE.value(),
                self.spinBox_R5_STA_TE.value(),
                self.spinBox_R5_STR_TE.value(),
                self.spinBox_R5_BLK_TE.value(),
                self.spinBox_R5_TKL_TE.value(),
                self.spinBox_R5_HAN_TE.value(),
                self.spinBox_R5_GI_TE.value(),
                self.spinBox_R5_ELU_TE.value(),
                self.spinBox_R5_TEC_TE.value()
            ])
        )

        self.lcdNumber_R6_TE.display(
            sum([
                self.spinBox_R6_ATH_TE.value(),
                self.spinBox_R6_SPD_TE.value(),
                self.spinBox_R6_DUR_TE.value(),
                self.spinBox_R6_WE_TE.value(),
                self.spinBox_R6_STA_TE.value(),
                self.spinBox_R6_STR_TE.value(),
                self.spinBox_R6_BLK_TE.value(),
                self.spinBox_R6_TKL_TE.value(),
                self.spinBox_R6_HAN_TE.value(),
                self.spinBox_R6_GI_TE.value(),
                self.spinBox_R6_ELU_TE.value(),
                self.spinBox_R6_TEC_TE.value()
            ])
        )

        # OL Section
        self.lcdNumber_R1_OL.display(
            sum([
                self.spinBox_R1_ATH_OL.value(),
                self.spinBox_R1_SPD_OL.value(),
                self.spinBox_R1_DUR_OL.value(),
                self.spinBox_R1_WE_OL.value(),
                self.spinBox_R1_STA_OL.value(),
                self.spinBox_R1_STR_OL.value(),
                self.spinBox_R1_BLK_OL.value(),
                self.spinBox_R1_TKL_OL.value(),
                self.spinBox_R1_HAN_OL.value(),
                self.spinBox_R1_GI_OL.value(),
                self.spinBox_R1_ELU_OL.value(),
                self.spinBox_R1_TEC_OL.value()
            ])
        )

        self.lcdNumber_R2_OL.display(
            sum([
                self.spinBox_R2_ATH_OL.value(),
                self.spinBox_R2_SPD_OL.value(),
                self.spinBox_R2_DUR_OL.value(),
                self.spinBox_R2_WE_OL.value(),
                self.spinBox_R2_STA_OL.value(),
                self.spinBox_R2_STR_OL.value(),
                self.spinBox_R2_BLK_OL.value(),
                self.spinBox_R2_TKL_OL.value(),
                self.spinBox_R2_HAN_OL.value(),
                self.spinBox_R2_GI_OL.value(),
                self.spinBox_R2_ELU_OL.value(),
                self.spinBox_R2_TEC_OL.value()
            ])
        )

        self.lcdNumber_R3_OL.display(
            sum([
                self.spinBox_R3_ATH_OL.value(),
                self.spinBox_R3_SPD_OL.value(),
                self.spinBox_R3_DUR_OL.value(),
                self.spinBox_R3_WE_OL.value(),
                self.spinBox_R3_STA_OL.value(),
                self.spinBox_R3_STR_OL.value(),
                self.spinBox_R3_BLK_OL.value(),
                self.spinBox_R3_TKL_OL.value(),
                self.spinBox_R3_HAN_OL.value(),
                self.spinBox_R3_GI_OL.value(),
                self.spinBox_R3_ELU_OL.value(),
                self.spinBox_R3_TEC_OL.value()
            ])
        )

        self.lcdNumber_R4_OL.display(
            sum([
                self.spinBox_R4_ATH_OL.value(),
                self.spinBox_R4_SPD_OL.value(),
                self.spinBox_R4_DUR_OL.value(),
                self.spinBox_R4_WE_OL.value(),
                self.spinBox_R4_STA_OL.value(),
                self.spinBox_R4_STR_OL.value(),
                self.spinBox_R4_BLK_OL.value(),
                self.spinBox_R4_TKL_OL.value(),
                self.spinBox_R4_HAN_OL.value(),
                self.spinBox_R4_GI_OL.value(),
                self.spinBox_R4_ELU_OL.value(),
                self.spinBox_R4_TEC_OL.value()
            ])
        )

        self.lcdNumber_R5_OL.display(
            sum([
                self.spinBox_R5_ATH_OL.value(),
                self.spinBox_R5_SPD_OL.value(),
                self.spinBox_R5_DUR_OL.value(),
                self.spinBox_R5_WE_OL.value(),
                self.spinBox_R5_STA_OL.value(),
                self.spinBox_R5_STR_OL.value(),
                self.spinBox_R5_BLK_OL.value(),
                self.spinBox_R5_TKL_OL.value(),
                self.spinBox_R5_HAN_OL.value(),
                self.spinBox_R5_GI_OL.value(),
                self.spinBox_R5_ELU_OL.value(),
                self.spinBox_R5_TEC_OL.value()
            ])
        )

        self.lcdNumber_R6_OL.display(
            sum([
                self.spinBox_R6_ATH_OL.value(),
                self.spinBox_R6_SPD_OL.value(),
                self.spinBox_R6_DUR_OL.value(),
                self.spinBox_R6_WE_OL.value(),
                self.spinBox_R6_STA_OL.value(),
                self.spinBox_R6_STR_OL.value(),
                self.spinBox_R6_BLK_OL.value(),
                self.spinBox_R6_TKL_OL.value(),
                self.spinBox_R6_HAN_OL.value(),
                self.spinBox_R6_GI_OL.value(),
                self.spinBox_R6_ELU_OL.value(),
                self.spinBox_R6_TEC_OL.value()
            ])
        )

        # DL Section
        self.lcdNumber_R1_DL.display(
            sum([
                self.spinBox_R1_ATH_DL.value(),
                self.spinBox_R1_SPD_DL.value(),
                self.spinBox_R1_DUR_DL.value(),
                self.spinBox_R1_WE_DL.value(),
                self.spinBox_R1_STA_DL.value(),
                self.spinBox_R1_STR_DL.value(),
                self.spinBox_R1_BLK_DL.value(),
                self.spinBox_R1_TKL_DL.value(),
                self.spinBox_R1_HAN_DL.value(),
                self.spinBox_R1_GI_DL.value(),
                self.spinBox_R1_ELU_DL.value(),
                self.spinBox_R1_TEC_DL.value()
            ])
        )

        self.lcdNumber_R2_DL.display(
            sum([
                self.spinBox_R2_ATH_DL.value(),
                self.spinBox_R2_SPD_DL.value(),
                self.spinBox_R2_DUR_DL.value(),
                self.spinBox_R2_WE_DL.value(),
                self.spinBox_R2_STA_DL.value(),
                self.spinBox_R2_STR_DL.value(),
                self.spinBox_R2_BLK_DL.value(),
                self.spinBox_R2_TKL_DL.value(),
                self.spinBox_R2_HAN_DL.value(),
                self.spinBox_R2_GI_DL.value(),
                self.spinBox_R2_ELU_DL.value(),
                self.spinBox_R2_TEC_DL.value()
            ])
        )

        self.lcdNumber_R3_DL.display(
            sum([
                self.spinBox_R3_ATH_DL.value(),
                self.spinBox_R3_SPD_DL.value(),
                self.spinBox_R3_DUR_DL.value(),
                self.spinBox_R3_WE_DL.value(),
                self.spinBox_R3_STA_DL.value(),
                self.spinBox_R3_STR_DL.value(),
                self.spinBox_R3_BLK_DL.value(),
                self.spinBox_R3_TKL_DL.value(),
                self.spinBox_R3_HAN_DL.value(),
                self.spinBox_R3_GI_DL.value(),
                self.spinBox_R3_ELU_DL.value(),
                self.spinBox_R3_TEC_DL.value()
            ])
        )

        self.lcdNumber_R4_DL.display(
            sum([
                self.spinBox_R4_ATH_DL.value(),
                self.spinBox_R4_SPD_DL.value(),
                self.spinBox_R4_DUR_DL.value(),
                self.spinBox_R4_WE_DL.value(),
                self.spinBox_R4_STA_DL.value(),
                self.spinBox_R4_STR_DL.value(),
                self.spinBox_R4_BLK_DL.value(),
                self.spinBox_R4_TKL_DL.value(),
                self.spinBox_R4_HAN_DL.value(),
                self.spinBox_R4_GI_DL.value(),
                self.spinBox_R4_ELU_DL.value(),
                self.spinBox_R4_TEC_DL.value()
            ])
        )

        self.lcdNumber_R5_DL.display(
            sum([
                self.spinBox_R5_ATH_DL.value(),
                self.spinBox_R5_SPD_DL.value(),
                self.spinBox_R5_DUR_DL.value(),
                self.spinBox_R5_WE_DL.value(),
                self.spinBox_R5_STA_DL.value(),
                self.spinBox_R5_STR_DL.value(),
                self.spinBox_R5_BLK_DL.value(),
                self.spinBox_R5_TKL_DL.value(),
                self.spinBox_R5_HAN_DL.value(),
                self.spinBox_R5_GI_DL.value(),
                self.spinBox_R5_ELU_DL.value(),
                self.spinBox_R5_TEC_DL.value()
            ])
        )

        self.lcdNumber_R6_DL.display(
            sum([
                self.spinBox_R6_ATH_DL.value(),
                self.spinBox_R6_SPD_DL.value(),
                self.spinBox_R6_DUR_DL.value(),
                self.spinBox_R6_WE_DL.value(),
                self.spinBox_R6_STA_DL.value(),
                self.spinBox_R6_STR_DL.value(),
                self.spinBox_R6_BLK_DL.value(),
                self.spinBox_R6_TKL_DL.value(),
                self.spinBox_R6_HAN_DL.value(),
                self.spinBox_R6_GI_DL.value(),
                self.spinBox_R6_ELU_DL.value(),
                self.spinBox_R6_TEC_DL.value()
            ])
        )

        # LB Section
        self.lcdNumber_R1_LB.display(
            sum([
                self.spinBox_R1_ATH_LB.value(),
                self.spinBox_R1_SPD_LB.value(),
                self.spinBox_R1_DUR_LB.value(),
                self.spinBox_R1_WE_LB.value(),
                self.spinBox_R1_STA_LB.value(),
                self.spinBox_R1_STR_LB.value(),
                self.spinBox_R1_BLK_LB.value(),
                self.spinBox_R1_TKL_LB.value(),
                self.spinBox_R1_HAN_LB.value(),
                self.spinBox_R1_GI_LB.value(),
                self.spinBox_R1_ELU_LB.value(),
                self.spinBox_R1_TEC_LB.value()
            ])
        )

        self.lcdNumber_R2_LB.display(
            sum([
                self.spinBox_R2_ATH_LB.value(),
                self.spinBox_R2_SPD_LB.value(),
                self.spinBox_R2_DUR_LB.value(),
                self.spinBox_R2_WE_LB.value(),
                self.spinBox_R2_STA_LB.value(),
                self.spinBox_R2_STR_LB.value(),
                self.spinBox_R2_BLK_LB.value(),
                self.spinBox_R2_TKL_LB.value(),
                self.spinBox_R2_HAN_LB.value(),
                self.spinBox_R2_GI_LB.value(),
                self.spinBox_R2_ELU_LB.value(),
                self.spinBox_R2_TEC_LB.value()
            ])
        )

        self.lcdNumber_R3_LB.display(
            sum([
                self.spinBox_R3_ATH_LB.value(),
                self.spinBox_R3_SPD_LB.value(),
                self.spinBox_R3_DUR_LB.value(),
                self.spinBox_R3_WE_LB.value(),
                self.spinBox_R3_STA_LB.value(),
                self.spinBox_R3_STR_LB.value(),
                self.spinBox_R3_BLK_LB.value(),
                self.spinBox_R3_TKL_LB.value(),
                self.spinBox_R3_HAN_LB.value(),
                self.spinBox_R3_GI_LB.value(),
                self.spinBox_R3_ELU_LB.value(),
                self.spinBox_R3_TEC_LB.value()
            ])
        )

        self.lcdNumber_R4_LB.display(
            sum([
                self.spinBox_R4_ATH_LB.value(),
                self.spinBox_R4_SPD_LB.value(),
                self.spinBox_R4_DUR_LB.value(),
                self.spinBox_R4_WE_LB.value(),
                self.spinBox_R4_STA_LB.value(),
                self.spinBox_R4_STR_LB.value(),
                self.spinBox_R4_BLK_LB.value(),
                self.spinBox_R4_TKL_LB.value(),
                self.spinBox_R4_HAN_LB.value(),
                self.spinBox_R4_GI_LB.value(),
                self.spinBox_R4_ELU_LB.value(),
                self.spinBox_R4_TEC_LB.value()
            ])
        )

        self.lcdNumber_R5_LB.display(
            sum([
                self.spinBox_R5_ATH_LB.value(),
                self.spinBox_R5_SPD_LB.value(),
                self.spinBox_R5_DUR_LB.value(),
                self.spinBox_R5_WE_LB.value(),
                self.spinBox_R5_STA_LB.value(),
                self.spinBox_R5_STR_LB.value(),
                self.spinBox_R5_BLK_LB.value(),
                self.spinBox_R5_TKL_LB.value(),
                self.spinBox_R5_HAN_LB.value(),
                self.spinBox_R5_GI_LB.value(),
                self.spinBox_R5_ELU_LB.value(),
                self.spinBox_R5_TEC_LB.value()
            ])
        )

        self.lcdNumber_R6_LB.display(
            sum([
                self.spinBox_R6_ATH_LB.value(),
                self.spinBox_R6_SPD_LB.value(),
                self.spinBox_R6_DUR_LB.value(),
                self.spinBox_R6_WE_LB.value(),
                self.spinBox_R6_STA_LB.value(),
                self.spinBox_R6_STR_LB.value(),
                self.spinBox_R6_BLK_LB.value(),
                self.spinBox_R6_TKL_LB.value(),
                self.spinBox_R6_HAN_LB.value(),
                self.spinBox_R6_GI_LB.value(),
                self.spinBox_R6_ELU_LB.value(),
                self.spinBox_R6_TEC_LB.value()
            ])
        )

        # DB Section
        self.lcdNumber_R1_DB.display(
            sum([
                self.spinBox_R1_ATH_DB.value(),
                self.spinBox_R1_SPD_DB.value(),
                self.spinBox_R1_DUR_DB.value(),
                self.spinBox_R1_WE_DB.value(),
                self.spinBox_R1_STA_DB.value(),
                self.spinBox_R1_STR_DB.value(),
                self.spinBox_R1_BLK_DB.value(),
                self.spinBox_R1_TKL_DB.value(),
                self.spinBox_R1_HAN_DB.value(),
                self.spinBox_R1_GI_DB.value(),
                self.spinBox_R1_ELU_DB.value(),
                self.spinBox_R1_TEC_DB.value()
            ])
        )

        self.lcdNumber_R2_DB.display(
            sum([
                self.spinBox_R2_ATH_DB.value(),
                self.spinBox_R2_SPD_DB.value(),
                self.spinBox_R2_DUR_DB.value(),
                self.spinBox_R2_WE_DB.value(),
                self.spinBox_R2_STA_DB.value(),
                self.spinBox_R2_STR_DB.value(),
                self.spinBox_R2_BLK_DB.value(),
                self.spinBox_R2_TKL_DB.value(),
                self.spinBox_R2_HAN_DB.value(),
                self.spinBox_R2_GI_DB.value(),
                self.spinBox_R2_ELU_DB.value(),
                self.spinBox_R2_TEC_DB.value()
            ])
        )

        self.lcdNumber_R3_DB.display(
            sum([
                self.spinBox_R3_ATH_DB.value(),
                self.spinBox_R3_SPD_DB.value(),
                self.spinBox_R3_DUR_DB.value(),
                self.spinBox_R3_WE_DB.value(),
                self.spinBox_R3_STA_DB.value(),
                self.spinBox_R3_STR_DB.value(),
                self.spinBox_R3_BLK_DB.value(),
                self.spinBox_R3_TKL_DB.value(),
                self.spinBox_R3_HAN_DB.value(),
                self.spinBox_R3_GI_DB.value(),
                self.spinBox_R3_ELU_DB.value(),
                self.spinBox_R3_TEC_DB.value()
            ])
        )

        self.lcdNumber_R4_DB.display(
            sum([
                self.spinBox_R4_ATH_DB.value(),
                self.spinBox_R4_SPD_DB.value(),
                self.spinBox_R4_DUR_DB.value(),
                self.spinBox_R4_WE_DB.value(),
                self.spinBox_R4_STA_DB.value(),
                self.spinBox_R4_STR_DB.value(),
                self.spinBox_R4_BLK_DB.value(),
                self.spinBox_R4_TKL_DB.value(),
                self.spinBox_R4_HAN_DB.value(),
                self.spinBox_R4_GI_DB.value(),
                self.spinBox_R4_ELU_DB.value(),
                self.spinBox_R4_TEC_DB.value()
            ])
        )

        self.lcdNumber_R5_DB.display(
            sum([
                self.spinBox_R5_ATH_DB.value(),
                self.spinBox_R5_SPD_DB.value(),
                self.spinBox_R5_DUR_DB.value(),
                self.spinBox_R5_WE_DB.value(),
                self.spinBox_R5_STA_DB.value(),
                self.spinBox_R5_STR_DB.value(),
                self.spinBox_R5_BLK_DB.value(),
                self.spinBox_R5_TKL_DB.value(),
                self.spinBox_R5_HAN_DB.value(),
                self.spinBox_R5_GI_DB.value(),
                self.spinBox_R5_ELU_DB.value(),
                self.spinBox_R5_TEC_DB.value()
            ])
        )

        self.lcdNumber_R6_DB.display(
            sum([
                self.spinBox_R6_ATH_DB.value(),
                self.spinBox_R6_SPD_DB.value(),
                self.spinBox_R6_DUR_DB.value(),
                self.spinBox_R6_WE_DB.value(),
                self.spinBox_R6_STA_DB.value(),
                self.spinBox_R6_STR_DB.value(),
                self.spinBox_R6_BLK_DB.value(),
                self.spinBox_R6_TKL_DB.value(),
                self.spinBox_R6_HAN_DB.value(),
                self.spinBox_R6_GI_DB.value(),
                self.spinBox_R6_ELU_DB.value(),
                self.spinBox_R6_TEC_DB.value()
            ])
        )

        # K Section
        self.lcdNumber_R1_K.display(
            sum([
                self.spinBox_R1_ATH_K.value(),
                self.spinBox_R1_SPD_K.value(),
                self.spinBox_R1_DUR_K.value(),
                self.spinBox_R1_WE_K.value(),
                self.spinBox_R1_STA_K.value(),
                self.spinBox_R1_STR_K.value(),
                self.spinBox_R1_BLK_K.value(),
                self.spinBox_R1_TKL_K.value(),
                self.spinBox_R1_HAN_K.value(),
                self.spinBox_R1_GI_K.value(),
                self.spinBox_R1_ELU_K.value(),
                self.spinBox_R1_TEC_K.value()
            ])
        )

        self.lcdNumber_R2_K.display(
            sum([
                self.spinBox_R2_ATH_K.value(),
                self.spinBox_R2_SPD_K.value(),
                self.spinBox_R2_DUR_K.value(),
                self.spinBox_R2_WE_K.value(),
                self.spinBox_R2_STA_K.value(),
                self.spinBox_R2_STR_K.value(),
                self.spinBox_R2_BLK_K.value(),
                self.spinBox_R2_TKL_K.value(),
                self.spinBox_R2_HAN_K.value(),
                self.spinBox_R2_GI_K.value(),
                self.spinBox_R2_ELU_K.value(),
                self.spinBox_R2_TEC_K.value()
            ])
        )

        self.lcdNumber_R3_K.display(
            sum([
                self.spinBox_R3_ATH_K.value(),
                self.spinBox_R3_SPD_K.value(),
                self.spinBox_R3_DUR_K.value(),
                self.spinBox_R3_WE_K.value(),
                self.spinBox_R3_STA_K.value(),
                self.spinBox_R3_STR_K.value(),
                self.spinBox_R3_BLK_K.value(),
                self.spinBox_R3_TKL_K.value(),
                self.spinBox_R3_HAN_K.value(),
                self.spinBox_R3_GI_K.value(),
                self.spinBox_R3_ELU_K.value(),
                self.spinBox_R3_TEC_K.value()
            ])
        )

        self.lcdNumber_R4_K.display(
            sum([
                self.spinBox_R4_ATH_K.value(),
                self.spinBox_R4_SPD_K.value(),
                self.spinBox_R4_DUR_K.value(),
                self.spinBox_R4_WE_K.value(),
                self.spinBox_R4_STA_K.value(),
                self.spinBox_R4_STR_K.value(),
                self.spinBox_R4_BLK_K.value(),
                self.spinBox_R4_TKL_K.value(),
                self.spinBox_R4_HAN_K.value(),
                self.spinBox_R4_GI_K.value(),
                self.spinBox_R4_ELU_K.value(),
                self.spinBox_R4_TEC_K.value()
            ])
        )

        self.lcdNumber_R5_K.display(
            sum([
                self.spinBox_R5_ATH_K.value(),
                self.spinBox_R5_SPD_K.value(),
                self.spinBox_R5_DUR_K.value(),
                self.spinBox_R5_WE_K.value(),
                self.spinBox_R5_STA_K.value(),
                self.spinBox_R5_STR_K.value(),
                self.spinBox_R5_BLK_K.value(),
                self.spinBox_R5_TKL_K.value(),
                self.spinBox_R5_HAN_K.value(),
                self.spinBox_R5_GI_K.value(),
                self.spinBox_R5_ELU_K.value(),
                self.spinBox_R5_TEC_K.value()
            ])
        )

        self.lcdNumber_R6_K.display(
            sum([
                self.spinBox_R6_ATH_K.value(),
                self.spinBox_R6_SPD_K.value(),
                self.spinBox_R6_DUR_K.value(),
                self.spinBox_R6_WE_K.value(),
                self.spinBox_R6_STA_K.value(),
                self.spinBox_R6_STR_K.value(),
                self.spinBox_R6_BLK_K.value(),
                self.spinBox_R6_TKL_K.value(),
                self.spinBox_R6_HAN_K.value(),
                self.spinBox_R6_GI_K.value(),
                self.spinBox_R6_ELU_K.value(),
                self.spinBox_R6_TEC_K.value()
            ])
        )

        # P Section
        self.lcdNumber_R1_P.display(
            sum([
                self.spinBox_R1_ATH_P.value(),
                self.spinBox_R1_SPD_P.value(),
                self.spinBox_R1_DUR_P.value(),
                self.spinBox_R1_WE_P.value(),
                self.spinBox_R1_STA_P.value(),
                self.spinBox_R1_STR_P.value(),
                self.spinBox_R1_BLK_P.value(),
                self.spinBox_R1_TKL_P.value(),
                self.spinBox_R1_HAN_P.value(),
                self.spinBox_R1_GI_P.value(),
                self.spinBox_R1_ELU_P.value(),
                self.spinBox_R1_TEC_P.value()
            ])
        )

        self.lcdNumber_R2_P.display(
            sum([
                self.spinBox_R2_ATH_P.value(),
                self.spinBox_R2_SPD_P.value(),
                self.spinBox_R2_DUR_P.value(),
                self.spinBox_R2_WE_P.value(),
                self.spinBox_R2_STA_P.value(),
                self.spinBox_R2_STR_P.value(),
                self.spinBox_R2_BLK_P.value(),
                self.spinBox_R2_TKL_P.value(),
                self.spinBox_R2_HAN_P.value(),
                self.spinBox_R2_GI_P.value(),
                self.spinBox_R2_ELU_P.value(),
                self.spinBox_R2_TEC_P.value()
            ])
        )

        self.lcdNumber_R3_P.display(
            sum([
                self.spinBox_R3_ATH_P.value(),
                self.spinBox_R3_SPD_P.value(),
                self.spinBox_R3_DUR_P.value(),
                self.spinBox_R3_WE_P.value(),
                self.spinBox_R3_STA_P.value(),
                self.spinBox_R3_STR_P.value(),
                self.spinBox_R3_BLK_P.value(),
                self.spinBox_R3_TKL_P.value(),
                self.spinBox_R3_HAN_P.value(),
                self.spinBox_R3_GI_P.value(),
                self.spinBox_R3_ELU_P.value(),
                self.spinBox_R3_TEC_P.value()
            ])
        )

        self.lcdNumber_R4_P.display(
            sum([
                self.spinBox_R4_ATH_P.value(),
                self.spinBox_R4_SPD_P.value(),
                self.spinBox_R4_DUR_P.value(),
                self.spinBox_R4_WE_P.value(),
                self.spinBox_R4_STA_P.value(),
                self.spinBox_R4_STR_P.value(),
                self.spinBox_R4_BLK_P.value(),
                self.spinBox_R4_TKL_P.value(),
                self.spinBox_R4_HAN_P.value(),
                self.spinBox_R4_GI_P.value(),
                self.spinBox_R4_ELU_P.value(),
                self.spinBox_R4_TEC_P.value()
            ])
        )

        self.lcdNumber_R5_P.display(
            sum([
                self.spinBox_R5_ATH_P.value(),
                self.spinBox_R5_SPD_P.value(),
                self.spinBox_R5_DUR_P.value(),
                self.spinBox_R5_WE_P.value(),
                self.spinBox_R5_STA_P.value(),
                self.spinBox_R5_STR_P.value(),
                self.spinBox_R5_BLK_P.value(),
                self.spinBox_R5_TKL_P.value(),
                self.spinBox_R5_HAN_P.value(),
                self.spinBox_R5_GI_P.value(),
                self.spinBox_R5_ELU_P.value(),
                self.spinBox_R5_TEC_P.value()
            ])
        )

        self.lcdNumber_R6_P.display(
            sum([
                self.spinBox_R6_ATH_P.value(),
                self.spinBox_R6_SPD_P.value(),
                self.spinBox_R6_DUR_P.value(),
                self.spinBox_R6_WE_P.value(),
                self.spinBox_R6_STA_P.value(),
                self.spinBox_R6_STR_P.value(),
                self.spinBox_R6_BLK_P.value(),
                self.spinBox_R6_TKL_P.value(),
                self.spinBox_R6_HAN_P.value(),
                self.spinBox_R6_GI_P.value(),
                self.spinBox_R6_ELU_P.value(),
                self.spinBox_R6_TEC_P.value()
            ])
        )

    
    def accept(self):

        # QB Section
        myconfig.role_ratings_df.loc['qbr1', 'label'] = self.lineEdit_R1_QB.text()
        myconfig.role_ratings_df.loc['qbr1', 'ath'] = self.spinBox_R1_ATH_QB.value()
        myconfig.role_ratings_df.loc['qbr1', 'spd'] = self.spinBox_R1_SPD_QB.value()
        myconfig.role_ratings_df.loc['qbr1', 'dur'] = self.spinBox_R1_DUR_QB.value()
        myconfig.role_ratings_df.loc['qbr1', 'we'] = self.spinBox_R1_WE_QB.value()
        myconfig.role_ratings_df.loc['qbr1', 'sta'] = self.spinBox_R1_STA_QB.value()
        myconfig.role_ratings_df.loc['qbr1', 'str'] = self.spinBox_R1_STR_QB.value()
        myconfig.role_ratings_df.loc['qbr1', 'blk'] = self.spinBox_R1_BLK_QB.value()
        myconfig.role_ratings_df.loc['qbr1', 'tkl'] = self.spinBox_R1_TKL_QB.value()
        myconfig.role_ratings_df.loc['qbr1', 'han'] = self.spinBox_R1_HAN_QB.value()
        myconfig.role_ratings_df.loc['qbr1', 'gi'] = self.spinBox_R1_GI_QB.value()
        myconfig.role_ratings_df.loc['qbr1', 'elu'] = self.spinBox_R1_ELU_QB.value()
        myconfig.role_ratings_df.loc['qbr1', 'tec'] = self.spinBox_R1_TEC_QB.value()

        myconfig.role_ratings_df.loc['qbr2', 'label'] = self.lineEdit_R2_QB.text()
        myconfig.role_ratings_df.loc['qbr2', 'ath'] = self.spinBox_R2_ATH_QB.value()
        myconfig.role_ratings_df.loc['qbr2', 'spd'] = self.spinBox_R2_SPD_QB.value()
        myconfig.role_ratings_df.loc['qbr2', 'dur'] = self.spinBox_R2_DUR_QB.value()
        myconfig.role_ratings_df.loc['qbr2', 'we'] = self.spinBox_R2_WE_QB.value()
        myconfig.role_ratings_df.loc['qbr2', 'sta'] = self.spinBox_R2_STA_QB.value()
        myconfig.role_ratings_df.loc['qbr2', 'str'] = self.spinBox_R2_STR_QB.value()
        myconfig.role_ratings_df.loc['qbr2', 'blk'] = self.spinBox_R2_BLK_QB.value()
        myconfig.role_ratings_df.loc['qbr2', 'tkl'] = self.spinBox_R2_TKL_QB.value()
        myconfig.role_ratings_df.loc['qbr2', 'han'] = self.spinBox_R2_HAN_QB.value()
        myconfig.role_ratings_df.loc['qbr2', 'gi'] = self.spinBox_R2_GI_QB.value()
        myconfig.role_ratings_df.loc['qbr2', 'elu'] = self.spinBox_R2_ELU_QB.value()
        myconfig.role_ratings_df.loc['qbr2', 'tec'] = self.spinBox_R2_TEC_QB.value()

        myconfig.role_ratings_df.loc['qbr3', 'label'] = self.lineEdit_R3_QB.text()
        myconfig.role_ratings_df.loc['qbr3', 'ath'] = self.spinBox_R3_ATH_QB.value()
        myconfig.role_ratings_df.loc['qbr3', 'spd'] = self.spinBox_R3_SPD_QB.value()
        myconfig.role_ratings_df.loc['qbr3', 'dur'] = self.spinBox_R3_DUR_QB.value()
        myconfig.role_ratings_df.loc['qbr3', 'we'] = self.spinBox_R3_WE_QB.value()
        myconfig.role_ratings_df.loc['qbr3', 'sta'] = self.spinBox_R3_STA_QB.value()
        myconfig.role_ratings_df.loc['qbr3', 'str'] = self.spinBox_R3_STR_QB.value()
        myconfig.role_ratings_df.loc['qbr3', 'blk'] = self.spinBox_R3_BLK_QB.value()
        myconfig.role_ratings_df.loc['qbr3', 'tkl'] = self.spinBox_R3_TKL_QB.value()
        myconfig.role_ratings_df.loc['qbr3', 'han'] = self.spinBox_R3_HAN_QB.value()
        myconfig.role_ratings_df.loc['qbr3', 'gi'] = self.spinBox_R3_GI_QB.value()
        myconfig.role_ratings_df.loc['qbr3', 'elu'] = self.spinBox_R3_ELU_QB.value()
        myconfig.role_ratings_df.loc['qbr3', 'tec'] = self.spinBox_R3_TEC_QB.value()

        myconfig.role_ratings_df.loc['qbr4', 'label'] = self.lineEdit_R4_QB.text()
        myconfig.role_ratings_df.loc['qbr4', 'ath'] = self.spinBox_R4_ATH_QB.value()
        myconfig.role_ratings_df.loc['qbr4', 'spd'] = self.spinBox_R4_SPD_QB.value()
        myconfig.role_ratings_df.loc['qbr4', 'dur'] = self.spinBox_R4_DUR_QB.value()
        myconfig.role_ratings_df.loc['qbr4', 'we'] = self.spinBox_R4_WE_QB.value()
        myconfig.role_ratings_df.loc['qbr4', 'sta'] = self.spinBox_R4_STA_QB.value()
        myconfig.role_ratings_df.loc['qbr4', 'str'] = self.spinBox_R4_STR_QB.value()
        myconfig.role_ratings_df.loc['qbr4', 'blk'] = self.spinBox_R4_BLK_QB.value()
        myconfig.role_ratings_df.loc['qbr4', 'tkl'] = self.spinBox_R4_TKL_QB.value()
        myconfig.role_ratings_df.loc['qbr4', 'han'] = self.spinBox_R4_HAN_QB.value()
        myconfig.role_ratings_df.loc['qbr4', 'gi'] = self.spinBox_R4_GI_QB.value()
        myconfig.role_ratings_df.loc['qbr4', 'elu'] = self.spinBox_R4_ELU_QB.value()
        myconfig.role_ratings_df.loc['qbr4', 'tec'] = self.spinBox_R4_TEC_QB.value()

        myconfig.role_ratings_df.loc['qbr5', 'label'] = self.lineEdit_R5_QB.text()
        myconfig.role_ratings_df.loc['qbr5', 'ath'] = self.spinBox_R5_ATH_QB.value()
        myconfig.role_ratings_df.loc['qbr5', 'spd'] = self.spinBox_R5_SPD_QB.value()
        myconfig.role_ratings_df.loc['qbr5', 'dur'] = self.spinBox_R5_DUR_QB.value()
        myconfig.role_ratings_df.loc['qbr5', 'we'] = self.spinBox_R5_WE_QB.value()
        myconfig.role_ratings_df.loc['qbr5', 'sta'] = self.spinBox_R5_STA_QB.value()
        myconfig.role_ratings_df.loc['qbr5', 'str'] = self.spinBox_R5_STR_QB.value()
        myconfig.role_ratings_df.loc['qbr5', 'blk'] = self.spinBox_R5_BLK_QB.value()
        myconfig.role_ratings_df.loc['qbr5', 'tkl'] = self.spinBox_R5_TKL_QB.value()
        myconfig.role_ratings_df.loc['qbr5', 'han'] = self.spinBox_R5_HAN_QB.value()
        myconfig.role_ratings_df.loc['qbr5', 'gi'] = self.spinBox_R5_GI_QB.value()
        myconfig.role_ratings_df.loc['qbr5', 'elu'] = self.spinBox_R5_ELU_QB.value()
        myconfig.role_ratings_df.loc['qbr5', 'tec'] = self.spinBox_R5_TEC_QB.value()

        myconfig.role_ratings_df.loc['qbr6', 'label'] = self.lineEdit_R6_QB.text()
        myconfig.role_ratings_df.loc['qbr6', 'ath'] = self.spinBox_R6_ATH_QB.value()
        myconfig.role_ratings_df.loc['qbr6', 'spd'] = self.spinBox_R6_SPD_QB.value()
        myconfig.role_ratings_df.loc['qbr6', 'dur'] = self.spinBox_R6_DUR_QB.value()
        myconfig.role_ratings_df.loc['qbr6', 'we'] = self.spinBox_R6_WE_QB.value()
        myconfig.role_ratings_df.loc['qbr6', 'sta'] = self.spinBox_R6_STA_QB.value()
        myconfig.role_ratings_df.loc['qbr6', 'str'] = self.spinBox_R6_STR_QB.value()
        myconfig.role_ratings_df.loc['qbr6', 'blk'] = self.spinBox_R6_BLK_QB.value()
        myconfig.role_ratings_df.loc['qbr6', 'tkl'] = self.spinBox_R6_TKL_QB.value()
        myconfig.role_ratings_df.loc['qbr6', 'han'] = self.spinBox_R6_HAN_QB.value()
        myconfig.role_ratings_df.loc['qbr6', 'gi'] = self.spinBox_R6_GI_QB.value()
        myconfig.role_ratings_df.loc['qbr6', 'elu'] = self.spinBox_R6_ELU_QB.value()
        myconfig.role_ratings_df.loc['qbr6', 'tec'] = self.spinBox_R6_TEC_QB.value()
        
        # RB Section
        myconfig.role_ratings_df.loc['rbr1', 'label'] = self.lineEdit_R1_RB.text()
        myconfig.role_ratings_df.loc['rbr1', 'ath'] = self.spinBox_R1_ATH_RB.value()
        myconfig.role_ratings_df.loc['rbr1', 'spd'] = self.spinBox_R1_SPD_RB.value()
        myconfig.role_ratings_df.loc['rbr1', 'dur'] = self.spinBox_R1_DUR_RB.value()
        myconfig.role_ratings_df.loc['rbr1', 'we'] = self.spinBox_R1_WE_RB.value()
        myconfig.role_ratings_df.loc['rbr1', 'sta'] = self.spinBox_R1_STA_RB.value()
        myconfig.role_ratings_df.loc['rbr1', 'str'] = self.spinBox_R1_STR_RB.value()
        myconfig.role_ratings_df.loc['rbr1', 'blk'] = self.spinBox_R1_BLK_RB.value()
        myconfig.role_ratings_df.loc['rbr1', 'tkl'] = self.spinBox_R1_TKL_RB.value()
        myconfig.role_ratings_df.loc['rbr1', 'han'] = self.spinBox_R1_HAN_RB.value()
        myconfig.role_ratings_df.loc['rbr1', 'gi'] = self.spinBox_R1_GI_RB.value()
        myconfig.role_ratings_df.loc['rbr1', 'elu'] = self.spinBox_R1_ELU_RB.value()
        myconfig.role_ratings_df.loc['rbr1', 'tec'] = self.spinBox_R1_TEC_RB.value()

        myconfig.role_ratings_df.loc['rbr2', 'label'] = self.lineEdit_R2_RB.text()
        myconfig.role_ratings_df.loc['rbr2', 'ath'] = self.spinBox_R2_ATH_RB.value()
        myconfig.role_ratings_df.loc['rbr2', 'spd'] = self.spinBox_R2_SPD_RB.value()
        myconfig.role_ratings_df.loc['rbr2', 'dur'] = self.spinBox_R2_DUR_RB.value()
        myconfig.role_ratings_df.loc['rbr2', 'we'] = self.spinBox_R2_WE_RB.value()
        myconfig.role_ratings_df.loc['rbr2', 'sta'] = self.spinBox_R2_STA_RB.value()
        myconfig.role_ratings_df.loc['rbr2', 'str'] = self.spinBox_R2_STR_RB.value()
        myconfig.role_ratings_df.loc['rbr2', 'blk'] = self.spinBox_R2_BLK_RB.value()
        myconfig.role_ratings_df.loc['rbr2', 'tkl'] = self.spinBox_R2_TKL_RB.value()
        myconfig.role_ratings_df.loc['rbr2', 'han'] = self.spinBox_R2_HAN_RB.value()
        myconfig.role_ratings_df.loc['rbr2', 'gi'] = self.spinBox_R2_GI_RB.value()
        myconfig.role_ratings_df.loc['rbr2', 'elu'] = self.spinBox_R2_ELU_RB.value()
        myconfig.role_ratings_df.loc['rbr2', 'tec'] = self.spinBox_R2_TEC_RB.value()

        myconfig.role_ratings_df.loc['rbr3', 'label'] = self.lineEdit_R3_RB.text()
        myconfig.role_ratings_df.loc['rbr3', 'ath'] = self.spinBox_R3_ATH_RB.value()
        myconfig.role_ratings_df.loc['rbr3', 'spd'] = self.spinBox_R3_SPD_RB.value()
        myconfig.role_ratings_df.loc['rbr3', 'dur'] = self.spinBox_R3_DUR_RB.value()
        myconfig.role_ratings_df.loc['rbr3', 'we'] = self.spinBox_R3_WE_RB.value()
        myconfig.role_ratings_df.loc['rbr3', 'sta'] = self.spinBox_R3_STA_RB.value()
        myconfig.role_ratings_df.loc['rbr3', 'str'] = self.spinBox_R3_STR_RB.value()
        myconfig.role_ratings_df.loc['rbr3', 'blk'] = self.spinBox_R3_BLK_RB.value()
        myconfig.role_ratings_df.loc['rbr3', 'tkl'] = self.spinBox_R3_TKL_RB.value()
        myconfig.role_ratings_df.loc['rbr3', 'han'] = self.spinBox_R3_HAN_RB.value()
        myconfig.role_ratings_df.loc['rbr3', 'gi'] = self.spinBox_R3_GI_RB.value()
        myconfig.role_ratings_df.loc['rbr3', 'elu'] = self.spinBox_R3_ELU_RB.value()
        myconfig.role_ratings_df.loc['rbr3', 'tec'] = self.spinBox_R3_TEC_RB.value()

        myconfig.role_ratings_df.loc['rbr4', 'label'] = self.lineEdit_R4_RB.text()
        myconfig.role_ratings_df.loc['rbr4', 'ath'] = self.spinBox_R4_ATH_RB.value()
        myconfig.role_ratings_df.loc['rbr4', 'spd'] = self.spinBox_R4_SPD_RB.value()
        myconfig.role_ratings_df.loc['rbr4', 'dur'] = self.spinBox_R4_DUR_RB.value()
        myconfig.role_ratings_df.loc['rbr4', 'we'] = self.spinBox_R4_WE_RB.value()
        myconfig.role_ratings_df.loc['rbr4', 'sta'] = self.spinBox_R4_STA_RB.value()
        myconfig.role_ratings_df.loc['rbr4', 'str'] = self.spinBox_R4_STR_RB.value()
        myconfig.role_ratings_df.loc['rbr4', 'blk'] = self.spinBox_R4_BLK_RB.value()
        myconfig.role_ratings_df.loc['rbr4', 'tkl'] = self.spinBox_R4_TKL_RB.value()
        myconfig.role_ratings_df.loc['rbr4', 'han'] = self.spinBox_R4_HAN_RB.value()
        myconfig.role_ratings_df.loc['rbr4', 'gi'] = self.spinBox_R4_GI_RB.value()
        myconfig.role_ratings_df.loc['rbr4', 'elu'] = self.spinBox_R4_ELU_RB.value()
        myconfig.role_ratings_df.loc['rbr4', 'tec'] = self.spinBox_R4_TEC_RB.value()

        myconfig.role_ratings_df.loc['rbr5', 'label'] = self.lineEdit_R5_RB.text()
        myconfig.role_ratings_df.loc['rbr5', 'ath'] = self.spinBox_R5_ATH_RB.value()
        myconfig.role_ratings_df.loc['rbr5', 'spd'] = self.spinBox_R5_SPD_RB.value()
        myconfig.role_ratings_df.loc['rbr5', 'dur'] = self.spinBox_R5_DUR_RB.value()
        myconfig.role_ratings_df.loc['rbr5', 'we'] = self.spinBox_R5_WE_RB.value()
        myconfig.role_ratings_df.loc['rbr5', 'sta'] = self.spinBox_R5_STA_RB.value()
        myconfig.role_ratings_df.loc['rbr5', 'str'] = self.spinBox_R5_STR_RB.value()
        myconfig.role_ratings_df.loc['rbr5', 'blk'] = self.spinBox_R5_BLK_RB.value()
        myconfig.role_ratings_df.loc['rbr5', 'tkl'] = self.spinBox_R5_TKL_RB.value()
        myconfig.role_ratings_df.loc['rbr5', 'han'] = self.spinBox_R5_HAN_RB.value()
        myconfig.role_ratings_df.loc['rbr5', 'gi'] = self.spinBox_R5_GI_RB.value()
        myconfig.role_ratings_df.loc['rbr5', 'elu'] = self.spinBox_R5_ELU_RB.value()
        myconfig.role_ratings_df.loc['rbr5', 'tec'] = self.spinBox_R5_TEC_RB.value()

        myconfig.role_ratings_df.loc['rbr6', 'label'] = self.lineEdit_R6_RB.text()
        myconfig.role_ratings_df.loc['rbr6', 'ath'] = self.spinBox_R6_ATH_RB.value()
        myconfig.role_ratings_df.loc['rbr6', 'spd'] = self.spinBox_R6_SPD_RB.value()
        myconfig.role_ratings_df.loc['rbr6', 'dur'] = self.spinBox_R6_DUR_RB.value()
        myconfig.role_ratings_df.loc['rbr6', 'we'] = self.spinBox_R6_WE_RB.value()
        myconfig.role_ratings_df.loc['rbr6', 'sta'] = self.spinBox_R6_STA_RB.value()
        myconfig.role_ratings_df.loc['rbr6', 'str'] = self.spinBox_R6_STR_RB.value()
        myconfig.role_ratings_df.loc['rbr6', 'blk'] = self.spinBox_R6_BLK_RB.value()
        myconfig.role_ratings_df.loc['rbr6', 'tkl'] = self.spinBox_R6_TKL_RB.value()
        myconfig.role_ratings_df.loc['rbr6', 'han'] = self.spinBox_R6_HAN_RB.value()
        myconfig.role_ratings_df.loc['rbr6', 'gi'] = self.spinBox_R6_GI_RB.value()
        myconfig.role_ratings_df.loc['rbr6', 'elu'] = self.spinBox_R6_ELU_RB.value()
        myconfig.role_ratings_df.loc['rbr6', 'tec'] = self.spinBox_R6_TEC_RB.value()

        # WR Section
        myconfig.role_ratings_df.loc['wrr1', 'label'] = self.lineEdit_R1_WR.text()
        myconfig.role_ratings_df.loc['wrr1', 'ath'] = self.spinBox_R1_ATH_WR.value()
        myconfig.role_ratings_df.loc['wrr1', 'spd'] = self.spinBox_R1_SPD_WR.value()
        myconfig.role_ratings_df.loc['wrr1', 'dur'] = self.spinBox_R1_DUR_WR.value()
        myconfig.role_ratings_df.loc['wrr1', 'we'] = self.spinBox_R1_WE_WR.value()
        myconfig.role_ratings_df.loc['wrr1', 'sta'] = self.spinBox_R1_STA_WR.value()
        myconfig.role_ratings_df.loc['wrr1', 'str'] = self.spinBox_R1_STR_WR.value()
        myconfig.role_ratings_df.loc['wrr1', 'blk'] = self.spinBox_R1_BLK_WR.value()
        myconfig.role_ratings_df.loc['wrr1', 'tkl'] = self.spinBox_R1_TKL_WR.value()
        myconfig.role_ratings_df.loc['wrr1', 'han'] = self.spinBox_R1_HAN_WR.value()
        myconfig.role_ratings_df.loc['wrr1', 'gi'] = self.spinBox_R1_GI_WR.value()
        myconfig.role_ratings_df.loc['wrr1', 'elu'] = self.spinBox_R1_ELU_WR.value()
        myconfig.role_ratings_df.loc['wrr1', 'tec'] = self.spinBox_R1_TEC_WR.value()

        myconfig.role_ratings_df.loc['wrr2', 'label'] = self.lineEdit_R2_WR.text()
        myconfig.role_ratings_df.loc['wrr2', 'ath'] = self.spinBox_R2_ATH_WR.value()
        myconfig.role_ratings_df.loc['wrr2', 'spd'] = self.spinBox_R2_SPD_WR.value()
        myconfig.role_ratings_df.loc['wrr2', 'dur'] = self.spinBox_R2_DUR_WR.value()
        myconfig.role_ratings_df.loc['wrr2', 'we'] = self.spinBox_R2_WE_WR.value()
        myconfig.role_ratings_df.loc['wrr2', 'sta'] = self.spinBox_R2_STA_WR.value()
        myconfig.role_ratings_df.loc['wrr2', 'str'] = self.spinBox_R2_STR_WR.value()
        myconfig.role_ratings_df.loc['wrr2', 'blk'] = self.spinBox_R2_BLK_WR.value()
        myconfig.role_ratings_df.loc['wrr2', 'tkl'] = self.spinBox_R2_TKL_WR.value()
        myconfig.role_ratings_df.loc['wrr2', 'han'] = self.spinBox_R2_HAN_WR.value()
        myconfig.role_ratings_df.loc['wrr2', 'gi'] = self.spinBox_R2_GI_WR.value()
        myconfig.role_ratings_df.loc['wrr2', 'elu'] = self.spinBox_R2_ELU_WR.value()
        myconfig.role_ratings_df.loc['wrr2', 'tec'] = self.spinBox_R2_TEC_WR.value()

        myconfig.role_ratings_df.loc['wrr3', 'label'] = self.lineEdit_R3_WR.text()
        myconfig.role_ratings_df.loc['wrr3', 'ath'] = self.spinBox_R3_ATH_WR.value()
        myconfig.role_ratings_df.loc['wrr3', 'spd'] = self.spinBox_R3_SPD_WR.value()
        myconfig.role_ratings_df.loc['wrr3', 'dur'] = self.spinBox_R3_DUR_WR.value()
        myconfig.role_ratings_df.loc['wrr3', 'we'] = self.spinBox_R3_WE_WR.value()
        myconfig.role_ratings_df.loc['wrr3', 'sta'] = self.spinBox_R3_STA_WR.value()
        myconfig.role_ratings_df.loc['wrr3', 'str'] = self.spinBox_R3_STR_WR.value()
        myconfig.role_ratings_df.loc['wrr3', 'blk'] = self.spinBox_R3_BLK_WR.value()
        myconfig.role_ratings_df.loc['wrr3', 'tkl'] = self.spinBox_R3_TKL_WR.value()
        myconfig.role_ratings_df.loc['wrr3', 'han'] = self.spinBox_R3_HAN_WR.value()
        myconfig.role_ratings_df.loc['wrr3', 'gi'] = self.spinBox_R3_GI_WR.value()
        myconfig.role_ratings_df.loc['wrr3', 'elu'] = self.spinBox_R3_ELU_WR.value()
        myconfig.role_ratings_df.loc['wrr3', 'tec'] = self.spinBox_R3_TEC_WR.value()

        myconfig.role_ratings_df.loc['wrr4', 'label'] = self.lineEdit_R4_WR.text()
        myconfig.role_ratings_df.loc['wrr4', 'ath'] = self.spinBox_R4_ATH_WR.value()
        myconfig.role_ratings_df.loc['wrr4', 'spd'] = self.spinBox_R4_SPD_WR.value()
        myconfig.role_ratings_df.loc['wrr4', 'dur'] = self.spinBox_R4_DUR_WR.value()
        myconfig.role_ratings_df.loc['wrr4', 'we'] = self.spinBox_R4_WE_WR.value()
        myconfig.role_ratings_df.loc['wrr4', 'sta'] = self.spinBox_R4_STA_WR.value()
        myconfig.role_ratings_df.loc['wrr4', 'str'] = self.spinBox_R4_STR_WR.value()
        myconfig.role_ratings_df.loc['wrr4', 'blk'] = self.spinBox_R4_BLK_WR.value()
        myconfig.role_ratings_df.loc['wrr4', 'tkl'] = self.spinBox_R4_TKL_WR.value()
        myconfig.role_ratings_df.loc['wrr4', 'han'] = self.spinBox_R4_HAN_WR.value()
        myconfig.role_ratings_df.loc['wrr4', 'gi'] = self.spinBox_R4_GI_WR.value()
        myconfig.role_ratings_df.loc['wrr4', 'elu'] = self.spinBox_R4_ELU_WR.value()
        myconfig.role_ratings_df.loc['wrr4', 'tec'] = self.spinBox_R4_TEC_WR.value()

        myconfig.role_ratings_df.loc['wrr5', 'label'] = self.lineEdit_R5_WR.text()
        myconfig.role_ratings_df.loc['wrr5', 'ath'] = self.spinBox_R5_ATH_WR.value()
        myconfig.role_ratings_df.loc['wrr5', 'spd'] = self.spinBox_R5_SPD_WR.value()
        myconfig.role_ratings_df.loc['wrr5', 'dur'] = self.spinBox_R5_DUR_WR.value()
        myconfig.role_ratings_df.loc['wrr5', 'we'] = self.spinBox_R5_WE_WR.value()
        myconfig.role_ratings_df.loc['wrr5', 'sta'] = self.spinBox_R5_STA_WR.value()
        myconfig.role_ratings_df.loc['wrr5', 'str'] = self.spinBox_R5_STR_WR.value()
        myconfig.role_ratings_df.loc['wrr5', 'blk'] = self.spinBox_R5_BLK_WR.value()
        myconfig.role_ratings_df.loc['wrr5', 'tkl'] = self.spinBox_R5_TKL_WR.value()
        myconfig.role_ratings_df.loc['wrr5', 'han'] = self.spinBox_R5_HAN_WR.value()
        myconfig.role_ratings_df.loc['wrr5', 'gi'] = self.spinBox_R5_GI_WR.value()
        myconfig.role_ratings_df.loc['wrr5', 'elu'] = self.spinBox_R5_ELU_WR.value()
        myconfig.role_ratings_df.loc['wrr5', 'tec'] = self.spinBox_R5_TEC_WR.value()

        myconfig.role_ratings_df.loc['wrr6', 'label'] = self.lineEdit_R6_WR.text()
        myconfig.role_ratings_df.loc['wrr6', 'ath'] = self.spinBox_R6_ATH_WR.value()
        myconfig.role_ratings_df.loc['wrr6', 'spd'] = self.spinBox_R6_SPD_WR.value()
        myconfig.role_ratings_df.loc['wrr6', 'dur'] = self.spinBox_R6_DUR_WR.value()
        myconfig.role_ratings_df.loc['wrr6', 'we'] = self.spinBox_R6_WE_WR.value()
        myconfig.role_ratings_df.loc['wrr6', 'sta'] = self.spinBox_R6_STA_WR.value()
        myconfig.role_ratings_df.loc['wrr6', 'str'] = self.spinBox_R6_STR_WR.value()
        myconfig.role_ratings_df.loc['wrr6', 'blk'] = self.spinBox_R6_BLK_WR.value()
        myconfig.role_ratings_df.loc['wrr6', 'tkl'] = self.spinBox_R6_TKL_WR.value()
        myconfig.role_ratings_df.loc['wrr6', 'han'] = self.spinBox_R6_HAN_WR.value()
        myconfig.role_ratings_df.loc['wrr6', 'gi'] = self.spinBox_R6_GI_WR.value()
        myconfig.role_ratings_df.loc['wrr6', 'elu'] = self.spinBox_R6_ELU_WR.value()
        myconfig.role_ratings_df.loc['wrr6', 'tec'] = self.spinBox_R6_TEC_WR.value()

        # TE Section
        myconfig.role_ratings_df.loc['ter1', 'label'] = self.lineEdit_R1_TE.text()
        myconfig.role_ratings_df.loc['ter1', 'ath'] = self.spinBox_R1_ATH_TE.value()
        myconfig.role_ratings_df.loc['ter1', 'spd'] = self.spinBox_R1_SPD_TE.value()
        myconfig.role_ratings_df.loc['ter1', 'dur'] = self.spinBox_R1_DUR_TE.value()
        myconfig.role_ratings_df.loc['ter1', 'we'] = self.spinBox_R1_WE_TE.value()
        myconfig.role_ratings_df.loc['ter1', 'sta'] = self.spinBox_R1_STA_TE.value()
        myconfig.role_ratings_df.loc['ter1', 'str'] = self.spinBox_R1_STR_TE.value()
        myconfig.role_ratings_df.loc['ter1', 'blk'] = self.spinBox_R1_BLK_TE.value()
        myconfig.role_ratings_df.loc['ter1', 'tkl'] = self.spinBox_R1_TKL_TE.value()
        myconfig.role_ratings_df.loc['ter1', 'han'] = self.spinBox_R1_HAN_TE.value()
        myconfig.role_ratings_df.loc['ter1', 'gi'] = self.spinBox_R1_GI_TE.value()
        myconfig.role_ratings_df.loc['ter1', 'elu'] = self.spinBox_R1_ELU_TE.value()
        myconfig.role_ratings_df.loc['ter1', 'tec'] = self.spinBox_R1_TEC_TE.value()

        myconfig.role_ratings_df.loc['ter2', 'label'] = self.lineEdit_R2_TE.text()
        myconfig.role_ratings_df.loc['ter2', 'ath'] = self.spinBox_R2_ATH_TE.value()
        myconfig.role_ratings_df.loc['ter2', 'spd'] = self.spinBox_R2_SPD_TE.value()
        myconfig.role_ratings_df.loc['ter2', 'dur'] = self.spinBox_R2_DUR_TE.value()
        myconfig.role_ratings_df.loc['ter2', 'we'] = self.spinBox_R2_WE_TE.value()
        myconfig.role_ratings_df.loc['ter2', 'sta'] = self.spinBox_R2_STA_TE.value()
        myconfig.role_ratings_df.loc['ter2', 'str'] = self.spinBox_R2_STR_TE.value()
        myconfig.role_ratings_df.loc['ter2', 'blk'] = self.spinBox_R2_BLK_TE.value()
        myconfig.role_ratings_df.loc['ter2', 'tkl'] = self.spinBox_R2_TKL_TE.value()
        myconfig.role_ratings_df.loc['ter2', 'han'] = self.spinBox_R2_HAN_TE.value()
        myconfig.role_ratings_df.loc['ter2', 'gi'] = self.spinBox_R2_GI_TE.value()
        myconfig.role_ratings_df.loc['ter2', 'elu'] = self.spinBox_R2_ELU_TE.value()
        myconfig.role_ratings_df.loc['ter2', 'tec'] = self.spinBox_R2_TEC_TE.value()

        myconfig.role_ratings_df.loc['ter3', 'label'] = self.lineEdit_R3_TE.text()
        myconfig.role_ratings_df.loc['ter3', 'ath'] = self.spinBox_R3_ATH_TE.value()
        myconfig.role_ratings_df.loc['ter3', 'spd'] = self.spinBox_R3_SPD_TE.value()
        myconfig.role_ratings_df.loc['ter3', 'dur'] = self.spinBox_R3_DUR_TE.value()
        myconfig.role_ratings_df.loc['ter3', 'we'] = self.spinBox_R3_WE_TE.value()
        myconfig.role_ratings_df.loc['ter3', 'sta'] = self.spinBox_R3_STA_TE.value()
        myconfig.role_ratings_df.loc['ter3', 'str'] = self.spinBox_R3_STR_TE.value()
        myconfig.role_ratings_df.loc['ter3', 'blk'] = self.spinBox_R3_BLK_TE.value()
        myconfig.role_ratings_df.loc['ter3', 'tkl'] = self.spinBox_R3_TKL_TE.value()
        myconfig.role_ratings_df.loc['ter3', 'han'] = self.spinBox_R3_HAN_TE.value()
        myconfig.role_ratings_df.loc['ter3', 'gi'] = self.spinBox_R3_GI_TE.value()
        myconfig.role_ratings_df.loc['ter3', 'elu'] = self.spinBox_R3_ELU_TE.value()
        myconfig.role_ratings_df.loc['ter3', 'tec'] = self.spinBox_R3_TEC_TE.value()

        myconfig.role_ratings_df.loc['ter4', 'label'] = self.lineEdit_R4_TE.text()
        myconfig.role_ratings_df.loc['ter4', 'ath'] = self.spinBox_R4_ATH_TE.value()
        myconfig.role_ratings_df.loc['ter4', 'spd'] = self.spinBox_R4_SPD_TE.value()
        myconfig.role_ratings_df.loc['ter4', 'dur'] = self.spinBox_R4_DUR_TE.value()
        myconfig.role_ratings_df.loc['ter4', 'we'] = self.spinBox_R4_WE_TE.value()
        myconfig.role_ratings_df.loc['ter4', 'sta'] = self.spinBox_R4_STA_TE.value()
        myconfig.role_ratings_df.loc['ter4', 'str'] = self.spinBox_R4_STR_TE.value()
        myconfig.role_ratings_df.loc['ter4', 'blk'] = self.spinBox_R4_BLK_TE.value()
        myconfig.role_ratings_df.loc['ter4', 'tkl'] = self.spinBox_R4_TKL_TE.value()
        myconfig.role_ratings_df.loc['ter4', 'han'] = self.spinBox_R4_HAN_TE.value()
        myconfig.role_ratings_df.loc['ter4', 'gi'] = self.spinBox_R4_GI_TE.value()
        myconfig.role_ratings_df.loc['ter4', 'elu'] = self.spinBox_R4_ELU_TE.value()
        myconfig.role_ratings_df.loc['ter4', 'tec'] = self.spinBox_R4_TEC_TE.value()

        myconfig.role_ratings_df.loc['ter5', 'label'] = self.lineEdit_R5_TE.text()
        myconfig.role_ratings_df.loc['ter5', 'ath'] = self.spinBox_R5_ATH_TE.value()
        myconfig.role_ratings_df.loc['ter5', 'spd'] = self.spinBox_R5_SPD_TE.value()
        myconfig.role_ratings_df.loc['ter5', 'dur'] = self.spinBox_R5_DUR_TE.value()
        myconfig.role_ratings_df.loc['ter5', 'we'] = self.spinBox_R5_WE_TE.value()
        myconfig.role_ratings_df.loc['ter5', 'sta'] = self.spinBox_R5_STA_TE.value()
        myconfig.role_ratings_df.loc['ter5', 'str'] = self.spinBox_R5_STR_TE.value()
        myconfig.role_ratings_df.loc['ter5', 'blk'] = self.spinBox_R5_BLK_TE.value()
        myconfig.role_ratings_df.loc['ter5', 'tkl'] = self.spinBox_R5_TKL_TE.value()
        myconfig.role_ratings_df.loc['ter5', 'han'] = self.spinBox_R5_HAN_TE.value()
        myconfig.role_ratings_df.loc['ter5', 'gi'] = self.spinBox_R5_GI_TE.value()
        myconfig.role_ratings_df.loc['ter5', 'elu'] = self.spinBox_R5_ELU_TE.value()
        myconfig.role_ratings_df.loc['ter5', 'tec'] = self.spinBox_R5_TEC_TE.value()

        myconfig.role_ratings_df.loc['ter6', 'label'] = self.lineEdit_R6_TE.text()
        myconfig.role_ratings_df.loc['ter6', 'ath'] = self.spinBox_R6_ATH_TE.value()
        myconfig.role_ratings_df.loc['ter6', 'spd'] = self.spinBox_R6_SPD_TE.value()
        myconfig.role_ratings_df.loc['ter6', 'dur'] = self.spinBox_R6_DUR_TE.value()
        myconfig.role_ratings_df.loc['ter6', 'we'] = self.spinBox_R6_WE_TE.value()
        myconfig.role_ratings_df.loc['ter6', 'sta'] = self.spinBox_R6_STA_TE.value()
        myconfig.role_ratings_df.loc['ter6', 'str'] = self.spinBox_R6_STR_TE.value()
        myconfig.role_ratings_df.loc['ter6', 'blk'] = self.spinBox_R6_BLK_TE.value()
        myconfig.role_ratings_df.loc['ter6', 'tkl'] = self.spinBox_R6_TKL_TE.value()
        myconfig.role_ratings_df.loc['ter6', 'han'] = self.spinBox_R6_HAN_TE.value()
        myconfig.role_ratings_df.loc['ter6', 'gi'] = self.spinBox_R6_GI_TE.value()
        myconfig.role_ratings_df.loc['ter6', 'elu'] = self.spinBox_R6_ELU_TE.value()
        myconfig.role_ratings_df.loc['ter6', 'tec'] = self.spinBox_R6_TEC_TE.value()

        # OL Section
        myconfig.role_ratings_df.loc['olr1', 'label'] = self.lineEdit_R1_OL.text()
        myconfig.role_ratings_df.loc['olr1', 'ath'] = self.spinBox_R1_ATH_OL.value()
        myconfig.role_ratings_df.loc['olr1', 'spd'] = self.spinBox_R1_SPD_OL.value()
        myconfig.role_ratings_df.loc['olr1', 'dur'] = self.spinBox_R1_DUR_OL.value()
        myconfig.role_ratings_df.loc['olr1', 'we'] = self.spinBox_R1_WE_OL.value()
        myconfig.role_ratings_df.loc['olr1', 'sta'] = self.spinBox_R1_STA_OL.value()
        myconfig.role_ratings_df.loc['olr1', 'str'] = self.spinBox_R1_STR_OL.value()
        myconfig.role_ratings_df.loc['olr1', 'blk'] = self.spinBox_R1_BLK_OL.value()
        myconfig.role_ratings_df.loc['olr1', 'tkl'] = self.spinBox_R1_TKL_OL.value()
        myconfig.role_ratings_df.loc['olr1', 'han'] = self.spinBox_R1_HAN_OL.value()
        myconfig.role_ratings_df.loc['olr1', 'gi'] = self.spinBox_R1_GI_OL.value()
        myconfig.role_ratings_df.loc['olr1', 'elu'] = self.spinBox_R1_ELU_OL.value()
        myconfig.role_ratings_df.loc['olr1', 'tec'] = self.spinBox_R1_TEC_OL.value()

        myconfig.role_ratings_df.loc['olr2', 'label'] = self.lineEdit_R2_OL.text()
        myconfig.role_ratings_df.loc['olr2', 'ath'] = self.spinBox_R2_ATH_OL.value()
        myconfig.role_ratings_df.loc['olr2', 'spd'] = self.spinBox_R2_SPD_OL.value()
        myconfig.role_ratings_df.loc['olr2', 'dur'] = self.spinBox_R2_DUR_OL.value()
        myconfig.role_ratings_df.loc['olr2', 'we'] = self.spinBox_R2_WE_OL.value()
        myconfig.role_ratings_df.loc['olr2', 'sta'] = self.spinBox_R2_STA_OL.value()
        myconfig.role_ratings_df.loc['olr2', 'str'] = self.spinBox_R2_STR_OL.value()
        myconfig.role_ratings_df.loc['olr2', 'blk'] = self.spinBox_R2_BLK_OL.value()
        myconfig.role_ratings_df.loc['olr2', 'tkl'] = self.spinBox_R2_TKL_OL.value()
        myconfig.role_ratings_df.loc['olr2', 'han'] = self.spinBox_R2_HAN_OL.value()
        myconfig.role_ratings_df.loc['olr2', 'gi'] = self.spinBox_R2_GI_OL.value()
        myconfig.role_ratings_df.loc['olr2', 'elu'] = self.spinBox_R2_ELU_OL.value()
        myconfig.role_ratings_df.loc['olr2', 'tec'] = self.spinBox_R2_TEC_OL.value()

        myconfig.role_ratings_df.loc['olr3', 'label'] = self.lineEdit_R3_OL.text()
        myconfig.role_ratings_df.loc['olr3', 'ath'] = self.spinBox_R3_ATH_OL.value()
        myconfig.role_ratings_df.loc['olr3', 'spd'] = self.spinBox_R3_SPD_OL.value()
        myconfig.role_ratings_df.loc['olr3', 'dur'] = self.spinBox_R3_DUR_OL.value()
        myconfig.role_ratings_df.loc['olr3', 'we'] = self.spinBox_R3_WE_OL.value()
        myconfig.role_ratings_df.loc['olr3', 'sta'] = self.spinBox_R3_STA_OL.value()
        myconfig.role_ratings_df.loc['olr3', 'str'] = self.spinBox_R3_STR_OL.value()
        myconfig.role_ratings_df.loc['olr3', 'blk'] = self.spinBox_R3_BLK_OL.value()
        myconfig.role_ratings_df.loc['olr3', 'tkl'] = self.spinBox_R3_TKL_OL.value()
        myconfig.role_ratings_df.loc['olr3', 'han'] = self.spinBox_R3_HAN_OL.value()
        myconfig.role_ratings_df.loc['olr3', 'gi'] = self.spinBox_R3_GI_OL.value()
        myconfig.role_ratings_df.loc['olr3', 'elu'] = self.spinBox_R3_ELU_OL.value()
        myconfig.role_ratings_df.loc['olr3', 'tec'] = self.spinBox_R3_TEC_OL.value()

        myconfig.role_ratings_df.loc['olr4', 'label'] = self.lineEdit_R4_OL.text()
        myconfig.role_ratings_df.loc['olr4', 'ath'] = self.spinBox_R4_ATH_OL.value()
        myconfig.role_ratings_df.loc['olr4', 'spd'] = self.spinBox_R4_SPD_OL.value()
        myconfig.role_ratings_df.loc['olr4', 'dur'] = self.spinBox_R4_DUR_OL.value()
        myconfig.role_ratings_df.loc['olr4', 'we'] = self.spinBox_R4_WE_OL.value()
        myconfig.role_ratings_df.loc['olr4', 'sta'] = self.spinBox_R4_STA_OL.value()
        myconfig.role_ratings_df.loc['olr4', 'str'] = self.spinBox_R4_STR_OL.value()
        myconfig.role_ratings_df.loc['olr4', 'blk'] = self.spinBox_R4_BLK_OL.value()
        myconfig.role_ratings_df.loc['olr4', 'tkl'] = self.spinBox_R4_TKL_OL.value()
        myconfig.role_ratings_df.loc['olr4', 'han'] = self.spinBox_R4_HAN_OL.value()
        myconfig.role_ratings_df.loc['olr4', 'gi'] = self.spinBox_R4_GI_OL.value()
        myconfig.role_ratings_df.loc['olr4', 'elu'] = self.spinBox_R4_ELU_OL.value()
        myconfig.role_ratings_df.loc['olr4', 'tec'] = self.spinBox_R4_TEC_OL.value()

        myconfig.role_ratings_df.loc['olr5', 'label'] = self.lineEdit_R5_OL.text()
        myconfig.role_ratings_df.loc['olr5', 'ath'] = self.spinBox_R5_ATH_OL.value()
        myconfig.role_ratings_df.loc['olr5', 'spd'] = self.spinBox_R5_SPD_OL.value()
        myconfig.role_ratings_df.loc['olr5', 'dur'] = self.spinBox_R5_DUR_OL.value()
        myconfig.role_ratings_df.loc['olr5', 'we'] = self.spinBox_R5_WE_OL.value()
        myconfig.role_ratings_df.loc['olr5', 'sta'] = self.spinBox_R5_STA_OL.value()
        myconfig.role_ratings_df.loc['olr5', 'str'] = self.spinBox_R5_STR_OL.value()
        myconfig.role_ratings_df.loc['olr5', 'blk'] = self.spinBox_R5_BLK_OL.value()
        myconfig.role_ratings_df.loc['olr5', 'tkl'] = self.spinBox_R5_TKL_OL.value()
        myconfig.role_ratings_df.loc['olr5', 'han'] = self.spinBox_R5_HAN_OL.value()
        myconfig.role_ratings_df.loc['olr5', 'gi'] = self.spinBox_R5_GI_OL.value()
        myconfig.role_ratings_df.loc['olr5', 'elu'] = self.spinBox_R5_ELU_OL.value()
        myconfig.role_ratings_df.loc['olr5', 'tec'] = self.spinBox_R5_TEC_OL.value()

        myconfig.role_ratings_df.loc['olr6', 'label'] = self.lineEdit_R6_OL.text()
        myconfig.role_ratings_df.loc['olr6', 'ath'] = self.spinBox_R6_ATH_OL.value()
        myconfig.role_ratings_df.loc['olr6', 'spd'] = self.spinBox_R6_SPD_OL.value()
        myconfig.role_ratings_df.loc['olr6', 'dur'] = self.spinBox_R6_DUR_OL.value()
        myconfig.role_ratings_df.loc['olr6', 'we'] = self.spinBox_R6_WE_OL.value()
        myconfig.role_ratings_df.loc['olr6', 'sta'] = self.spinBox_R6_STA_OL.value()
        myconfig.role_ratings_df.loc['olr6', 'str'] = self.spinBox_R6_STR_OL.value()
        myconfig.role_ratings_df.loc['olr6', 'blk'] = self.spinBox_R6_BLK_OL.value()
        myconfig.role_ratings_df.loc['olr6', 'tkl'] = self.spinBox_R6_TKL_OL.value()
        myconfig.role_ratings_df.loc['olr6', 'han'] = self.spinBox_R6_HAN_OL.value()
        myconfig.role_ratings_df.loc['olr6', 'gi'] = self.spinBox_R6_GI_OL.value()
        myconfig.role_ratings_df.loc['olr6', 'elu'] = self.spinBox_R6_ELU_OL.value()
        myconfig.role_ratings_df.loc['olr6', 'tec'] = self.spinBox_R6_TEC_OL.value()

        # DL Section
        myconfig.role_ratings_df.loc['dlr1', 'label'] = self.lineEdit_R1_DL.text()
        myconfig.role_ratings_df.loc['dlr1', 'ath'] = self.spinBox_R1_ATH_DL.value()
        myconfig.role_ratings_df.loc['dlr1', 'spd'] = self.spinBox_R1_SPD_DL.value()
        myconfig.role_ratings_df.loc['dlr1', 'dur'] = self.spinBox_R1_DUR_DL.value()
        myconfig.role_ratings_df.loc['dlr1', 'we'] = self.spinBox_R1_WE_DL.value()
        myconfig.role_ratings_df.loc['dlr1', 'sta'] = self.spinBox_R1_STA_DL.value()
        myconfig.role_ratings_df.loc['dlr1', 'str'] = self.spinBox_R1_STR_DL.value()
        myconfig.role_ratings_df.loc['dlr1', 'blk'] = self.spinBox_R1_BLK_DL.value()
        myconfig.role_ratings_df.loc['dlr1', 'tkl'] = self.spinBox_R1_TKL_DL.value()
        myconfig.role_ratings_df.loc['dlr1', 'han'] = self.spinBox_R1_HAN_DL.value()
        myconfig.role_ratings_df.loc['dlr1', 'gi'] = self.spinBox_R1_GI_DL.value()
        myconfig.role_ratings_df.loc['dlr1', 'elu'] = self.spinBox_R1_ELU_DL.value()
        myconfig.role_ratings_df.loc['dlr1', 'tec'] = self.spinBox_R1_TEC_DL.value()

        myconfig.role_ratings_df.loc['dlr2', 'label'] = self.lineEdit_R2_DL.text()
        myconfig.role_ratings_df.loc['dlr2', 'ath'] = self.spinBox_R2_ATH_DL.value()
        myconfig.role_ratings_df.loc['dlr2', 'spd'] = self.spinBox_R2_SPD_DL.value()
        myconfig.role_ratings_df.loc['dlr2', 'dur'] = self.spinBox_R2_DUR_DL.value()
        myconfig.role_ratings_df.loc['dlr2', 'we'] = self.spinBox_R2_WE_DL.value()
        myconfig.role_ratings_df.loc['dlr2', 'sta'] = self.spinBox_R2_STA_DL.value()
        myconfig.role_ratings_df.loc['dlr2', 'str'] = self.spinBox_R2_STR_DL.value()
        myconfig.role_ratings_df.loc['dlr2', 'blk'] = self.spinBox_R2_BLK_DL.value()
        myconfig.role_ratings_df.loc['dlr2', 'tkl'] = self.spinBox_R2_TKL_DL.value()
        myconfig.role_ratings_df.loc['dlr2', 'han'] = self.spinBox_R2_HAN_DL.value()
        myconfig.role_ratings_df.loc['dlr2', 'gi'] = self.spinBox_R2_GI_DL.value()
        myconfig.role_ratings_df.loc['dlr2', 'elu'] = self.spinBox_R2_ELU_DL.value()
        myconfig.role_ratings_df.loc['dlr2', 'tec'] = self.spinBox_R2_TEC_DL.value()

        myconfig.role_ratings_df.loc['dlr3', 'label'] = self.lineEdit_R3_DL.text()
        myconfig.role_ratings_df.loc['dlr3', 'ath'] = self.spinBox_R3_ATH_DL.value()
        myconfig.role_ratings_df.loc['dlr3', 'spd'] = self.spinBox_R3_SPD_DL.value()
        myconfig.role_ratings_df.loc['dlr3', 'dur'] = self.spinBox_R3_DUR_DL.value()
        myconfig.role_ratings_df.loc['dlr3', 'we'] = self.spinBox_R3_WE_DL.value()
        myconfig.role_ratings_df.loc['dlr3', 'sta'] = self.spinBox_R3_STA_DL.value()
        myconfig.role_ratings_df.loc['dlr3', 'str'] = self.spinBox_R3_STR_DL.value()
        myconfig.role_ratings_df.loc['dlr3', 'blk'] = self.spinBox_R3_BLK_DL.value()
        myconfig.role_ratings_df.loc['dlr3', 'tkl'] = self.spinBox_R3_TKL_DL.value()
        myconfig.role_ratings_df.loc['dlr3', 'han'] = self.spinBox_R3_HAN_DL.value()
        myconfig.role_ratings_df.loc['dlr3', 'gi'] = self.spinBox_R3_GI_DL.value()
        myconfig.role_ratings_df.loc['dlr3', 'elu'] = self.spinBox_R3_ELU_DL.value()
        myconfig.role_ratings_df.loc['dlr3', 'tec'] = self.spinBox_R3_TEC_DL.value()

        myconfig.role_ratings_df.loc['dlr4', 'label'] = self.lineEdit_R4_DL.text()
        myconfig.role_ratings_df.loc['dlr4', 'ath'] = self.spinBox_R4_ATH_DL.value()
        myconfig.role_ratings_df.loc['dlr4', 'spd'] = self.spinBox_R4_SPD_DL.value()
        myconfig.role_ratings_df.loc['dlr4', 'dur'] = self.spinBox_R4_DUR_DL.value()
        myconfig.role_ratings_df.loc['dlr4', 'we'] = self.spinBox_R4_WE_DL.value()
        myconfig.role_ratings_df.loc['dlr4', 'sta'] = self.spinBox_R4_STA_DL.value()
        myconfig.role_ratings_df.loc['dlr4', 'str'] = self.spinBox_R4_STR_DL.value()
        myconfig.role_ratings_df.loc['dlr4', 'blk'] = self.spinBox_R4_BLK_DL.value()
        myconfig.role_ratings_df.loc['dlr4', 'tkl'] = self.spinBox_R4_TKL_DL.value()
        myconfig.role_ratings_df.loc['dlr4', 'han'] = self.spinBox_R4_HAN_DL.value()
        myconfig.role_ratings_df.loc['dlr4', 'gi'] = self.spinBox_R4_GI_DL.value()
        myconfig.role_ratings_df.loc['dlr4', 'elu'] = self.spinBox_R4_ELU_DL.value()
        myconfig.role_ratings_df.loc['dlr4', 'tec'] = self.spinBox_R4_TEC_DL.value()

        myconfig.role_ratings_df.loc['dlr5', 'label'] = self.lineEdit_R5_DL.text()
        myconfig.role_ratings_df.loc['dlr5', 'ath'] = self.spinBox_R5_ATH_DL.value()
        myconfig.role_ratings_df.loc['dlr5', 'spd'] = self.spinBox_R5_SPD_DL.value()
        myconfig.role_ratings_df.loc['dlr5', 'dur'] = self.spinBox_R5_DUR_DL.value()
        myconfig.role_ratings_df.loc['dlr5', 'we'] = self.spinBox_R5_WE_DL.value()
        myconfig.role_ratings_df.loc['dlr5', 'sta'] = self.spinBox_R5_STA_DL.value()
        myconfig.role_ratings_df.loc['dlr5', 'str'] = self.spinBox_R5_STR_DL.value()
        myconfig.role_ratings_df.loc['dlr5', 'blk'] = self.spinBox_R5_BLK_DL.value()
        myconfig.role_ratings_df.loc['dlr5', 'tkl'] = self.spinBox_R5_TKL_DL.value()
        myconfig.role_ratings_df.loc['dlr5', 'han'] = self.spinBox_R5_HAN_DL.value()
        myconfig.role_ratings_df.loc['dlr5', 'gi'] = self.spinBox_R5_GI_DL.value()
        myconfig.role_ratings_df.loc['dlr5', 'elu'] = self.spinBox_R5_ELU_DL.value()
        myconfig.role_ratings_df.loc['dlr5', 'tec'] = self.spinBox_R5_TEC_DL.value()

        myconfig.role_ratings_df.loc['dlr6', 'label'] = self.lineEdit_R6_DL.text()
        myconfig.role_ratings_df.loc['dlr6', 'ath'] = self.spinBox_R6_ATH_DL.value()
        myconfig.role_ratings_df.loc['dlr6', 'spd'] = self.spinBox_R6_SPD_DL.value()
        myconfig.role_ratings_df.loc['dlr6', 'dur'] = self.spinBox_R6_DUR_DL.value()
        myconfig.role_ratings_df.loc['dlr6', 'we'] = self.spinBox_R6_WE_DL.value()
        myconfig.role_ratings_df.loc['dlr6', 'sta'] = self.spinBox_R6_STA_DL.value()
        myconfig.role_ratings_df.loc['dlr6', 'str'] = self.spinBox_R6_STR_DL.value()
        myconfig.role_ratings_df.loc['dlr6', 'blk'] = self.spinBox_R6_BLK_DL.value()
        myconfig.role_ratings_df.loc['dlr6', 'tkl'] = self.spinBox_R6_TKL_DL.value()
        myconfig.role_ratings_df.loc['dlr6', 'han'] = self.spinBox_R6_HAN_DL.value()
        myconfig.role_ratings_df.loc['dlr6', 'gi'] = self.spinBox_R6_GI_DL.value()
        myconfig.role_ratings_df.loc['dlr6', 'elu'] = self.spinBox_R6_ELU_DL.value()
        myconfig.role_ratings_df.loc['dlr6', 'tec'] = self.spinBox_R6_TEC_DL.value()

        # LB Section
        myconfig.role_ratings_df.loc['lbr1', 'label'] = self.lineEdit_R1_LB.text()
        myconfig.role_ratings_df.loc['lbr1', 'ath'] = self.spinBox_R1_ATH_LB.value()
        myconfig.role_ratings_df.loc['lbr1', 'spd'] = self.spinBox_R1_SPD_LB.value()
        myconfig.role_ratings_df.loc['lbr1', 'dur'] = self.spinBox_R1_DUR_LB.value()
        myconfig.role_ratings_df.loc['lbr1', 'we'] = self.spinBox_R1_WE_LB.value()
        myconfig.role_ratings_df.loc['lbr1', 'sta'] = self.spinBox_R1_STA_LB.value()
        myconfig.role_ratings_df.loc['lbr1', 'str'] = self.spinBox_R1_STR_LB.value()
        myconfig.role_ratings_df.loc['lbr1', 'blk'] = self.spinBox_R1_BLK_LB.value()
        myconfig.role_ratings_df.loc['lbr1', 'tkl'] = self.spinBox_R1_TKL_LB.value()
        myconfig.role_ratings_df.loc['lbr1', 'han'] = self.spinBox_R1_HAN_LB.value()
        myconfig.role_ratings_df.loc['lbr1', 'gi'] = self.spinBox_R1_GI_LB.value()
        myconfig.role_ratings_df.loc['lbr1', 'elu'] = self.spinBox_R1_ELU_LB.value()
        myconfig.role_ratings_df.loc['lbr1', 'tec'] = self.spinBox_R1_TEC_LB.value()

        myconfig.role_ratings_df.loc['lbr2', 'label'] = self.lineEdit_R2_LB.text()
        myconfig.role_ratings_df.loc['lbr2', 'ath'] = self.spinBox_R2_ATH_LB.value()
        myconfig.role_ratings_df.loc['lbr2', 'spd'] = self.spinBox_R2_SPD_LB.value()
        myconfig.role_ratings_df.loc['lbr2', 'dur'] = self.spinBox_R2_DUR_LB.value()
        myconfig.role_ratings_df.loc['lbr2', 'we'] = self.spinBox_R2_WE_LB.value()
        myconfig.role_ratings_df.loc['lbr2', 'sta'] = self.spinBox_R2_STA_LB.value()
        myconfig.role_ratings_df.loc['lbr2', 'str'] = self.spinBox_R2_STR_LB.value()
        myconfig.role_ratings_df.loc['lbr2', 'blk'] = self.spinBox_R2_BLK_LB.value()
        myconfig.role_ratings_df.loc['lbr2', 'tkl'] = self.spinBox_R2_TKL_LB.value()
        myconfig.role_ratings_df.loc['lbr2', 'han'] = self.spinBox_R2_HAN_LB.value()
        myconfig.role_ratings_df.loc['lbr2', 'gi'] = self.spinBox_R2_GI_LB.value()
        myconfig.role_ratings_df.loc['lbr2', 'elu'] = self.spinBox_R2_ELU_LB.value()
        myconfig.role_ratings_df.loc['lbr2', 'tec'] = self.spinBox_R2_TEC_LB.value()

        myconfig.role_ratings_df.loc['lbr3', 'label'] = self.lineEdit_R3_LB.text()
        myconfig.role_ratings_df.loc['lbr3', 'ath'] = self.spinBox_R3_ATH_LB.value()
        myconfig.role_ratings_df.loc['lbr3', 'spd'] = self.spinBox_R3_SPD_LB.value()
        myconfig.role_ratings_df.loc['lbr3', 'dur'] = self.spinBox_R3_DUR_LB.value()
        myconfig.role_ratings_df.loc['lbr3', 'we'] = self.spinBox_R3_WE_LB.value()
        myconfig.role_ratings_df.loc['lbr3', 'sta'] = self.spinBox_R3_STA_LB.value()
        myconfig.role_ratings_df.loc['lbr3', 'str'] = self.spinBox_R3_STR_LB.value()
        myconfig.role_ratings_df.loc['lbr3', 'blk'] = self.spinBox_R3_BLK_LB.value()
        myconfig.role_ratings_df.loc['lbr3', 'tkl'] = self.spinBox_R3_TKL_LB.value()
        myconfig.role_ratings_df.loc['lbr3', 'han'] = self.spinBox_R3_HAN_LB.value()
        myconfig.role_ratings_df.loc['lbr3', 'gi'] = self.spinBox_R3_GI_LB.value()
        myconfig.role_ratings_df.loc['lbr3', 'elu'] = self.spinBox_R3_ELU_LB.value()
        myconfig.role_ratings_df.loc['lbr3', 'tec'] = self.spinBox_R3_TEC_LB.value()

        myconfig.role_ratings_df.loc['lbr4', 'label'] = self.lineEdit_R4_LB.text()
        myconfig.role_ratings_df.loc['lbr4', 'ath'] = self.spinBox_R4_ATH_LB.value()
        myconfig.role_ratings_df.loc['lbr4', 'spd'] = self.spinBox_R4_SPD_LB.value()
        myconfig.role_ratings_df.loc['lbr4', 'dur'] = self.spinBox_R4_DUR_LB.value()
        myconfig.role_ratings_df.loc['lbr4', 'we'] = self.spinBox_R4_WE_LB.value()
        myconfig.role_ratings_df.loc['lbr4', 'sta'] = self.spinBox_R4_STA_LB.value()
        myconfig.role_ratings_df.loc['lbr4', 'str'] = self.spinBox_R4_STR_LB.value()
        myconfig.role_ratings_df.loc['lbr4', 'blk'] = self.spinBox_R4_BLK_LB.value()
        myconfig.role_ratings_df.loc['lbr4', 'tkl'] = self.spinBox_R4_TKL_LB.value()
        myconfig.role_ratings_df.loc['lbr4', 'han'] = self.spinBox_R4_HAN_LB.value()
        myconfig.role_ratings_df.loc['lbr4', 'gi'] = self.spinBox_R4_GI_LB.value()
        myconfig.role_ratings_df.loc['lbr4', 'elu'] = self.spinBox_R4_ELU_LB.value()
        myconfig.role_ratings_df.loc['lbr4', 'tec'] = self.spinBox_R4_TEC_LB.value()

        myconfig.role_ratings_df.loc['lbr5', 'label'] = self.lineEdit_R5_LB.text()
        myconfig.role_ratings_df.loc['lbr5', 'ath'] = self.spinBox_R5_ATH_LB.value()
        myconfig.role_ratings_df.loc['lbr5', 'spd'] = self.spinBox_R5_SPD_LB.value()
        myconfig.role_ratings_df.loc['lbr5', 'dur'] = self.spinBox_R5_DUR_LB.value()
        myconfig.role_ratings_df.loc['lbr5', 'we'] = self.spinBox_R5_WE_LB.value()
        myconfig.role_ratings_df.loc['lbr5', 'sta'] = self.spinBox_R5_STA_LB.value()
        myconfig.role_ratings_df.loc['lbr5', 'str'] = self.spinBox_R5_STR_LB.value()
        myconfig.role_ratings_df.loc['lbr5', 'blk'] = self.spinBox_R5_BLK_LB.value()
        myconfig.role_ratings_df.loc['lbr5', 'tkl'] = self.spinBox_R5_TKL_LB.value()
        myconfig.role_ratings_df.loc['lbr5', 'han'] = self.spinBox_R5_HAN_LB.value()
        myconfig.role_ratings_df.loc['lbr5', 'gi'] = self.spinBox_R5_GI_LB.value()
        myconfig.role_ratings_df.loc['lbr5', 'elu'] = self.spinBox_R5_ELU_LB.value()
        myconfig.role_ratings_df.loc['lbr5', 'tec'] = self.spinBox_R5_TEC_LB.value()

        myconfig.role_ratings_df.loc['lbr6', 'label'] = self.lineEdit_R6_LB.text()
        myconfig.role_ratings_df.loc['lbr6', 'ath'] = self.spinBox_R6_ATH_LB.value()
        myconfig.role_ratings_df.loc['lbr6', 'spd'] = self.spinBox_R6_SPD_LB.value()
        myconfig.role_ratings_df.loc['lbr6', 'dur'] = self.spinBox_R6_DUR_LB.value()
        myconfig.role_ratings_df.loc['lbr6', 'we'] = self.spinBox_R6_WE_LB.value()
        myconfig.role_ratings_df.loc['lbr6', 'sta'] = self.spinBox_R6_STA_LB.value()
        myconfig.role_ratings_df.loc['lbr6', 'str'] = self.spinBox_R6_STR_LB.value()
        myconfig.role_ratings_df.loc['lbr6', 'blk'] = self.spinBox_R6_BLK_LB.value()
        myconfig.role_ratings_df.loc['lbr6', 'tkl'] = self.spinBox_R6_TKL_LB.value()
        myconfig.role_ratings_df.loc['lbr6', 'han'] = self.spinBox_R6_HAN_LB.value()
        myconfig.role_ratings_df.loc['lbr6', 'gi'] = self.spinBox_R6_GI_LB.value()
        myconfig.role_ratings_df.loc['lbr6', 'elu'] = self.spinBox_R6_ELU_LB.value()
        myconfig.role_ratings_df.loc['lbr6', 'tec'] = self.spinBox_R6_TEC_LB.value()

        # DB Section
        myconfig.role_ratings_df.loc['dbr1', 'label'] = self.lineEdit_R1_DB.text()
        myconfig.role_ratings_df.loc['dbr1', 'ath'] = self.spinBox_R1_ATH_DB.value()
        myconfig.role_ratings_df.loc['dbr1', 'spd'] = self.spinBox_R1_SPD_DB.value()
        myconfig.role_ratings_df.loc['dbr1', 'dur'] = self.spinBox_R1_DUR_DB.value()
        myconfig.role_ratings_df.loc['dbr1', 'we'] = self.spinBox_R1_WE_DB.value()
        myconfig.role_ratings_df.loc['dbr1', 'sta'] = self.spinBox_R1_STA_DB.value()
        myconfig.role_ratings_df.loc['dbr1', 'str'] = self.spinBox_R1_STR_DB.value()
        myconfig.role_ratings_df.loc['dbr1', 'blk'] = self.spinBox_R1_BLK_DB.value()
        myconfig.role_ratings_df.loc['dbr1', 'tkl'] = self.spinBox_R1_TKL_DB.value()
        myconfig.role_ratings_df.loc['dbr1', 'han'] = self.spinBox_R1_HAN_DB.value()
        myconfig.role_ratings_df.loc['dbr1', 'gi'] = self.spinBox_R1_GI_DB.value()
        myconfig.role_ratings_df.loc['dbr1', 'elu'] = self.spinBox_R1_ELU_DB.value()
        myconfig.role_ratings_df.loc['dbr1', 'tec'] = self.spinBox_R1_TEC_DB.value()

        myconfig.role_ratings_df.loc['dbr2', 'label'] = self.lineEdit_R2_DB.text()
        myconfig.role_ratings_df.loc['dbr2', 'ath'] = self.spinBox_R2_ATH_DB.value()
        myconfig.role_ratings_df.loc['dbr2', 'spd'] = self.spinBox_R2_SPD_DB.value()
        myconfig.role_ratings_df.loc['dbr2', 'dur'] = self.spinBox_R2_DUR_DB.value()
        myconfig.role_ratings_df.loc['dbr2', 'we'] = self.spinBox_R2_WE_DB.value()
        myconfig.role_ratings_df.loc['dbr2', 'sta'] = self.spinBox_R2_STA_DB.value()
        myconfig.role_ratings_df.loc['dbr2', 'str'] = self.spinBox_R2_STR_DB.value()
        myconfig.role_ratings_df.loc['dbr2', 'blk'] = self.spinBox_R2_BLK_DB.value()
        myconfig.role_ratings_df.loc['dbr2', 'tkl'] = self.spinBox_R2_TKL_DB.value()
        myconfig.role_ratings_df.loc['dbr2', 'han'] = self.spinBox_R2_HAN_DB.value()
        myconfig.role_ratings_df.loc['dbr2', 'gi'] = self.spinBox_R2_GI_DB.value()
        myconfig.role_ratings_df.loc['dbr2', 'elu'] = self.spinBox_R2_ELU_DB.value()
        myconfig.role_ratings_df.loc['dbr2', 'tec'] = self.spinBox_R2_TEC_DB.value()

        myconfig.role_ratings_df.loc['dbr3', 'label'] = self.lineEdit_R3_DB.text()
        myconfig.role_ratings_df.loc['dbr3', 'ath'] = self.spinBox_R3_ATH_DB.value()
        myconfig.role_ratings_df.loc['dbr3', 'spd'] = self.spinBox_R3_SPD_DB.value()
        myconfig.role_ratings_df.loc['dbr3', 'dur'] = self.spinBox_R3_DUR_DB.value()
        myconfig.role_ratings_df.loc['dbr3', 'we'] = self.spinBox_R3_WE_DB.value()
        myconfig.role_ratings_df.loc['dbr3', 'sta'] = self.spinBox_R3_STA_DB.value()
        myconfig.role_ratings_df.loc['dbr3', 'str'] = self.spinBox_R3_STR_DB.value()
        myconfig.role_ratings_df.loc['dbr3', 'blk'] = self.spinBox_R3_BLK_DB.value()
        myconfig.role_ratings_df.loc['dbr3', 'tkl'] = self.spinBox_R3_TKL_DB.value()
        myconfig.role_ratings_df.loc['dbr3', 'han'] = self.spinBox_R3_HAN_DB.value()
        myconfig.role_ratings_df.loc['dbr3', 'gi'] = self.spinBox_R3_GI_DB.value()
        myconfig.role_ratings_df.loc['dbr3', 'elu'] = self.spinBox_R3_ELU_DB.value()
        myconfig.role_ratings_df.loc['dbr3', 'tec'] = self.spinBox_R3_TEC_DB.value()

        myconfig.role_ratings_df.loc['dbr4', 'label'] = self.lineEdit_R4_DB.text()
        myconfig.role_ratings_df.loc['dbr4', 'ath'] = self.spinBox_R4_ATH_DB.value()
        myconfig.role_ratings_df.loc['dbr4', 'spd'] = self.spinBox_R4_SPD_DB.value()
        myconfig.role_ratings_df.loc['dbr4', 'dur'] = self.spinBox_R4_DUR_DB.value()
        myconfig.role_ratings_df.loc['dbr4', 'we'] = self.spinBox_R4_WE_DB.value()
        myconfig.role_ratings_df.loc['dbr4', 'sta'] = self.spinBox_R4_STA_DB.value()
        myconfig.role_ratings_df.loc['dbr4', 'str'] = self.spinBox_R4_STR_DB.value()
        myconfig.role_ratings_df.loc['dbr4', 'blk'] = self.spinBox_R4_BLK_DB.value()
        myconfig.role_ratings_df.loc['dbr4', 'tkl'] = self.spinBox_R4_TKL_DB.value()
        myconfig.role_ratings_df.loc['dbr4', 'han'] = self.spinBox_R4_HAN_DB.value()
        myconfig.role_ratings_df.loc['dbr4', 'gi'] = self.spinBox_R4_GI_DB.value()
        myconfig.role_ratings_df.loc['dbr4', 'elu'] = self.spinBox_R4_ELU_DB.value()
        myconfig.role_ratings_df.loc['dbr4', 'tec'] = self.spinBox_R4_TEC_DB.value()

        myconfig.role_ratings_df.loc['dbr5', 'label'] = self.lineEdit_R5_DB.text()
        myconfig.role_ratings_df.loc['dbr5', 'ath'] = self.spinBox_R5_ATH_DB.value()
        myconfig.role_ratings_df.loc['dbr5', 'spd'] = self.spinBox_R5_SPD_DB.value()
        myconfig.role_ratings_df.loc['dbr5', 'dur'] = self.spinBox_R5_DUR_DB.value()
        myconfig.role_ratings_df.loc['dbr5', 'we'] = self.spinBox_R5_WE_DB.value()
        myconfig.role_ratings_df.loc['dbr5', 'sta'] = self.spinBox_R5_STA_DB.value()
        myconfig.role_ratings_df.loc['dbr5', 'str'] = self.spinBox_R5_STR_DB.value()
        myconfig.role_ratings_df.loc['dbr5', 'blk'] = self.spinBox_R5_BLK_DB.value()
        myconfig.role_ratings_df.loc['dbr5', 'tkl'] = self.spinBox_R5_TKL_DB.value()
        myconfig.role_ratings_df.loc['dbr5', 'han'] = self.spinBox_R5_HAN_DB.value()
        myconfig.role_ratings_df.loc['dbr5', 'gi'] = self.spinBox_R5_GI_DB.value()
        myconfig.role_ratings_df.loc['dbr5', 'elu'] = self.spinBox_R5_ELU_DB.value()
        myconfig.role_ratings_df.loc['dbr5', 'tec'] = self.spinBox_R5_TEC_DB.value()

        myconfig.role_ratings_df.loc['dbr6', 'label'] = self.lineEdit_R6_DB.text()
        myconfig.role_ratings_df.loc['dbr6', 'ath'] = self.spinBox_R6_ATH_DB.value()
        myconfig.role_ratings_df.loc['dbr6', 'spd'] = self.spinBox_R6_SPD_DB.value()
        myconfig.role_ratings_df.loc['dbr6', 'dur'] = self.spinBox_R6_DUR_DB.value()
        myconfig.role_ratings_df.loc['dbr6', 'we'] = self.spinBox_R6_WE_DB.value()
        myconfig.role_ratings_df.loc['dbr6', 'sta'] = self.spinBox_R6_STA_DB.value()
        myconfig.role_ratings_df.loc['dbr6', 'str'] = self.spinBox_R6_STR_DB.value()
        myconfig.role_ratings_df.loc['dbr6', 'blk'] = self.spinBox_R6_BLK_DB.value()
        myconfig.role_ratings_df.loc['dbr6', 'tkl'] = self.spinBox_R6_TKL_DB.value()
        myconfig.role_ratings_df.loc['dbr6', 'han'] = self.spinBox_R6_HAN_DB.value()
        myconfig.role_ratings_df.loc['dbr6', 'gi'] = self.spinBox_R6_GI_DB.value()
        myconfig.role_ratings_df.loc['dbr6', 'elu'] = self.spinBox_R6_ELU_DB.value()
        myconfig.role_ratings_df.loc['dbr6', 'tec'] = self.spinBox_R6_TEC_DB.value()

        # K Section
        myconfig.role_ratings_df.loc['kr1', 'label'] = self.lineEdit_R1_K.text()
        myconfig.role_ratings_df.loc['kr1', 'ath'] = self.spinBox_R1_ATH_K.value()
        myconfig.role_ratings_df.loc['kr1', 'spd'] = self.spinBox_R1_SPD_K.value()
        myconfig.role_ratings_df.loc['kr1', 'dur'] = self.spinBox_R1_DUR_K.value()
        myconfig.role_ratings_df.loc['kr1', 'we'] = self.spinBox_R1_WE_K.value()
        myconfig.role_ratings_df.loc['kr1', 'sta'] = self.spinBox_R1_STA_K.value()
        myconfig.role_ratings_df.loc['kr1', 'str'] = self.spinBox_R1_STR_K.value()
        myconfig.role_ratings_df.loc['kr1', 'blk'] = self.spinBox_R1_BLK_K.value()
        myconfig.role_ratings_df.loc['kr1', 'tkl'] = self.spinBox_R1_TKL_K.value()
        myconfig.role_ratings_df.loc['kr1', 'han'] = self.spinBox_R1_HAN_K.value()
        myconfig.role_ratings_df.loc['kr1', 'gi'] = self.spinBox_R1_GI_K.value()
        myconfig.role_ratings_df.loc['kr1', 'elu'] = self.spinBox_R1_ELU_K.value()
        myconfig.role_ratings_df.loc['kr1', 'tec'] = self.spinBox_R1_TEC_K.value()

        myconfig.role_ratings_df.loc['kr2', 'label'] = self.lineEdit_R2_K.text()
        myconfig.role_ratings_df.loc['kr2', 'ath'] = self.spinBox_R2_ATH_K.value()
        myconfig.role_ratings_df.loc['kr2', 'spd'] = self.spinBox_R2_SPD_K.value()
        myconfig.role_ratings_df.loc['kr2', 'dur'] = self.spinBox_R2_DUR_K.value()
        myconfig.role_ratings_df.loc['kr2', 'we'] = self.spinBox_R2_WE_K.value()
        myconfig.role_ratings_df.loc['kr2', 'sta'] = self.spinBox_R2_STA_K.value()
        myconfig.role_ratings_df.loc['kr2', 'str'] = self.spinBox_R2_STR_K.value()
        myconfig.role_ratings_df.loc['kr2', 'blk'] = self.spinBox_R2_BLK_K.value()
        myconfig.role_ratings_df.loc['kr2', 'tkl'] = self.spinBox_R2_TKL_K.value()
        myconfig.role_ratings_df.loc['kr2', 'han'] = self.spinBox_R2_HAN_K.value()
        myconfig.role_ratings_df.loc['kr2', 'gi'] = self.spinBox_R2_GI_K.value()
        myconfig.role_ratings_df.loc['kr2', 'elu'] = self.spinBox_R2_ELU_K.value()
        myconfig.role_ratings_df.loc['kr2', 'tec'] = self.spinBox_R2_TEC_K.value()

        myconfig.role_ratings_df.loc['kr3', 'label'] = self.lineEdit_R3_K.text()
        myconfig.role_ratings_df.loc['kr3', 'ath'] = self.spinBox_R3_ATH_K.value()
        myconfig.role_ratings_df.loc['kr3', 'spd'] = self.spinBox_R3_SPD_K.value()
        myconfig.role_ratings_df.loc['kr3', 'dur'] = self.spinBox_R3_DUR_K.value()
        myconfig.role_ratings_df.loc['kr3', 'we'] = self.spinBox_R3_WE_K.value()
        myconfig.role_ratings_df.loc['kr3', 'sta'] = self.spinBox_R3_STA_K.value()
        myconfig.role_ratings_df.loc['kr3', 'str'] = self.spinBox_R3_STR_K.value()
        myconfig.role_ratings_df.loc['kr3', 'blk'] = self.spinBox_R3_BLK_K.value()
        myconfig.role_ratings_df.loc['kr3', 'tkl'] = self.spinBox_R3_TKL_K.value()
        myconfig.role_ratings_df.loc['kr3', 'han'] = self.spinBox_R3_HAN_K.value()
        myconfig.role_ratings_df.loc['kr3', 'gi'] = self.spinBox_R3_GI_K.value()
        myconfig.role_ratings_df.loc['kr3', 'elu'] = self.spinBox_R3_ELU_K.value()
        myconfig.role_ratings_df.loc['kr3', 'tec'] = self.spinBox_R3_TEC_K.value()

        myconfig.role_ratings_df.loc['kr4', 'label'] = self.lineEdit_R4_K.text()
        myconfig.role_ratings_df.loc['kr4', 'ath'] = self.spinBox_R4_ATH_K.value()
        myconfig.role_ratings_df.loc['kr4', 'spd'] = self.spinBox_R4_SPD_K.value()
        myconfig.role_ratings_df.loc['kr4', 'dur'] = self.spinBox_R4_DUR_K.value()
        myconfig.role_ratings_df.loc['kr4', 'we'] = self.spinBox_R4_WE_K.value()
        myconfig.role_ratings_df.loc['kr4', 'sta'] = self.spinBox_R4_STA_K.value()
        myconfig.role_ratings_df.loc['kr4', 'str'] = self.spinBox_R4_STR_K.value()
        myconfig.role_ratings_df.loc['kr4', 'blk'] = self.spinBox_R4_BLK_K.value()
        myconfig.role_ratings_df.loc['kr4', 'tkl'] = self.spinBox_R4_TKL_K.value()
        myconfig.role_ratings_df.loc['kr4', 'han'] = self.spinBox_R4_HAN_K.value()
        myconfig.role_ratings_df.loc['kr4', 'gi'] = self.spinBox_R4_GI_K.value()
        myconfig.role_ratings_df.loc['kr4', 'elu'] = self.spinBox_R4_ELU_K.value()
        myconfig.role_ratings_df.loc['kr4', 'tec'] = self.spinBox_R4_TEC_K.value()

        myconfig.role_ratings_df.loc['kr5', 'label'] = self.lineEdit_R5_K.text()
        myconfig.role_ratings_df.loc['kr5', 'ath'] = self.spinBox_R5_ATH_K.value()
        myconfig.role_ratings_df.loc['kr5', 'spd'] = self.spinBox_R5_SPD_K.value()
        myconfig.role_ratings_df.loc['kr5', 'dur'] = self.spinBox_R5_DUR_K.value()
        myconfig.role_ratings_df.loc['kr5', 'we'] = self.spinBox_R5_WE_K.value()
        myconfig.role_ratings_df.loc['kr5', 'sta'] = self.spinBox_R5_STA_K.value()
        myconfig.role_ratings_df.loc['kr5', 'str'] = self.spinBox_R5_STR_K.value()
        myconfig.role_ratings_df.loc['kr5', 'blk'] = self.spinBox_R5_BLK_K.value()
        myconfig.role_ratings_df.loc['kr5', 'tkl'] = self.spinBox_R5_TKL_K.value()
        myconfig.role_ratings_df.loc['kr5', 'han'] = self.spinBox_R5_HAN_K.value()
        myconfig.role_ratings_df.loc['kr5', 'gi'] = self.spinBox_R5_GI_K.value()
        myconfig.role_ratings_df.loc['kr5', 'elu'] = self.spinBox_R5_ELU_K.value()
        myconfig.role_ratings_df.loc['kr5', 'tec'] = self.spinBox_R5_TEC_K.value()

        myconfig.role_ratings_df.loc['kr6', 'label'] = self.lineEdit_R6_K.text()
        myconfig.role_ratings_df.loc['kr6', 'ath'] = self.spinBox_R6_ATH_K.value()
        myconfig.role_ratings_df.loc['kr6', 'spd'] = self.spinBox_R6_SPD_K.value()
        myconfig.role_ratings_df.loc['kr6', 'dur'] = self.spinBox_R6_DUR_K.value()
        myconfig.role_ratings_df.loc['kr6', 'we'] = self.spinBox_R6_WE_K.value()
        myconfig.role_ratings_df.loc['kr6', 'sta'] = self.spinBox_R6_STA_K.value()
        myconfig.role_ratings_df.loc['kr6', 'str'] = self.spinBox_R6_STR_K.value()
        myconfig.role_ratings_df.loc['kr6', 'blk'] = self.spinBox_R6_BLK_K.value()
        myconfig.role_ratings_df.loc['kr6', 'tkl'] = self.spinBox_R6_TKL_K.value()
        myconfig.role_ratings_df.loc['kr6', 'han'] = self.spinBox_R6_HAN_K.value()
        myconfig.role_ratings_df.loc['kr6', 'gi'] = self.spinBox_R6_GI_K.value()
        myconfig.role_ratings_df.loc['kr6', 'elu'] = self.spinBox_R6_ELU_K.value()
        myconfig.role_ratings_df.loc['kr6', 'tec'] = self.spinBox_R6_TEC_K.value()

        # P Section
        myconfig.role_ratings_df.loc['pr1', 'label'] = self.lineEdit_R1_P.text()
        myconfig.role_ratings_df.loc['pr1', 'ath'] = self.spinBox_R1_ATH_P.value()
        myconfig.role_ratings_df.loc['pr1', 'spd'] = self.spinBox_R1_SPD_P.value()
        myconfig.role_ratings_df.loc['pr1', 'dur'] = self.spinBox_R1_DUR_P.value()
        myconfig.role_ratings_df.loc['pr1', 'we'] = self.spinBox_R1_WE_P.value()
        myconfig.role_ratings_df.loc['pr1', 'sta'] = self.spinBox_R1_STA_P.value()
        myconfig.role_ratings_df.loc['pr1', 'str'] = self.spinBox_R1_STR_P.value()
        myconfig.role_ratings_df.loc['pr1', 'blk'] = self.spinBox_R1_BLK_P.value()
        myconfig.role_ratings_df.loc['pr1', 'tkl'] = self.spinBox_R1_TKL_P.value()
        myconfig.role_ratings_df.loc['pr1', 'han'] = self.spinBox_R1_HAN_P.value()
        myconfig.role_ratings_df.loc['pr1', 'gi'] = self.spinBox_R1_GI_P.value()
        myconfig.role_ratings_df.loc['pr1', 'elu'] = self.spinBox_R1_ELU_P.value()
        myconfig.role_ratings_df.loc['pr1', 'tec'] = self.spinBox_R1_TEC_P.value()

        myconfig.role_ratings_df.loc['pr2', 'label'] = self.lineEdit_R2_P.text()
        myconfig.role_ratings_df.loc['pr2', 'ath'] = self.spinBox_R2_ATH_P.value()
        myconfig.role_ratings_df.loc['pr2', 'spd'] = self.spinBox_R2_SPD_P.value()
        myconfig.role_ratings_df.loc['pr2', 'dur'] = self.spinBox_R2_DUR_P.value()
        myconfig.role_ratings_df.loc['pr2', 'we'] = self.spinBox_R2_WE_P.value()
        myconfig.role_ratings_df.loc['pr2', 'sta'] = self.spinBox_R2_STA_P.value()
        myconfig.role_ratings_df.loc['pr2', 'str'] = self.spinBox_R2_STR_P.value()
        myconfig.role_ratings_df.loc['pr2', 'blk'] = self.spinBox_R2_BLK_P.value()
        myconfig.role_ratings_df.loc['pr2', 'tkl'] = self.spinBox_R2_TKL_P.value()
        myconfig.role_ratings_df.loc['pr2', 'han'] = self.spinBox_R2_HAN_P.value()
        myconfig.role_ratings_df.loc['pr2', 'gi'] = self.spinBox_R2_GI_P.value()
        myconfig.role_ratings_df.loc['pr2', 'elu'] = self.spinBox_R2_ELU_P.value()
        myconfig.role_ratings_df.loc['pr2', 'tec'] = self.spinBox_R2_TEC_P.value()

        myconfig.role_ratings_df.loc['pr3', 'label'] = self.lineEdit_R3_P.text()
        myconfig.role_ratings_df.loc['pr3', 'ath'] = self.spinBox_R3_ATH_P.value()
        myconfig.role_ratings_df.loc['pr3', 'spd'] = self.spinBox_R3_SPD_P.value()
        myconfig.role_ratings_df.loc['pr3', 'dur'] = self.spinBox_R3_DUR_P.value()
        myconfig.role_ratings_df.loc['pr3', 'we'] = self.spinBox_R3_WE_P.value()
        myconfig.role_ratings_df.loc['pr3', 'sta'] = self.spinBox_R3_STA_P.value()
        myconfig.role_ratings_df.loc['pr3', 'str'] = self.spinBox_R3_STR_P.value()
        myconfig.role_ratings_df.loc['pr3', 'blk'] = self.spinBox_R3_BLK_P.value()
        myconfig.role_ratings_df.loc['pr3', 'tkl'] = self.spinBox_R3_TKL_P.value()
        myconfig.role_ratings_df.loc['pr3', 'han'] = self.spinBox_R3_HAN_P.value()
        myconfig.role_ratings_df.loc['pr3', 'gi'] = self.spinBox_R3_GI_P.value()
        myconfig.role_ratings_df.loc['pr3', 'elu'] = self.spinBox_R3_ELU_P.value()
        myconfig.role_ratings_df.loc['pr3', 'tec'] = self.spinBox_R3_TEC_P.value()

        myconfig.role_ratings_df.loc['pr4', 'label'] = self.lineEdit_R4_P.text()
        myconfig.role_ratings_df.loc['pr4', 'ath'] = self.spinBox_R4_ATH_P.value()
        myconfig.role_ratings_df.loc['pr4', 'spd'] = self.spinBox_R4_SPD_P.value()
        myconfig.role_ratings_df.loc['pr4', 'dur'] = self.spinBox_R4_DUR_P.value()
        myconfig.role_ratings_df.loc['pr4', 'we'] = self.spinBox_R4_WE_P.value()
        myconfig.role_ratings_df.loc['pr4', 'sta'] = self.spinBox_R4_STA_P.value()
        myconfig.role_ratings_df.loc['pr4', 'str'] = self.spinBox_R4_STR_P.value()
        myconfig.role_ratings_df.loc['pr4', 'blk'] = self.spinBox_R4_BLK_P.value()
        myconfig.role_ratings_df.loc['pr4', 'tkl'] = self.spinBox_R4_TKL_P.value()
        myconfig.role_ratings_df.loc['pr4', 'han'] = self.spinBox_R4_HAN_P.value()
        myconfig.role_ratings_df.loc['pr4', 'gi'] = self.spinBox_R4_GI_P.value()
        myconfig.role_ratings_df.loc['pr4', 'elu'] = self.spinBox_R4_ELU_P.value()
        myconfig.role_ratings_df.loc['pr4', 'tec'] = self.spinBox_R4_TEC_P.value()

        myconfig.role_ratings_df.loc['pr5', 'label'] = self.lineEdit_R5_P.text()
        myconfig.role_ratings_df.loc['pr5', 'ath'] = self.spinBox_R5_ATH_P.value()
        myconfig.role_ratings_df.loc['pr5', 'spd'] = self.spinBox_R5_SPD_P.value()
        myconfig.role_ratings_df.loc['pr5', 'dur'] = self.spinBox_R5_DUR_P.value()
        myconfig.role_ratings_df.loc['pr5', 'we'] = self.spinBox_R5_WE_P.value()
        myconfig.role_ratings_df.loc['pr5', 'sta'] = self.spinBox_R5_STA_P.value()
        myconfig.role_ratings_df.loc['pr5', 'str'] = self.spinBox_R5_STR_P.value()
        myconfig.role_ratings_df.loc['pr5', 'blk'] = self.spinBox_R5_BLK_P.value()
        myconfig.role_ratings_df.loc['pr5', 'tkl'] = self.spinBox_R5_TKL_P.value()
        myconfig.role_ratings_df.loc['pr5', 'han'] = self.spinBox_R5_HAN_P.value()
        myconfig.role_ratings_df.loc['pr5', 'gi'] = self.spinBox_R5_GI_P.value()
        myconfig.role_ratings_df.loc['pr5', 'elu'] = self.spinBox_R5_ELU_P.value()
        myconfig.role_ratings_df.loc['pr5', 'tec'] = self.spinBox_R5_TEC_P.value()

        myconfig.role_ratings_df.loc['pr6', 'label'] = self.lineEdit_R6_P.text()
        myconfig.role_ratings_df.loc['pr6', 'ath'] = self.spinBox_R6_ATH_P.value()
        myconfig.role_ratings_df.loc['pr6', 'spd'] = self.spinBox_R6_SPD_P.value()
        myconfig.role_ratings_df.loc['pr6', 'dur'] = self.spinBox_R6_DUR_P.value()
        myconfig.role_ratings_df.loc['pr6', 'we'] = self.spinBox_R6_WE_P.value()
        myconfig.role_ratings_df.loc['pr6', 'sta'] = self.spinBox_R6_STA_P.value()
        myconfig.role_ratings_df.loc['pr6', 'str'] = self.spinBox_R6_STR_P.value()
        myconfig.role_ratings_df.loc['pr6', 'blk'] = self.spinBox_R6_BLK_P.value()
        myconfig.role_ratings_df.loc['pr6', 'tkl'] = self.spinBox_R6_TKL_P.value()
        myconfig.role_ratings_df.loc['pr6', 'han'] = self.spinBox_R6_HAN_P.value()
        myconfig.role_ratings_df.loc['pr6', 'gi'] = self.spinBox_R6_GI_P.value()
        myconfig.role_ratings_df.loc['pr6', 'elu'] = self.spinBox_R6_ELU_P.value()
        myconfig.role_ratings_df.loc['pr6', 'tec'] = self.spinBox_R6_TEC_P.value()


        # Write to csv file
        list_total = ['ath', 'spd', 'dur', 'we', 'sta', 'str', 'blk', 'tkl', 'han', 'gi', 'elu', 'tec']
        myconfig.role_ratings_df['total'] = myconfig.role_ratings_df.loc[:,list_total].sum(axis=1)
        logger.info("Saving role ratings to csv...")
        myconfig.role_ratings_df.to_csv(myconfig.role_ratings_csv)
        myconfig.show_update_role_ratings_dialog = True

        geometry = self.saveGeometry()
        self.settings.setValue('RoleRatingsGeometry', geometry)

        super().accept()


    def closeEvent(self, event):
        # Now we define the closeEvent
        # This is called whenever a window is closed.
        # It is passed an event which we can choose to accept or reject, but in this case we'll just pass it on after we're done.
        
        # First we need to get the current size and position of the window.
        # This can be fetchesd using the built in saveGeometry() method. 
        # This is got back as a byte array. It won't really make sense to a human directly, but it makes sense to Qt.
        geometry = self.saveGeometry()

        # Once we know the geometry we can save it in our settings under geometry
        self.settings.setValue('RoleRatingsGeometry', geometry)
        
        # Finally we pass the event to the class we inherit from. It can choose to accept or reject the event, but we don't need to deal with it ourselves
        super(RoleRatings, self).closeEvent(event)


class RoleRatingsUpdateDB(QDialog, Ui_DialogRoleRatingUpdateDB_Progress):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = QSettings()
        geometry = self.settings.value('RoleRatingsUpdateDBGeometry', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)
        self.runUpdateJob()

    def accept(self):
        geometry = self.saveGeometry()
        self.settings.setValue('RoleRatingsUpdateDBGeometry', geometry)
        super().accept()

    
    def runUpdateJob(self):
        logger.info("Updating Role Ratings in Recruits DB")
        # Step 1: Create a QThread object
        self.thread = QThread()
        # Step 2: Create a worker object
        self.worker = RoleRatingDBWorker()
        # Step 3: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 4: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.progress)
        # Step 6: Start the thread
        self.thread.start()
        # Final resets
        self.thread.finished.connect(self.accept)

    
    def progress(self, n):
        self.progressBar.setValue(n) 


    def closeEvent(self, event):
        # Now we define the closeEvent
        # This is called whenever a window is closed.
        # It is passed an event which we can choose to accept or reject, but in this case we'll just pass it on after we're done.
        
        # First we need to get the current size and position of the window.
        # This can be fetchesd using the built in saveGeometry() method. 
        # This is got back as a byte array. It won't really make sense to a human directly, but it makes sense to Qt.
        geometry = self.saveGeometry()

        # Once we know the geometry we can save it in our settings under geometry
        self.settings.setValue('RoleRatingsUpdateDBGeometry', geometry)
        
        # Finally we pass the event to the class we inherit from. It can choose to accept or reject the event, but we don't need to deal with it ourselves
        super(RoleRatingsUpdateDB, self).closeEvent(event)

class BoldAttributes(QDialog, Ui_DialogBoldAttributes):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = QSettings()
        geometry = self.settings.value('BoldAttributesGeometry', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)
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
        bold_attributes_df.to_csv(myconfig.bold_attributes_csv)
        geometry = self.saveGeometry()
        self.settings.setValue('BoldAttributesGeometry', geometry)
        super().accept()

    
    def closeEvent(self, event):
        # Now we define the closeEvent
        # This is called whenever a window is closed.
        # It is passed an event which we can choose to accept or reject, but in this case we'll just pass it on after we're done.
        
        # First we need to get the current size and position of the window.
        # This can be fetchesd using the built in saveGeometry() method. 
        # This is got back as a byte array. It won't really make sense to a human directly, but it makes sense to Qt.
        geometry = self.saveGeometry()

        # Once we know the geometry we can save it in our settings under geometry
        self.settings.setValue('BoldAttributesGeometry', geometry)
        
        # Finally we pass the event to the class we inherit from. It can choose to accept or reject the event, but we don't need to deal with it ourselves
        super(BoldAttributes, self).closeEvent(event)


class AdvancedDialog(QDialog, Ui_DialogAdvancedConfigOptions):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        # Restore dialog window geometry
        self.settings = QSettings()
        geometry = self.settings.value('AdvancedDialogGeometry', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)
        self.c = load_config()
        self.config = c['config']
        self.headless = config.getboolean('Browser', 'headless')
        logger.debug(f"Browser headless option = {self.headless}")
        self.log_level = config.get('Logging', 'level')
        logger.debug(f"Logging level option = {self.log_level}")
        if self.headless == False:
            self.checkBoxBrowserEnableNonHeadlessMode.setChecked(True)
            self.headless_state = True
        else:
            self.headless_state = False
        if self.log_level.upper() == 'DEBUG':
            self.checkBoxEnableDebugLogging.setChecked(True)
            self.log_level_state = True
        else:
            self.log_level_state = False


    def accept(self):
        self.new_headless_state = self.checkBoxBrowserEnableNonHeadlessMode.isChecked()
        self.new_log_level_state = self.checkBoxEnableDebugLogging.isChecked()
        if self.new_headless_state == self.headless_state and self.new_log_level_state == self.log_level_state:
            logger.info("No changes were made to Advanced Config Options. No need to write to config file.")
        else:
            if self.new_headless_state != self.headless_state:
                if self.new_headless_state == True:
                    self.config.set('Browser', 'headless', 'false')
                else:
                    self.config.set('Browser', 'headless', 'true')
                write_config(self.config)
            if self.new_log_level_state != self.log_level_state:
                if self.new_log_level_state == True:
                    self.config.set('Logging', 'level', 'DEBUG')
                    start_logging('DEBUG')
                else:
                    self.config.set('Logging', 'level', 'INFO')
                    start_logging('INFO')
            logger.info("Changes were made to Advanced Config Options. Writing changes to config file.")
            (config)
        
        geometry = self.saveGeometry()
        self.settings.setValue('AdvancedDialogGeometry', geometry)
        
        super().accept()


    def closeEvent(self, event):
        # Now we define the closeEvent
        # This is called whenever a window is closed.
        # It is passed an event which we can choose to accept or reject, but in this case we'll just pass it on after we're done.
        
        # First we need to get the current size and position of the window.
        # This can be fetchesd using the built in saveGeometry() method. 
        # This is got back as a byte array. It won't really make sense to a human directly, but it makes sense to Qt.
        geometry = self.saveGeometry()

        # Once we know the geometry we can save it in our settings under geometry
        self.settings.setValue('AdvancedDialogGeometry', geometry)
        
        # Finally we pass the event to the class we inherit from. It can choose to accept or reject the event, but we don't need to deal with it ourselves
        super(AdvancedDialog, self).closeEvent(event)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = QSettings()
        geometry = self.settings.value('MainWindowGeometry', bytes('', 'utf-8'))
        self.restoreGeometry(geometry)
        logger.info(f"QSettings.fileName() = {self.settings.fileName()}")
        self.recruit_tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.h_header = self.recruit_tableView.horizontalHeader()
        self.h_header.setSectionsMovable(True)
        self.h_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.v_header = self.recruit_tableView.verticalHeader()
        self.v_header.setSectionResizeMode(QHeaderView.ResizeToContents)

        # This can format the text of the entire table view.
        #self.recruit_tableView.setStyleSheet("""
        #                                   color: #123456;
        #                                    """)

        # Disable Recruit Table until a DB table is loaded.
        self.recruit_tableView.setEnabled(False)
        
        
        # Disable all filters by default. They will be enabled when model is loaded.
        self.pushButtonClearRatingsFilters.setText(QCoreApplication.translate("MainWindow", u"&Clear", None))
        self.pushButtonApplyRatingsFilters.setText(QCoreApplication.translate("MainWindow", u"&Apply", None))
        self.pushButtonMarkWatchlistPotential.setText(QCoreApplication.translate("MainWindow", u"&Mark Watchlist/Potential", None))
        self.pushButtonUpdateConsidering.setText(QCoreApplication.translate("MainWindow", u"&Update Considering", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menudata.setTitle(QCoreApplication.translate("MainWindow", u"&Data", None))
        self.menuExport_to_CSV.setTitle(QCoreApplication.translate("MainWindow", u"&Export to CSV", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"&Options", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.actionNew_Season.setText(QCoreApplication.translate("MainWindow", u"&New Season", None))
        self.actionLoad_Season.setText(QCoreApplication.translate("MainWindow", u"&Load Season", None))
        self.actionGrabSeasonData.setText(QCoreApplication.translate("MainWindow", u"&Initialize Recruit Data", None))
        self.actionAll_Recruits.setText(QCoreApplication.translate("MainWindow", u"&All Recruits", None))
        self.actionWatchlist_Only.setText(QCoreApplication.translate("MainWindow", u"&Watchlist Only", None))
        self.actionWIS_Credentials.setText(QCoreApplication.translate("MainWindow", u"&WIS Credentials", None))
        self.actionBold_Attributes.setText(QCoreApplication.translate("MainWindow", u"&Bold Attributes", None))
        self.actionRole_Ratings.setText(QCoreApplication.translate("MainWindow", u"&Role Ratings", None))
        self.actionShow_Columns.setText(QCoreApplication.translate("MainWindow", u"&Show Columns", None))
        self.actionAdvanced.setText(QCoreApplication.translate("MainWindow", u"&Advanced", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"&About", None))
        self.comboBoxPositionFilter.setEnabled(False)
        self.checkBoxHideSigned.setEnabled(False)
        self.checkBoxUndecided.setEnabled(False)
        self.checkBoxWatched.setEnabled(False)
        self.comboBoxMilesFilter.setEnabled(False)
        self.comboBoxDivisionFilter.setEnabled(False)
        self.pushButtonApplyRatingsFilters.setEnabled(False)
        self.pushButtonClearRatingsFilters.setEnabled(False)
        self.pushButtonUpdateConsidering.setEnabled(False)
        self.pushButtonMarkWatchlistPotential.setEnabled(False)
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
        self.actionAll_Recruits.setEnabled(False)
        self.actionWatchlist_Only.setEnabled(False)
        
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
        self.actionAll_Recruits.triggered.connect(self.export_db_to_csv_all)
        self.actionWatchlist_Only.triggered.connect(self.export_db_to_csv_watchlist)
        self.actionBold_Attributes.triggered.connect(self.open_Bold_Attributes)
        self.actionRole_Ratings.triggered.connect(self.open_Role_Ratings)
        self.actionShow_Columns.triggered.connect(self.open_show_columns)
        self.actionAdvanced.triggered.connect(self.open_advanced)
        self.actionAbout.triggered.connect(self.open_help_about)
        self.comboBoxPositionFilter.activated.connect(self.position_filter)
        self.comboBoxMilesFilter.activated.connect(self.miles_filter)
        self.comboBoxDivisionFilter.activated.connect(self.division_filter)
        self.checkBoxHideSigned.stateChanged.connect(self.hide_signed_filter)
        self.checkBoxUndecided.stateChanged.connect(self.undecided_filter)
        self.checkBoxWatched.stateChanged.connect(self.watched_filter)
        self.pushButtonApplyRatingsFilters.clicked.connect(self.apply_ratings_filters)
        self.pushButtonClearRatingsFilters.clicked.connect(self.clear_ratings_filter_fields)
        self.recruit_tableView.clicked.connect(self.tableclickaction)
        self.pushButtonUpdateConsidering.clicked.connect(self.open_update_considering)
        self.pushButtonMarkWatchlistPotential.clicked.connect(self.open_mark_watchlist_potential)
        self.pushButtonDonatePayPal.clicked.connect(self.donation)
        
        self.h_header.sectionMoved.connect(self.save_column_order)
        
        # Filter data structure used to track which filters are active
        # And then used to build the filter string
        self.string_filter =  self.get_clean_string_filter()
        
        if self.check_stored_creds():
            # Grab coachid from config file
            # Use it to grab active GD teams from coach profile page
            # and save to config file
            c = load_config()
            coachid = c['coachid']
            update_active_teams(coachid)
            self.statusbar.showMessage(f"Current coachid = {coachid} (Auth Cookie Saved)")
        else:
            c = load_config()
            coachid = c['coachid']
            if coachid == "":
                self.statusbar.showMessage("No coachid configured")
            else:
                self.statusbar.showMessage(f"Current coachid = {coachid} (No Auth Cookie)")


    def closeEvent(self, event):
        # Now we define the closeEvent
        # This is called whenever a window is closed.
        # It is passed an event which we can choose to accept or reject, but in this case we'll just pass it on after we're done.
        
        # First we need to get the current size and position of the window.
        # This can be fetchesd using the built in saveGeometry() method. 
        # This is got back as a byte array. It won't really make sense to a human directly, but it makes sense to Qt.
        geometry = self.saveGeometry()

        # Once we know the geometry we can save it in our settings under geometry
        self.settings.setValue('MainWindowGeometry', geometry)
        
        # Finally we pass the event to the class we inherit from. It can choose to accept or reject the event, but we don't need to deal with it ourselves
        super(MainWindow, self).closeEvent(event)


    def open_help_about(self):
        url = QUrl("https://github.com/ebzimny01/gd-recruit/wiki")
        logger.info(f"Opening Help About URL --> {url}")
        QDesktopServices.openUrl(url)


    def save_column_order(self):
        logger.debug("Header column moved. Saving new column order state.")
        self.settings.setValue("table_header_order", self.h_header.saveState())


    def get_clean_string_filter(self):
        logger.debug("Creating new clean filter...")
        clean_filter = {
            'pos': "",
            'hide_signed': "",
            'undecided': "",
            'miles': "",
            'division': "",
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
        return clean_filter

    
    def export_db_to_csv_all(self):
        dbname = db.databaseName()
        logger.info(f"Exporting {dbname} to csv...")
        conn = sqlite3.connect(db.databaseName(), isolation_level=None,
                        detect_types=sqlite3.PARSE_COLNAMES)
        filename = f"{dbname} (ALL).csv"
        try:
            logger.debug(f"Export to CSV -> Querying DB for ALL recruits...")
            db_df = pd.read_sql_query("SELECT * FROM recruits", conn)
        except Exception as e:
            logger.debug(f"Export to CSV exception: {e}")
            mw.statusbar.showMessage(f"Export failure. Be sure you have a season loaded with recruits before exporting.")
        else:
            db_df.to_csv(filename, index=False)
            print(f"Exported data to: '{filename}'")
            logger.info(f"Exported data to: '{filename}'")
            mw.statusbar.showMessage(f"Exported data to: '{filename}'")

    
    def export_db_to_csv_watchlist(self):
        dbname = db.databaseName()
        logger.info(f"Exporting {dbname} to csv...")
        conn = sqlite3.connect(db.databaseName(), isolation_level=None,
                        detect_types=sqlite3.PARSE_COLNAMES)
        filename = f"{dbname} (WATCHLIST).csv"
        try:
            logger.debug(f"Export to CSV -> Querying DB for WATCHLIST recruits...")
            db_df = pd.read_sql_query("SELECT * FROM recruits WHERE watched=1", conn)
        except Exception as e:
            logger.debug(f"Export to CSV exception: {e}")
            mw.statusbar.showMessage(f"Export failure. Be sure you have a season loaded with recruits before exporting.")
        else:
            db_df.to_csv(filename, index=False)
            print(f"Exported data to: '{filename}'")
            logger.info(f"Exported data to: '{filename}'")
            mw.statusbar.showMessage(f"Exported data to: '{filename}'")

    
    def donation(self):
        url = QUrl("https://paypal.me/EdZimny?locale.x=en_US")
        logger.info(f"Opening Donation URL --> {url}")
        QDesktopServices.openUrl(url)

    
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
            world = myconfig.wis_gd_df.world[wis_id]
            division = myconfig.wis_gd_df.division[wis_id]
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


    def clear_ui_filter_controls(self):
        # This resets the UI filter controls to defaults.
        logger.info("Clearing/resetting UI filter controls to defaults...")
        self.comboBoxPositionFilter.setCurrentIndex(0)
        self.comboBoxMilesFilter.setCurrentIndex(0)
        self.comboBoxDivisionFilter.setCurrentIndex(0)
        self.checkBoxHideSigned.setChecked(False)
        self.checkBoxUndecided.setChecked(False)
        self.checkBoxWatched.setChecked(False)

    
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
        
        try:
            self.newFilter(self.model)
        except AttributeError as err:
            logger.error(f"Exception ({err}).")
            logger.error(f"No model to apply new filter.")

    
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

    
    def division_filter(self):
        combo_box_filter = f"division = '{self.comboBoxDivisionFilter.currentText()}'"
        logger.info(f"Previous filter = {self.getFilterString()}")
        if self.comboBoxDivisionFilter.currentText() == "All":
            logger.info("Clearing Division Filter...")
            self.string_filter['division'] = ""
        else:
            logger.info("Adding Division Filter...")
            self.string_filter['division'] = combo_box_filter
        
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
        if self.check_stored_creds():
            # Grab coachid from config file
            # Use it to grab active GD teams from coach profile page
            # and save to config file
            c = load_config()
            coachid = c['coachid']
            self.statusbar.showMessage(f"Current coachid = {coachid} (Auth Cookie Saved)")
        else:
            c = load_config()
            coachid = c['coachid']
            if coachid == "":
                self.statusbar.showMessage("No coachid configured")
            else:
                self.statusbar.showMessage(f"Current coachid = {coachid} (No Auth Cookie)")
        
        if myconfig.clear_model:
            self.clearmodel()
    

    def open_New_Season(self):
        dialog = NewSeason()
        dialog.ui = Ui_DialogNewSeason()
        dialog.exec_()
        dialog.show()
        logger.info("Exiting New Season dialog")
        logger.info(f"Season database name = {myconfig.season_filename}")
        if myconfig.clear_model:
            self.clearmodel()
            if myconfig.season_filename != "":
                self.loadModel()
       
                
    def open_Load_Season(self):
        dialog = LoadSeason()
        dialog.ui = Ui_DialogLoadSeason()
        dialog.exec_()
        dialog.show()
        logger.info("Exiting Load Season dialog")
        logger.info(f"Season database name = {myconfig.season_filename}")
        if myconfig.clear_model:
            self.clearmodel()
            if myconfig.season_filename != "":
                self.loadModel()
            
    
    def open_Grab_Season_Data(self):
        dialog = GrabSeasonData()
        dialog.ui = Ui_WidgetGrabSeasonData()
        dialog.exec_()
        dialog.show()
        logger.info("Exiting Grab Season Data dialog")
        logger.info(f"Season database name = {myconfig.season_filename}")
        if db.databaseName() != "":
            self.loadModel()


    def open_update_considering(self):
        dialog = UpdateConsidering()
        dialog.ui = Ui_DialogUpdateConsidering()
        dialog.exec_()
        dialog.show()
        logger.info("Exiting Update Considering dialog")
        logger.info(f"Season database name = {myconfig.season_filename}")
        if db.databaseName() != "":
            self.loadModel()


    def open_mark_watchlist_potential(self):
        dialog = MarkWatchlistPotential()
        dialog.ui = Ui_DialogMarkWatchlistPotential()
        dialog.exec_()
        dialog.show()
        logger.info("Exiting Mark Watchlist/Potential dialog")
        logger.info(f"Season database name = {myconfig.season_filename}")
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

    
    def open_Role_Ratings(self):
        logger.debug("Entering Role Ratings dialog")
        myconfig.show_update_role_ratings_dialog = False
        dialog = RoleRatings()
        dialog.ui = Ui_DialogRoleRatings()
        dialog.exec_()
        dialog.show()
        if db.databaseName() != "":
            if myconfig.show_update_role_ratings_dialog:
                logger.debug("Showing Role Rating Update DB progress dialog")
                update_dialog = RoleRatingsUpdateDB()
                update_dialog.ui = Ui_DialogRoleRatingUpdateDB_Progress()
                update_dialog.exec_()
                update_dialog.show()
                self.loadModel()
        logger.debug("Exiting Role Ratings dialog")

    
    def open_show_columns(self):
        logger.info("Entering Show Columns dialog")
        dialog = ShowColumns()
        dialog.ui = Ui_DialogShowColumns()
        dialog.exec_()
        dialog.show()
        logger.info("Exiting Show Columns dialog")
        if db.databaseName() != "":
            self.loadModel()
        

    def open_advanced(self):
        logger.debug("Entering Advanced dialog")
        dialog = AdvancedDialog()
        dialog.ui = Ui_DialogAdvancedConfigOptions()
        dialog.exec_()
        dialog.show() 
        logger.debug("Exiting Advanced dialog")

    
    def check_stored_creds(self):
        c = load_config()
        coachid = c['coachid']
        cookiefile = os.path.join(myconfig.cookies_directory_path, f"browser_cookie_{coachid}.json")
        if coachid != '' and path.exists(cookiefile):
            self.actionNew_Season.setEnabled(True)
            self.actionLoad_Season.setEnabled(True)
            return True
        else:
            self.actionNew_Season.setEnabled(False)
            self.actionLoad_Season.setEnabled(False)
            return False
   

    def clearmodel(self):
        logger.debug("Entering clearmodel() function...")
        logger.debug("Clearing database name...")
        db.setDatabaseName("")
        logger.debug("Setting default window title...")
        self.setWindowTitle(f"{window_title}")
        self.actionGrabSeasonData.setEnabled(False)
        self.actionAll_Recruits.setEnabled(False)
        self.actionWatchlist_Only.setEnabled(False)
        self.actionAll_Recruits.setEnabled(False)
        self.actionWatchlist_Only.setEnabled(False)
        self.string_filter = self.get_clean_string_filter()
        self.clear_ratings_filter_fields()
        self.clear_ui_filter_controls()
        self.recruit_tableView.setModel(None)
        self.recruit_tableView.setEnabled(False)
        self.comboBoxPositionFilter.setEnabled(False)
        self.checkBoxHideSigned.setEnabled(False)
        self.checkBoxUndecided.setEnabled(False)
        self.checkBoxWatched.setEnabled(False)
        self.comboBoxMilesFilter.setEnabled(False)
        self.comboBoxDivisionFilter.setEnabled(False)
        self.pushButtonUpdateConsidering.setEnabled(False)
        self.pushButtonMarkWatchlistPotential.setEnabled(False)
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
        myconfig.clear_model = False

    
    def loadModel(self):
        logger.debug("Entering loadModel() function...")
        db.setDatabaseName(myconfig.season_filename)
        logger.debug(f"Database name = {db.databaseName()}")
        logger.debug(f"Updating window title to {window_title} - {db.databaseName()}")
        self.setWindowTitle(f"{window_title} - {db.databaseName()}")
        self.actionGrabSeasonData.setEnabled(True)
        rids = query_Recruit_IDs("all", db)
        myconfig.rids_all_length = len(rids)
        if myconfig.rids_all_length != 0:
            self.model = TableModel()
            # initializeModel(self.model)
            self.recruit_tableView.setModel(self.model)
            #while self.model.canFetchMore():
            #    self.model.fetchMore()
            logger.info(f"Total Recruits = {myconfig.rids_all_length}")
            mw.statusbar.showMessage(f"{myconfig.rids_all_length} recruits loaded.")
            self.actionAll_Recruits.setEnabled(True)
            self.actionWatchlist_Only.setEnabled(True)
            self.recruit_tableView.setEnabled(True)
            self.comboBoxPositionFilter.setEnabled(True)
            self.checkBoxHideSigned.setEnabled(True)
            self.checkBoxUndecided.setEnabled(True)
            self.checkBoxWatched.setEnabled(True)
            self.comboBoxMilesFilter.setEnabled(True)
            self.comboBoxDivisionFilter.setEnabled(True)
            self.pushButtonApplyRatingsFilters.setEnabled(True)
            self.pushButtonClearRatingsFilters.setEnabled(True)
            if myconfig.rids_all_length != 0:
                self.pushButtonUpdateConsidering.setEnabled(True)
                self.pushButtonMarkWatchlistPotential.setEnabled(True)
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
            logger.debug("Checking for saved table header order state...")
            if self.settings.contains("table_header_order"):
                logger.debug(f"Restoring saved table header order state...")
                self.h_header.restoreState(self.settings.value("table_header_order", self.h_header.state()))

            # Process hidden columns config
            hidden = self.settings.value('HideColumns', [])
            if hidden != []:
                logger.info(f"Hiding columns = {hidden}")
                for col in hidden:
                    c = int(col)
                    self.recruit_tableView.setColumnHidden(c, True)


def load_config():
    config = configparser.ConfigParser()
    configfile = config.read(myconfig.config_file)
    config_changed = False
    old_config_file = os.path.join(myconfig.cwd, "config.ini")
    if path.exists(old_config_file):
        logger.info(f"Found old config.ini. Deleting {old_config_file}")
        os.remove(old_config_file)
    if  configfile == []:
        logger.info("config.ini file not found")
        logger.info("Creating config.ini with WISCreds section")
        config['WISCreds'] = {
                        'coachid': ''
                        }
        config['Browser'] = {
            'headless': 'false'
        }
        config['Logging'] = {
            'level': 'INFO'
        }
        config_changed = True
    else:
        logger.info("config.ini file found")
        # If config file exists but does not contain WISCreds section, add it
        if config.has_section('WISCreds'):
            logger.info("Config WISCreds section found")
            if not config.has_option('WISCreds','coachid'):
                logger.info("Adding missing coachid option to WISCreds section")
                config.set('WISCreds','coachid','')
                config_changed = True
            if config.has_option('WISCreds','username'):
                logger.info("Deleting username from config.ini because it is no longer needed.")
                config.remove_option('WISCreds','username')
                config_changed = True
            if config.has_option('WISCreds','password'):
                logger.info("Deleting password from config.ini because it is no longer needed.")
                config.remove_option('WISCreds','password')
                config_changed = True
        else:
            logger.info("Adding missing WISCreds section")
            config['WISCreds'] = {
                        'coachid' : ''
                        }
            config_changed = True
        # If config file exists but does not contain Browser section, add it
        if config.has_section('Browser'):
            logger.info("Config Browser section found")
            if not config.has_option('Browser', 'headless'):
                logger.info("Adding missing headless option to Browser section")
                config.set('Browser', 'headless', 'false')
                config_changed = True
        else:
            logger.info("Adding missing Browser section")
            config['Browser'] = {
                        'headless': 'false'
                        }
            config_changed = True
        # If config file exists but does not contain Logging section, add it
        if config.has_section('Logging'):
            logger.info("Config Logging section found")
            if not config.has_option('Logging', 'level'):
                logger.info("Adding missing level option to Logging section")
                config.set('Logging', 'level', 'INFO')
                config_changed = True
        else:
            logger.info("Adding missing Logging section")
            config['Logging'] = {
                        'level': 'INFO'
                        }
            config_changed = True
                

    if config_changed:
        logger.info("Config changed. Writing changed to config.ini file...")
        write_config(config)

    coachid = config['WISCreds']['coachid']
    c = {'config': config, 'coachid': coachid}
    return c


def write_config(config):
    logger.info("Writing config to config.ini file...")
    with open(myconfig.config_file, 'w') as file:
        config.write(file)


def update_active_teams(coachid):
    c = load_config()
    config = c['config']
    config.remove_section('Schools')
    config.add_section('Schools')
    requests_session = requests.Session()
    headers = {'User-Agent': 'gdrecruit-coach-update-active-teams/0.5.1 python-requests/2.25.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
    
    coach_profile_page = requests_session.get(f"https://wis-dev.shub.dog/account/UserProfile/Games/GridironDynasty/?user={coachid}", headers=headers)
    #coach_profile_page = requests_session.get(f"https://www.whatifsports.com/account/UserProfile/Games/GridironDynasty/?user={coachid}", headers=headers)
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
    
        write_config(config)

    elif coach_profile_page.status_code == 503:
        logger.error(f"Request to grab {coachid} profile page was NOT successful. Please check coach ID.")


def create_bold_attributes_df():
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
    df = pd.DataFrame(data, columns=column_headers, index=index_names)
    return df


def create_role_ratings_df():
    data = [['QB', 10, 4, 0, 0, 0, 26, 0, 0, 0, 24, 8, 28, 100],
            ['QBRun', 8, 18, 2, 1, 3, 24, 0, 0, 0, 16, 20, 8, 100],
            ['QBU1', 8, 4, 1, 1, 2, 26, 0, 0, 0, 26, 8, 24, 100],
            ['QBU2', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['QBU3', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['QBU4', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['RB', 8, 22, 1, 1, 3, 21, 0, 0, 3, 11, 22, 8, 100],
            ['FB', 8, 0, 1, 1, 3, 36, 30, 0, 0, 0, 13, 8, 100],
            ['RBSpeed', 8, 24, 1, 1, 3, 20, 0, 0, 0, 10, 25, 8, 100],
            ['RBPow', 8, 20, 1, 1, 3, 25, 0, 0, 0, 10, 24, 8, 100],
            ['RBPoss', 8, 22, 1, 1, 3, 21, 0, 0, 3, 11, 22, 8, 100],
            ['RBU1', 8, 22, 1, 1, 3, 21, 0, 0, 3, 11, 22, 8, 100],
            ['WR', 15, 18, 1, 1, 3, 0, 0, 0, 18, 20, 16, 8, 100],
            ['WRPoss', 16, 12, 1, 1, 3, 0, 0, 0, 24, 24, 11, 8, 100],
            ['WRDeep', 12, 23, 1, 1, 3, 0, 0, 0, 11, 18, 23, 8, 100],
            ['WRU1', 15, 18, 1, 1, 3, 0, 0, 0, 18, 20, 16, 8, 100],
            ['WRU2', 15, 18, 1, 1, 3, 0, 0, 0, 18, 20, 16, 8, 100],
            ['WRU3', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['TE', 14, 6, 1, 1, 2, 18, 13, 0, 13, 18, 6, 8, 100],
            ['TEBlock', 11, 0, 1, 1, 2, 36, 26, 0, 0, 15, 0, 8, 100],
            ['TEPoss', 16, 12, 1, 1, 2, 0, 0, 0, 24, 24, 12, 8, 100],
            ['TEU1', 14, 6, 1, 1, 2, 18, 13, 0, 13, 18, 6, 8, 100],
            ['TEU2', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['TEU3', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['OL', 12, 0, 1, 1, 2, 32, 32, 0, 0, 12, 0, 8, 100],
            ['Tackle', 12, 0, 1, 1, 2, 23, 41, 0, 0, 12, 0, 8, 100],
            ['Grd-Cntr', 12, 0, 1, 1, 2, 41, 23, 0, 0, 12, 0, 8, 100],
            ['OLU1', 12, 0, 1, 1, 2, 32, 32, 0, 0, 12, 0, 8, 100],
            ['OLU2', 12, 0, 1, 1, 2, 32, 32, 0, 0, 12, 0, 8, 100],
            ['OLU3', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['DL', 13, 8, 1, 1, 2, 32, 0, 20, 0, 15, 0, 8, 100],
            ['DT', 12, 6, 1, 1, 2, 38, 0, 17, 0, 15, 0, 8, 100],
            ['DE', 12, 15, 1, 1, 2, 22, 0, 24, 0, 15, 0, 8, 100],
            ['DLU1', 13, 8, 1, 1, 2, 32, 0, 20, 0, 15, 0, 8, 100],
            ['DLU2', 13, 8, 1, 1, 2, 32, 0, 20, 0, 15, 0, 8, 100],
            ['DLU3', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['LB', 15, 8, 1, 1, 2, 30, 0, 20, 0, 15, 0, 8, 100],
            ['ILB', 12, 4, 1, 1, 2, 38, 0, 22, 0, 12, 0, 8, 100],
            ['OLB', 13, 12, 1, 1, 2, 21, 0, 21, 0, 21, 0, 8, 100],
            ['LBU1', 13, 19, 1, 1, 2, 15, 0, 20, 0, 21, 0, 8, 100],
            ['LBU2', 15, 8, 1, 1, 2, 30, 0, 20, 0, 15, 0, 8, 100],
            ['LBU3', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['DB', 16, 20, 1, 1, 4, 10, 0, 10, 10, 20, 0, 8, 100],
            ['Safety', 18, 17, 1, 1, 4, 12, 0, 12, 10, 17, 0, 8, 100],
            ['CB', 21, 21, 1, 1, 4, 7, 0, 7, 12, 18, 0, 8, 100],
            ['DBU1', 15, 20, 1, 1, 4, 11, 0, 20, 8, 12, 0, 8, 100],
            ['DBU2', 15, 20, 1, 1, 4, 11, 0, 20, 8, 12, 0, 8, 100],
            ['DBU3', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['K', 8, 4, 1, 1, 0, 36, 0, 0, 0, 14, 0, 36, 100],
            ['KU1', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['KU2', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['KU3', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['KU4', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['KU5', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['P', 8, 4, 1, 1, 0, 36, 0, 0, 0, 14, 0, 36, 100],
            ['PU1', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['PU2', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['PU3', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['PU4', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['PU5', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    index_names = ['qbr1', 'qbr2', 'qbr3', 'qbr4', 'qbr5', 'qbr6',
                    'rbr1', 'rbr2', 'rbr3', 'rbr4', 'rbr5', 'rbr6',
                    'wrr1', 'wrr2', 'wrr3', 'wrr4', 'wrr5', 'wrr6',
                    'ter1', 'ter2', 'ter3', 'ter4', 'ter5', 'ter6',
                    'olr1', 'olr2', 'olr3', 'olr4', 'olr5', 'olr6',
                    'dlr1', 'dlr2', 'dlr3', 'dlr4', 'dlr5', 'dlr6',
                    'lbr1', 'lbr2', 'lbr3', 'lbr4', 'lbr5', 'lbr6',
                    'dbr1', 'dbr2', 'dbr3', 'dbr4', 'dbr5', 'dbr6',
                    'kr1', 'kr2', 'kr3', 'kr4', 'kr5', 'kr6',
                    'pr1', 'pr2', 'pr3', 'pr4', 'pr5', 'pr6',
    ]
    column_headers = ['label', 'ath', 'spd', 'dur', 'we', 'sta', 'str', 'blk', 'tkl', 'han', 'gi', 'elu', 'tec', 'total']
    df = pd.DataFrame(data, columns=column_headers, index=index_names)
    list_total = ['ath', 'spd', 'dur', 'we', 'sta', 'str', 'blk', 'tkl', 'han', 'gi', 'elu', 'tec']
    df['total'] = df.loc[:,list_total].sum(axis=1)
    return df


class TableModel(QSqlTableModel):
    def __init__(self, *args, **kwargs):
        super(TableModel, self).__init__(*args, **kwargs)
        logger.debug("-> TableModel.__init__:")
        self.setTable('recruits')
        # model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.select()
        dbname = db.databaseName()
        dbname_re = re.search(r'(\d{5})', dbname)
        teamid = f"{dbname_re.group(1)}"
        self.teamname = f"{myconfig.wis_gd_df.school_short[int(teamid)]}"
        c = load_config()
        self.coachid = c['coachid']
        self.team_filter = f"{self.teamname} ({self.coachid})"
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
            'Watched': 31,
            'Division': 32
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
        self.setHeaderData(col_head['Division'], Qt.Horizontal, "Division")
        self.info()
        logger.debug("<- TableModel.__init__")

        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            self.checkmarkicon = f"{Path(sys._MEIPASS) / 'images' / 'checkmark_1.png'}"
            self.checkmarkicon_yellow = f"{Path(sys._MEIPASS) / 'images' / 'checkmark_yellow.png'}"
            self.x_icon = f"{Path(sys._MEIPASS) / 'images' / 'x_icon.png'}"
            self.blank_icon = f"{Path(sys._MEIPASS) / 'images' / 'blank_icon.png'}"
        #checkmarkicon = f"{sys._MEIPASS}/images/checkmark_1.png"
        else:
            self.checkmarkicon = f"./images/checkmark_1.png"
            self.checkmarkicon_yellow = f"./images/checkmark_yellow.png"
            self.x_icon = f"./images/x_icon.png"
            self.blank_icon = f"./images/blank_icon.png"

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
            
            if index.column() == 6:
                value = super(TableModel, self).data(index)
                if value == 999:
                    return None

        # Add a checkmark icon if a player is watched
        if role == Qt.DecorationRole:
            if index.column() in [31]:
                value = super(TableModel, self).data(index)
                if value == 1:
                    return QIcon(self.checkmarkicon)
            
            if index.column() in [1]:
                if super(TableModel, self).data(self.index(index.row(), 31), Qt.DisplayRole) == 1:
                    return QIcon(self.checkmarkicon)
                else:
                    return QIcon(self.blank_icon)

            if index.column() in [9]:
                value = super(TableModel, self).data(index)
                if super(TableModel, self).data(self.index(index.row(), 30), Qt.DisplayRole) == 1 and self.teamname == value:
                    return QIcon(self.checkmarkicon)
                else:
                    return QIcon(self.blank_icon)

            # Format considering text
            # Red not considering
            # Orange considering with others
            # Green only considering your own school
            #if index.column() == 9:
            #    value = super(TableModel, self).data(index)
            #    if self.teamname in value and "\n" not in value:
            #        return QIcon(self.checkmarkicon)
            #    if self.teamname in value and "\n" in value:
            #        return QIcon(self.checkmarkicon_yellow)
            #    if self.teamname not in value:
            #        return QIcon(self.blank_icon)

        # Format background of the entire row to light gray if a player is signed
        if role == Qt.BackgroundRole:
            if super(TableModel, self).data(self.index(index.row(), 30), Qt.DisplayRole) == 1:
                return QBrush(Qt.lightGray)
        
            # Format considering text
            # Red not considering
            # Orange considering with others
            # Green only considering your own school
            if index.column() == 9:
                value = super(TableModel, self).data(index)
                if (self.team_filter in value and "\n" not in value) or self.teamname == value:
                    return QBrush(Qt.green)
                if self.team_filter in value and "\n" in value:
                    return QBrush(Qt.yellow)
                #if self.teamname not in value:
                #    return QIcon(self.blank_icon)
            

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

def start_logging(level):
    logger.remove()
    logger.add("gdrecruit.log",
                format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {thread.name: >10}:{module: <8}:{line: >4}:{function: <20} - {message}",
                level=level,
                rotation="10 MB",
                compression="zip")
    logger.info(f"Logging level = {level}")
    

if __name__ == "__main__":
    
    log_level = "INFO"
    start_logging(log_level)
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
    
    # Config data
    QCoreApplication.setOrganizationName("GD Apps")
    QCoreApplication.setApplicationName("GD Recruit Assistant")
    logger.info(f"Current working directory = {myconfig.cwd}")
    logger.info(f"Config file path = {myconfig.config_file}")
    logger.info(f"Role Ratings CSV file path = {myconfig.role_ratings_csv}")
    logger.info(f"Bold Attributes CSV file path = {myconfig.bold_attributes_csv}")
    logger.info(f"gdr.csv path is = {myconfig.gdr_csv}")
    logger.info(f"Checkmark icon path is = {myconfig.checkmarkicon}")
    logger.info(f"X icon path is = {myconfig.x_icon}")
    c = load_config()
    config = c['config']
    coachid = c['coachid']
    logger.info("Read config.ini file")
    if config.has_section('Logging'):
        logger.info("Config.ini contains Logging section")
        if config.has_option('Logging', 'level'):
            logger.info("Logging section contains 'level' option")
            try:
                log_level = config.get('Logging', 'level')
            except Exception as e:
                logger.error(f"Oops...exception getting Log Level setting from config.ini: {e.__class__}")
            else:
                start_logging(log_level.upper())
        else:
            logger.info("Logging section does not contain 'level' option")
    else:
        logger.info("Config.ini does not contain Logging section")

    # global variables
    code = ""
    wait_for_code = False
    gdr_csv = ''
    

    # Bold Attributes Config
    if path.exists(myconfig.bold_attributes_csv):
        logger.debug("bold_attributes_csv file path found.")
        try:
            bold_attributes_df = pd.read_csv(myconfig.bold_attributes_csv, header = 0, index_col=0)
        except Exception as e:
            logger.error(f"Exception ({e}) reading bold_attributes.csv file.")
    else:
        logger.debug("bold_attributes_csv file path NOT found.")
        logger.debug("Creating bold_attributes.csv file...")
        bold_attributes_df = create_bold_attributes_df()
        bold_attributes_df.to_csv(myconfig.bold_attributes_csv)

    
    
    if path.exists(myconfig.role_ratings_csv):
        logger.debug("role_ratings_csv file path found.")
        try:
            myconfig.role_ratings_df = pd.read_csv(myconfig.role_ratings_csv, header = 0, index_col=0)
        except Exception as e:
            logger.error(f"Exception ({e}) reading role_ratings.csv file.")
    else:
        logger.debug("role_ratings_csv file path NOT found.")
        logger.debug("Creating role_ratings.csv file...")
        myconfig.role_ratings_df = create_myconfig.role_ratings_df()
        myconfig.role_ratings_df.to_csv(myconfig.role_ratings_csv)

    # Configure for High DPI
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    app = QApplication(sys.argv)
    
        
    # Default database connection
    db = QSqlDatabase.addDatabase('QSQLITE')
    # Database connection to be used by thread
    db_t = QSqlDatabase.addDatabase('QSQLITE', connectionName='worker_connection')
    db_m = QSqlDatabase.addDatabase('QSQLITE', connectionName='worker_connection_watchlist')
    mw = MainWindow()
    mw.setWindowTitle(window_title)
    mw.show() 
    sys.exit(app.exec_())