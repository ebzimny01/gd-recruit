from mypackages.initialize_recruits_widget import Ui_WidgetInitializeRecruits
import os
import sys
import asyncio
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


# https://stackoverflow.com/questions/61316258/how-to-overwrite-qdialog-accept


def initialize_recruit_data(config, user, pwd):
    requests_session = requests.Session()
    wis_browser(config, user, pwd, "scrape_recruit_IDs", db)
    if not db.open():
        QMessageBox.critical(
            None,
            "GD Recruiting App - Error!",
            "Database Error: %s" % db.lastError().databaseText()
            )
        sys.exit(1)
    query = QSqlQuery()
    query.exec_("SELECT id FROM recruits")
    rids = []
    while query.next():
        rids.append(query.value(id))
    query.finish()
    queryUpdate = QSqlQuery()
    with Bar('Initializing Recruit Static Data without Playwright', max=len(rids)) as bar:
        for rid in rids:
            recruitpage = requests_session.get(f"https://www.whatifsports.com/gd/RecruitProfile/Ratings.aspx?rid={rid}")
            recruitpage_soup = BeautifulSoup(recruitpage.content, "lxml")
            # name_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_name")
            # name = name_section.text
            # pos_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_position")
            # pos = pos_section.text
            recruit_ratings_section = recruitpage_soup.find(class_="ratingsDisplayCtl")
            recruit_ratings_values = recruit_ratings_section.find_all(class_="value")
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
            tot = ath + spd + dur + we + sta + strength + blk + tkl + han + gi + elu + tec
            gpa_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_gpa")
            gpa = float(gpa_section.text)
            # hometown_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_homeTown")
            # hometown = hometown_section.text
            queryUpdate.exec_(
                        f"""
                        UPDATE recruits SET ath = {ath} ,
                                            spd = {spd} ,
                                            dur = {dur} ,
                                            we = {we} ,
                                            sta = {sta} ,
                                            str = {strength} ,
                                            blk = {blk} ,
                                            tkl = {tkl} ,
                                            han = {han} ,
                                            gi = {gi} ,
                                            elu = {elu} ,
                                            tec = {tec} ,
                                            tot = {tot} ,
                                            gpa = {gpa}
                            WHERE id = {rid}
                        """
            )
            bar.next()
    queryUpdate.finish()
    db.close()


class InitializeRecruits(QDialog, Ui_WidgetInitializeRecruits):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        config = configparser.ConfigParser()
        config.read('config.ini')
        user = config['WISCreds']['username']
        pwd = config['WISCreds']['password']
        initialize_recruit_data(config, user, pwd)
    
    def accept(self):
        # Need to add functionality for loading season
        super().accept()

class LoadSeason(QDialog, Ui_DialogLoadSeason):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        db_files = [x for x in os.listdir() if x.endswith(".db")]
        if len(db_files) > 0:
            self.comboBoxSelectSeason.addItems(db_files)

    def accept(self):
        # Need to add functionality for loading season
        season_filename = self.comboBoxSelectSeason.currentText()
        db.setDatabaseName(season_filename)
        super().accept()

