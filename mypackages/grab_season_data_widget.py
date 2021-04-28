from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
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

# WARNING!!!
# Pasting new code from Designer, need to make sure you replace check mark and X icons!

class Ui_WidgetGrabSeasonData(object):
    def setupUi(self, WidgetGrabSeasonData):
        if not WidgetGrabSeasonData.objectName():
            WidgetGrabSeasonData.setObjectName(u"WidgetGrabSeasonData")
        WidgetGrabSeasonData.setWindowModality(Qt.ApplicationModal)
        WidgetGrabSeasonData.resize(534, 570)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetGrabSeasonData.sizePolicy().hasHeightForWidth())
        WidgetGrabSeasonData.setSizePolicy(sizePolicy)
        WidgetGrabSeasonData.setMinimumSize(QSize(534, 570))
        WidgetGrabSeasonData.setMaximumSize(QSize(534, 570))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        WidgetGrabSeasonData.setFont(font)
        self.gridLayout_2 = QGridLayout(WidgetGrabSeasonData)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_10, 9, 0, 1, 1)

        self.labelGrabUnsigned = QLabel(WidgetGrabSeasonData)
        self.labelGrabUnsigned.setObjectName(u"labelGrabUnsigned")
        sizePolicy.setHeightForWidth(self.labelGrabUnsigned.sizePolicy().hasHeightForWidth())
        self.labelGrabUnsigned.setSizePolicy(sizePolicy)
        self.labelGrabUnsigned.setMinimumSize(QSize(350, 20))
        self.labelGrabUnsigned.setMaximumSize(QSize(350, 20))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.labelGrabUnsigned.setFont(font1)

        self.gridLayout.addWidget(self.labelGrabUnsigned, 7, 3, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_16, 21, 0, 1, 1)

        self.labelGrabSigned = QLabel(WidgetGrabSeasonData)
        self.labelGrabSigned.setObjectName(u"labelGrabSigned")
        sizePolicy.setHeightForWidth(self.labelGrabSigned.sizePolicy().hasHeightForWidth())
        self.labelGrabSigned.setSizePolicy(sizePolicy)
        self.labelGrabSigned.setMinimumSize(QSize(350, 20))
        self.labelGrabSigned.setMaximumSize(QSize(350, 20))
        self.labelGrabSigned.setFont(font1)

        self.gridLayout.addWidget(self.labelGrabSigned, 8, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 17, 3, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_11, 10, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_13, 15, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_15, 20, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_8, 7, 0, 1, 1)

        self.labelAuthWIS = QLabel(WidgetGrabSeasonData)
        self.labelAuthWIS.setObjectName(u"labelAuthWIS")
        sizePolicy.setHeightForWidth(self.labelAuthWIS.sizePolicy().hasHeightForWidth())
        self.labelAuthWIS.setSizePolicy(sizePolicy)
        self.labelAuthWIS.setMinimumSize(QSize(350, 20))
        self.labelAuthWIS.setMaximumSize(QSize(350, 20))
        self.labelAuthWIS.setFont(font1)

        self.gridLayout.addWidget(self.labelAuthWIS, 5, 3, 1, 1)

        self.labelCheckMarkGrabUnsigned = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkGrabUnsigned.setObjectName(u"labelCheckMarkGrabUnsigned")
        sizePolicy.setHeightForWidth(self.labelCheckMarkGrabUnsigned.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkGrabUnsigned.setSizePolicy(sizePolicy)
        self.labelCheckMarkGrabUnsigned.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkGrabUnsigned.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkGrabUnsigned.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkGrabUnsigned.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkGrabUnsigned, 7, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_14, 16, 0, 1, 1)

        self.labelUpdateStatusText = QLabel(WidgetGrabSeasonData)
        self.labelUpdateStatusText.setObjectName(u"labelUpdateStatusText")
        sizePolicy.setHeightForWidth(self.labelUpdateStatusText.sizePolicy().hasHeightForWidth())
        self.labelUpdateStatusText.setSizePolicy(sizePolicy)
        self.labelUpdateStatusText.setMinimumSize(QSize(350, 20))
        self.labelUpdateStatusText.setMaximumSize(QSize(350, 20))
        self.labelUpdateStatusText.setFont(font1)

        self.gridLayout.addWidget(self.labelUpdateStatusText, 15, 3, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_7, 5, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_12, 14, 0, 1, 1)

        self.labelCheckMarkAuthWIS_Error = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkAuthWIS_Error.setObjectName(u"labelCheckMarkAuthWIS_Error")
        sizePolicy.setHeightForWidth(self.labelCheckMarkAuthWIS_Error.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkAuthWIS_Error.setSizePolicy(sizePolicy)
        self.labelCheckMarkAuthWIS_Error.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS_Error.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS_Error.setPixmap(QPixmap(x_icon))
        self.labelCheckMarkAuthWIS_Error.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkAuthWIS_Error, 5, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.progressBarMarkWatchlist = QProgressBar(WidgetGrabSeasonData)
        self.progressBarMarkWatchlist.setObjectName(u"progressBarMarkWatchlist")
        self.progressBarMarkWatchlist.setEnabled(False)
        sizePolicy.setHeightForWidth(self.progressBarMarkWatchlist.sizePolicy().hasHeightForWidth())
        self.progressBarMarkWatchlist.setSizePolicy(sizePolicy)
        self.progressBarMarkWatchlist.setMinimumSize(QSize(350, 25))
        self.progressBarMarkWatchlist.setMaximumSize(QSize(350, 25))
        self.progressBarMarkWatchlist.setFont(font)
        self.progressBarMarkWatchlist.setMinimum(0)
        self.progressBarMarkWatchlist.setMaximum(100)
        self.progressBarMarkWatchlist.setValue(-1)
        self.progressBarMarkWatchlist.setTextVisible(True)

        self.gridLayout.addWidget(self.progressBarMarkWatchlist, 22, 3, 1, 1)

        self.pushButtonUpdateConsideringSigned = QPushButton(WidgetGrabSeasonData)
        self.pushButtonUpdateConsideringSigned.setObjectName(u"pushButtonUpdateConsideringSigned")
        sizePolicy.setHeightForWidth(self.pushButtonUpdateConsideringSigned.sizePolicy().hasHeightForWidth())
        self.pushButtonUpdateConsideringSigned.setSizePolicy(sizePolicy)
        self.pushButtonUpdateConsideringSigned.setMinimumSize(QSize(350, 35))
        self.pushButtonUpdateConsideringSigned.setMaximumSize(QSize(350, 35))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(18)
        self.pushButtonUpdateConsideringSigned.setFont(font2)

        self.gridLayout.addWidget(self.pushButtonUpdateConsideringSigned, 14, 3, 1, 1)

        self.labelCheckMarkGrabSigned = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkGrabSigned.setObjectName(u"labelCheckMarkGrabSigned")
        sizePolicy.setHeightForWidth(self.labelCheckMarkGrabSigned.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkGrabSigned.setSizePolicy(sizePolicy)
        self.labelCheckMarkGrabSigned.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkGrabSigned.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkGrabSigned.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkGrabSigned.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkGrabSigned, 8, 2, 1, 1)

        self.labelAuthWIS_MarkRecruits = QLabel(WidgetGrabSeasonData)
        self.labelAuthWIS_MarkRecruits.setObjectName(u"labelAuthWIS_MarkRecruits")
        sizePolicy.setHeightForWidth(self.labelAuthWIS_MarkRecruits.sizePolicy().hasHeightForWidth())
        self.labelAuthWIS_MarkRecruits.setSizePolicy(sizePolicy)
        self.labelAuthWIS_MarkRecruits.setMinimumSize(QSize(350, 20))
        self.labelAuthWIS_MarkRecruits.setMaximumSize(QSize(350, 20))
        self.labelAuthWIS_MarkRecruits.setFont(font1)

        self.gridLayout.addWidget(self.labelAuthWIS_MarkRecruits, 21, 3, 1, 1)

        self.pushButtonMarkRecruitsFromWatchlist = QPushButton(WidgetGrabSeasonData)
        self.pushButtonMarkRecruitsFromWatchlist.setObjectName(u"pushButtonMarkRecruitsFromWatchlist")
        self.pushButtonMarkRecruitsFromWatchlist.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButtonMarkRecruitsFromWatchlist.sizePolicy().hasHeightForWidth())
        self.pushButtonMarkRecruitsFromWatchlist.setSizePolicy(sizePolicy)
        self.pushButtonMarkRecruitsFromWatchlist.setMinimumSize(QSize(350, 35))
        self.pushButtonMarkRecruitsFromWatchlist.setMaximumSize(QSize(350, 35))
        self.pushButtonMarkRecruitsFromWatchlist.setFont(font2)

        self.gridLayout.addWidget(self.pushButtonMarkRecruitsFromWatchlist, 20, 3, 1, 1)

        self.labelCheckMarkAuthWIS_Error_MarkRecruits = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setObjectName(u"labelCheckMarkAuthWIS_Error_MarkRecruits")
        sizePolicy.setHeightForWidth(self.labelCheckMarkAuthWIS_Error_MarkRecruits.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setSizePolicy(sizePolicy)
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setPixmap(QPixmap(x_icon))
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkAuthWIS_Error_MarkRecruits, 21, 1, 1, 1)

        self.labelCheckmarkUpdateConsidering = QLabel(WidgetGrabSeasonData)
        self.labelCheckmarkUpdateConsidering.setObjectName(u"labelCheckmarkUpdateConsidering")
        sizePolicy.setHeightForWidth(self.labelCheckmarkUpdateConsidering.sizePolicy().hasHeightForWidth())
        self.labelCheckmarkUpdateConsidering.setSizePolicy(sizePolicy)
        self.labelCheckmarkUpdateConsidering.setMinimumSize(QSize(20, 20))
        self.labelCheckmarkUpdateConsidering.setMaximumSize(QSize(20, 20))
        self.labelCheckmarkUpdateConsidering.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckmarkUpdateConsidering.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckmarkUpdateConsidering, 15, 2, 1, 1)

        self.labelCheckMarkGrabStaticData = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkGrabStaticData.setObjectName(u"labelCheckMarkGrabStaticData")
        sizePolicy.setHeightForWidth(self.labelCheckMarkGrabStaticData.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkGrabStaticData.setSizePolicy(sizePolicy)
        self.labelCheckMarkGrabStaticData.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkGrabStaticData.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkGrabStaticData.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkGrabStaticData.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkGrabStaticData, 9, 2, 1, 1)

        self.labelGrabStaticData = QLabel(WidgetGrabSeasonData)
        self.labelGrabStaticData.setObjectName(u"labelGrabStaticData")
        sizePolicy.setHeightForWidth(self.labelGrabStaticData.sizePolicy().hasHeightForWidth())
        self.labelGrabStaticData.setSizePolicy(sizePolicy)
        self.labelGrabStaticData.setMinimumSize(QSize(350, 20))
        self.labelGrabStaticData.setMaximumSize(QSize(350, 20))
        self.labelGrabStaticData.setFont(font1)

        self.gridLayout.addWidget(self.labelGrabStaticData, 9, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.pushButtonInitializeRecruits = QPushButton(WidgetGrabSeasonData)
        self.pushButtonInitializeRecruits.setObjectName(u"pushButtonInitializeRecruits")
        sizePolicy.setHeightForWidth(self.pushButtonInitializeRecruits.sizePolicy().hasHeightForWidth())
        self.pushButtonInitializeRecruits.setSizePolicy(sizePolicy)
        self.pushButtonInitializeRecruits.setMinimumSize(QSize(350, 35))
        self.pushButtonInitializeRecruits.setMaximumSize(QSize(350, 35))
        self.pushButtonInitializeRecruits.setFont(font2)

        self.gridLayout.addWidget(self.pushButtonInitializeRecruits, 1, 3, 1, 1)

        self.labelCheckMarkCreateDB = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkCreateDB.setObjectName(u"labelCheckMarkCreateDB")
        sizePolicy.setHeightForWidth(self.labelCheckMarkCreateDB.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkCreateDB.setSizePolicy(sizePolicy)
        self.labelCheckMarkCreateDB.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkCreateDB.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkCreateDB.setLayoutDirection(Qt.LeftToRight)
        self.labelCheckMarkCreateDB.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkCreateDB.setScaledContents(True)
        self.labelCheckMarkCreateDB.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelCheckMarkCreateDB.setIndent(-1)

        self.gridLayout.addWidget(self.labelCheckMarkCreateDB, 3, 2, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_17, 22, 0, 1, 1)

        self.progressBarUpdateConsidering = QProgressBar(WidgetGrabSeasonData)
        self.progressBarUpdateConsidering.setObjectName(u"progressBarUpdateConsidering")
        sizePolicy.setHeightForWidth(self.progressBarUpdateConsidering.sizePolicy().hasHeightForWidth())
        self.progressBarUpdateConsidering.setSizePolicy(sizePolicy)
        self.progressBarUpdateConsidering.setMinimumSize(QSize(350, 25))
        self.progressBarUpdateConsidering.setMaximumSize(QSize(350, 25))
        self.progressBarUpdateConsidering.setFont(font)
        self.progressBarUpdateConsidering.setStyleSheet(u"")
        self.progressBarUpdateConsidering.setValue(24)
        self.progressBarUpdateConsidering.setTextVisible(True)

        self.gridLayout.addWidget(self.progressBarUpdateConsidering, 16, 3, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_9, 8, 0, 1, 1)

        self.labelRecruitsInitialized = QLabel(WidgetGrabSeasonData)
        self.labelRecruitsInitialized.setObjectName(u"labelRecruitsInitialized")
        sizePolicy.setHeightForWidth(self.labelRecruitsInitialized.sizePolicy().hasHeightForWidth())
        self.labelRecruitsInitialized.setSizePolicy(sizePolicy)
        self.labelRecruitsInitialized.setMinimumSize(QSize(350, 25))
        self.labelRecruitsInitialized.setMaximumSize(QSize(350, 25))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(16)
        self.labelRecruitsInitialized.setFont(font3)
        self.labelRecruitsInitialized.setStyleSheet(u"color: rgb(255, 20, 20);")
        self.labelRecruitsInitialized.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelRecruitsInitialized, 0, 3, 1, 1)

        self.line_2 = QFrame(WidgetGrabSeasonData)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 18, 0, 1, 5)

        self.labelCheckMarkAuthWIS = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkAuthWIS.setObjectName(u"labelCheckMarkAuthWIS")
        sizePolicy.setHeightForWidth(self.labelCheckMarkAuthWIS.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkAuthWIS.setSizePolicy(sizePolicy)
        self.labelCheckMarkAuthWIS.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkAuthWIS.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkAuthWIS, 5, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 11, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 19, 3, 1, 1)

        self.line = QFrame(WidgetGrabSeasonData)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 12, 0, 1, 5)

        self.labelProgressCreateRecruitDB = QLabel(WidgetGrabSeasonData)
        self.labelProgressCreateRecruitDB.setObjectName(u"labelProgressCreateRecruitDB")
        sizePolicy.setHeightForWidth(self.labelProgressCreateRecruitDB.sizePolicy().hasHeightForWidth())
        self.labelProgressCreateRecruitDB.setSizePolicy(sizePolicy)
        self.labelProgressCreateRecruitDB.setMinimumSize(QSize(350, 20))
        self.labelProgressCreateRecruitDB.setMaximumSize(QSize(350, 20))
        self.labelProgressCreateRecruitDB.setFont(font1)

        self.gridLayout.addWidget(self.labelProgressCreateRecruitDB, 3, 3, 1, 1)

        self.progressBarInitializeRecruits = QProgressBar(WidgetGrabSeasonData)
        self.progressBarInitializeRecruits.setObjectName(u"progressBarInitializeRecruits")
        sizePolicy.setHeightForWidth(self.progressBarInitializeRecruits.sizePolicy().hasHeightForWidth())
        self.progressBarInitializeRecruits.setSizePolicy(sizePolicy)
        self.progressBarInitializeRecruits.setMinimumSize(QSize(350, 25))
        self.progressBarInitializeRecruits.setMaximumSize(QSize(350, 25))
        self.progressBarInitializeRecruits.setFont(font)
        self.progressBarInitializeRecruits.setStyleSheet(u"")
        self.progressBarInitializeRecruits.setValue(24)
        self.progressBarInitializeRecruits.setTextVisible(True)

        self.gridLayout.addWidget(self.progressBarInitializeRecruits, 10, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 13, 3, 1, 1)

        self.labelCheckMarkAuthWIS_MarkRecruits = QLabel(WidgetGrabSeasonData)
        self.labelCheckMarkAuthWIS_MarkRecruits.setObjectName(u"labelCheckMarkAuthWIS_MarkRecruits")
        sizePolicy.setHeightForWidth(self.labelCheckMarkAuthWIS_MarkRecruits.sizePolicy().hasHeightForWidth())
        self.labelCheckMarkAuthWIS_MarkRecruits.setSizePolicy(sizePolicy)
        self.labelCheckMarkAuthWIS_MarkRecruits.setMinimumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS_MarkRecruits.setMaximumSize(QSize(20, 20))
        self.labelCheckMarkAuthWIS_MarkRecruits.setPixmap(QPixmap(checkmarkicon))
        self.labelCheckMarkAuthWIS_MarkRecruits.setScaledContents(True)

        self.gridLayout.addWidget(self.labelCheckMarkAuthWIS_MarkRecruits, 21, 2, 1, 1)

        self.checkBoxGrabHigherRecruits = QCheckBox(WidgetGrabSeasonData)
        self.checkBoxGrabHigherRecruits.setObjectName(u"checkBoxGrabHigherRecruits")
        sizePolicy.setHeightForWidth(self.checkBoxGrabHigherRecruits.sizePolicy().hasHeightForWidth())
        self.checkBoxGrabHigherRecruits.setSizePolicy(sizePolicy)
        self.checkBoxGrabHigherRecruits.setMinimumSize(QSize(350, 25))
        self.checkBoxGrabHigherRecruits.setMaximumSize(QSize(350, 25))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(8)
        self.checkBoxGrabHigherRecruits.setFont(font4)
        self.checkBoxGrabHigherRecruits.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.checkBoxGrabHigherRecruits, 2, 3, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_18, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(WidgetGrabSeasonData)

        QMetaObject.connectSlotsByName(WidgetGrabSeasonData)
    # setupUi

    def retranslateUi(self, WidgetGrabSeasonData):
        WidgetGrabSeasonData.setWindowTitle(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Recruit Data", None))
        self.labelGrabUnsigned.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Unsigned Recruits", None))
        self.labelGrabSigned.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Signed Recruits", None))
        self.labelAuthWIS.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Authenticate to WIS - Gridiron Dynasty", None))
        self.labelCheckMarkGrabUnsigned.setText("")
        self.labelUpdateStatusText.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Grabs data/saves data to season database...", None))
        self.labelCheckMarkAuthWIS_Error.setText("")
        self.pushButtonUpdateConsideringSigned.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Update Considering / Signed", None))
        self.labelCheckMarkGrabSigned.setText("")
        self.labelAuthWIS_MarkRecruits.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Authenticate to WIS - Gridiron Dynasty", None))
        self.pushButtonMarkRecruitsFromWatchlist.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Mark Watchlist and Potential", None))
        self.labelCheckMarkAuthWIS_Error_MarkRecruits.setText("")
        self.labelCheckmarkUpdateConsidering.setText("")
        self.labelCheckMarkGrabStaticData.setText("")
        self.labelGrabStaticData.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab Recruit Static Ratings Data and GPA", None))
        self.pushButtonInitializeRecruits.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Initialize Recruits", None))
        self.labelCheckMarkCreateDB.setText("")
        self.progressBarUpdateConsidering.setFormat(QCoreApplication.translate("WidgetGrabSeasonData", u"%v", None))
        self.labelRecruitsInitialized.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Recruits Initialized = 0", None))
        self.labelCheckMarkAuthWIS.setText("")
        self.labelProgressCreateRecruitDB.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Create / Re-create Recruit Database Table", None))
        self.labelCheckMarkAuthWIS_MarkRecruits.setText("")
        self.checkBoxGrabHigherRecruits.setText(QCoreApplication.translate("WidgetGrabSeasonData", u"Grab recruits from 1 division higher (valid for DIII, DII, DIAA only)", None))
    # retranslateUi

