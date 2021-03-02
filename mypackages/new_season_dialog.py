from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *


class Ui_DialogNewSeason(object):
    def setupUi(self, DialogNewSeason):
        if not DialogNewSeason.objectName():
            DialogNewSeason.setObjectName(u"DialogNewSeason")
        DialogNewSeason.setWindowModality(Qt.WindowModal)
        DialogNewSeason.resize(400, 300)
        self.buttonBox = QDialogButtonBox(DialogNewSeason)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.labelTeamID = QLabel(DialogNewSeason)
        self.labelTeamID.setObjectName(u"labelTeamID")
        self.labelTeamID.setGeometry(QRect(60, 60, 47, 14))
        self.labelSeasonNumber = QLabel(DialogNewSeason)
        self.labelSeasonNumber.setObjectName(u"labelSeasonNumber")
        self.labelSeasonNumber.setGeometry(QRect(40, 120, 91, 16))
        self.lineEditTeamID = QLineEdit(DialogNewSeason)
        self.lineEditTeamID.setObjectName(u"lineEditTeamID")
        self.lineEditTeamID.setGeometry(QRect(200, 60, 113, 20))
        self.lineEditSeasonNumber = QLineEdit(DialogNewSeason)
        self.lineEditSeasonNumber.setObjectName(u"lineEditSeasonNumber")
        self.lineEditSeasonNumber.setGeometry(QRect(200, 120, 113, 20))

        self.retranslateUi(DialogNewSeason)
        self.buttonBox.accepted.connect(DialogNewSeason.accept)
        self.buttonBox.rejected.connect(DialogNewSeason.reject)

        QMetaObject.connectSlotsByName(DialogNewSeason)
    # setupUi

    def retranslateUi(self, DialogNewSeason):
        DialogNewSeason.setWindowTitle(QCoreApplication.translate("DialogNewSeason", u"New Season", None))
        self.labelTeamID.setText(QCoreApplication.translate("DialogNewSeason", u"Team ID", None))
        self.labelSeasonNumber.setText(QCoreApplication.translate("DialogNewSeason", u"Season Number", None))
    # retranslateUi

    def save_NewSeason(self):
        teamID = self.lineEditTeamID.text()
        season_num = self.lineEditSeasonNumber.text()
        print(f"Team ID = {teamID}")
        print(f"Season Number = {season_num}")