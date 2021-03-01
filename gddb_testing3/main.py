# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiLoiFdD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, model):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"GD Recruit Helper")
        
        self.actionNew_Season = QAction(MainWindow)
        self.actionNew_Season.setObjectName(u"actionNew_Season")
        self.actionLoad_Season = QAction(MainWindow)
        self.actionLoad_Season.setObjectName(u"actionLoad_Season")
        self.actionInitialize_Recruits = QAction(MainWindow)
        self.actionInitialize_Recruits.setObjectName(u"actionInitialize_Recruits")
        self.actionWIS_Credentials = QAction(MainWindow)
        self.actionWIS_Credentials.setObjectName(u"actionWIS_Credentials")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView.setSortingEnabled(True)
        self.verticalLayout.addWidget(self.tableView)

        self.tableView.setModel(model)
        self.tableView.setSortingEnabled(True)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        # self.menubar.setGeometry(QRect(0, 0, 1740, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menudata = QMenu(self.menubar)
        self.menudata.setObjectName(u"menudata")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menudata.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuFile.addAction(self.actionNew_Season)
        self.menuFile.addAction(self.actionLoad_Season)
        self.menudata.addAction(self.actionInitialize_Recruits)
        self.menuSettings.addAction(self.actionWIS_Credentials)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew_Season.setText(QCoreApplication.translate("MainWindow", u"New Season", None))
        self.actionLoad_Season.setText(QCoreApplication.translate("MainWindow", u"Load Season", None))
        self.actionInitialize_Recruits.setText(QCoreApplication.translate("MainWindow", u"Initialize Recruits", None))
        self.actionWIS_Credentials.setText(QCoreApplication.translate("MainWindow", u"WIS Credentials", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menudata.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi


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
    db.setDatabaseName("gddb_testing\\recruit.db")
    model = QSqlTableModel()
    initializeModel(model)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, model) 
    MainWindow.setWindowTitle(u"GD Recruit Helper")
    MainWindow.show() 
    sys.exit(app.exec_()) 