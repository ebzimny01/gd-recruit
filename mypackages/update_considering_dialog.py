from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import mypackages.config as myconfig


class Ui_DialogUpdateConsidering(object):
    def setupUi(self, DialogUpdateConsidering):
        if not DialogUpdateConsidering.objectName():
            DialogUpdateConsidering.setObjectName(u"DialogUpdateConsidering")
        DialogUpdateConsidering.setWindowModality(Qt.ApplicationModal)
        DialogUpdateConsidering.resize(400, 184)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogUpdateConsidering.sizePolicy().hasHeightForWidth())
        DialogUpdateConsidering.setSizePolicy(sizePolicy)
        DialogUpdateConsidering.setMinimumSize(QSize(400, 184))
        DialogUpdateConsidering.setMaximumSize(QSize(400, 184))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        DialogUpdateConsidering.setFont(font)
        self.gridLayout = QGridLayout(DialogUpdateConsidering)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelUpdateStatusText = QLabel(DialogUpdateConsidering)
        self.labelUpdateStatusText.setObjectName(u"labelUpdateStatusText")
        sizePolicy.setHeightForWidth(self.labelUpdateStatusText.sizePolicy().hasHeightForWidth())
        self.labelUpdateStatusText.setSizePolicy(sizePolicy)
        self.labelUpdateStatusText.setMinimumSize(QSize(350, 20))
        self.labelUpdateStatusText.setMaximumSize(QSize(350, 20))
        self.labelUpdateStatusText.setFont(font)

        self.gridLayout.addWidget(self.labelUpdateStatusText, 0, 1, 1, 1)

        self.labelCheckmarkUpdateConsidering = QLabel(DialogUpdateConsidering)
        self.labelCheckmarkUpdateConsidering.setObjectName(u"labelCheckmarkUpdateConsidering")
        sizePolicy.setHeightForWidth(self.labelCheckmarkUpdateConsidering.sizePolicy().hasHeightForWidth())
        self.labelCheckmarkUpdateConsidering.setSizePolicy(sizePolicy)
        self.labelCheckmarkUpdateConsidering.setMinimumSize(QSize(20, 20))
        self.labelCheckmarkUpdateConsidering.setMaximumSize(QSize(20, 20))
        self.labelCheckmarkUpdateConsidering.setPixmap(QPixmap(myconfig.checkmarkicon))
        self.labelCheckmarkUpdateConsidering.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckmarkUpdateConsidering, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(DialogUpdateConsidering)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.progressBarUpdateConsidering = QProgressBar(DialogUpdateConsidering)
        self.progressBarUpdateConsidering.setObjectName(u"progressBarUpdateConsidering")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBarUpdateConsidering.sizePolicy().hasHeightForWidth())
        self.progressBarUpdateConsidering.setSizePolicy(sizePolicy1)
        self.progressBarUpdateConsidering.setMinimumSize(QSize(350, 25))
        self.progressBarUpdateConsidering.setMaximumSize(QSize(167777, 25))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        self.progressBarUpdateConsidering.setFont(font1)
        self.progressBarUpdateConsidering.setStyleSheet(u"")
        self.progressBarUpdateConsidering.setValue(24)
        self.progressBarUpdateConsidering.setTextVisible(True)

        self.gridLayout.addWidget(self.progressBarUpdateConsidering, 1, 0, 1, 2)


        self.retranslateUi(DialogUpdateConsidering)
        self.buttonBox.accepted.connect(DialogUpdateConsidering.accept)
        self.buttonBox.rejected.connect(DialogUpdateConsidering.reject)

        QMetaObject.connectSlotsByName(DialogUpdateConsidering)
    # setupUi

    def retranslateUi(self, DialogUpdateConsidering):
        DialogUpdateConsidering.setWindowTitle(QCoreApplication.translate("DialogUpdateConsidering", u"Update Considering and Signed", None))
        self.labelUpdateStatusText.setText(QCoreApplication.translate("DialogUpdateConsidering", u"Grabs data/saves data to season database...", None))
        self.labelCheckmarkUpdateConsidering.setText("")
        self.progressBarUpdateConsidering.setFormat(QCoreApplication.translate("DialogUpdateConsidering", u"%v", None))
    # retranslateUi

