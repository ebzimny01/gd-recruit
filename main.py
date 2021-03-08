from mypackages.grab_season_data_widget import Ui_WidgetGrabSeasonData
from mypackages.initialize_recruits_widget import Ui_WidgetInitializeRecruits
import os
import sys
import asyncio
import datetime
import logging
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
from mypackages.logging import *
import configparser
from progress.bar import Bar


# https://stackoverflow.com/questions/61316258/how-to-overwrite-qdialog-accept


def query_Recruit_IDs(type):
    openDB(db)
    queryRecruitIDs = QSqlQuery()
    rids = []
    if type == "all":
        if not queryRecruitIDs.exec_("SELECT id FROM recruits"):
            logQueryError(queryRecruitIDs)
        while queryRecruitIDs.next():
            rids.append(queryRecruitIDs.value('id'))
    elif type == "unsigned":
        if not queryRecruitIDs.exec_("SELECT id FROM recruits WHERE signed=0"):
            logQueryError(queryRecruitIDs)
        while queryRecruitIDs.next():
            rids.append(queryRecruitIDs.value('id'))
    queryRecruitIDs.finish()
    db.close()
    return rids


class GrabSeasonData(QDialog, Ui_WidgetGrabSeasonData):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButtonInitializeRecruits.clicked.connect(self.initialize_recruit_data)
        self.pushButtonUpdateConsideringSigned.clicked.connect(self.update_considering)


    def accept(self):
        super().accept()


    def initialize_recruit_data(self):
        user, pwd, config = load_config()
        requests_session = requests.Session()
        
        openDB(db)

        createRecruitTableQuery = QSqlQuery()
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
                gpa REAL,
                pot TEXT,
                signed INTEGER
            )
            """
        ):
            logQueryError(createRecruitTableQuery)
        if db.tables() == ['recruits']:
            if not createRecruitTableQuery.exec_("DELETE from recruits"):
                logQueryError(createRecruitTableQuery)
        createRecruitTableQuery.finish()
        db.close()
        
        wis_browser(config, user, pwd, "scrape_recruit_IDs", db)
        rids = query_Recruit_IDs("all")
        openDB(db)
        queryUpdate = QSqlQuery()
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
                                "gpa = :gpa "
                            "WHERE id = :id")
                    
        with Bar('Initializing Recruit Static Data without Playwright', max=len(rids)) as bar:
            for rid in rids:
                recruitpage = requests_session.get(f"https://www.whatifsports.com/gd/RecruitProfile/Ratings.aspx?rid={rid}")
                recruitpage_soup = BeautifulSoup(recruitpage.content, "lxml")
                recruit_ratings_section = recruitpage_soup.find(class_="ratingsDisplayCtl")
                recruit_ratings_values = recruit_ratings_section.find_all(class_="value")
                gpa_section = recruitpage_soup.find(id="ctl00_ctl00_ctl00_Main_Main_gpa")
                gpa = float(gpa_section.text)
                queryUpdate.bindValue(":ath", int(recruit_ratings_values[0].text))
                queryUpdate.bindValue(":spd", int(recruit_ratings_values[1].text))
                queryUpdate.bindValue(":dur", int(recruit_ratings_values[2].text))
                queryUpdate.bindValue(":we", int(recruit_ratings_values[3].text))
                queryUpdate.bindValue(":sta", int(recruit_ratings_values[4].text))
                queryUpdate.bindValue(":str", int(recruit_ratings_values[5].text))
                queryUpdate.bindValue(":blk", int(recruit_ratings_values[6].text))
                queryUpdate.bindValue(":tkl", int(recruit_ratings_values[7].text))
                queryUpdate.bindValue(":han", int(recruit_ratings_values[8].text))
                queryUpdate.bindValue(":gi", int(recruit_ratings_values[9].text))
                queryUpdate.bindValue(":elu", int(recruit_ratings_values[10].text))
                queryUpdate.bindValue(":tec", int(recruit_ratings_values[11].text))
                queryUpdate.bindValue(":gpa", gpa)
                queryUpdate.bindValue(":id", rid)
                
                if not queryUpdate.exec_():
                    logQueryError(queryUpdate)
                bar.next()
        queryUpdate.finish()
        db.close()


    def update_considering(self):
        requests_session = requests.Session()
        rids = query_Recruit_IDs("unsigned")
        openDB(db)
        queryUpdateConsidering = QSqlQuery()
        queryUpdateConsidering.prepare("UPDATE recruits "
                                        "SET considering = :considering, "
                                        "signed = :signed "
                                        "WHERE id = :id")
        with Bar('Update Recruits Considering without Playwright', max=len(rids)) as bar:
            for rid in rids:
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
                        considering = f"{href_tag_re.group(1)}"
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
                bar.next()
        queryUpdateConsidering.finish()
        db.close()


class LoadSeason(QDialog, Ui_DialogLoadSeason):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        db_files = [x for x in os.listdir() if x.endswith(".db")]
        if len(db_files) > 0:
            self.comboBoxSelectSeason.addItems(db_files)

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
        config.read('config.ini')
        if config.has_section('Schools') and len(config['Schools']) > 0:
            self.comboBoxTeamID.addItems(config['Schools'])


    def accept(self):
        teamID = self.comboBoxTeamID.currentText()
        seasonnum = self.lineEditSeasonNumber.text()
        wid_world = wid_world_list()
        world = wid_world[teamID]
        # Need to add functionality for New Season
        season_filename = f"{world} {seasonnum} - {teamID}.db"
        print(f"Setting database name to: {season_filename}")
        db.setDatabaseName(season_filename)
        db.close()
        db.open()
        super().accept()


class WISCred(QDialog, Ui_WISCredentialDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        wisuser, pwd, config = load_config()
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
        super().__init__(parent)
        self.setupUi(self)
        self.recruit_tableView.setEditTriggers(QTableView.NoEditTriggers)
        h_header = self.recruit_tableView.horizontalHeader()
        h_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        v_header = self.recruit_tableView.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        
        # Allow only integeres to be entered into the ratings filter fields
        self.onlyInt = QIntValidator()
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
        
        # UI triggers
        self.actionWIS_Credentials.triggered.connect(self.open_WIS_cred)
        self.actionNew_Season.triggered.connect(self.open_New_Season)
        self.actionLoad_Season.triggered.connect(self.open_Load_Season)
        self.actionGrabSeasonData.triggered.connect(self.open_Grab_Season_Data)
        self.comboBoxPositionFilter.activated.connect(self.position_filter)
        self.comboBoxMilesFilter.activated.connect(self.miles_filter)
        self.checkBoxHideSigned.stateChanged.connect(self.hide_signed_filter)
        self.checkBoxUndecided.stateChanged.connect(self.undecided_filter)
        self.pushButtonApplyRatingsFilters.clicked.connect(self.apply_ratings_filters)
        self.pushButtonClearRatingsFilters.clicked.connect(self.clear_ratings_filter_fields)
        
        # Filter data structure used to track which filters are active
        # And then used to build the filter string
        self.string_filter = {
            'pos' : "",
            'hide_signed' : "",
            'undecided' : "",
            'miles' : "",
            'ath' : "",
            'spd' : "",
            'dur' : "",
            'we' : "",
            'sta' : "",
            'str' : "",
            'blk' : "",
            'tkl' : "",
            'han' : "",
            'gi' : "",
            'elu' : "",
            'tec' : ""
        }
        
        if self.check_stored_creds():
            # Need to attempt to authenticate to WIS
            # After successful auth then grab active GD teams
            # Then store teams in config.ini
            user, pwd, config = load_config()
            f = "updateteams"
            # wis_browser(config, user, pwd, f, db)
        else:
            False


    def newFilter(self, model):
        filter = self.getFilterString()
        print(f"New filter string = {filter}")
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
        print("Clear Ratings Filters button was clicked!")
        print(f"Previous filter = {self.getFilterString()}")
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
        text_fields = {
            'ath' : self.lineEditfilterATH.text(),
            'spd' : self.lineEditfilterSPD.text(),
            'we' : self.lineEditfilterWE.text(),
            'dur' : self.lineEditfilterDUR.text(),
            'sta' : self.lineEditfilterSTA.text(),
            'str' : self.lineEditfilterSTR.text(),
            'blk' : self.lineEditfilterBLK.text(),
            'tkl' : self.lineEditfilterTKL.text(),
            'han' : self.lineEditfilterHAN.text(),
            'gi' : self.lineEditfilterGI.text(),
            'elu' : self.lineEditfilterELU.text(),
            'tec' : self.lineEditfilterTEC.text()
            }
        
        for k,v in text_fields.items():
            self.apply_helper(k, v)
        
        print(f"Clearing Considering filter...")
        self.string_filter['considering'] = ""
        
        self.newFilter(self.model)


    def apply_helper(self, k, v):
            if v:
                print(f"Enabling {k} filter...")
                self.string_filter[k] = f"{k} > {int(v)}"
            else:
                print(f"Clearing {k} filter...")
                self.string_filter[k] = ""


    def apply_ratings_filters(self):
        print("Ratings Filters Apply button was clicked!")
        print(f"Previous filter = {self.getFilterString()}")
        text_fields = {
            'ath' : self.lineEditfilterATH.text(),
            'spd' : self.lineEditfilterSPD.text(),
            'we' : self.lineEditfilterWE.text(),
            'dur' : self.lineEditfilterDUR.text(),
            'sta' : self.lineEditfilterSTA.text(),
            'str' : self.lineEditfilterSTR.text(),
            'blk' : self.lineEditfilterBLK.text(),
            'tkl' : self.lineEditfilterTKL.text(),
            'han' : self.lineEditfilterHAN.text(),
            'gi' : self.lineEditfilterGI.text(),
            'elu' : self.lineEditfilterELU.text(),
            'tec' : self.lineEditfilterTEC.text()
            }
        
        for k,v in text_fields.items():
            self.apply_helper(k, v)

        # Considering handled separately since it needs different operator
        considering = self.lineEditConsideringTextSearch.text()
        if considering:
            print(f"Enabling Considering filter...")
            self.string_filter['considering'] = f"considering LIKE '%{considering}%'"
        else:
            print(f"Clearing Considering filter...")
            self.string_filter['considering'] = ""

        self.newFilter(self.model)

    def undecided_filter(self):
        state = self.checkBoxUndecided.checkState()
        print(f"Previous filter = {self.getFilterString()}")
        if state == 0:
            print("Clearing Undecided filter...")
            self.string_filter['undecided'] = ""
        elif state == 2:
            print("Enabling Undecided filter...")
            self.string_filter['undecided'] = "considering = 'undecided'"
        else:
            raise Exception
        
        self.newFilter(self.model)


    def hide_signed_filter(self):
        state = self.checkBoxHideSigned.checkState()
        print(f"Previous filter = {self.getFilterString()}")
        if state == 0:
            print("Clearing Hide Signed filter...")
            self.string_filter['hide_signed'] = ""
        elif state == 2:
            print("Enabling Hide Signed filter...")
            self.string_filter['hide_signed'] = "signed = 0"
        else:
            raise Exception
        
        self.newFilter(self.model)
    

    def miles_filter(self):
        combo_box_filter = f"miles < {self.comboBoxMilesFilter.currentText()}"
        print(f"Previous filter = {self.getFilterString()}")
        if self.comboBoxMilesFilter.currentText() == "Any":
            print("Clearing Miles Filter...")
            self.string_filter['miles'] = ""
        else:
            print("Adding Miles Filter...")
            self.string_filter['miles'] = combo_box_filter
        
        self.newFilter(self.model)


    def position_filter(self):
        combo_box_filter = f"pos = '{self.comboBoxPositionFilter.currentText()}'"
        print(f"Previous filter = {self.getFilterString()}")
        if self.comboBoxPositionFilter.currentText() == "ALL":
            print("Clearing Position Filter...")
            self.string_filter['pos'] = ""
        else:
            print("Adding Position Filter...")
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
        print("Exiting New Season dialog")
        print(f"database name = {db.databaseName()}")
        if db.databaseName() != "":
            self.setWindowTitle(f"GD Recruit Helper - {db.databaseName()}")
            self.actionGrabSeasonData.setEnabled(True)
            self.loadModel()
            
            
    def open_Load_Season(self):
        dialog = LoadSeason()
        dialog.ui = Ui_DialogLoadSeason()
        dialog.exec_()
        dialog.show()
        print("Exiting Load Season dialog")
        print(f"database name = {db.databaseName()}")
        if db.databaseName() != "":
            self.setWindowTitle(f"GD Recruit Helper - {db.databaseName()}")
            self.actionGrabSeasonData.setEnabled(True)
            self.loadModel()
            

    def open_Grab_Season_Data(self):
        dialog = GrabSeasonData()
        dialog.ui = Ui_WidgetGrabSeasonData()
        dialog.exec_()
        dialog.show()
        print("Exiting Grab Season Data dialog")
        print(f"database name = {db.databaseName()}")
        if db.databaseName() != "":
            self.loadModel()
        

    def check_stored_creds(self):
        user, pwd, config = load_config()
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

    return username, password, config


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
   model.setHeaderData(22, Qt.Horizontal, "GPA")
   model.setHeaderData(23, Qt.Horizontal, "Pot")
   model.setHeaderData(24, Qt.Horizontal, "Signed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    #db.setDatabaseName('wilkinson 172 - 51194.db')
    #model = QSqlTableModel()
    #initializeModel(model)
    mw = MainWindow()
    mw.setWindowTitle(u"GD Recruit Helper")
    mw.show() 
    sys.exit(app.exec_())