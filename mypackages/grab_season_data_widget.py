from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WidgetGrabSeasonData(object):
    def setupUi(self, WidgetGrabSeasonData):
        if not WidgetGrabSeasonData.objectName():
            WidgetGrabSeasonData.setObjectName(u"WidgetGrabSeasonData")
        WidgetGrabSeasonData.setWindowModality(Qt.ApplicationModal)
        WidgetGrabSeasonData.resize(685, 540)
        self.pushButtonInitializeRecruits = QPushButton(WidgetGrabSeasonData)
        self.pushButtonInitializeRecruits.setObjectName(u"pushButtonInitializeRecruits")
        self.pushButtonInitializeRecruits.setGeometry(QRect(90, 50, 501, 121))
        font = QFont()
        font.setPointSize(24)
        self.pushButtonInitializeRecruits.setFont(font)
        self.pushButtonUpdateConsideringSigned = QPushButton(WidgetGrabSeasonData)
        self.pushButtonUpdateConsideringSigned.setObjectName(u"pushButtonUpdateConsideringSigned")
        self.pushButtonUpdateConsideringSigned.setGeometry(QRect(90, 200, 501, 121))
        self.pushButtonUpdateConsideringSigned.setFont(font)

        self.retranslateUi(WidgetGrabSeasonData)

        QMetaObject.connectSlotsByName(WidgetGrabSeasonData)
    # setupUi

    def retranslateUi(self, WidgetGrabSeasonData):
        WidgetGrabSeasonData.setWindowTitle(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Season Data", None))
        self.pushButtonInitializeRecruits.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Initialize Recruits", None))
        self.pushButtonUpdateConsideringSigned.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Update Considering / Signed", None))
    # retranslateUi
