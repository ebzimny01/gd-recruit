from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *

# Need to be carefule editing this file.
# Don't blindly copy/paste code from Designer.
# There are extra arguments passed and code near bottom that needs to be preserved.
class Ui_WISCredentialDialog(object):
    def setupUi(self, WISCredentialDialog, coachid, username, password):
        if not WISCredentialDialog.objectName():
            WISCredentialDialog.setObjectName(u"WISCredentialDialog")
        WISCredentialDialog.setWindowModality(Qt.WindowModal)
        WISCredentialDialog.resize(400, 313)
        WISCredentialDialog.setModal(True)
        self.buttonBox = QDialogButtonBox(WISCredentialDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.labelWISUsername = QLabel(WISCredentialDialog)
        self.labelWISUsername.setObjectName(u"labelWISUsername")
        self.labelWISUsername.setGeometry(QRect(20, 110, 141, 16))
        self.labelWISPassword = QLabel(WISCredentialDialog)
        self.labelWISPassword.setObjectName(u"labelWISPassword")
        self.labelWISPassword.setGeometry(QRect(20, 160, 141, 16))
        self.lineEditWISUsername = QLineEdit(WISCredentialDialog)
        self.lineEditWISUsername.setObjectName(u"lineEditWISUsername")
        self.lineEditWISUsername.setGeometry(QRect(170, 110, 191, 20))
        self.lineEditWISPassword = QLineEdit(WISCredentialDialog)
        self.lineEditWISPassword.setObjectName(u"lineEditWISPassword")
        self.lineEditWISPassword.setGeometry(QRect(170, 160, 191, 20))
        self.lineEditWISPassword.setEchoMode(QLineEdit.Password)
        self.labelWISCoachID = QLabel(WISCredentialDialog)
        self.labelWISCoachID.setObjectName(u"labelWISCoachID")
        self.labelWISCoachID.setGeometry(QRect(20, 60, 141, 16))
        self.lineEditWISCoachID = QLineEdit(WISCredentialDialog)
        self.lineEditWISCoachID.setObjectName(u"lineEditWISCoachID")
        self.lineEditWISCoachID.setGeometry(QRect(170, 60, 191, 20))
        QWidget.setTabOrder(self.lineEditWISCoachID, self.lineEditWISUsername)
        QWidget.setTabOrder(self.lineEditWISUsername, self.lineEditWISPassword)

        self.retranslateUi(WISCredentialDialog, coachid, username, password)
        self.buttonBox.accepted.connect(WISCredentialDialog.accept)
        self.buttonBox.rejected.connect(WISCredentialDialog.reject)

        QMetaObject.connectSlotsByName(WISCredentialDialog)
    # setupUi

    def retranslateUi(self, WISCredentialDialog, coachid, username, password):
        WISCredentialDialog.setWindowTitle(QCoreApplication.translate("WISCredentialDialog", u"Save WIS Credentials", None))
        self.labelWISUsername.setText(QCoreApplication.translate("WISCredentialDialog", u"WIS Email Login", None))
        self.labelWISPassword.setText(QCoreApplication.translate("WISCredentialDialog", u"WIS Password", None))
        self.labelWISCoachID.setText(QCoreApplication.translate("WISCredentialDialog", u"WIS Coach ID", None))
    # retranslateUi

        self.lineEditWISCoachID.setText(coachid)
        self.lineEditWISUsername.setText(username)
        self.lineEditWISPassword.setText(password)
        