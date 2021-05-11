from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from loguru import logger
import mypackages.config as myconfig

# WARNING!!!
# Pasting new code from Designer, need to make sure you replace check mark and X icons!

class Ui_WidgetGrabSeasonData(object):
    def setupUi(self, WidgetGrabSeasonData):
        if not WidgetGrabSeasonData.objectName():
            WidgetGrabSeasonData.setObjectName(u"WidgetGrabSeasonData")
        WidgetGrabSeasonData.setWindowModality(Qt.ApplicationModal)
        WidgetGrabSeasonData.resize(534, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetGrabSeasonData.sizePolicy().hasHeightForWidth())
        WidgetGrabSeasonData.setSizePolicy(sizePolicy)
        WidgetGrabSeasonData.setMinimumSize(QSize(534, 450))
        WidgetGrabSeasonData.setMaximumSize(QSize(534, 450))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        WidgetGrabSeasonData.setFont(font)
        self.gridLayout_2 = QGridLayout(WidgetGrabSeasonData)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelGrabUnsigned = QLabel(WidgetGrabSeasonData)
        self.labelGrabUnsigned.setObjectName(u"labelGrabUnsigned")
        sizePolicy.setHeightForWidth(self.labelGrabUnsigned.sizePolicy().hasHeightForWidth())
        self.labelGrabUnsigned.setSizePolicy(sizePolicy)
        self.labelGrabUnsigned.setMinimumSize(QSize(350, 20))
        self.labelGrabUnsigned.setMaximumSize(QSize(350, 20))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.labelGrabUnsigned.setFont(font1)

        self.gridLayout.addWidget(self.labelGrabUnsigned, 7, 3, 1, 1)

        self.labelCheckMarkAuthWIS_Error = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkAuthWIS_Error.setObjectName(u"labelCheckMarkAuthWIS_Error")
        sizePolicy.setHeightForWidth(self.labelCheckMarkAuthWIS_Error.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkAuthWIS_Error.setSizePolicy(sizePolicy)
        self.labelCheckMarkAuthWIS_Error.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS_Error.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS_Error.setPixmap(QPixmap(myconfig.x_icon))
        self.labelCheckMarkAuthWIS_Error.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkAuthWIS_Error, 5, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 13, 0, 1, 1)

        self.labelCheckMarkGrabUnsigned = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkGrabUnsigned.setObjectName(u"labelCheckMarkGrabUnsigned")
        sizePolicy.setHeightForWidth(self.labelCheckMarkGrabUnsigned.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkGrabUnsigned.setSizePolicy(sizePolicy)
        self.labelCheckMarkGrabUnsigned.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkGrabUnsigned.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkGrabUnsigned.setPixmap(QPixmap(myconfig.checkmarkicon))
        self.labelCheckMarkGrabUnsigned.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkGrabUnsigned, 7, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_8, 7, 0, 1, 1)

        self.labelCheckMarkCreateDB = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkCreateDB.setObjectName(u"labelCheckMarkCreateDB")
        sizePolicy.setHeightForWidth(self.labelCheckMarkCreateDB.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkCreateDB.setSizePolicy(sizePolicy)
        self.labelCheckMarkCreateDB.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkCreateDB.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkCreateDB.setLayoutDirection(Qt.LeftToRight)
        self.labelCheckMarkCreateDB.setPixmap(QPixmap(myconfig.checkmarkicon))
        self.labelCheckMarkCreateDB.setScaledContents(True)
        self.labelCheckMarkCreateDB.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelCheckMarkCreateDB.setIndent(-1)

        self.gridLayout.addWidget(self.labelCheckMarkCreateDB, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_7, 5, 0, 1, 1)

        self.labelGrabSigned = QLabel(WidgetGrabSeasonData)
        self.labelGrabSigned.setObjectName(u"labelGrabSigned")
        sizePolicy.setHeightForWidth(self.labelGrabSigned.sizePolicy().hasHeightForWidth())
        self.labelGrabSigned.setSizePolicy(sizePolicy)
        self.labelGrabSigned.setMinimumSize(QSize(350, 20))
        self.labelGrabSigned.setMaximumSize(QSize(350, 20))
        self.labelGrabSigned.setFont(font1)

        self.gridLayout.addWidget(self.labelGrabSigned, 8, 3, 1, 1)

        self.pushButtonInitializeRecruits = QPushButton(WidgetGrabSeasonData)
        self.pushButtonInitializeRecruits.setObjectName(u"pushButtonInitializeRecruits")
        sizePolicy.setHeightForWidth(self.pushButtonInitializeRecruits.sizePolicy().hasHeightForWidth())
        self.pushButtonInitializeRecruits.setSizePolicy(sizePolicy)
        self.pushButtonInitializeRecruits.setMinimumSize(QSize(350, 35))
        self.pushButtonInitializeRecruits.setMaximumSize(QSize(350, 35))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(18)
        self.pushButtonInitializeRecruits.setFont(font2)

        self.gridLayout.addWidget(self.pushButtonInitializeRecruits, 1, 3, 1, 1)

        self.buttonBox = QDialogButtonBox(WidgetGrabSeasonData)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font1)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 14, 0, 1, 5)

        self.checkBoxGrabHigherRecruits = QCheckBox(WidgetGrabSeasonData)
        self.checkBoxGrabHigherRecruits.setObjectName(u"checkBoxGrabHigherRecruits")
        sizePolicy.setHeightForWidth(self.checkBoxGrabHigherRecruits.sizePolicy().hasHeightForWidth())
        self.checkBoxGrabHigherRecruits.setSizePolicy(sizePolicy)
        self.checkBoxGrabHigherRecruits.setMinimumSize(QSize(350, 25))
        self.checkBoxGrabHigherRecruits.setMaximumSize(QSize(350, 25))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(8)
        self.checkBoxGrabHigherRecruits.setFont(font3)
        self.checkBoxGrabHigherRecruits.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.checkBoxGrabHigherRecruits, 2, 3, 1, 1)

        self.labelRecruitsInitialized = QLabel(WidgetGrabSeasonData)
        self.labelRecruitsInitialized.setObjectName(u"labelRecruitsInitialized")
        sizePolicy.setHeightForWidth(self.labelRecruitsInitialized.sizePolicy().hasHeightForWidth())
        self.labelRecruitsInitialized.setSizePolicy(sizePolicy)
        self.labelRecruitsInitialized.setMinimumSize(QSize(350, 25))
        self.labelRecruitsInitialized.setMaximumSize(QSize(350, 25))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(16)
        self.labelRecruitsInitialized.setFont(font4)
        self.labelRecruitsInitialized.setStyleSheet(u"color: rgb(255, 20, 20);")
        self.labelRecruitsInitialized.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelRecruitsInitialized, 0, 3, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_11, 10, 0, 1, 1)

        self.labelCheckMarkAuthWIS = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkAuthWIS.setObjectName(u"labelCheckMarkAuthWIS")
        sizePolicy.setHeightForWidth(self.labelCheckMarkAuthWIS.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkAuthWIS.setSizePolicy(sizePolicy)
        self.labelCheckMarkAuthWIS.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS.setPixmap(QPixmap(myconfig.checkmarkicon))
        self.labelCheckMarkAuthWIS.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkAuthWIS, 5, 2, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_18, 2, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.progressBarInitializeRecruits = QProgressBar(WidgetGrabSeasonData)
        self.progressBarInitializeRecruits.setObjectName(u"progressBarInitializeRecruits")
        sizePolicy.setHeightForWidth(self.progressBarInitializeRecruits.sizePolicy().hasHeightForWidth())
        self.progressBarInitializeRecruits.setSizePolicy(sizePolicy)
        self.progressBarInitializeRecruits.setMinimumSize(QSize(350, 25))
        self.progressBarInitializeRecruits.setMaximumSize(QSize(350, 25))
        self.progressBarInitializeRecruits.setFont(font)
        self.progressBarInitializeRecruits.setStyleSheet(u"")
        self.progressBarInitializeRecruits.setValue(24)
        self.progressBarInitializeRecruits.setTextVisible(True)

        self.gridLayout.addWidget(self.progressBarInitializeRecruits, 10, 3, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_10, 9, 0, 1, 1)

        self.labelAuthWIS = QLabel(WidgetGrabSeasonData)
        self.labelAuthWIS.setObjectName(u"labelAuthWIS")
        sizePolicy.setHeightForWidth(self.labelAuthWIS.sizePolicy().hasHeightForWidth())
        self.labelAuthWIS.setSizePolicy(sizePolicy)
        self.labelAuthWIS.setMinimumSize(QSize(350, 20))
        self.labelAuthWIS.setMaximumSize(QSize(350, 20))
        self.labelAuthWIS.setFont(font1)

        self.gridLayout.addWidget(self.labelAuthWIS, 5, 3, 1, 1)

        self.labelCheckMarkGrabStaticData = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkGrabStaticData.setObjectName(u"labelCheckMarkGrabStaticData")
        sizePolicy.setHeightForWidth(self.labelCheckMarkGrabStaticData.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkGrabStaticData.setSizePolicy(sizePolicy)
        self.labelCheckMarkGrabStaticData.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkGrabStaticData.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkGrabStaticData.setPixmap(QPixmap(myconfig.checkmarkicon))
        self.labelCheckMarkGrabStaticData.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkGrabStaticData, 9, 2, 1, 1)

        self.labelCheckMarkGrabSigned = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkGrabSigned.setObjectName(u"labelCheckMarkGrabSigned")
        sizePolicy.setHeightForWidth(self.labelCheckMarkGrabSigned.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkGrabSigned.setSizePolicy(sizePolicy)
        self.labelCheckMarkGrabSigned.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkGrabSigned.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkGrabSigned.setPixmap(QPixmap(myconfig.checkmarkicon))
        self.labelCheckMarkGrabSigned.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkGrabSigned, 8, 2, 1, 1)

        self.labelProgressCreateRecruitDB = QLabel(WidgetGrabSeasonData)
        self.labelProgressCreateRecruitDB.setObjectName(u"labelProgressCreateRecruitDB")
        sizePolicy.setHeightForWidth(self.labelProgressCreateRecruitDB.sizePolicy().hasHeightForWidth())
        self.labelProgressCreateRecruitDB.setSizePolicy(sizePolicy)
        self.labelProgressCreateRecruitDB.setMinimumSize(QSize(350, 20))
        self.labelProgressCreateRecruitDB.setMaximumSize(QSize(350, 20))
        self.labelProgressCreateRecruitDB.setFont(font1)

        self.gridLayout.addWidget(self.labelProgressCreateRecruitDB, 3, 3, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_9, 8, 0, 1, 1)

        self.labelGrabStaticData = QLabel(WidgetGrabSeasonData)
        self.labelGrabStaticData.setObjectName(u"labelGrabStaticData")
        sizePolicy.setHeightForWidth(self.labelGrabStaticData.sizePolicy().hasHeightForWidth())
        self.labelGrabStaticData.setSizePolicy(sizePolicy)
        self.labelGrabStaticData.setMinimumSize(QSize(350, 20))
        self.labelGrabStaticData.setMaximumSize(QSize(350, 20))
        self.labelGrabStaticData.setFont(font1)

        self.gridLayout.addWidget(self.labelGrabStaticData, 9, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 11, 0, 1, 1)

        self.line = QFrame(WidgetGrabSeasonData)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 12, 2, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        QWidget.setTabOrder(self.pushButtonInitializeRecruits, self.checkBoxGrabHigherRecruits)

        self.retranslateUi(WidgetGrabSeasonData)
        self.buttonBox.accepted.connect(WidgetGrabSeasonData.close)

        QMetaObject.connectSlotsByName(WidgetGrabSeasonData)
    # setupUi

    def retranslateUi(self, WidgetGrabSeasonData):
        WidgetGrabSeasonData.setWindowTitle(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Recruit Data", None))
        self.labelGrabUnsigned.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Unsigned Recruits", None))
        self.labelCheckMarkAuthWIS_Error.setText("")
        self.labelCheckMarkGrabUnsigned.setText("")
        self.labelCheckMarkCreateDB.setText("")
        self.labelGrabSigned.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Signed Recruits", None))
        self.pushButtonInitializeRecruits.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Initialize Recruits", None))
        self.checkBoxGrabHigherRecruits.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab recruits from 1 division higher (valid for DIII, DII, DIAA only)", None))
        self.labelRecruitsInitialized.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Recruits Initialized = 0", None))
        self.labelCheckMarkAuthWIS.setText("")
        self.labelAuthWIS.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Authenticate to WIS - Gridiron Dynasty", None))
        self.labelCheckMarkGrabStaticData.setText("")
        self.labelCheckMarkGrabSigned.setText("")
        self.labelProgressCreateRecruitDB.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Create / Re-create Recruit Database Table", None))
        self.labelGrabStaticData.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Recruit Static Ratings Data and GPA", None))
    # retranslateUi



