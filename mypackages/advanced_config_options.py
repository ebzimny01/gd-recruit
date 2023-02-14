from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_DialogAdvancedConfigOptions(object):
    def setupUi(self, DialogAdvancedConfigOptions):
        if not DialogAdvancedConfigOptions.objectName():
            DialogAdvancedConfigOptions.setObjectName(u"DialogAdvancedConfigOptions")
        DialogAdvancedConfigOptions.setWindowModality(Qt.ApplicationModal)
        DialogAdvancedConfigOptions.resize(460, 230)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogAdvancedConfigOptions.sizePolicy().hasHeightForWidth())
        DialogAdvancedConfigOptions.setSizePolicy(sizePolicy)
        DialogAdvancedConfigOptions.setMinimumSize(QSize(460, 230))
        DialogAdvancedConfigOptions.setMaximumSize(QSize(460, 230))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        DialogAdvancedConfigOptions.setFont(font)
        self.gridLayout = QGridLayout(DialogAdvancedConfigOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelAdvancedConfig = QLabel(DialogAdvancedConfigOptions)
        self.labelAdvancedConfig.setObjectName(u"labelAdvancedConfig")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelAdvancedConfig.sizePolicy().hasHeightForWidth())
        self.labelAdvancedConfig.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(20)
        self.labelAdvancedConfig.setFont(font1)
        self.labelAdvancedConfig.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelAdvancedConfig, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(DialogAdvancedConfigOptions)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)

        self.frame = QFrame(DialogAdvancedConfigOptions)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(20, 10, 20, 10)
        self.checkBoxBrowserEnableNonHeadlessMode = QCheckBox(self.frame)
        self.checkBoxBrowserEnableNonHeadlessMode.setObjectName(u"checkBoxBrowserEnableNonHeadlessMode")

        self.verticalLayout.addWidget(self.checkBoxBrowserEnableNonHeadlessMode)

        self.checkBoxEnableDebugLogging = QCheckBox(self.frame)
        self.checkBoxEnableDebugLogging.setObjectName(u"checkBoxEnableDebugLogging")

        self.verticalLayout.addWidget(self.checkBoxEnableDebugLogging)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 4, 1)


        self.retranslateUi(DialogAdvancedConfigOptions)
        self.buttonBox.accepted.connect(DialogAdvancedConfigOptions.accept)
        self.buttonBox.rejected.connect(DialogAdvancedConfigOptions.reject)

        QMetaObject.connectSlotsByName(DialogAdvancedConfigOptions)
    # setupUi

    def retranslateUi(self, DialogAdvancedConfigOptions):
        DialogAdvancedConfigOptions.setWindowTitle(QCoreApplication.translate("DialogAdvancedConfigOptions", u"Advanced Configuration Options", None))
        self.labelAdvancedConfig.setText(QCoreApplication.translate("DialogAdvancedConfigOptions", u"Advanced Configuration Options", None))
        self.checkBoxBrowserEnableNonHeadlessMode.setText(QCoreApplication.translate("DialogAdvancedConfigOptions", u"Always show browser automation", None))
        self.checkBoxEnableDebugLogging.setText(QCoreApplication.translate("DialogAdvancedConfigOptions", u"Enable debug level logging", None))
    # retranslateUi

