from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogLoadSeason(object):
    def setupUi(self, DialogLoadSeason):
        if not DialogLoadSeason.objectName():
            DialogLoadSeason.setObjectName(u"DialogLoadSeason")
        DialogLoadSeason.setWindowModality(Qt.ApplicationModal)
        DialogLoadSeason.resize(480, 238)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        DialogLoadSeason.setFont(font)
        self.buttonBox = QDialogButtonBox(DialogLoadSeason)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 170, 461, 32))
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.labelSelectSeason = QLabel(DialogLoadSeason)
        self.labelSelectSeason.setObjectName(u"labelSelectSeason")
        self.labelSelectSeason.setGeometry(QRect(20, 30, 271, 21))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(18)
        self.labelSelectSeason.setFont(font1)
        self.comboBoxSelectSeason = QComboBox(DialogLoadSeason)
        self.comboBoxSelectSeason.setObjectName(u"comboBoxSelectSeason")
        self.comboBoxSelectSeason.setGeometry(QRect(20, 70, 441, 22))
        self.comboBoxSelectSeason.setFont(font)

        self.retranslateUi(DialogLoadSeason)
        self.buttonBox.accepted.connect(DialogLoadSeason.accept)
        self.buttonBox.rejected.connect(DialogLoadSeason.reject)

        QMetaObject.connectSlotsByName(DialogLoadSeason)
    # setupUi

    def retranslateUi(self, DialogLoadSeason):
        DialogLoadSeason.setWindowTitle(QCoreApplication.translate("DialogLoadSeason", u"Load Season", None))
        self.labelSelectSeason.setText(QCoreApplication.translate("DialogLoadSeason", u"Select season to load:", None))
    # retranslateUi



