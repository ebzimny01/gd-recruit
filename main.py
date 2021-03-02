from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *
from mypackages.mainwindow_ui import Ui_MainWindow
from mypackages.wis_cred_dialog import Ui_WISCredentialDialog
from mypackages.new_season_dialog import Ui_DialogNewSeason
import configparser


# https://stackoverflow.com/questions/61316258/how-to-overwrite-qdialog-accept

class NewSeason(QDialog, Ui_DialogNewSeason):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def accept(self):
        print("custom func")
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
        super().__init__(parent)
        self.setupUi(self, model)
        self.actionWIS_Credentials.triggered.connect(self.open_WIS_cred)
        self.actionNew_Season.triggered.connect(self.open_New_Season)

    def open_WIS_cred(self):
        dialog = WISCred()
        dialog.ui = Ui_WISCredentialDialog()
        #dialog.ui.setupUi(dialog)
        
        dialog.exec_()
        dialog.show()

    def open_New_Season(self):
        dialog = NewSeason()
        dialog.ui = Ui_DialogNewSeason()
        # dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

        
        

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
    import sys
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName("recruit.db")
    model = QSqlTableModel()
    initializeModel(model)
    mw = MainWindow()
    mw.setWindowTitle(u"GD Recruit Helper")
    mw.show() 
    sys.exit(app.exec_())