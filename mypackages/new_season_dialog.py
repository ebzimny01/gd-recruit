from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtSql import *


class Ui_DialogNewSeason(object):
    def setupUi(self, DialogNewSeason):
        if not DialogNewSeason.objectName():
            DialogNewSeason.setObjectName(u"DialogNewSeason")
        DialogNewSeason.setWindowModality(Qt.ApplicationModal)
        DialogNewSeason.resize(400, 330)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogNewSeason.sizePolicy().hasHeightForWidth())
        DialogNewSeason.setSizePolicy(sizePolicy)
        DialogNewSeason.setMinimumSize(QSize(400, 330))
        DialogNewSeason.setMaximumSize(QSize(400, 330))
        self.formLayout = QFormLayout(DialogNewSeason)
        self.formLayout.setObjectName(u"formLayout")
        self.labelTeamID = QLabel(DialogNewSeason)
        self.labelTeamID.setObjectName(u"labelTeamID")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(16)
        self.labelTeamID.setFont(font)
        self.labelTeamID.setMargin(5)
        self.labelTeamID.setIndent(20)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelTeamID)

        self.comboBoxTeamID = QComboBox(DialogNewSeason)
        self.comboBoxTeamID.addItem("")
        self.comboBoxTeamID.setObjectName(u"comboBoxTeamID")
        sizePolicy.setHeightForWidth(self.comboBoxTeamID.sizePolicy().hasHeightForWidth())
        self.comboBoxTeamID.setSizePolicy(sizePolicy)
        self.comboBoxTeamID.setMinimumSize(QSize(250, 30))
        self.comboBoxTeamID.setMaximumSize(QSize(250, 30))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(8)
        self.comboBoxTeamID.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBoxTeamID)

        self.labelSeasonNumber = QLabel(DialogNewSeason)
        self.labelSeasonNumber.setObjectName(u"labelSeasonNumber")
        self.labelSeasonNumber.setFont(font)
        self.labelSeasonNumber.setMargin(5)
        self.labelSeasonNumber.setIndent(10)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelSeasonNumber)

        self.lineEditSeasonNumber = QLineEdit(DialogNewSeason)
        self.lineEditSeasonNumber.setObjectName(u"lineEditSeasonNumber")
        sizePolicy.setHeightForWidth(self.lineEditSeasonNumber.sizePolicy().hasHeightForWidth())
        self.lineEditSeasonNumber.setSizePolicy(sizePolicy)
        self.lineEditSeasonNumber.setMinimumSize(QSize(100, 30))
        self.lineEditSeasonNumber.setMaximumSize(QSize(100, 30))
        self.lineEditSeasonNumber.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEditSeasonNumber)

        self.buttonBox = QDialogButtonBox(DialogNewSeason)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setEnabled(True)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.buttonBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(4, QFormLayout.LabelRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(6, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(0, QFormLayout.FieldRole, self.verticalSpacer_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(8, QFormLayout.LabelRole, self.verticalSpacer_4)

        QWidget.setTabOrder(self.comboBoxTeamID, self.lineEditSeasonNumber)

        self.retranslateUi(DialogNewSeason)
        self.buttonBox.accepted.connect(DialogNewSeason.accept)
        self.buttonBox.rejected.connect(DialogNewSeason.reject)

        QMetaObject.connectSlotsByName(DialogNewSeason)
    # setupUi

    def retranslateUi(self, DialogNewSeason):
        DialogNewSeason.setWindowTitle(QCoreApplication.translate("DialogNewSeason", u"New Season", None))
        self.labelTeamID.setText(QCoreApplication.translate("DialogNewSeason", u"Team", None))
        self.comboBoxTeamID.setItemText(0, QCoreApplication.translate("DialogNewSeason", u"Penn State (Wilkinson) 51194", None))

        self.labelSeasonNumber.setText(QCoreApplication.translate("DialogNewSeason", u"Season #", None))
    # retranslateUi