class NewSeason(QDialog, Ui_DialogNewSeason):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        config = configparser.ConfigParser()
        config.read('config.ini')
        if config.has_section('Schools') and len(config['Schools']) > 0:
            self.comboBoxTeamID.addItems(config['Schools'])
            #i = 0
            #for id in config['Schools']:
                #self.comboBoxTeamID.addItem(f"{id}")
                # self.comboBoxTeamID.setItemText(i, QCoreApplication.translate("DialogNewSeason", f"{id}", None))
                #i += 1

    def accept(self):
        teamID = self.comboBoxTeamID.currentText()
        seasonnum = self.lineEditSeasonNumber.text()
        wid_world = wid_world_list()
        world = wid_world[teamID]
        # Need to add functionality for New Season
        season_filename = f"{world} {seasonnum} - {teamID}.db"
        db.setDatabaseName(season_filename)
        if not db.open():
            QMessageBox.critical(
                self,
                "GD Recruiting App - Error!",
                "Database Error: %s" % db.lastError().databaseText()
                )
            sys.exit(1)
        createRecruitTableQuery = QSqlQuery()
        createRecruitTableQuery.exec_(
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
                tot INTEGER,
                gpa REAL,
                pot TEXT
            )
            """
        )
        db.close()
        super().accept()


class WISCred(QDialog, Ui_WISCredentialDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        wisuser, pwd = load_config()
        self.setupUi(self, wisuser, pwd)

    def accept(self):
        user = self.lineEditWISUsername.text()
        pwd = self.lineEditWISPassword.text()
        print(f"Username = {user}")
        print(f"password = {pwd}")
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.set('WISCreds', 'username', user)
        config.set('WISCreds', 'password', pwd)
        with open("config.ini", 'w') as file:
            config.write(file)
        super().accept()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent),
        self.setupUi(self, model)
        self.recruit_tableView.setModel(model)
        h_header = self.recruit_tableView.horizontalHeader()
        h_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        v_header = self.recruit_tableView.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.actionWIS_Credentials.triggered.connect(self.open_WIS_cred)
        self.actionNew_Season.triggered.connect(self.open_New_Season)
        self.actionLoad_Season.triggered.connect(self.open_Load_Season)
        self.actionInitialize_Recruits.triggered.connect(self.open_Initialize_Recruits)
        config = configparser.ConfigParser()
        config.read('config.ini')
        if self.check_stored_creds(config):
            # Need to attempt to authenticate to WIS
            # After successful auth then grab active GD teams
            # Then store teams in config.ini
            user = config['WISCreds']['username']
            pwd = config['WISCreds']['password']
            f = "updateteams"
            # wis_browser(config, user, pwd, f, db)
        else:
            False
            

    def open_WIS_cred(self):
        dialog = WISCred()
        dialog.ui = Ui_WISCredentialDialog()        
        dialog.exec_()
        dialog.show()
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.check_stored_creds(config)


    def open_New_Season(self):
        dialog = NewSeason()
        dialog.ui = Ui_DialogNewSeason()
        dialog.exec_()
        dialog.show()


    def open_Load_Season(self):
        dialog = LoadSeason()
        dialog.ui = Ui_DialogLoadSeason()
        dialog.exec_()
        dialog.show()
        self.setWindowTitle(f"GD Recruit Helper - {db.databaseName()}")


    def open_Initialize_Recruits(self):
        dialog = InitializeRecruits()
        dialog.ui = Ui_WidgetInitializeRecruits()
        dialog.exec_()
        dialog.show()


    def check_stored_creds(self, config):
        if config['WISCreds']['username'] == '' or config['WISCreds']['password'] == '':
            self.actionNew_Season.setEnabled(False)
            self.actionLoad_Season.setEnabled(False)
            return False
        else:
            self.actionNew_Season.setEnabled(True)
            self.actionLoad_Season.setEnabled(True)
            return True
   

def load_config():
    config = configparser.ConfigParser()
    configfile = config.read('config.ini')
    if  configfile == []:
        print("config.ini file not found")
        print("Creating config.ini . . . ")
        config['WISCreds'] = {
                        'Username' : '',
                        'Password' : ''
                        }
        with open("config.ini", 'w') as file:
            config.write(file)
    else:
        print("config.ini file found")
    
    username = config['WISCreds']['username']
    password = config['WISCreds']['password']

    return username, password


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
   model.setHeaderData(22, Qt.Horizontal, "TOT")
   model.setHeaderData(23, Qt.Horizontal, "GPA")
   model.setHeaderData(24, Qt.Horizontal, "Pot")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    # db.setDatabaseName("recruit.db")
    model = QSqlTableModel()
    initializeModel(model)
    mw = MainWindow()
    mw.setWindowTitle(u"GD Recruit Helper")
    mw.show() 
    sys.exit(app.exec_())