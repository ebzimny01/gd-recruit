from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import logging
from pathlib import Path
import sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    checkmarkicon = f"{Path(sys._MEIPASS) / 'images' / 'checkmark_1.png'}"
    x_icon = f"{Path(sys._MEIPASS) / 'images' / 'x_icon.png'}"
    #checkmarkicon = f"{sys._MEIPASS}/images/checkmark_1.png"
else:
    checkmarkicon = f"./images/checkmark_1.png"
    x_icon = f"./images/x_icon.png"

logging.info(f"Checkmark icon path is = {checkmarkicon}")
logging.info(f"X icon path is = {x_icon}")

# WARNING!!!
# Pasting new code from Designer, need to make sure you replace check mark icon!

class Ui_WidgetGrabSeasonData(object):
    def setupUi(self, WidgetGrabSeasonData):
        if not WidgetGrabSeasonData.objectName():
            WidgetGrabSeasonData.setObjectName(u"WidgetGrabSeasonData")
        WidgetGrabSeasonData.setWindowModality(Qt.ApplicationModal)
        WidgetGrabSeasonData.resize(685, 565)
        self.pushButtonInitializeRecruits = QPushButton(WidgetGrabSeasonData)
        self.pushButtonInitializeRecruits.setObjectName(u"pushButtonInitializeRecruits")
        self.pushButtonInitializeRecruits.setGeometry(QRect(150, 46, 411, 41))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(20)
        self.pushButtonInitializeRecruits.setFont(font)
        self.pushButtonUpdateConsideringSigned = QPushButton(WidgetGrabSeasonData)
        self.pushButtonUpdateConsideringSigned.setObjectName(u"pushButtonUpdateConsideringSigned")
        self.pushButtonUpdateConsideringSigned.setGeometry(QRect(120, 308, 471, 41))
        self.pushButtonUpdateConsideringSigned.setFont(font)
        self.progressBarInitializeRecruits = QProgressBar(WidgetGrabSeasonData)
        self.progressBarInitializeRecruits.setObjectName(u"progressBarInitializeRecruits")
        self.progressBarInitializeRecruits.setGeometry(QRect(200, 250, 321, 31))
        self.progressBarInitializeRecruits.setStyleSheet(u"")
        self.progressBarInitializeRecruits.setValue(24)
        self.progressBarInitializeRecruits.setTextVisible(True)
        self.progressBarUpdateConsidering = QProgressBar(WidgetGrabSeasonData)
        self.progressBarUpdateConsidering.setObjectName(u"progressBarUpdateConsidering")
        self.progressBarUpdateConsidering.setGeometry(QRect(200, 363, 321, 31))
        self.progressBarUpdateConsidering.setStyleSheet(u"")
        self.progressBarUpdateConsidering.setValue(24)
        self.progressBarUpdateConsidering.setTextVisible(True)
        self.labelUpdateProgressBarMax = QLabel(WidgetGrabSeasonData)
        self.labelUpdateProgressBarMax.setObjectName(u"labelUpdateProgressBarMax")
        self.labelUpdateProgressBarMax.setEnabled(True)
        self.labelUpdateProgressBarMax.setGeometry(QRect(530, 371, 81, 16))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        self.labelUpdateProgressBarMax.setFont(font1)
        self.labelRecruitsInitialized = QLabel(WidgetGrabSeasonData)
        self.labelRecruitsInitialized.setObjectName(u"labelRecruitsInitialized")
        self.labelRecruitsInitialized.setGeometry(QRect(150, 10, 401, 31))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(16)
        self.labelRecruitsInitialized.setFont(font2)
        self.labelRecruitsInitialized.setStyleSheet(u"color: rgb(255, 20, 20);")
        self.labelRecruitsInitialized.setAlignment(Qt.AlignCenter)
        self.labelProgressCreateRecruitDB = QLabel(WidgetGrabSeasonData)
        self.labelProgressCreateRecruitDB.setObjectName(u"labelProgressCreateRecruitDB")
        self.labelProgressCreateRecruitDB.setGeometry(QRect(227, 100, 341, 16))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        self.labelProgressCreateRecruitDB.setFont(font3)
        self.labelCheckMarkCreateDB = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkCreateDB.setObjectName(u"labelCheckMarkCreateDB")
        self.labelCheckMarkCreateDB.setGeometry(QRect(197, 97, 21, 21))
        self.labelCheckMarkCreateDB.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkCreateDB.setScaledContents(True)
        self.labelCheckMarkAuthWIS = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkAuthWIS.setObjectName(u"labelCheckMarkAuthWIS")
        self.labelCheckMarkAuthWIS.setGeometry(QRect(197, 126, 21, 21))
        self.labelCheckMarkAuthWIS.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkAuthWIS.setScaledContents(True)
        self.labelAuthWIS = QLabel(WidgetGrabSeasonData)
        self.labelAuthWIS.setObjectName(u"labelAuthWIS")
        self.labelAuthWIS.setGeometry(QRect(227, 128, 341, 16))
        self.labelAuthWIS.setFont(font3)
        self.labelGrabUnsigned = QLabel(WidgetGrabSeasonData)
        self.labelGrabUnsigned.setObjectName(u"labelGrabUnsigned")
        self.labelGrabUnsigned.setGeometry(QRect(227, 159, 341, 16))
        self.labelGrabUnsigned.setFont(font3)
        self.labelCheckMarkGrabUnsigned = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkGrabUnsigned.setObjectName(u"labelCheckMarkGrabUnsigned")
        self.labelCheckMarkGrabUnsigned.setGeometry(QRect(197, 157, 21, 21))
        self.labelCheckMarkGrabUnsigned.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkGrabUnsigned.setScaledContents(True)
        self.labelGrabSigned = QLabel(WidgetGrabSeasonData)
        self.labelGrabSigned.setObjectName(u"labelGrabSigned")
        self.labelGrabSigned.setGeometry(QRect(227, 189, 341, 16))
        self.labelGrabSigned.setFont(font3)
        self.labelCheckMarkGrabSigned = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkGrabSigned.setObjectName(u"labelCheckMarkGrabSigned")
        self.labelCheckMarkGrabSigned.setGeometry(QRect(197, 187, 21, 21))
        self.labelCheckMarkGrabSigned.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkGrabSigned.setScaledContents(True)
        self.labelGrabStaticData = QLabel(WidgetGrabSeasonData)
        self.labelGrabStaticData.setObjectName(u"labelGrabStaticData")
        self.labelGrabStaticData.setGeometry(QRect(227, 219, 341, 16))
        self.labelGrabStaticData.setFont(font3)
        self.labelCheckMarkGrabStaticData = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkGrabStaticData.setObjectName(u"labelCheckMarkGrabStaticData")
        self.labelCheckMarkGrabStaticData.setGeometry(QRect(197, 217, 21, 21))
        self.labelCheckMarkGrabStaticData.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkGrabStaticData.setScaledContents(True)
        self.pushButtonMarkRecruitsFromWatchlist = QPushButton(WidgetGrabSeasonData)
        self.pushButtonMarkRecruitsFromWatchlist.setObjectName(u"pushButtonMarkRecruitsFromWatchlist")
        self.pushButtonMarkRecruitsFromWatchlist.setEnabled(False)
        self.pushButtonMarkRecruitsFromWatchlist.setGeometry(QRect(120, 420, 471, 41))
        self.pushButtonMarkRecruitsFromWatchlist.setFont(font)
        self.progressBarMarkWatchlist = QProgressBar(WidgetGrabSeasonData)
        self.progressBarMarkWatchlist.setObjectName(u"progressBarMarkWatchlist")
        self.progressBarMarkWatchlist.setEnabled(False)
        self.progressBarMarkWatchlist.setGeometry(QRect(200, 510, 321, 31))
        self.progressBarMarkWatchlist.setMinimum(0)
        self.progressBarMarkWatchlist.setMaximum(100)
        self.progressBarMarkWatchlist.setValue(-1)
        self.progressBarMarkWatchlist.setTextVisible(True)
        self.labelCheckMarkAuthWIS_Error = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkAuthWIS_Error.setObjectName(u"labelCheckMarkAuthWIS_Error")
        self.labelCheckMarkAuthWIS_Error.setGeometry(QRect(197, 126, 21, 21))
        self.labelCheckMarkAuthWIS_Error.setPixmap(QPixmap(x_icon))
        self.labelCheckMarkAuthWIS_Error.setScaledContents(True)
        self.labelAuthWIS_MarkRecruits = QLabel(WidgetGrabSeasonData)
        self.labelAuthWIS_MarkRecruits.setObjectName(u"labelAuthWIS_MarkRecruits")
        self.labelAuthWIS_MarkRecruits.setGeometry(QRect(230, 474, 341, 16))
        self.labelAuthWIS_MarkRecruits.setFont(font3)
        self.labelCheckMarkAuthWIS_MarkRecruits = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkAuthWIS_MarkRecruits.setObjectName(u"labelCheckMarkAuthWIS_MarkRecruits")
        self.labelCheckMarkAuthWIS_MarkRecruits.setGeometry(QRect(200, 472, 21, 21))
        self.labelCheckMarkAuthWIS_MarkRecruits.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkAuthWIS_MarkRecruits.setScaledContents(True)
        self.labelCheckMarkAuthWIS_Error_MarkRecruits = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setObjectName(u"labelCheckMarkAuthWIS_Error_MarkRecruits")
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setGeometry(QRect(199, 472, 21, 21))
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setPixmap(QPixmap(x_icon))
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setScaledContents(True)

        self.retranslateUi(WidgetGrabSeasonData)

        QMetaObject.connectSlotsByName(WidgetGrabSeasonData)
    # setupUi

    def retranslateUi(self, WidgetGrabSeasonData):
        WidgetGrabSeasonData.setWindowTitle(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Recruit Data", None))
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
        self.labelGrabStaticData.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Recruit Static Ratings Data and GPA", None))
        self.labelCheckMarkGrabStaticData.setText("")
        self.pushButtonMarkRecruitsFromWatchlist.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Mark Recruits From Watchlist", None))
        self.labelCheckMarkAuthWIS_Error.setText("")
        self.labelAuthWIS_MarkRecruits.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Authenticate to WIS - Gridiron Dynasty", None))
        self.labelCheckMarkAuthWIS_MarkRecruits.setText("")
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setText("")
    # retranslateUi