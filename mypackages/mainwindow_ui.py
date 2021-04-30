from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1169, 1265)
        self.actionNew_Season = QAction(MainWindow)
        self.actionNew_Season.setObjectName(u"actionNew_Season")
        font = QFont()
        font.setFamily(u"Arial")
        self.actionNew_Season.setFont(font)
        self.actionLoad_Season = QAction(MainWindow)
        self.actionLoad_Season.setObjectName(u"actionLoad_Season")
        self.actionLoad_Season.setFont(font)
        self.actionGrabSeasonData = QAction(MainWindow)
        self.actionGrabSeasonData.setObjectName(u"actionGrabSeasonData")
        self.actionGrabSeasonData.setEnabled(False)
        self.actionGrabSeasonData.setFont(font)
        self.actionWIS_Credentials = QAction(MainWindow)
        self.actionWIS_Credentials.setObjectName(u"actionWIS_Credentials")
        self.actionWIS_Credentials.setFont(font)
        self.actionBold_Attributes = QAction(MainWindow)
        self.actionBold_Attributes.setObjectName(u"actionBold_Attributes")
        self.actionRole_Ratings = QAction(MainWindow)
        self.actionRole_Ratings.setObjectName(u"actionRole_Ratings")
        self.actionAll_Recruits = QAction(MainWindow)
        self.actionAll_Recruits.setObjectName(u"actionAll_Recruits")
        self.actionWatchlist_Only = QAction(MainWindow)
        self.actionWatchlist_Only.setObjectName(u"actionWatchlist_Only")
        self.actionAdvanced = QAction(MainWindow)
        self.actionAdvanced.setObjectName(u"actionAdvanced")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionShow_Columns = QAction(MainWindow)
        self.actionShow_Columns.setObjectName(u"actionShow_Columns")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.labelPositionFilter = QLabel(self.centralwidget)
        self.labelPositionFilter.setObjectName(u"labelPositionFilter")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPositionFilter.sizePolicy().hasHeightForWidth())
        self.labelPositionFilter.setSizePolicy(sizePolicy)
        self.labelPositionFilter.setMaximumSize(QSize(30, 16777215))
        self.labelPositionFilter.setFont(font)
        self.labelPositionFilter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelPositionFilter)

        self.comboBoxPositionFilter = QComboBox(self.centralwidget)
        self.comboBoxPositionFilter.addItem("")
        self.comboBoxPositionFilter.addItem("")
        self.comboBoxPositionFilter.addItem("")
        self.comboBoxPositionFilter.addItem("")
        self.comboBoxPositionFilter.addItem("")
        self.comboBoxPositionFilter.addItem("")
        self.comboBoxPositionFilter.addItem("")
        self.comboBoxPositionFilter.addItem("")
        self.comboBoxPositionFilter.addItem("")
        self.comboBoxPositionFilter.addItem("")
        self.comboBoxPositionFilter.addItem("")
        self.comboBoxPositionFilter.setObjectName(u"comboBoxPositionFilter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBoxPositionFilter.sizePolicy().hasHeightForWidth())
        self.comboBoxPositionFilter.setSizePolicy(sizePolicy1)
        self.comboBoxPositionFilter.setMinimumSize(QSize(45, 0))
        self.comboBoxPositionFilter.setMaximumSize(QSize(45, 30))
        self.comboBoxPositionFilter.setFont(font)
        self.comboBoxPositionFilter.setMaxVisibleItems(11)
        self.comboBoxPositionFilter.setMaxCount(11)

        self.horizontalLayout.addWidget(self.comboBoxPositionFilter)

        self.checkBoxHideSigned = QCheckBox(self.centralwidget)
        self.checkBoxHideSigned.setObjectName(u"checkBoxHideSigned")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBoxHideSigned.sizePolicy().hasHeightForWidth())
        self.checkBoxHideSigned.setSizePolicy(sizePolicy2)
        self.checkBoxHideSigned.setMaximumSize(QSize(100, 16777215))
        self.checkBoxHideSigned.setFont(font)

        self.horizontalLayout.addWidget(self.checkBoxHideSigned)

        self.checkBoxUndecided = QCheckBox(self.centralwidget)
        self.checkBoxUndecided.setObjectName(u"checkBoxUndecided")
        self.checkBoxUndecided.setMaximumSize(QSize(100, 16777215))
        self.checkBoxUndecided.setFont(font)

        self.horizontalLayout.addWidget(self.checkBoxUndecided)

        self.checkBoxWatched = QCheckBox(self.centralwidget)
        self.checkBoxWatched.setObjectName(u"checkBoxWatched")

        self.horizontalLayout.addWidget(self.checkBoxWatched)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setMaximumSize(QSize(50, 16777215))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.comboBoxMilesFilter = QComboBox(self.centralwidget)
        self.comboBoxMilesFilter.addItem("")
        self.comboBoxMilesFilter.addItem("")
        self.comboBoxMilesFilter.addItem("")
        self.comboBoxMilesFilter.addItem("")
        self.comboBoxMilesFilter.setObjectName(u"comboBoxMilesFilter")
        sizePolicy1.setHeightForWidth(self.comboBoxMilesFilter.sizePolicy().hasHeightForWidth())
        self.comboBoxMilesFilter.setSizePolicy(sizePolicy1)
        self.comboBoxMilesFilter.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxMilesFilter)

        self.label_DivisionFilter = QLabel(self.centralwidget)
        self.label_DivisionFilter.setObjectName(u"label_DivisionFilter")
        sizePolicy.setHeightForWidth(self.label_DivisionFilter.sizePolicy().hasHeightForWidth())
        self.label_DivisionFilter.setSizePolicy(sizePolicy)
        self.label_DivisionFilter.setMinimumSize(QSize(50, 0))
        self.label_DivisionFilter.setMaximumSize(QSize(50, 16777215))
        self.label_DivisionFilter.setFont(font)
        self.label_DivisionFilter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_DivisionFilter)

        self.comboBoxDivisionFilter = QComboBox(self.centralwidget)
        self.comboBoxDivisionFilter.addItem("")
        self.comboBoxDivisionFilter.addItem("")
        self.comboBoxDivisionFilter.addItem("")
        self.comboBoxDivisionFilter.addItem("")
        self.comboBoxDivisionFilter.addItem("")
        self.comboBoxDivisionFilter.setObjectName(u"comboBoxDivisionFilter")
        self.comboBoxDivisionFilter.setFont(font)

        self.horizontalLayout.addWidget(self.comboBoxDivisionFilter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonDonatePayPal = QPushButton(self.centralwidget)
        self.pushButtonDonatePayPal.setObjectName(u"pushButtonDonatePayPal")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.pushButtonDonatePayPal.setFont(font1)
        self.pushButtonDonatePayPal.setStyleSheet(u"color: white;\n"
"background-color: green;")

        self.horizontalLayout.addWidget(self.pushButtonDonatePayPal)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.lineEditfilterBLK = QLineEdit(self.centralwidget)
        self.lineEditfilterBLK.setObjectName(u"lineEditfilterBLK")
        self.lineEditfilterBLK.setFont(font)

        self.gridLayout.addWidget(self.lineEditfilterBLK, 1, 7, 1, 1)

        self.lineEditfilterTEC = QLineEdit(self.centralwidget)
        self.lineEditfilterTEC.setObjectName(u"lineEditfilterTEC")
        self.lineEditfilterTEC.setFont(font)

        self.gridLayout.addWidget(self.lineEditfilterTEC, 1, 12, 1, 1)

        self.pushButtonApplyRatingsFilters = QPushButton(self.centralwidget)
        self.pushButtonApplyRatingsFilters.setObjectName(u"pushButtonApplyRatingsFilters")
        self.pushButtonApplyRatingsFilters.setFont(font)

        self.gridLayout.addWidget(self.pushButtonApplyRatingsFilters, 1, 14, 1, 1)

        self.labelfilterBLK = QLabel(self.centralwidget)
        self.labelfilterBLK.setObjectName(u"labelfilterBLK")
        self.labelfilterBLK.setFont(font)
        self.labelfilterBLK.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterBLK, 0, 7, 1, 1)

        self.lineEditfilterGI = QLineEdit(self.centralwidget)
        self.lineEditfilterGI.setObjectName(u"lineEditfilterGI")
        self.lineEditfilterGI.setFont(font)

        self.gridLayout.addWidget(self.lineEditfilterGI, 1, 10, 1, 1)

        self.lineEditfilterSTR = QLineEdit(self.centralwidget)
        self.lineEditfilterSTR.setObjectName(u"lineEditfilterSTR")
        self.lineEditfilterSTR.setFont(font)

        self.gridLayout.addWidget(self.lineEditfilterSTR, 1, 6, 1, 1)

        self.lineEditfilterDUR = QLineEdit(self.centralwidget)
        self.lineEditfilterDUR.setObjectName(u"lineEditfilterDUR")
        self.lineEditfilterDUR.setFont(font)

        self.gridLayout.addWidget(self.lineEditfilterDUR, 1, 3, 1, 1)

        self.lineEditfilterATH = QLineEdit(self.centralwidget)
        self.lineEditfilterATH.setObjectName(u"lineEditfilterATH")
        self.lineEditfilterATH.setFont(font)

        self.gridLayout.addWidget(self.lineEditfilterATH, 1, 1, 1, 1)

        self.labelfilterHAN = QLabel(self.centralwidget)
        self.labelfilterHAN.setObjectName(u"labelfilterHAN")
        self.labelfilterHAN.setFont(font)
        self.labelfilterHAN.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterHAN, 0, 9, 1, 1)

        self.pushButtonClearRatingsFilters = QPushButton(self.centralwidget)
        self.pushButtonClearRatingsFilters.setObjectName(u"pushButtonClearRatingsFilters")
        self.pushButtonClearRatingsFilters.setFont(font)

        self.gridLayout.addWidget(self.pushButtonClearRatingsFilters, 0, 14, 1, 1)

        self.lineEditfilterTKL = QLineEdit(self.centralwidget)
        self.lineEditfilterTKL.setObjectName(u"lineEditfilterTKL")
        self.lineEditfilterTKL.setFont(font)

        self.gridLayout.addWidget(self.lineEditfilterTKL, 1, 8, 1, 1)

        self.labelfilterGI = QLabel(self.centralwidget)
        self.labelfilterGI.setObjectName(u"labelfilterGI")
        self.labelfilterGI.setFont(font)
        self.labelfilterGI.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterGI, 0, 10, 1, 1)

        self.lineEditConsideringTextSearch = QLineEdit(self.centralwidget)
        self.lineEditConsideringTextSearch.setObjectName(u"lineEditConsideringTextSearch")
        sizePolicy2.setHeightForWidth(self.lineEditConsideringTextSearch.sizePolicy().hasHeightForWidth())
        self.lineEditConsideringTextSearch.setSizePolicy(sizePolicy2)
        self.lineEditConsideringTextSearch.setMinimumSize(QSize(100, 0))
        self.lineEditConsideringTextSearch.setMaximumSize(QSize(200, 16777215))
        self.lineEditConsideringTextSearch.setFont(font)

        self.gridLayout.addWidget(self.lineEditConsideringTextSearch, 1, 0, 1, 1)

        self.labelfilterSTR = QLabel(self.centralwidget)
        self.labelfilterSTR.setObjectName(u"labelfilterSTR")
        self.labelfilterSTR.setFont(font)
        self.labelfilterSTR.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterSTR, 0, 6, 1, 1)

        self.lineEditfilterSTA = QLineEdit(self.centralwidget)
        self.lineEditfilterSTA.setObjectName(u"lineEditfilterSTA")
        self.lineEditfilterSTA.setFont(font)

        self.gridLayout.addWidget(self.lineEditfilterSTA, 1, 5, 1, 1)

        self.lineEditfilterELU = QLineEdit(self.centralwidget)
        self.lineEditfilterELU.setObjectName(u"lineEditfilterELU")
        self.lineEditfilterELU.setFont(font)

        self.gridLayout.addWidget(self.lineEditfilterELU, 1, 11, 1, 1)

        self.labelfilterELU = QLabel(self.centralwidget)
        self.labelfilterELU.setObjectName(u"labelfilterELU")
        self.labelfilterELU.setFont(font)
        self.labelfilterELU.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterELU, 0, 11, 1, 1)

        self.labelfilterDUR = QLabel(self.centralwidget)
        self.labelfilterDUR.setObjectName(u"labelfilterDUR")
        self.labelfilterDUR.setFont(font)
        self.labelfilterDUR.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterDUR, 0, 3, 1, 1)

        self.lineEditfilterHAN = QLineEdit(self.centralwidget)
        self.lineEditfilterHAN.setObjectName(u"lineEditfilterHAN")
        self.lineEditfilterHAN.setFont(font)

        self.gridLayout.addWidget(self.lineEditfilterHAN, 1, 9, 1, 1)

        self.labelfilterTEC = QLabel(self.centralwidget)
        self.labelfilterTEC.setObjectName(u"labelfilterTEC")
        self.labelfilterTEC.setFont(font)
        self.labelfilterTEC.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterTEC, 0, 12, 1, 1)

        self.labelfilterTKL = QLabel(self.centralwidget)
        self.labelfilterTKL.setObjectName(u"labelfilterTKL")
        self.labelfilterTKL.setFont(font)
        self.labelfilterTKL.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterTKL, 0, 8, 1, 1)

        self.labelfilterATH = QLabel(self.centralwidget)
        self.labelfilterATH.setObjectName(u"labelfilterATH")
        self.labelfilterATH.setFont(font)
        self.labelfilterATH.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterATH, 0, 1, 1, 1)

        self.labelfilterSPD = QLabel(self.centralwidget)
        self.labelfilterSPD.setObjectName(u"labelfilterSPD")
        self.labelfilterSPD.setFont(font)
        self.labelfilterSPD.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterSPD, 0, 2, 1, 1)

        self.labelConsideringTextSearch = QLabel(self.centralwidget)
        self.labelConsideringTextSearch.setObjectName(u"labelConsideringTextSearch")
        self.labelConsideringTextSearch.setMinimumSize(QSize(100, 0))
        self.labelConsideringTextSearch.setMaximumSize(QSize(100, 16777215))
        self.labelConsideringTextSearch.setFont(font)

        self.gridLayout.addWidget(self.labelConsideringTextSearch, 0, 0, 1, 1)

        self.lineEditfilterWE = QLineEdit(self.centralwidget)
        self.lineEditfilterWE.setObjectName(u"lineEditfilterWE")
        self.lineEditfilterWE.setFont(font)

        self.gridLayout.addWidget(self.lineEditfilterWE, 1, 4, 1, 1)

        self.lineEditfilterSPD = QLineEdit(self.centralwidget)
        self.lineEditfilterSPD.setObjectName(u"lineEditfilterSPD")
        self.lineEditfilterSPD.setFont(font)

        self.gridLayout.addWidget(self.lineEditfilterSPD, 1, 2, 1, 1)

        self.labelfilterWE = QLabel(self.centralwidget)
        self.labelfilterWE.setObjectName(u"labelfilterWE")
        self.labelfilterWE.setFont(font)
        self.labelfilterWE.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterWE, 0, 4, 1, 1)

        self.labelfilterSTA = QLabel(self.centralwidget)
        self.labelfilterSTA.setObjectName(u"labelfilterSTA")
        self.labelfilterSTA.setFont(font)
        self.labelfilterSTA.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterSTA, 0, 5, 1, 1)

        self.labelfilterGPA = QLabel(self.centralwidget)
        self.labelfilterGPA.setObjectName(u"labelfilterGPA")
        self.labelfilterGPA.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterGPA, 0, 13, 1, 1)

        self.lineEditfilterGPA = QLineEdit(self.centralwidget)
        self.lineEditfilterGPA.setObjectName(u"lineEditfilterGPA")

        self.gridLayout.addWidget(self.lineEditfilterGPA, 1, 13, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.recruit_tableView = QTableView(self.centralwidget)
        self.recruit_tableView.setObjectName(u"recruit_tableView")
        self.recruit_tableView.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.recruit_tableView.sizePolicy().hasHeightForWidth())
        self.recruit_tableView.setSizePolicy(sizePolicy3)
        self.recruit_tableView.setFont(font)
        self.recruit_tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.recruit_tableView.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.recruit_tableView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1169, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menudata = QMenu(self.menubar)
        self.menudata.setObjectName(u"menudata")
        self.menuExport_to_CSV = QMenu(self.menudata)
        self.menuExport_to_CSV.setObjectName(u"menuExport_to_CSV")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.comboBoxPositionFilter, self.checkBoxHideSigned)
        QWidget.setTabOrder(self.checkBoxHideSigned, self.checkBoxUndecided)
        QWidget.setTabOrder(self.checkBoxUndecided, self.checkBoxWatched)
        QWidget.setTabOrder(self.checkBoxWatched, self.comboBoxMilesFilter)
        QWidget.setTabOrder(self.comboBoxMilesFilter, self.comboBoxDivisionFilter)
        QWidget.setTabOrder(self.comboBoxDivisionFilter, self.lineEditConsideringTextSearch)
        QWidget.setTabOrder(self.lineEditConsideringTextSearch, self.lineEditfilterATH)
        QWidget.setTabOrder(self.lineEditfilterATH, self.lineEditfilterSPD)
        QWidget.setTabOrder(self.lineEditfilterSPD, self.lineEditfilterDUR)
        QWidget.setTabOrder(self.lineEditfilterDUR, self.lineEditfilterWE)
        QWidget.setTabOrder(self.lineEditfilterWE, self.lineEditfilterSTA)
        QWidget.setTabOrder(self.lineEditfilterSTA, self.lineEditfilterSTR)
        QWidget.setTabOrder(self.lineEditfilterSTR, self.lineEditfilterBLK)
        QWidget.setTabOrder(self.lineEditfilterBLK, self.lineEditfilterTKL)
        QWidget.setTabOrder(self.lineEditfilterTKL, self.lineEditfilterHAN)
        QWidget.setTabOrder(self.lineEditfilterHAN, self.lineEditfilterGI)
        QWidget.setTabOrder(self.lineEditfilterGI, self.lineEditfilterELU)
        QWidget.setTabOrder(self.lineEditfilterELU, self.lineEditfilterTEC)
        QWidget.setTabOrder(self.lineEditfilterTEC, self.lineEditfilterGPA)
        QWidget.setTabOrder(self.lineEditfilterGPA, self.pushButtonApplyRatingsFilters)
        QWidget.setTabOrder(self.pushButtonApplyRatingsFilters, self.pushButtonClearRatingsFilters)
        QWidget.setTabOrder(self.pushButtonClearRatingsFilters, self.pushButtonDonatePayPal)
        QWidget.setTabOrder(self.pushButtonDonatePayPal, self.recruit_tableView)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menudata.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionWIS_Credentials)
        self.menuFile.addAction(self.actionNew_Season)
        self.menuFile.addAction(self.actionLoad_Season)
        self.menudata.addAction(self.actionGrabSeasonData)
        self.menudata.addAction(self.menuExport_to_CSV.menuAction())
        self.menuExport_to_CSV.addAction(self.actionAll_Recruits)
        self.menuExport_to_CSV.addAction(self.actionWatchlist_Only)
        self.menuOptions.addAction(self.actionBold_Attributes)
        self.menuOptions.addAction(self.actionRole_Ratings)
        self.menuOptions.addAction(self.actionShow_Columns)
        self.menuOptions.addAction(self.actionAdvanced)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GD Recruit Assistant", None))
        self.actionNew_Season.setText(QCoreApplication.translate("MainWindow", u"New Season", None))
        self.actionLoad_Season.setText(QCoreApplication.translate("MainWindow", u"Load Season", None))
        self.actionGrabSeasonData.setText(QCoreApplication.translate("MainWindow", u"Grab Recruit Data", None))
        self.actionWIS_Credentials.setText(QCoreApplication.translate("MainWindow", u"WIS Credentials", None))
        self.actionBold_Attributes.setText(QCoreApplication.translate("MainWindow", u"Bold Attributes", None))
        self.actionRole_Ratings.setText(QCoreApplication.translate("MainWindow", u"Role Ratings", None))
        self.actionAll_Recruits.setText(QCoreApplication.translate("MainWindow", u"All Recruits", None))
        self.actionWatchlist_Only.setText(QCoreApplication.translate("MainWindow", u"Watchlist Only", None))
        self.actionAdvanced.setText(QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionShow_Columns.setText(QCoreApplication.translate("MainWindow", u"Show Columns", None))
        self.labelPositionFilter.setText(QCoreApplication.translate("MainWindow", u"Pos:", None))
        self.comboBoxPositionFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"ALL", None))
        self.comboBoxPositionFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"QB", None))
        self.comboBoxPositionFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"RB", None))
        self.comboBoxPositionFilter.setItemText(3, QCoreApplication.translate("MainWindow", u"WR", None))
        self.comboBoxPositionFilter.setItemText(4, QCoreApplication.translate("MainWindow", u"TE", None))
        self.comboBoxPositionFilter.setItemText(5, QCoreApplication.translate("MainWindow", u"OL", None))
        self.comboBoxPositionFilter.setItemText(6, QCoreApplication.translate("MainWindow", u"DL", None))
        self.comboBoxPositionFilter.setItemText(7, QCoreApplication.translate("MainWindow", u"LB", None))
        self.comboBoxPositionFilter.setItemText(8, QCoreApplication.translate("MainWindow", u"DB", None))
        self.comboBoxPositionFilter.setItemText(9, QCoreApplication.translate("MainWindow", u"K", None))
        self.comboBoxPositionFilter.setItemText(10, QCoreApplication.translate("MainWindow", u"P", None))

