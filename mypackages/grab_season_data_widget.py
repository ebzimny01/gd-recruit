from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


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
        self.progressBarUpdateConsidering.setGeometry(QRect(180, 480, 321, 31))
        self.progressBarUpdateConsidering.setStyleSheet(u"")
        self.progressBarUpdateConsidering.setValue(24)
        self.progressBarUpdateConsidering.setTextVisible(True)
        self.labelUpdateProgressBarMax = QLabel(WidgetGrabSeasonData)
        self.labelUpdateProgressBarMax.setObjectName(u"labelUpdateProgressBarMax")
        self.labelUpdateProgressBarMax.setEnabled(True)
        self.labelUpdateProgressBarMax.setGeometry(QRect(523, 490, 81, 16))
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
    # retranslateUi

