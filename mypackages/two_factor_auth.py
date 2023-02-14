from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_DialogTwoFactorAuth(object):
    def setupUi(self, DialogTwoFactorAuth):
        if not DialogTwoFactorAuth.objectName():
            DialogTwoFactorAuth.setObjectName(u"DialogTwoFactorAuth")
        DialogTwoFactorAuth.setWindowModality(Qt.ApplicationModal)
        DialogTwoFactorAuth.resize(502, 226)
        font = QFont()
        font.setFamily(u"Arial")
        DialogTwoFactorAuth.setFont(font)
        DialogTwoFactorAuth.setInputMethodHints(Qt.ImhNone)
        self.pushButtonSubmit = QPushButton(DialogTwoFactorAuth)
        self.pushButtonSubmit.setObjectName(u"pushButtonSubmit")
        self.pushButtonSubmit.setGeometry(QRect(270, 110, 111, 41))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        self.pushButtonSubmit.setFont(font1)
        self.lineEdit_6_digit_code = QLineEdit(DialogTwoFactorAuth)
        self.lineEdit_6_digit_code.setObjectName(u"lineEdit_6_digit_code")
        self.lineEdit_6_digit_code.setGeometry(QRect(90, 110, 151, 41))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(28)
        self.lineEdit_6_digit_code.setFont(font2)
        self.lineEdit_6_digit_code.setMaxLength(6)
        self.label = QLabel(DialogTwoFactorAuth)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 471, 41))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(20)
        self.label.setFont(font3)
        self.label_Format_Error = QLabel(DialogTwoFactorAuth)
        self.label_Format_Error.setObjectName(u"label_Format_Error")
        self.label_Format_Error.setGeometry(QRect(90, 160, 171, 16))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        self.label_Format_Error.setFont(font4)
        self.label_Format_Error.setStyleSheet(u"color: red;")
        QWidget.setTabOrder(self.lineEdit_6_digit_code, self.pushButtonSubmit)

        self.retranslateUi(DialogTwoFactorAuth)

        QMetaObject.connectSlotsByName(DialogTwoFactorAuth)
    # setupUi

    def retranslateUi(self, DialogTwoFactorAuth):
        DialogTwoFactorAuth.setWindowTitle(QCoreApplication.translate("DialogTwoFactorAuth", u"Fanball-WIS Two Factor Auth", None))
        self.pushButtonSubmit.setText(QCoreApplication.translate("DialogTwoFactorAuth", u"Submit", None))
        self.lineEdit_6_digit_code.setInputMask("")
        self.lineEdit_6_digit_code.setText("")
        self.label.setText(QCoreApplication.translate("DialogTwoFactorAuth", u"Enter your 6-digit security code here:", None))
        self.label_Format_Error.setText(QCoreApplication.translate("DialogTwoFactorAuth", u"Code must be 6 numbers.", None))
    # retranslateUi