#if QT_CONFIG(tooltip)
        self.comboBoxPositionFilter.setToolTip(QCoreApplication.translate("MainWindow", u"Position Filter", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxHideSigned.setText(QCoreApplication.translate("MainWindow", u"Hide Signed", None))
        self.checkBoxUndecided.setText(QCoreApplication.translate("MainWindow", u"Undecided", None))
        self.checkBoxWatched.setText(QCoreApplication.translate("MainWindow", u"Watched", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Miles <", None))
        self.comboBoxMilesFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"Any", None))
        self.comboBoxMilesFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"180", None))
        self.comboBoxMilesFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"360", None))
        self.comboBoxMilesFilter.setItemText(3, QCoreApplication.translate("MainWindow", u"1400", None))

        self.label_DivisionFilter.setText(QCoreApplication.translate("MainWindow", u"Division", None))
        self.comboBoxDivisionFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.comboBoxDivisionFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"D-IA", None))
        self.comboBoxDivisionFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"D-IAA", None))
        self.comboBoxDivisionFilter.setItemText(3, QCoreApplication.translate("MainWindow", u"D-II", None))
        self.comboBoxDivisionFilter.setItemText(4, QCoreApplication.translate("MainWindow", u"D-III", None))

#if QT_CONFIG(tooltip)
        self.pushButtonDonatePayPal.setToolTip(QCoreApplication.translate("MainWindow", u"PayPal Donation Link", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonDonatePayPal.setText(QCoreApplication.translate("MainWindow", u"Donate $", None))
        self.pushButtonApplyRatingsFilters.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
#if QT_CONFIG(shortcut)
        self.pushButtonApplyRatingsFilters.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.labelfilterBLK.setText(QCoreApplication.translate("MainWindow", u"BLK >=", None))
        self.labelfilterHAN.setText(QCoreApplication.translate("MainWindow", u"HAN >=", None))
        self.pushButtonClearRatingsFilters.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.labelfilterGI.setText(QCoreApplication.translate("MainWindow", u"GI >=", None))
        self.labelfilterSTR.setText(QCoreApplication.translate("MainWindow", u"STR >=", None))
        self.labelfilterELU.setText(QCoreApplication.translate("MainWindow", u"ELU >=", None))
        self.labelfilterDUR.setText(QCoreApplication.translate("MainWindow", u"DUR >=", None))
        self.labelfilterTEC.setText(QCoreApplication.translate("MainWindow", u"TEC >=", None))
        self.labelfilterTKL.setText(QCoreApplication.translate("MainWindow", u"TKL >=", None))
        self.labelfilterATH.setText(QCoreApplication.translate("MainWindow", u"ATH >=", None))
        self.labelfilterSPD.setText(QCoreApplication.translate("MainWindow", u"SPD >=", None))
        self.labelConsideringTextSearch.setText(QCoreApplication.translate("MainWindow", u"Considering Search:", None))
        self.labelfilterWE.setText(QCoreApplication.translate("MainWindow", u"WE >=", None))
        self.labelfilterSTA.setText(QCoreApplication.translate("MainWindow", u"STA >=", None))
        self.labelfilterGPA.setText(QCoreApplication.translate("MainWindow", u"GPA >=", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menudata.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.menuExport_to_CSV.setTitle(QCoreApplication.translate("MainWindow", u"Export to CSV", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

