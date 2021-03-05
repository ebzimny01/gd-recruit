from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, model):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1754, 1154)
        self.actionNew_Season = QAction(MainWindow)
        self.actionNew_Season.setObjectName(u"actionNew_Season")
        self.actionLoad_Season = QAction(MainWindow)
        self.actionLoad_Season.setObjectName(u"actionLoad_Season")
        self.actionInitialize_Recruits = QAction(MainWindow)
        self.actionInitialize_Recruits.setObjectName(u"actionInitialize_Recruits")
        self.actionInitialize_Recruits.setEnabled(False)
        self.actionWIS_Credentials = QAction(MainWindow)
        self.actionWIS_Credentials.setObjectName(u"actionWIS_Credentials")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.recruit_tableView = QTableView(self.centralwidget)
        self.recruit_tableView.setObjectName(u"recruit_tableView")
        self.recruit_tableView.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recruit_tableView.sizePolicy().hasHeightForWidth())
        self.recruit_tableView.setSizePolicy(sizePolicy)
        self.recruit_tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.recruit_tableView.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.recruit_tableView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1754, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menudata = QMenu(self.menubar)
        self.menudata.setObjectName(u"menudata")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menudata.menuAction())
        self.menuFile.addAction(self.actionWIS_Credentials)
        self.menuFile.addAction(self.actionNew_Season)
        self.menuFile.addAction(self.actionLoad_Season)
        self.menudata.addAction(self.actionInitialize_Recruits)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GD Recruit Helper", None))
        self.actionNew_Season.setText(QCoreApplication.translate("MainWindow", u"New Season", None))
        self.actionLoad_Season.setText(QCoreApplication.translate("MainWindow", u"Load Season", None))
        self.actionInitialize_Recruits.setText(QCoreApplication.translate("MainWindow", u"Initialize Recruits", None))
        self.actionWIS_Credentials.setText(QCoreApplication.translate("MainWindow", u"WIS Credentials", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menudata.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
    # retranslateUi