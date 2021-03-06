from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WidgetInitializeRecruits(object):
    def setupUi(self, WidgetInitializeRecruits):
        if not WidgetInitializeRecruits.objectName():
            WidgetInitializeRecruits.setObjectName(u"WidgetInitializeRecruits")
        WidgetInitializeRecruits.setWindowModality(Qt.ApplicationModal)
        WidgetInitializeRecruits.resize(400, 300)
        self.progressBar = QProgressBar(WidgetInitializeRecruits)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(150, 150, 118, 23))
        self.progressBar.setValue(24)
        self.label = QLabel(WidgetInitializeRecruits)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 80, 161, 16))

        self.retranslateUi(WidgetInitializeRecruits)

        QMetaObject.connectSlotsByName(WidgetInitializeRecruits)
    # setupUi

    def retranslateUi(self, WidgetInitializeRecruits):
        WidgetInitializeRecruits.setWindowTitle(QCoreApplication.translate("WidgetInitializeRecruits", u"Initialize Recruits", None))
        self.label.setText(QCoreApplication.translate("WidgetInitializeRecruits", u"Initializing recruits . . . ", None))
    # retranslateUi

