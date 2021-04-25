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
    def setupUi(self, WISCredentialDialog, coachid):
        if not WISCredentialDialog.objectName():
            WISCredentialDialog.setObjectName(u"WISCredentialDialog")
        WISCredentialDialog.setWindowModality(Qt.ApplicationModal)
        WISCredentialDialog.resize(417, 253)
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        WISCredentialDialog.setFont(font)
        WISCredentialDialog.setModal(True)
        self.buttonBox = QDialogButtonBox(WISCredentialDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(140, 200, 111, 32))
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.labelWISCoachID = QLabel(WISCredentialDialog)
        self.labelWISCoachID.setObjectName(u"labelWISCoachID")
        self.labelWISCoachID.setGeometry(QRect(20, 58, 111, 16))
        self.labelWISCoachID.setFont(font)
        self.lineEditWISCoachID = QLineEdit(WISCredentialDialog)
        self.lineEditWISCoachID.setObjectName(u"lineEditWISCoachID")
        self.lineEditWISCoachID.setGeometry(QRect(130, 50, 221, 31))
        self.lineEditWISCoachID.setFont(font)
        self.labelCheckMarkcoachIDValidated = QLabel(WISCredentialDialog)
        self.labelCheckMarkcoachIDValidated.setObjectName(u"labelCheckMarkcoachIDValidated")
        self.labelCheckMarkcoachIDValidated.setGeometry(QRect(370, 55, 21, 21))
        self.labelCheckMarkcoachIDValidated.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkcoachIDValidated.setScaledContents(True)
        self.labelCheckMarkcoachIDValidationError = QLabel(WISCredentialDialog)
        self.labelCheckMarkcoachIDValidationError.setObjectName(u"labelCheckMarkcoachIDValidationError")
        self.labelCheckMarkcoachIDValidationError.setGeometry(QRect(369, 55, 21, 21))
        self.labelCheckMarkcoachIDValidationError.setPixmap(QPixmap(x_icon))
        self.labelCheckMarkcoachIDValidationError.setScaledContents(True)
        self.labelCookieStored = QLabel(WISCredentialDialog)
        self.labelCookieStored.setObjectName(u"labelCookieStored")
        self.labelCookieStored.setGeometry(QRect(250, 114, 111, 21))
        self.labelCookieStoredError = QLabel(WISCredentialDialog)
        self.labelCookieStoredError.setObjectName(u"labelCookieStoredError")
        self.labelCookieStoredError.setGeometry(QRect(369, 114, 21, 21))
        self.labelCookieStoredError.setPixmap(QPixmap(x_icon))
        self.labelCookieStoredError.setScaledContents(True)
        self.labelCheckMarkCookieStored = QLabel(WISCredentialDialog)
        self.labelCheckMarkCookieStored.setObjectName(u"labelCheckMarkCookieStored")
        self.labelCheckMarkCookieStored.setGeometry(QRect(370, 114, 21, 21))
        self.labelCheckMarkCookieStored.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkCookieStored.setScaledContents(True)
        self.pushButton_LoginStoreCookie = QPushButton(WISCredentialDialog)
        self.pushButton_LoginStoreCookie.setObjectName(u"pushButton_LoginStoreCookie")
        self.pushButton_LoginStoreCookie.setGeometry(QRect(20, 109, 191, 31))
        self.progressBarLoginStoreCookies = QProgressBar(WISCredentialDialog)
        self.progressBarLoginStoreCookies.setObjectName(u"progressBarLoginStoreCookies")
        self.progressBarLoginStoreCookies.setGeometry(QRect(20, 160, 371, 23))
        self.progressBarLoginStoreCookies.setMinimum(0)
        self.progressBarLoginStoreCookies.setMaximum(0)
        self.progressBarLoginStoreCookies.setValue(100)
        self.progressBarLoginStoreCookies.setTextVisible(False)

        self.retranslateUi(WISCredentialDialog, coachid)
        self.buttonBox.accepted.connect(WISCredentialDialog.accept)
        self.buttonBox.rejected.connect(WISCredentialDialog.reject)

        QMetaObject.connectSlotsByName(WISCredentialDialog)
    # setupUi

    def retranslateUi(self, WISCredentialDialog, coachid):
        WISCredentialDialog.setWindowTitle(QCoreApplication.translate("WISCredentialDialog", u"Save WIS Credentials", None))
        self.labelWISCoachID.setText(QCoreApplication.translate("WISCredentialDialog", u"WIS Coach ID:", None))
        self.lineEditWISCoachID.setText("")
        self.lineEditWISCoachID.setPlaceholderText(QCoreApplication.translate("WISCredentialDialog", u"e.g. johnsmith123", None))
        self.labelCheckMarkcoachIDValidated.setText("")
        self.labelCheckMarkcoachIDValidationError.setText("")
        self.labelCookieStored.setText(QCoreApplication.translate("WISCredentialDialog", u"Cookie Stored:", None))
        self.labelCookieStoredError.setText("")
        self.labelCheckMarkCookieStored.setText("")
        self.pushButton_LoginStoreCookie.setText(QCoreApplication.translate("WISCredentialDialog", u"Login To Store Cookie", None))
    # retranslateUi

        self.lineEditWISCoachID.setText(coachid)





        