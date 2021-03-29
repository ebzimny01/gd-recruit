from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *
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

# Need to be carefule editing this file.
# Don't blindly copy/paste code from Designer.
# There are extra arguments passed and code near bottom that needs to be preserved.


class Ui_WISCredentialDialog(object):
    def setupUi(self, WISCredentialDialog, coachid, username, password):
        if not WISCredentialDialog.objectName():
            WISCredentialDialog.setObjectName(u"WISCredentialDialog")
        WISCredentialDialog.setWindowModality(Qt.WindowModal)
        WISCredentialDialog.resize(417, 313)
        WISCredentialDialog.setModal(True)
        self.buttonBox = QDialogButtonBox(WISCredentialDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        font = QFont()
        font.setFamily(u"Arial")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.labelWISUsername = QLabel(WISCredentialDialog)
        self.labelWISUsername.setObjectName(u"labelWISUsername")
        self.labelWISUsername.setGeometry(QRect(20, 110, 141, 16))
        self.labelWISUsername.setFont(font)
        self.labelWISPassword = QLabel(WISCredentialDialog)
        self.labelWISPassword.setObjectName(u"labelWISPassword")
        self.labelWISPassword.setGeometry(QRect(20, 160, 141, 16))
        self.labelWISPassword.setFont(font)
        self.lineEditWISUsername = QLineEdit(WISCredentialDialog)
        self.lineEditWISUsername.setObjectName(u"lineEditWISUsername")
        self.lineEditWISUsername.setGeometry(QRect(170, 110, 191, 20))
        self.lineEditWISUsername.setFont(font)
        self.lineEditWISPassword = QLineEdit(WISCredentialDialog)
        self.lineEditWISPassword.setObjectName(u"lineEditWISPassword")
        self.lineEditWISPassword.setGeometry(QRect(170, 160, 191, 20))
        self.lineEditWISPassword.setFont(font)
        self.lineEditWISPassword.setEchoMode(QLineEdit.Password)
        self.labelWISCoachID = QLabel(WISCredentialDialog)
        self.labelWISCoachID.setObjectName(u"labelWISCoachID")
        self.labelWISCoachID.setGeometry(QRect(20, 60, 141, 16))
        self.labelWISCoachID.setFont(font)
        self.lineEditWISCoachID = QLineEdit(WISCredentialDialog)
        self.lineEditWISCoachID.setObjectName(u"lineEditWISCoachID")
        self.lineEditWISCoachID.setGeometry(QRect(170, 60, 191, 20))
        self.lineEditWISCoachID.setFont(font)
        self.labelCheckMarkcoachIDValidated = QLabel(WISCredentialDialog)
        self.labelCheckMarkcoachIDValidated.setObjectName(u"labelCheckMarkcoachIDValidated")
        self.labelCheckMarkcoachIDValidated.setGeometry(QRect(370, 60, 21, 21))
        self.labelCheckMarkcoachIDValidated.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkcoachIDValidated.setScaledContents(True)
        self.labelCheckMarkcoachIDValidationError = QLabel(WISCredentialDialog)
        self.labelCheckMarkcoachIDValidationError.setObjectName(u"labelCheckMarkcoachIDValidationError")
        self.labelCheckMarkcoachIDValidationError.setGeometry(QRect(369, 60, 21, 21))
        self.labelCheckMarkcoachIDValidationError.setPixmap(QPixmap(x_icon))
        self.labelCheckMarkcoachIDValidationError.setScaledContents(True)
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
        self.labelCheckMarkcoachIDValidated.setText("")
        self.labelCheckMarkcoachIDValidationError.setText("")
    # retranslateUi



        self.lineEditWISCoachID.setText(coachid)
        self.lineEditWISUsername.setText(username)
        self.lineEditWISPassword.setText(password)
        