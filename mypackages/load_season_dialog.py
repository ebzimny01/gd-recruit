from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_DialogLoadSeason(object):
    def setupUi(self, DialogLoadSeason):
        if not DialogLoadSeason.objectName():
            DialogLoadSeason.setObjectName(u"DialogLoadSeason")
        DialogLoadSeason.setWindowModality(Qt.ApplicationModal)
        DialogLoadSeason.resize(404, 230)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogLoadSeason.sizePolicy().hasHeightForWidth())
        DialogLoadSeason.setSizePolicy(sizePolicy)
        DialogLoadSeason.setMinimumSize(QSize(404, 230))
        DialogLoadSeason.setMaximumSize(QSize(404, 230))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        DialogLoadSeason.setFont(font)
        self.formLayout = QFormLayout(DialogLoadSeason)
        self.formLayout.setObjectName(u"formLayout")
        self.labelSelectSeason = QLabel(DialogLoadSeason)
        self.labelSelectSeason.setObjectName(u"labelSelectSeason")
        sizePolicy.setHeightForWidth(self.labelSelectSeason.sizePolicy().hasHeightForWidth())
        self.labelSelectSeason.setSizePolicy(sizePolicy)
        self.labelSelectSeason.setMinimumSize(QSize(380, 50))
        self.labelSelectSeason.setMaximumSize(QSize(380, 50))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(18)
        self.labelSelectSeason.setFont(font1)
        self.labelSelectSeason.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelSelectSeason)

        self.comboBoxSelectSeason = QComboBox(DialogLoadSeason)
        self.comboBoxSelectSeason.setObjectName(u"comboBoxSelectSeason")
        sizePolicy.setHeightForWidth(self.comboBoxSelectSeason.sizePolicy().hasHeightForWidth())
        self.comboBoxSelectSeason.setSizePolicy(sizePolicy)
        self.comboBoxSelectSeason.setMinimumSize(QSize(380, 30))
        self.comboBoxSelectSeason.setMaximumSize(QSize(380, 30))
        self.comboBoxSelectSeason.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.comboBoxSelectSeason)

        self.buttonBox = QDialogButtonBox(DialogLoadSeason)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QSize(380, 30))
        self.buttonBox.setMaximumSize(QSize(380, 30))
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.buttonBox)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(1, QFormLayout.LabelRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.verticalSpacer_2)


        self.retranslateUi(DialogLoadSeason)
        self.buttonBox.accepted.connect(DialogLoadSeason.accept)
        self.buttonBox.rejected.connect(DialogLoadSeason.reject)

        QMetaObject.connectSlotsByName(DialogLoadSeason)
    # setupUi

    def retranslateUi(self, DialogLoadSeason):
        DialogLoadSeason.setWindowTitle(QCoreApplication.translate("DialogLoadSeason", u"Load Season", None))
        self.labelSelectSeason.setText(QCoreApplication.translate("DialogLoadSeason", u"Select season to load:", None))
    # retranslateUi





