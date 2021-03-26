from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import logging
from pathlib import Path
import sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    checkmarkicon = f"{Path(sys._MEIPASS) / 'images' / 'checkmark_1.png'}"
    #checkmarkicon = f"{sys._MEIPASS}/images/checkmark_1.png"
else:
    checkmarkicon = f"./images/checkmark_1.png"

logging.info(f"Checkmark icon path is = {checkmarkicon}")

class Ui_WidgetGrabSeasonData(object):
    def setupUi(self, WidgetGrabSeasonData):
        if not WidgetGrabSeasonData.objectName():
            WidgetGrabSeasonData.setObjectName(u"WidgetGrabSeasonData")
        WidgetGrabSeasonData.setWindowModality(Qt.ApplicationModal)
        WidgetGrabSeasonData.resize(685, 565)
        self.pushButtonInitializeRecruits = QPushButton(WidgetGrabSeasonData)
        self.pushButtonInitializeRecruits.setObjectName(u"pushButtonInitializeRecruits")
        self.pushButtonInitializeRecruits.setGeometry(QRect(30, 70, 621, 61))
        font = QFont()
        font.setPointSize(24)
        self.pushButtonInitializeRecruits.setFont(font)
        self.pushButtonUpdateConsideringSigned = QPushButton(WidgetGrabSeasonData)
        self.pushButtonUpdateConsideringSigned.setObjectName(u"pushButtonUpdateConsideringSigned")
        self.pushButtonUpdateConsideringSigned.setGeometry(QRect(30, 403, 621, 61))
        self.pushButtonUpdateConsideringSigned.setFont(font)
        self.progressBarInitializeRecruits = QProgressBar(WidgetGrabSeasonData)
        self.progressBarInitializeRecruits.setObjectName(u"progressBarInitializeRecruits")
        self.progressBarInitializeRecruits.setGeometry(QRect(180, 320, 321, 31))
        self.progressBarInitializeRecruits.setValue(24)
        self.progressBarInitializeRecruits.setTextVisible(True)
        self.progressBarUpdateConsidering = QProgressBar(WidgetGrabSeasonData)
        self.progressBarUpdateConsidering.setObjectName(u"progressBarUpdateConsidering")
        self.progressBarUpdateConsidering.setGeometry(QRect(180, 490, 321, 31))
        self.progressBarUpdateConsidering.setStyleSheet(u"")
        self.progressBarUpdateConsidering.setValue(24)
        self.progressBarUpdateConsidering.setTextVisible(True)
        self.labelUpdateProgressBarMax = QLabel(WidgetGrabSeasonData)
        self.labelUpdateProgressBarMax.setObjectName(u"labelUpdateProgressBarMax")
        self.labelUpdateProgressBarMax.setEnabled(True)
        self.labelUpdateProgressBarMax.setGeometry(QRect(510, 498, 81, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.labelUpdateProgressBarMax.setFont(font1)
        self.labelRecruitsInitialized = QLabel(WidgetGrabSeasonData)
        self.labelRecruitsInitialized.setObjectName(u"labelRecruitsInitialized")
        self.labelRecruitsInitialized.setGeometry(QRect(150, 20, 401, 31))
        font2 = QFont()
        font2.setPointSize(16)
        self.labelRecruitsInitialized.setFont(font2)
        self.labelRecruitsInitialized.setStyleSheet(u"color: rgb(255, 20, 20);")
        self.labelRecruitsInitialized.setAlignment(Qt.AlignCenter)
        self.labelProgressCreateRecruitDB = QLabel(WidgetGrabSeasonData)
        self.labelProgressCreateRecruitDB.setObjectName(u"labelProgressCreateRecruitDB")
        self.labelProgressCreateRecruitDB.setGeometry(QRect(250, 161, 221, 16))
        self.labelCheckMarkCreateDB = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkCreateDB.setObjectName(u"labelCheckMarkCreateDB")
        self.labelCheckMarkCreateDB.setGeometry(QRect(220, 160, 21, 21))
        self.labelCheckMarkCreateDB.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkCreateDB.setScaledContents(True)
        self.labelCheckMarkAuthWIS = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkAuthWIS.setObjectName(u"labelCheckMarkAuthWIS")
        self.labelCheckMarkAuthWIS.setGeometry(QRect(220, 190, 21, 21))
        self.labelCheckMarkAuthWIS.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkAuthWIS.setScaledContents(True)
        self.labelAuthWIS = QLabel(WidgetGrabSeasonData)
        self.labelAuthWIS.setObjectName(u"labelAuthWIS")
        self.labelAuthWIS.setGeometry(QRect(250, 190, 221, 16))
        self.labelGrabUnsigned = QLabel(WidgetGrabSeasonData)
        self.labelGrabUnsigned.setObjectName(u"labelGrabUnassigned")
        self.labelGrabUnsigned.setGeometry(QRect(250, 220, 221, 16))
        self.labelCheckMarkGrabUnsigned = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkGrabUnsigned.setObjectName(u"labelCheckMarkGrabUnassigned")
        self.labelCheckMarkGrabUnsigned.setGeometry(QRect(220, 220, 21, 21))
        self.labelCheckMarkGrabUnsigned.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkGrabUnsigned.setScaledContents(True)
        self.labelGrabSigned = QLabel(WidgetGrabSeasonData)
        self.labelGrabSigned.setObjectName(u"labelGrabSigned")
        self.labelGrabSigned.setGeometry(QRect(250, 250, 221, 16))
        self.labelCheckMarkGrabSigned = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkGrabSigned.setObjectName(u"labelCheckMarkGrabSigned")
        self.labelCheckMarkGrabSigned.setGeometry(QRect(220, 250, 21, 21))
        self.labelCheckMarkGrabSigned.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkGrabSigned.setScaledContents(True)
        self.labelGrabStaticData = QLabel(WidgetGrabSeasonData)
        self.labelGrabStaticData.setObjectName(u"labelGrabStaticData")
        self.labelGrabStaticData.setGeometry(QRect(250, 280, 221, 16))
        self.labelCheckMarkGrabStaticData = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkGrabStaticData.setObjectName(u"labelCheckMarkGrabStaticData")
        self.labelCheckMarkGrabStaticData.setGeometry(QRect(220, 280, 21, 21))
        self.labelCheckMarkGrabStaticData.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkGrabStaticData.setScaledContents(True)

        self.retranslateUi(WidgetGrabSeasonData)

        QMetaObject.connectSlotsByName(WidgetGrabSeasonData)
    # setupUi

    def retranslateUi(self, WidgetGrabSeasonData):
        WidgetGrabSeasonData.setWindowTitle(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Season Data", None))
        self.pushButtonInitializeRecruits.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Initialize Recruits", None))
        self.pushButtonUpdateConsideringSigned.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Update Considering / Signed", None))
        self.progressBarUpdateConsidering.setFormat(QCoreApplication.translate("WidgetGrabSeasonData", u"%v", None))
        self.labelUpdateProgressBarMax.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"TextLabel", None))
        self.labelRecruitsInitialized.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Recruits Initialized = 0", None))
        self.labelProgressCreateRecruitDB.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Create / Re-create Recruit Database Table", None))
        self.labelCheckMarkCreateDB.setText("")
        self.labelCheckMarkAuthWIS.setText("")
        self.labelAuthWIS.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Authenticate to WIS - Gridiron Dynasty", None))
        self.labelGrabUnsigned.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Unsigned Recruits", None))
        self.labelCheckMarkGrabUnsigned.setText("")
        self.labelGrabSigned.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Signed Recruits", None))
        self.labelCheckMarkGrabSigned.setText("")
        self.labelGrabStaticData.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Recruit Static Data", None))
        self.labelCheckMarkGrabStaticData.setText("")
    # retranslateUi

