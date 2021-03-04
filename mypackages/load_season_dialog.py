from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogLoadSeason(object):
    def setupUi(self, DialogLoadSeason):
        if not DialogLoadSeason.objectName():
            DialogLoadSeason.setObjectName(u"DialogLoadSeason")
        DialogLoadSeason.setWindowModality(Qt.ApplicationModal)
        DialogLoadSeason.resize(400, 300)
        self.buttonBox = QDialogButtonBox(DialogLoadSeason)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.labelSelectSeason = QLabel(DialogLoadSeason)
        self.labelSelectSeason.setObjectName(u"labelSelectSeason")
        self.labelSelectSeason.setGeometry(QRect(20, 30, 81, 21))
        self.comboBoxSelectSeason = QComboBox(DialogLoadSeason)
        self.comboBoxSelectSeason.setObjectName(u"comboBoxSelectSeason")
        self.comboBoxSelectSeason.setGeometry(QRect(150, 30, 231, 22))

        self.retranslateUi(DialogLoadSeason)
        self.buttonBox.accepted.connect(DialogLoadSeason.accept)
        self.buttonBox.rejected.connect(DialogLoadSeason.reject)

        QMetaObject.connectSlotsByName(DialogLoadSeason)
    # setupUi

    def retranslateUi(self, DialogLoadSeason):
        DialogLoadSeason.setWindowTitle(QCoreApplication.translate("DialogLoadSeason", u"Load Season", None))
        self.labelSelectSeason.setText(QCoreApplication.translate("DialogLoadSeason", u"Select season:", None))
    # retranslateUi

