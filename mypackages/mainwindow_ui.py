from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1169, 1265)
        self.actionNew_Season = QAction(MainWindow)
        self.actionNew_Season.setObjectName(u"actionNew_Season")
        self.actionLoad_Season = QAction(MainWindow)
        self.actionLoad_Season.setObjectName(u"actionLoad_Season")
        self.actionGrabSeasonData = QAction(MainWindow)
        self.actionGrabSeasonData.setObjectName(u"actionGrabSeasonData")
        self.actionGrabSeasonData.setEnabled(False)
        self.actionWIS_Credentials = QAction(MainWindow)
        self.actionWIS_Credentials.setObjectName(u"actionWIS_Credentials")
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

        self.horizontalLayout.addWidget(self.checkBoxHideSigned)

        self.checkBoxUndecided = QCheckBox(self.centralwidget)
        self.checkBoxUndecided.setObjectName(u"checkBoxUndecided")
        self.checkBoxUndecided.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.checkBoxUndecided)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setMaximumSize(QSize(50, 16777215))
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

        self.horizontalLayout.addWidget(self.comboBoxMilesFilter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.lineEditfilterDUR = QLineEdit(self.centralwidget)
        self.lineEditfilterDUR.setObjectName(u"lineEditfilterDUR")

        self.gridLayout.addWidget(self.lineEditfilterDUR, 1, 3, 1, 1)

        self.labelfilterGI = QLabel(self.centralwidget)
        self.labelfilterGI.setObjectName(u"labelfilterGI")
        self.labelfilterGI.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterGI, 0, 10, 1, 1)

        self.lineEditfilterHAN = QLineEdit(self.centralwidget)
        self.lineEditfilterHAN.setObjectName(u"lineEditfilterHAN")

        self.gridLayout.addWidget(self.lineEditfilterHAN, 1, 9, 1, 1)

        self.pushButtonApplyRatingsFilters = QPushButton(self.centralwidget)
        self.pushButtonApplyRatingsFilters.setObjectName(u"pushButtonApplyRatingsFilters")

        self.gridLayout.addWidget(self.pushButtonApplyRatingsFilters, 1, 13, 1, 1)

        self.labelfilterBLK = QLabel(self.centralwidget)
        self.labelfilterBLK.setObjectName(u"labelfilterBLK")
        self.labelfilterBLK.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterBLK, 0, 7, 1, 1)

        self.labelfilterSTR = QLabel(self.centralwidget)
        self.labelfilterSTR.setObjectName(u"labelfilterSTR")
        self.labelfilterSTR.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterSTR, 0, 6, 1, 1)

        self.lineEditfilterELU = QLineEdit(self.centralwidget)
        self.lineEditfilterELU.setObjectName(u"lineEditfilterELU")

        self.gridLayout.addWidget(self.lineEditfilterELU, 1, 11, 1, 1)

        self.lineEditfilterGI = QLineEdit(self.centralwidget)
        self.lineEditfilterGI.setObjectName(u"lineEditfilterGI")

        self.gridLayout.addWidget(self.lineEditfilterGI, 1, 10, 1, 1)

        self.lineEditfilterBLK = QLineEdit(self.centralwidget)
        self.lineEditfilterBLK.setObjectName(u"lineEditfilterBLK")

        self.gridLayout.addWidget(self.lineEditfilterBLK, 1, 7, 1, 1)

        self.labelfilterWE = QLabel(self.centralwidget)
        self.labelfilterWE.setObjectName(u"labelfilterWE")
        self.labelfilterWE.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterWE, 0, 4, 1, 1)

        self.labelfilterTEC = QLabel(self.centralwidget)
        self.labelfilterTEC.setObjectName(u"labelfilterTEC")
        self.labelfilterTEC.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterTEC, 0, 12, 1, 1)

        self.lineEditfilterWE = QLineEdit(self.centralwidget)
        self.lineEditfilterWE.setObjectName(u"lineEditfilterWE")

        self.gridLayout.addWidget(self.lineEditfilterWE, 1, 4, 1, 1)

        self.labelfilterELU = QLabel(self.centralwidget)
        self.labelfilterELU.setObjectName(u"labelfilterELU")
        self.labelfilterELU.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterELU, 0, 11, 1, 1)

        self.labelfilterDUR = QLabel(self.centralwidget)
        self.labelfilterDUR.setObjectName(u"labelfilterDUR")
        self.labelfilterDUR.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterDUR, 0, 3, 1, 1)

        self.lineEditfilterSTR = QLineEdit(self.centralwidget)
        self.lineEditfilterSTR.setObjectName(u"lineEditfilterSTR")

        self.gridLayout.addWidget(self.lineEditfilterSTR, 1, 6, 1, 1)

        self.lineEditfilterSPD = QLineEdit(self.centralwidget)
        self.lineEditfilterSPD.setObjectName(u"lineEditfilterSPD")

        self.gridLayout.addWidget(self.lineEditfilterSPD, 1, 2, 1, 1)

        self.pushButtonClearRatingsFilters = QPushButton(self.centralwidget)
        self.pushButtonClearRatingsFilters.setObjectName(u"pushButtonClearRatingsFilters")

        self.gridLayout.addWidget(self.pushButtonClearRatingsFilters, 0, 13, 1, 1)

        self.lineEditfilterATH = QLineEdit(self.centralwidget)
        self.lineEditfilterATH.setObjectName(u"lineEditfilterATH")

        self.gridLayout.addWidget(self.lineEditfilterATH, 1, 1, 1, 1)

        self.labelfilterTKL = QLabel(self.centralwidget)
        self.labelfilterTKL.setObjectName(u"labelfilterTKL")
        self.labelfilterTKL.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterTKL, 0, 8, 1, 1)

        self.lineEditfilterSTA = QLineEdit(self.centralwidget)
        self.lineEditfilterSTA.setObjectName(u"lineEditfilterSTA")

        self.gridLayout.addWidget(self.lineEditfilterSTA, 1, 5, 1, 1)

        self.labelfilterATH = QLabel(self.centralwidget)
        self.labelfilterATH.setObjectName(u"labelfilterATH")
        self.labelfilterATH.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterATH, 0, 1, 1, 1)

        self.labelfilterSTA = QLabel(self.centralwidget)
        self.labelfilterSTA.setObjectName(u"labelfilterSTA")
        self.labelfilterSTA.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterSTA, 0, 5, 1, 1)

        self.lineEditfilterTKL = QLineEdit(self.centralwidget)
        self.lineEditfilterTKL.setObjectName(u"lineEditfilterTKL")

        self.gridLayout.addWidget(self.lineEditfilterTKL, 1, 8, 1, 1)

        self.labelfilterHAN = QLabel(self.centralwidget)
        self.labelfilterHAN.setObjectName(u"labelfilterHAN")
        self.labelfilterHAN.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterHAN, 0, 9, 1, 1)

        self.lineEditfilterTEC = QLineEdit(self.centralwidget)
        self.lineEditfilterTEC.setObjectName(u"lineEditfilterTEC")

        self.gridLayout.addWidget(self.lineEditfilterTEC, 1, 12, 1, 1)

        self.labelfilterSPD = QLabel(self.centralwidget)
        self.labelfilterSPD.setObjectName(u"labelfilterSPD")
        self.labelfilterSPD.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelfilterSPD, 0, 2, 1, 1)

        self.labelConsideringTextSearch = QLabel(self.centralwidget)
        self.labelConsideringTextSearch.setObjectName(u"labelConsideringTextSearch")
        self.labelConsideringTextSearch.setMinimumSize(QSize(100, 0))
        self.labelConsideringTextSearch.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.labelConsideringTextSearch, 0, 0, 1, 1)

        self.lineEditConsideringTextSearch = QLineEdit(self.centralwidget)
        self.lineEditConsideringTextSearch.setObjectName(u"lineEditConsideringTextSearch")
        sizePolicy2.setHeightForWidth(self.lineEditConsideringTextSearch.sizePolicy().hasHeightForWidth())
        self.lineEditConsideringTextSearch.setSizePolicy(sizePolicy2)
        self.lineEditConsideringTextSearch.setMinimumSize(QSize(100, 0))
        self.lineEditConsideringTextSearch.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.lineEditConsideringTextSearch, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.recruit_tableView = QTableView(self.centralwidget)
        self.recruit_tableView.setObjectName(u"recruit_tableView")
        self.recruit_tableView.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.recruit_tableView.sizePolicy().hasHeightForWidth())
        self.recruit_tableView.setSizePolicy(sizePolicy3)
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.comboBoxPositionFilter, self.checkBoxHideSigned)
        QWidget.setTabOrder(self.checkBoxHideSigned, self.checkBoxUndecided)
        QWidget.setTabOrder(self.checkBoxUndecided, self.comboBoxMilesFilter)
        QWidget.setTabOrder(self.comboBoxMilesFilter, self.lineEditConsideringTextSearch)
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
        QWidget.setTabOrder(self.lineEditfilterTEC, self.pushButtonClearRatingsFilters)
        QWidget.setTabOrder(self.pushButtonClearRatingsFilters, self.pushButtonApplyRatingsFilters)
        QWidget.setTabOrder(self.pushButtonApplyRatingsFilters, self.recruit_tableView)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menudata.menuAction())
        self.menuFile.addAction(self.actionWIS_Credentials)
        self.menuFile.addAction(self.actionNew_Season)
        self.menuFile.addAction(self.actionLoad_Season)
        self.menudata.addAction(self.actionGrabSeasonData)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GD Recruit Helper", None))
        self.actionNew_Season.setText(QCoreApplication.translate("MainWindow", u"New Season", None))
        self.actionLoad_Season.setText(QCoreApplication.translate("MainWindow", u"Load Season", None))
        self.actionGrabSeasonData.setText(QCoreApplication.translate("MainWindow", u"Grab Season Data", None))
        self.actionWIS_Credentials.setText(QCoreApplication.translate("MainWindow", u"WIS Credentials", None))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Miles <", None))
        self.comboBoxMilesFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"Any", None))
        self.comboBoxMilesFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"180", None))
        self.comboBoxMilesFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"360", None))
        self.comboBoxMilesFilter.setItemText(3, QCoreApplication.translate("MainWindow", u"1400", None))

        self.labelfilterGI.setText(QCoreApplication.translate("MainWindow", u"GI >", None))
        self.pushButtonApplyRatingsFilters.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.labelfilterBLK.setText(QCoreApplication.translate("MainWindow", u"BLK >", None))
        self.labelfilterSTR.setText(QCoreApplication.translate("MainWindow", u"STR >", None))
        self.labelfilterWE.setText(QCoreApplication.translate("MainWindow", u"WE >", None))
        self.labelfilterTEC.setText(QCoreApplication.translate("MainWindow", u"TEC >", None))
        self.labelfilterELU.setText(QCoreApplication.translate("MainWindow", u"ELU >", None))
        self.labelfilterDUR.setText(QCoreApplication.translate("MainWindow", u"DUR >", None))
        self.pushButtonClearRatingsFilters.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.labelfilterTKL.setText(QCoreApplication.translate("MainWindow", u"TKL >", None))
        self.labelfilterATH.setText(QCoreApplication.translate("MainWindow", u"ATH >", None))
        self.labelfilterSTA.setText(QCoreApplication.translate("MainWindow", u"STA >", None))
        self.labelfilterHAN.setText(QCoreApplication.translate("MainWindow", u"HAN >", None))
        self.labelfilterSPD.setText(QCoreApplication.translate("MainWindow", u"SPD >", None))
        self.labelConsideringTextSearch.setText(QCoreApplication.translate("MainWindow", u"Considering Search:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menudata.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
    # retranslateUi