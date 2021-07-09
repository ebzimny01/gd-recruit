from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import mypackages.config as myconfig


class Ui_DialogMarkWatchlistPotential(object):
    def setupUi(self, DialogMarkWatchlistPotential):
        if not DialogMarkWatchlistPotential.objectName():
            DialogMarkWatchlistPotential.setObjectName(u"DialogMarkWatchlistPotential")
        DialogMarkWatchlistPotential.setWindowModality(Qt.ApplicationModal)
        DialogMarkWatchlistPotential.resize(420, 184)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogMarkWatchlistPotential.sizePolicy().hasHeightForWidth())
        DialogMarkWatchlistPotential.setSizePolicy(sizePolicy)
        DialogMarkWatchlistPotential.setMinimumSize(QSize(420, 184))
        DialogMarkWatchlistPotential.setMaximumSize(QSize(420, 184))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        DialogMarkWatchlistPotential.setFont(font)
        self.gridLayout = QGridLayout(DialogMarkWatchlistPotential)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelAuthWIS_MarkRecruits = QLabel(DialogMarkWatchlistPotential)
        self.labelAuthWIS_MarkRecruits.setObjectName(u"labelAuthWIS_MarkRecruits")
        sizePolicy.setHeightForWidth(self.labelAuthWIS_MarkRecruits.sizePolicy().hasHeightForWidth())
        self.labelAuthWIS_MarkRecruits.setSizePolicy(sizePolicy)
        self.labelAuthWIS_MarkRecruits.setMinimumSize(QSize(350, 20))
        self.labelAuthWIS_MarkRecruits.setMaximumSize(QSize(350, 20))
        self.labelAuthWIS_MarkRecruits.setFont(font)

        self.gridLayout.addWidget(self.labelAuthWIS_MarkRecruits, 0, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(DialogMarkWatchlistPotential)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 3)

        self.labelCheckMarkAuthWIS_Error_MarkRecruits = QLabel(DialogMarkWatchlistPotential)
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setObjectName(u"labelCheckMarkAuthWIS_Error_MarkRecruits")
        sizePolicy.setHeightForWidth(self.labelCheckMarkAuthWIS_Error_MarkRecruits.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setSizePolicy(sizePolicy)
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setPixmap(QPixmap(myconfig.x_icon))
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkAuthWIS_Error_MarkRecruits, 0, 0, 1, 1)

        self.labelCheckMarkAuthWIS_MarkRecruits = QLabel(DialogMarkWatchlistPotential)
        self.labelCheckMarkAuthWIS_MarkRecruits.setObjectName(u"labelCheckMarkAuthWIS_MarkRecruits")
        sizePolicy.setHeightForWidth(self.labelCheckMarkAuthWIS_MarkRecruits.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkAuthWIS_MarkRecruits.setSizePolicy(sizePolicy)
        self.labelCheckMarkAuthWIS_MarkRecruits.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS_MarkRecruits.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS_MarkRecruits.setPixmap(QPixmap(myconfig.checkmarkicon))
        self.labelCheckMarkAuthWIS_MarkRecruits.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkAuthWIS_MarkRecruits, 0, 1, 1, 1)

        self.progressBarMarkWatchlist = QProgressBar(DialogMarkWatchlistPotential)
        self.progressBarMarkWatchlist.setObjectName(u"progressBarMarkWatchlist")
        self.progressBarMarkWatchlist.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBarMarkWatchlist.sizePolicy().hasHeightForWidth())
        self.progressBarMarkWatchlist.setSizePolicy(sizePolicy1)
        self.progressBarMarkWatchlist.setMinimumSize(QSize(350, 25))
        self.progressBarMarkWatchlist.setMaximumSize(QSize(16777, 25))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        self.progressBarMarkWatchlist.setFont(font1)
        self.progressBarMarkWatchlist.setMinimum(0)
        self.progressBarMarkWatchlist.setMaximum(100)
        self.progressBarMarkWatchlist.setValue(-1)
        self.progressBarMarkWatchlist.setTextVisible(True)

        self.gridLayout.addWidget(self.progressBarMarkWatchlist, 1, 0, 1, 3)


        self.retranslateUi(DialogMarkWatchlistPotential)
        self.buttonBox.accepted.connect(DialogMarkWatchlistPotential.accept)
        self.buttonBox.rejected.connect(DialogMarkWatchlistPotential.reject)

        QMetaObject.connectSlotsByName(DialogMarkWatchlistPotential)
    # setupUi

    def retranslateUi(self, DialogMarkWatchlistPotential):
        DialogMarkWatchlistPotential.setWindowTitle(QCoreApplication.translate("DialogMarkWatchlistPotential", u"Mark Watchlist and Potential", None))
        self.labelAuthWIS_MarkRecruits.setText(QCoreApplication.translate("DialogMarkWatchlistPotential", u"Authenticate to WIS - Gridiron Dynasty", None))
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setText("")
        self.labelCheckMarkAuthWIS_MarkRecruits.setText("")
    # retranslateUi

