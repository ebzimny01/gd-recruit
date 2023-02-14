from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSql import *
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
        WISCredentialDialog.resize(400, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WISCredentialDialog.sizePolicy().hasHeightForWidth())
        WISCredentialDialog.setSizePolicy(sizePolicy)
        WISCredentialDialog.setMinimumSize(QSize(400, 400))
        WISCredentialDialog.setMaximumSize(QSize(400, 406))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        WISCredentialDialog.setFont(font)
        WISCredentialDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(WISCredentialDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_LoginStoreCookie = QPushButton(WISCredentialDialog)
        self.pushButton_LoginStoreCookie.setObjectName(u"pushButton_LoginStoreCookie")
        sizePolicy.setHeightForWidth(self.pushButton_LoginStoreCookie.sizePolicy().hasHeightForWidth())
        self.pushButton_LoginStoreCookie.setSizePolicy(sizePolicy)
        self.pushButton_LoginStoreCookie.setMinimumSize(QSize(230, 30))
        self.pushButton_LoginStoreCookie.setMaximumSize(QSize(230, 30))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        self.pushButton_LoginStoreCookie.setFont(font1)

        self.gridLayout.addWidget(self.pushButton_LoginStoreCookie, 8, 1, 1, 1)

        self.labelCheckMarkcoachIDValidationError = QLabel(WISCredentialDialog)
        self.labelCheckMarkcoachIDValidationError.setObjectName(u"labelCheckMarkcoachIDValidationError")
        sizePolicy.setHeightForWidth(self.labelCheckMarkcoachIDValidationError.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkcoachIDValidationError.setSizePolicy(sizePolicy)
        self.labelCheckMarkcoachIDValidationError.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkcoachIDValidationError.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkcoachIDValidationError.setPixmap(QPixmap(x_icon))
        self.labelCheckMarkcoachIDValidationError.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkcoachIDValidationError, 2, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.labelCheckMarkCookieStored = QLabel(WISCredentialDialog)
        self.labelCheckMarkCookieStored.setObjectName(u"labelCheckMarkCookieStored")
        sizePolicy.setHeightForWidth(self.labelCheckMarkCookieStored.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkCookieStored.setSizePolicy(sizePolicy)
        self.labelCheckMarkCookieStored.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkCookieStored.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkCookieStored.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkCookieStored.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkCookieStored, 12, 2, 1, 1)

        self.labelCookieStored = QLabel(WISCredentialDialog)
        self.labelCookieStored.setObjectName(u"labelCookieStored")
        sizePolicy.setHeightForWidth(self.labelCookieStored.sizePolicy().hasHeightForWidth())
        self.labelCookieStored.setSizePolicy(sizePolicy)
        self.labelCookieStored.setMinimumSize(QSize(230, 30))
        self.labelCookieStored.setMaximumSize(QSize(230, 30))
        self.labelCookieStored.setFont(font1)
        self.labelCookieStored.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelCookieStored, 12, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.labelCheckMarkcoachIDValidated = QLabel(WISCredentialDialog)
        self.labelCheckMarkcoachIDValidated.setObjectName(u"labelCheckMarkcoachIDValidated")
        sizePolicy.setHeightForWidth(self.labelCheckMarkcoachIDValidated.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkcoachIDValidated.setSizePolicy(sizePolicy)
        self.labelCheckMarkcoachIDValidated.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkcoachIDValidated.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkcoachIDValidated.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkcoachIDValidated.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkcoachIDValidated, 2, 2, 1, 1)

        self.lineEditWISCoachID = QLineEdit(WISCredentialDialog)
        self.lineEditWISCoachID.setObjectName(u"lineEditWISCoachID")
        sizePolicy.setHeightForWidth(self.lineEditWISCoachID.sizePolicy().hasHeightForWidth())
        self.lineEditWISCoachID.setSizePolicy(sizePolicy)
        self.lineEditWISCoachID.setMinimumSize(QSize(230, 30))
        self.lineEditWISCoachID.setMaximumSize(QSize(230, 30))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        self.lineEditWISCoachID.setFont(font2)

        self.gridLayout.addWidget(self.lineEditWISCoachID, 2, 1, 1, 1)

        self.progressBarLoginStoreCookies = QProgressBar(WISCredentialDialog)
        self.progressBarLoginStoreCookies.setObjectName(u"progressBarLoginStoreCookies")
        sizePolicy.setHeightForWidth(self.progressBarLoginStoreCookies.sizePolicy().hasHeightForWidth())
        self.progressBarLoginStoreCookies.setSizePolicy(sizePolicy)
        self.progressBarLoginStoreCookies.setMinimumSize(QSize(230, 30))
        self.progressBarLoginStoreCookies.setMaximumSize(QSize(230, 30))
        self.progressBarLoginStoreCookies.setMinimum(0)
        self.progressBarLoginStoreCookies.setMaximum(0)
        self.progressBarLoginStoreCookies.setValue(100)
        self.progressBarLoginStoreCookies.setTextVisible(False)

        self.gridLayout.addWidget(self.progressBarLoginStoreCookies, 10, 1, 1, 1)

        self.labelWISCoachID = QLabel(WISCredentialDialog)
        self.labelWISCoachID.setObjectName(u"labelWISCoachID")
        sizePolicy.setHeightForWidth(self.labelWISCoachID.sizePolicy().hasHeightForWidth())
        self.labelWISCoachID.setSizePolicy(sizePolicy)
        self.labelWISCoachID.setMinimumSize(QSize(230, 30))
        self.labelWISCoachID.setMaximumSize(QSize(230, 30))
        self.labelWISCoachID.setFont(font1)

        self.gridLayout.addWidget(self.labelWISCoachID, 1, 1, 1, 1)

        self.labelCookieStoredError = QLabel(WISCredentialDialog)
        self.labelCookieStoredError.setObjectName(u"labelCookieStoredError")
        sizePolicy.setHeightForWidth(self.labelCookieStoredError.sizePolicy().hasHeightForWidth())
        self.labelCookieStoredError.setSizePolicy(sizePolicy)
        self.labelCookieStoredError.setMinimumSize(QSize(20, 20))
        self.labelCookieStoredError.setMaximumSize(QSize(20, 20))
        self.labelCookieStoredError.setPixmap(QPixmap(x_icon))
        self.labelCookieStoredError.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCookieStoredError, 12, 3, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_7, 15, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 13, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_6, 5, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.line = QFrame(WISCredentialDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 5)

        self.buttonBox = QDialogButtonBox(WISCredentialDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 16, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 11, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 9, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.line_2 = QFrame(WISCredentialDialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 14, 0, 1, 5)

        self.verticalSpacer_8 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_8, 8, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_9, 12, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        QWidget.setTabOrder(self.lineEditWISCoachID, self.pushButton_LoginStoreCookie)

        self.retranslateUi(WISCredentialDialog, coachid)
        self.buttonBox.accepted.connect(WISCredentialDialog.accept)
        self.buttonBox.rejected.connect(WISCredentialDialog.reject)

        QMetaObject.connectSlotsByName(WISCredentialDialog)
    # setupUi

    def retranslateUi(self, WISCredentialDialog, coachid):
        WISCredentialDialog.setWindowTitle(QCoreApplication.translate("WISCredentialDialog", u"WIS Authentication", None))
        self.pushButton_LoginStoreCookie.setText(QCoreApplication.translate("WISCredentialDialog", u"Login To Store Cookie", None))
        self.labelCheckMarkcoachIDValidationError.setText("")
        self.labelCheckMarkCookieStored.setText("")
        self.labelCookieStored.setText(QCoreApplication.translate("WISCredentialDialog", u"Cookie Stored:", None))
        self.labelCheckMarkcoachIDValidated.setText("")
        self.lineEditWISCoachID.setText("")
        self.lineEditWISCoachID.setPlaceholderText(QCoreApplication.translate("WISCredentialDialog", u"e.g. johnsmith123", None))
        self.labelWISCoachID.setText(QCoreApplication.translate("WISCredentialDialog", u"WIS Coach ID:", None))
        self.labelCookieStoredError.setText("")
    # retranslateUi





        self.lineEditWISCoachID.setText(coachid)





        