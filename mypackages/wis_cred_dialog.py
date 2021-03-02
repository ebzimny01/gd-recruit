from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *


class Ui_WISCredentialDialog(object):    
    def setupUi(self, WISCredentialDialog, username, password):
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
        self.labelWISUsername.setGeometry(QRect(20, 50, 101, 16))
        self.labelWISPassword = QLabel(WISCredentialDialog)
        self.labelWISPassword.setObjectName(u"labelWISPassword")
        self.labelWISPassword.setGeometry(QRect(20, 130, 91, 16))
        self.lineEditWISUsername = QLineEdit(WISCredentialDialog)
        self.lineEditWISUsername.setObjectName(u"lineEditWISUsername")
        self.lineEditWISUsername.setGeometry(QRect(170, 50, 191, 20))
        # self.lineEditWISUsername.text = username
        self.lineEditWISPassword = QLineEdit(WISCredentialDialog)
        self.lineEditWISPassword.setObjectName(u"lineEditWISPassword")
        self.lineEditWISPassword.setGeometry(QRect(170, 130, 191, 20))
        self.lineEditWISPassword.setEchoMode(QLineEdit.Password)
        # self.lineEditWISPassword.text = password

        self.retranslateUi(WISCredentialDialog, username, password)
        self.buttonBox.accepted.connect(WISCredentialDialog.accept)
        self.buttonBox.rejected.connect(WISCredentialDialog.reject)

        QMetaObject.connectSlotsByName(WISCredentialDialog)

    def retranslateUi(self, WISCredentialDialog, username, password):
        WISCredentialDialog.setWindowTitle(QCoreApplication.translate("WISCredentialDialog", u"Save WIS Credentials", None))
        self.labelWISUsername.setText(QCoreApplication.translate("WISCredentialDialog", u"WIS Username", None))
        self.lineEditWISUsername.setText(QCoreApplication.translate("WISCredentialDialog", username, None))
        self.labelWISPassword.setText(QCoreApplication.translate("WISCredentialDialog", u"WIS Password", None))
        self.lineEditWISPassword.setText(password)

    def save_credentials(self):
        user = self.lineEditWISUsername.text()
        pwd = self.lineEditWISPassword.text()
        print(f"Username = {user}")
        print(f"password = {pwd}")
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.set('WISCreds', 'username', user)
        config.set('WISCreds', 'password', pwd)
        with open("config.ini", 'w') as file:
            config.write(file)
        print("Now what?????")
        WISCredentialDialog.accept()