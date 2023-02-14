from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_DialogBoldAttributes(object):
    def setupUi(self, DialogBoldAttributes):
        if not DialogBoldAttributes.objectName():
            DialogBoldAttributes.setObjectName(u"DialogBoldAttributes")
        DialogBoldAttributes.setWindowModality(Qt.WindowModal)
        DialogBoldAttributes.resize(675, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogBoldAttributes.sizePolicy().hasHeightForWidth())
        DialogBoldAttributes.setSizePolicy(sizePolicy)
        DialogBoldAttributes.setMinimumSize(QSize(675, 460))
        DialogBoldAttributes.setMaximumSize(QSize(675, 460))
        self.buttonBox = QDialogButtonBox(DialogBoldAttributes)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(470, 400, 171, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.label = QLabel(DialogBoldAttributes)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 471, 31))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: blue;")
        self.gridLayoutWidget = QWidget(DialogBoldAttributes)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 70, 631, 295))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.checkBox_DB_DUR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DB_DUR.setObjectName(u"checkBox_DB_DUR")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_DB_DUR.sizePolicy().hasHeightForWidth())
        self.checkBox_DB_DUR.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Arial")
        self.checkBox_DB_DUR.setFont(font1)
        self.checkBox_DB_DUR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DB_DUR.setIconSize(QSize(16, 16))
        self.checkBox_DB_DUR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DB_DUR, 8, 3, 1, 1)

        self.label_BLK = QLabel(self.gridLayoutWidget)
        self.label_BLK.setObjectName(u"label_BLK")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(10)
        self.label_BLK.setFont(font2)
        self.label_BLK.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_BLK, 0, 7, 1, 1)

        self.checkBox_WR_ELU = QCheckBox(self.gridLayoutWidget)
        self.checkBox_WR_ELU.setObjectName(u"checkBox_WR_ELU")
        sizePolicy1.setHeightForWidth(self.checkBox_WR_ELU.sizePolicy().hasHeightForWidth())
        self.checkBox_WR_ELU.setSizePolicy(sizePolicy1)
        self.checkBox_WR_ELU.setFont(font1)
        self.checkBox_WR_ELU.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_WR_ELU.setIconSize(QSize(16, 16))
        self.checkBox_WR_ELU.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_WR_ELU, 3, 11, 1, 1)

        self.checkBox_DB_GI = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DB_GI.setObjectName(u"checkBox_DB_GI")
        sizePolicy1.setHeightForWidth(self.checkBox_DB_GI.sizePolicy().hasHeightForWidth())
        self.checkBox_DB_GI.setSizePolicy(sizePolicy1)
        self.checkBox_DB_GI.setFont(font1)
        self.checkBox_DB_GI.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DB_GI.setIconSize(QSize(16, 16))
        self.checkBox_DB_GI.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DB_GI, 8, 10, 1, 1)

        self.checkBox_TE_DUR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_TE_DUR.setObjectName(u"checkBox_TE_DUR")
        sizePolicy1.setHeightForWidth(self.checkBox_TE_DUR.sizePolicy().hasHeightForWidth())
        self.checkBox_TE_DUR.setSizePolicy(sizePolicy1)
        self.checkBox_TE_DUR.setFont(font1)
        self.checkBox_TE_DUR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_TE_DUR.setIconSize(QSize(16, 16))
        self.checkBox_TE_DUR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_TE_DUR, 4, 3, 1, 1)

        self.label_ELU = QLabel(self.gridLayoutWidget)
        self.label_ELU.setObjectName(u"label_ELU")
        self.label_ELU.setFont(font2)
        self.label_ELU.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_ELU, 0, 11, 1, 1)

        self.checkBox_P_WE = QCheckBox(self.gridLayoutWidget)
        self.checkBox_P_WE.setObjectName(u"checkBox_P_WE")
        sizePolicy1.setHeightForWidth(self.checkBox_P_WE.sizePolicy().hasHeightForWidth())
        self.checkBox_P_WE.setSizePolicy(sizePolicy1)
        self.checkBox_P_WE.setFont(font1)
        self.checkBox_P_WE.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_P_WE.setIconSize(QSize(16, 16))
        self.checkBox_P_WE.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_P_WE, 10, 4, 1, 1)

        self.checkBox_OL_ATH = QCheckBox(self.gridLayoutWidget)
        self.checkBox_OL_ATH.setObjectName(u"checkBox_OL_ATH")
        sizePolicy1.setHeightForWidth(self.checkBox_OL_ATH.sizePolicy().hasHeightForWidth())
        self.checkBox_OL_ATH.setSizePolicy(sizePolicy1)
        self.checkBox_OL_ATH.setFont(font1)
        self.checkBox_OL_ATH.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_OL_ATH.setIconSize(QSize(16, 16))
        self.checkBox_OL_ATH.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_OL_ATH, 5, 1, 1, 1)

        self.checkBox_P_DUR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_P_DUR.setObjectName(u"checkBox_P_DUR")
        sizePolicy1.setHeightForWidth(self.checkBox_P_DUR.sizePolicy().hasHeightForWidth())
        self.checkBox_P_DUR.setSizePolicy(sizePolicy1)
        self.checkBox_P_DUR.setFont(font1)
        self.checkBox_P_DUR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_P_DUR.setIconSize(QSize(16, 16))
        self.checkBox_P_DUR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_P_DUR, 10, 3, 1, 1)

        self.checkBox_WR_DUR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_WR_DUR.setObjectName(u"checkBox_WR_DUR")
        sizePolicy1.setHeightForWidth(self.checkBox_WR_DUR.sizePolicy().hasHeightForWidth())
        self.checkBox_WR_DUR.setSizePolicy(sizePolicy1)
        self.checkBox_WR_DUR.setFont(font1)
        self.checkBox_WR_DUR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_WR_DUR.setIconSize(QSize(16, 16))
        self.checkBox_WR_DUR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_WR_DUR, 3, 3, 1, 1)

        self.checkBox_DL_ATH = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DL_ATH.setObjectName(u"checkBox_DL_ATH")
        sizePolicy1.setHeightForWidth(self.checkBox_DL_ATH.sizePolicy().hasHeightForWidth())
        self.checkBox_DL_ATH.setSizePolicy(sizePolicy1)
        self.checkBox_DL_ATH.setFont(font1)
        self.checkBox_DL_ATH.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DL_ATH.setIconSize(QSize(16, 16))
        self.checkBox_DL_ATH.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DL_ATH, 6, 1, 1, 1)

        self.checkBox_LB_DUR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_LB_DUR.setObjectName(u"checkBox_LB_DUR")
        sizePolicy1.setHeightForWidth(self.checkBox_LB_DUR.sizePolicy().hasHeightForWidth())
        self.checkBox_LB_DUR.setSizePolicy(sizePolicy1)
        self.checkBox_LB_DUR.setFont(font1)
        self.checkBox_LB_DUR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_LB_DUR.setIconSize(QSize(16, 16))
        self.checkBox_LB_DUR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_LB_DUR, 7, 3, 1, 1)

        self.checkBox_OL_DUR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_OL_DUR.setObjectName(u"checkBox_OL_DUR")
        sizePolicy1.setHeightForWidth(self.checkBox_OL_DUR.sizePolicy().hasHeightForWidth())
        self.checkBox_OL_DUR.setSizePolicy(sizePolicy1)
        self.checkBox_OL_DUR.setFont(font1)
        self.checkBox_OL_DUR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_OL_DUR.setIconSize(QSize(16, 16))
        self.checkBox_OL_DUR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_OL_DUR, 5, 3, 1, 1)

        self.checkBox_RB_TEC = QCheckBox(self.gridLayoutWidget)
        self.checkBox_RB_TEC.setObjectName(u"checkBox_RB_TEC")
        sizePolicy1.setHeightForWidth(self.checkBox_RB_TEC.sizePolicy().hasHeightForWidth())
        self.checkBox_RB_TEC.setSizePolicy(sizePolicy1)
        self.checkBox_RB_TEC.setFont(font1)
        self.checkBox_RB_TEC.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_RB_TEC.setIconSize(QSize(16, 16))
        self.checkBox_RB_TEC.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_RB_TEC, 2, 12, 1, 1)

        self.checkBox_LB_TEC = QCheckBox(self.gridLayoutWidget)
        self.checkBox_LB_TEC.setObjectName(u"checkBox_LB_TEC")
        sizePolicy1.setHeightForWidth(self.checkBox_LB_TEC.sizePolicy().hasHeightForWidth())
        self.checkBox_LB_TEC.setSizePolicy(sizePolicy1)
        self.checkBox_LB_TEC.setFont(font1)
        self.checkBox_LB_TEC.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_LB_TEC.setIconSize(QSize(16, 16))
        self.checkBox_LB_TEC.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_LB_TEC, 7, 12, 1, 1)

        self.checkBox_QB_TEC = QCheckBox(self.gridLayoutWidget)
        self.checkBox_QB_TEC.setObjectName(u"checkBox_QB_TEC")
        sizePolicy1.setHeightForWidth(self.checkBox_QB_TEC.sizePolicy().hasHeightForWidth())
        self.checkBox_QB_TEC.setSizePolicy(sizePolicy1)
        self.checkBox_QB_TEC.setFont(font1)
        self.checkBox_QB_TEC.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_QB_TEC.setIconSize(QSize(16, 16))
        self.checkBox_QB_TEC.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_QB_TEC, 1, 12, 1, 1)

        self.checkBox_LB_HAN = QCheckBox(self.gridLayoutWidget)
        self.checkBox_LB_HAN.setObjectName(u"checkBox_LB_HAN")
        sizePolicy1.setHeightForWidth(self.checkBox_LB_HAN.sizePolicy().hasHeightForWidth())
        self.checkBox_LB_HAN.setSizePolicy(sizePolicy1)
        self.checkBox_LB_HAN.setFont(font1)
        self.checkBox_LB_HAN.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_LB_HAN.setIconSize(QSize(16, 16))
        self.checkBox_LB_HAN.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_LB_HAN, 7, 9, 1, 1)

        self.checkBox_QB_ELU = QCheckBox(self.gridLayoutWidget)
        self.checkBox_QB_ELU.setObjectName(u"checkBox_QB_ELU")
        sizePolicy1.setHeightForWidth(self.checkBox_QB_ELU.sizePolicy().hasHeightForWidth())
        self.checkBox_QB_ELU.setSizePolicy(sizePolicy1)
        self.checkBox_QB_ELU.setFont(font1)
        self.checkBox_QB_ELU.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_QB_ELU.setIconSize(QSize(16, 16))
        self.checkBox_QB_ELU.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_QB_ELU, 1, 11, 1, 1)

        self.checkBox_K_WE = QCheckBox(self.gridLayoutWidget)
        self.checkBox_K_WE.setObjectName(u"checkBox_K_WE")
        sizePolicy.setHeightForWidth(self.checkBox_K_WE.sizePolicy().hasHeightForWidth())
        self.checkBox_K_WE.setSizePolicy(sizePolicy)
        self.checkBox_K_WE.setFont(font1)
        self.checkBox_K_WE.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_K_WE.setIconSize(QSize(20, 20))
        self.checkBox_K_WE.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_K_WE, 9, 4, 1, 1)

        self.label_WR = QLabel(self.gridLayoutWidget)
        self.label_WR.setObjectName(u"label_WR")
        self.label_WR.setFont(font2)
        self.label_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_WR, 3, 0, 1, 1)

        self.checkBox_DL_STR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DL_STR.setObjectName(u"checkBox_DL_STR")
        sizePolicy1.setHeightForWidth(self.checkBox_DL_STR.sizePolicy().hasHeightForWidth())
        self.checkBox_DL_STR.setSizePolicy(sizePolicy1)
        self.checkBox_DL_STR.setFont(font1)
        self.checkBox_DL_STR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DL_STR.setIconSize(QSize(16, 16))
        self.checkBox_DL_STR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DL_STR, 6, 6, 1, 1)

        self.checkBox_DL_HAN = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DL_HAN.setObjectName(u"checkBox_DL_HAN")
        sizePolicy1.setHeightForWidth(self.checkBox_DL_HAN.sizePolicy().hasHeightForWidth())
        self.checkBox_DL_HAN.setSizePolicy(sizePolicy1)
        self.checkBox_DL_HAN.setFont(font1)
        self.checkBox_DL_HAN.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DL_HAN.setIconSize(QSize(16, 16))
        self.checkBox_DL_HAN.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DL_HAN, 6, 9, 1, 1)

        self.checkBox_RB_ELU = QCheckBox(self.gridLayoutWidget)
        self.checkBox_RB_ELU.setObjectName(u"checkBox_RB_ELU")
        sizePolicy1.setHeightForWidth(self.checkBox_RB_ELU.sizePolicy().hasHeightForWidth())
        self.checkBox_RB_ELU.setSizePolicy(sizePolicy1)
        self.checkBox_RB_ELU.setFont(font1)
        self.checkBox_RB_ELU.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_RB_ELU.setIconSize(QSize(16, 16))
        self.checkBox_RB_ELU.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_RB_ELU, 2, 11, 1, 1)

        self.checkBox_DB_TEC = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DB_TEC.setObjectName(u"checkBox_DB_TEC")
        sizePolicy1.setHeightForWidth(self.checkBox_DB_TEC.sizePolicy().hasHeightForWidth())
        self.checkBox_DB_TEC.setSizePolicy(sizePolicy1)
        self.checkBox_DB_TEC.setFont(font1)
        self.checkBox_DB_TEC.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DB_TEC.setIconSize(QSize(16, 16))
        self.checkBox_DB_TEC.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DB_TEC, 8, 12, 1, 1)

        self.checkBox_OL_STR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_OL_STR.setObjectName(u"checkBox_OL_STR")
        sizePolicy1.setHeightForWidth(self.checkBox_OL_STR.sizePolicy().hasHeightForWidth())
        self.checkBox_OL_STR.setSizePolicy(sizePolicy1)
        self.checkBox_OL_STR.setFont(font1)
        self.checkBox_OL_STR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_OL_STR.setIconSize(QSize(16, 16))
        self.checkBox_OL_STR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_OL_STR, 5, 6, 1, 1)

        self.checkBox_RB_GI = QCheckBox(self.gridLayoutWidget)
        self.checkBox_RB_GI.setObjectName(u"checkBox_RB_GI")
        sizePolicy1.setHeightForWidth(self.checkBox_RB_GI.sizePolicy().hasHeightForWidth())
        self.checkBox_RB_GI.setSizePolicy(sizePolicy1)
        self.checkBox_RB_GI.setFont(font1)
        self.checkBox_RB_GI.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_RB_GI.setIconSize(QSize(20, 20))
        self.checkBox_RB_GI.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_RB_GI, 2, 10, 1, 1)

        self.checkBox_WR_HAN = QCheckBox(self.gridLayoutWidget)
        self.checkBox_WR_HAN.setObjectName(u"checkBox_WR_HAN")
        sizePolicy1.setHeightForWidth(self.checkBox_WR_HAN.sizePolicy().hasHeightForWidth())
        self.checkBox_WR_HAN.setSizePolicy(sizePolicy1)
        self.checkBox_WR_HAN.setFont(font1)
        self.checkBox_WR_HAN.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_WR_HAN.setIconSize(QSize(16, 16))
        self.checkBox_WR_HAN.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_WR_HAN, 3, 9, 1, 1)

        self.checkBox_TE_HAN = QCheckBox(self.gridLayoutWidget)
        self.checkBox_TE_HAN.setObjectName(u"checkBox_TE_HAN")
        sizePolicy1.setHeightForWidth(self.checkBox_TE_HAN.sizePolicy().hasHeightForWidth())
        self.checkBox_TE_HAN.setSizePolicy(sizePolicy1)
        self.checkBox_TE_HAN.setFont(font1)
        self.checkBox_TE_HAN.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_TE_HAN.setIconSize(QSize(16, 16))
        self.checkBox_TE_HAN.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_TE_HAN, 4, 9, 1, 1)

        self.checkBox_DL_DUR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DL_DUR.setObjectName(u"checkBox_DL_DUR")
        sizePolicy1.setHeightForWidth(self.checkBox_DL_DUR.sizePolicy().hasHeightForWidth())
        self.checkBox_DL_DUR.setSizePolicy(sizePolicy1)
        self.checkBox_DL_DUR.setFont(font1)
        self.checkBox_DL_DUR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DL_DUR.setIconSize(QSize(16, 16))
        self.checkBox_DL_DUR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DL_DUR, 6, 3, 1, 1)

        self.checkBox_DB_HAN = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DB_HAN.setObjectName(u"checkBox_DB_HAN")
        sizePolicy1.setHeightForWidth(self.checkBox_DB_HAN.sizePolicy().hasHeightForWidth())
        self.checkBox_DB_HAN.setSizePolicy(sizePolicy1)
        self.checkBox_DB_HAN.setFont(font1)
        self.checkBox_DB_HAN.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DB_HAN.setIconSize(QSize(16, 16))
        self.checkBox_DB_HAN.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DB_HAN, 8, 9, 1, 1)

        self.checkBox_OL_ELU = QCheckBox(self.gridLayoutWidget)
        self.checkBox_OL_ELU.setObjectName(u"checkBox_OL_ELU")
        sizePolicy1.setHeightForWidth(self.checkBox_OL_ELU.sizePolicy().hasHeightForWidth())
        self.checkBox_OL_ELU.setSizePolicy(sizePolicy1)
        self.checkBox_OL_ELU.setFont(font1)
        self.checkBox_OL_ELU.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_OL_ELU.setIconSize(QSize(16, 16))
        self.checkBox_OL_ELU.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_OL_ELU, 5, 11, 1, 1)

        self.checkBox_WR_STR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_WR_STR.setObjectName(u"checkBox_WR_STR")
        sizePolicy1.setHeightForWidth(self.checkBox_WR_STR.sizePolicy().hasHeightForWidth())
        self.checkBox_WR_STR.setSizePolicy(sizePolicy1)
        self.checkBox_WR_STR.setFont(font1)
        self.checkBox_WR_STR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_WR_STR.setIconSize(QSize(16, 16))
        self.checkBox_WR_STR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_WR_STR, 3, 6, 1, 1)

        self.checkBox_DL_STA = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DL_STA.setObjectName(u"checkBox_DL_STA")
        sizePolicy1.setHeightForWidth(self.checkBox_DL_STA.sizePolicy().hasHeightForWidth())
        self.checkBox_DL_STA.setSizePolicy(sizePolicy1)
        self.checkBox_DL_STA.setFont(font1)
        self.checkBox_DL_STA.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DL_STA.setIconSize(QSize(16, 16))
        self.checkBox_DL_STA.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DL_STA, 6, 5, 1, 1)

        self.checkBox_DB_STA = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DB_STA.setObjectName(u"checkBox_DB_STA")
        sizePolicy1.setHeightForWidth(self.checkBox_DB_STA.sizePolicy().hasHeightForWidth())
        self.checkBox_DB_STA.setSizePolicy(sizePolicy1)
        self.checkBox_DB_STA.setFont(font1)
        self.checkBox_DB_STA.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DB_STA.setIconSize(QSize(16, 16))
        self.checkBox_DB_STA.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DB_STA, 8, 5, 1, 1)

        self.checkBox_P_ATH = QCheckBox(self.gridLayoutWidget)
        self.checkBox_P_ATH.setObjectName(u"checkBox_P_ATH")
        sizePolicy1.setHeightForWidth(self.checkBox_P_ATH.sizePolicy().hasHeightForWidth())
        self.checkBox_P_ATH.setSizePolicy(sizePolicy1)
        self.checkBox_P_ATH.setFont(font1)
        self.checkBox_P_ATH.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_P_ATH.setIconSize(QSize(16, 16))
        self.checkBox_P_ATH.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_P_ATH, 10, 1, 1, 1)

        self.checkBox_QB_GI = QCheckBox(self.gridLayoutWidget)
        self.checkBox_QB_GI.setObjectName(u"checkBox_QB_GI")
        sizePolicy1.setHeightForWidth(self.checkBox_QB_GI.sizePolicy().hasHeightForWidth())
        self.checkBox_QB_GI.setSizePolicy(sizePolicy1)
        self.checkBox_QB_GI.setFont(font1)
        self.checkBox_QB_GI.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_QB_GI.setIconSize(QSize(16, 16))
        self.checkBox_QB_GI.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_QB_GI, 1, 10, 1, 1)

        self.checkBox_DL_SPD = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DL_SPD.setObjectName(u"checkBox_DL_SPD")
        sizePolicy1.setHeightForWidth(self.checkBox_DL_SPD.sizePolicy().hasHeightForWidth())
        self.checkBox_DL_SPD.setSizePolicy(sizePolicy1)
        self.checkBox_DL_SPD.setFont(font1)
        self.checkBox_DL_SPD.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DL_SPD.setIconSize(QSize(16, 16))
        self.checkBox_DL_SPD.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DL_SPD, 6, 2, 1, 1)

        self.checkBox_P_HAN = QCheckBox(self.gridLayoutWidget)
        self.checkBox_P_HAN.setObjectName(u"checkBox_P_HAN")
        sizePolicy1.setHeightForWidth(self.checkBox_P_HAN.sizePolicy().hasHeightForWidth())
        self.checkBox_P_HAN.setSizePolicy(sizePolicy1)
        self.checkBox_P_HAN.setFont(font1)
        self.checkBox_P_HAN.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_P_HAN.setIconSize(QSize(16, 16))
        self.checkBox_P_HAN.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_P_HAN, 10, 9, 1, 1)

        self.checkBox_DL_ELU = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DL_ELU.setObjectName(u"checkBox_DL_ELU")
        sizePolicy1.setHeightForWidth(self.checkBox_DL_ELU.sizePolicy().hasHeightForWidth())
        self.checkBox_DL_ELU.setSizePolicy(sizePolicy1)
        self.checkBox_DL_ELU.setFont(font1)
        self.checkBox_DL_ELU.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DL_ELU.setIconSize(QSize(16, 16))
        self.checkBox_DL_ELU.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DL_ELU, 6, 11, 1, 1)

        self.checkBox_TE_ATH = QCheckBox(self.gridLayoutWidget)
        self.checkBox_TE_ATH.setObjectName(u"checkBox_TE_ATH")
        sizePolicy1.setHeightForWidth(self.checkBox_TE_ATH.sizePolicy().hasHeightForWidth())
        self.checkBox_TE_ATH.setSizePolicy(sizePolicy1)
        self.checkBox_TE_ATH.setFont(font1)
        self.checkBox_TE_ATH.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_TE_ATH.setIconSize(QSize(16, 16))
        self.checkBox_TE_ATH.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_TE_ATH, 4, 1, 1, 1)

        self.checkBox_DL_TKL = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DL_TKL.setObjectName(u"checkBox_DL_TKL")
        sizePolicy1.setHeightForWidth(self.checkBox_DL_TKL.sizePolicy().hasHeightForWidth())
        self.checkBox_DL_TKL.setSizePolicy(sizePolicy1)
        self.checkBox_DL_TKL.setFont(font1)
        self.checkBox_DL_TKL.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DL_TKL.setIconSize(QSize(16, 16))
        self.checkBox_DL_TKL.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DL_TKL, 6, 8, 1, 1)

        self.checkBox_OL_STA = QCheckBox(self.gridLayoutWidget)
        self.checkBox_OL_STA.setObjectName(u"checkBox_OL_STA")
        sizePolicy1.setHeightForWidth(self.checkBox_OL_STA.sizePolicy().hasHeightForWidth())
        self.checkBox_OL_STA.setSizePolicy(sizePolicy1)
        self.checkBox_OL_STA.setFont(font1)
        self.checkBox_OL_STA.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_OL_STA.setIconSize(QSize(16, 16))
        self.checkBox_OL_STA.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_OL_STA, 5, 5, 1, 1)

        self.checkBox_QB_SPD = QCheckBox(self.gridLayoutWidget)
        self.checkBox_QB_SPD.setObjectName(u"checkBox_QB_SPD")
        sizePolicy1.setHeightForWidth(self.checkBox_QB_SPD.sizePolicy().hasHeightForWidth())
        self.checkBox_QB_SPD.setSizePolicy(sizePolicy1)
        self.checkBox_QB_SPD.setFont(font1)
        self.checkBox_QB_SPD.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_QB_SPD.setIconSize(QSize(16, 16))
        self.checkBox_QB_SPD.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_QB_SPD, 1, 2, 1, 1)

        self.checkBox_K_BLK = QCheckBox(self.gridLayoutWidget)
        self.checkBox_K_BLK.setObjectName(u"checkBox_K_BLK")
        sizePolicy1.setHeightForWidth(self.checkBox_K_BLK.sizePolicy().hasHeightForWidth())
        self.checkBox_K_BLK.setSizePolicy(sizePolicy1)
        self.checkBox_K_BLK.setFont(font1)
        self.checkBox_K_BLK.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_K_BLK.setIconSize(QSize(16, 16))
        self.checkBox_K_BLK.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_K_BLK, 9, 7, 1, 1)

        self.checkBox_TE_TEC = QCheckBox(self.gridLayoutWidget)
        self.checkBox_TE_TEC.setObjectName(u"checkBox_TE_TEC")
        sizePolicy1.setHeightForWidth(self.checkBox_TE_TEC.sizePolicy().hasHeightForWidth())
        self.checkBox_TE_TEC.setSizePolicy(sizePolicy1)
        self.checkBox_TE_TEC.setFont(font1)
        self.checkBox_TE_TEC.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_TE_TEC.setIconSize(QSize(16, 16))
        self.checkBox_TE_TEC.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_TE_TEC, 4, 12, 1, 1)

        self.label_RB = QLabel(self.gridLayoutWidget)
        self.label_RB.setObjectName(u"label_RB")
        self.label_RB.setFont(font2)
        self.label_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_RB, 2, 0, 1, 1)

        self.checkBox_DB_SPD = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DB_SPD.setObjectName(u"checkBox_DB_SPD")
        sizePolicy1.setHeightForWidth(self.checkBox_DB_SPD.sizePolicy().hasHeightForWidth())
        self.checkBox_DB_SPD.setSizePolicy(sizePolicy1)
        self.checkBox_DB_SPD.setFont(font1)
        self.checkBox_DB_SPD.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DB_SPD.setIconSize(QSize(16, 16))
        self.checkBox_DB_SPD.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DB_SPD, 8, 2, 1, 1)

        self.checkBox_RB_TKL = QCheckBox(self.gridLayoutWidget)
        self.checkBox_RB_TKL.setObjectName(u"checkBox_RB_TKL")
        sizePolicy1.setHeightForWidth(self.checkBox_RB_TKL.sizePolicy().hasHeightForWidth())
        self.checkBox_RB_TKL.setSizePolicy(sizePolicy1)
        self.checkBox_RB_TKL.setFont(font1)
        self.checkBox_RB_TKL.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_RB_TKL.setIconSize(QSize(16, 16))
        self.checkBox_RB_TKL.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_RB_TKL, 2, 8, 1, 1)

        self.checkBox_TE_TKL = QCheckBox(self.gridLayoutWidget)
        self.checkBox_TE_TKL.setObjectName(u"checkBox_TE_TKL")
        sizePolicy1.setHeightForWidth(self.checkBox_TE_TKL.sizePolicy().hasHeightForWidth())
        self.checkBox_TE_TKL.setSizePolicy(sizePolicy1)
        self.checkBox_TE_TKL.setFont(font1)
        self.checkBox_TE_TKL.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_TE_TKL.setIconSize(QSize(16, 16))
        self.checkBox_TE_TKL.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_TE_TKL, 4, 8, 1, 1)

        self.label_DB = QLabel(self.gridLayoutWidget)
        self.label_DB.setObjectName(u"label_DB")
        self.label_DB.setFont(font2)
        self.label_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_DB, 8, 0, 1, 1)

        self.checkBox_LB_STA = QCheckBox(self.gridLayoutWidget)
        self.checkBox_LB_STA.setObjectName(u"checkBox_LB_STA")
        sizePolicy.setHeightForWidth(self.checkBox_LB_STA.sizePolicy().hasHeightForWidth())
        self.checkBox_LB_STA.setSizePolicy(sizePolicy)
        self.checkBox_LB_STA.setFont(font1)
        self.checkBox_LB_STA.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_LB_STA.setIconSize(QSize(20, 20))
        self.checkBox_LB_STA.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_LB_STA, 7, 5, 1, 1)

        self.checkBox_DL_WE = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DL_WE.setObjectName(u"checkBox_DL_WE")
        sizePolicy1.setHeightForWidth(self.checkBox_DL_WE.sizePolicy().hasHeightForWidth())
        self.checkBox_DL_WE.setSizePolicy(sizePolicy1)
        self.checkBox_DL_WE.setFont(font1)
        self.checkBox_DL_WE.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DL_WE.setIconSize(QSize(16, 16))
        self.checkBox_DL_WE.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DL_WE, 6, 4, 1, 1)

        self.checkBox_LB_BLK = QCheckBox(self.gridLayoutWidget)
        self.checkBox_LB_BLK.setObjectName(u"checkBox_LB_BLK")
        sizePolicy1.setHeightForWidth(self.checkBox_LB_BLK.sizePolicy().hasHeightForWidth())
        self.checkBox_LB_BLK.setSizePolicy(sizePolicy1)
        self.checkBox_LB_BLK.setFont(font1)
        self.checkBox_LB_BLK.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_LB_BLK.setIconSize(QSize(16, 16))
        self.checkBox_LB_BLK.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_LB_BLK, 7, 7, 1, 1)

        self.label_ATH = QLabel(self.gridLayoutWidget)
        self.label_ATH.setObjectName(u"label_ATH")
        self.label_ATH.setFont(font2)
        self.label_ATH.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_ATH, 0, 1, 1, 1)

        self.checkBox_K_TEC = QCheckBox(self.gridLayoutWidget)
        self.checkBox_K_TEC.setObjectName(u"checkBox_K_TEC")
        sizePolicy1.setHeightForWidth(self.checkBox_K_TEC.sizePolicy().hasHeightForWidth())
        self.checkBox_K_TEC.setSizePolicy(sizePolicy1)
        self.checkBox_K_TEC.setFont(font1)
        self.checkBox_K_TEC.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_K_TEC.setIconSize(QSize(16, 16))
        self.checkBox_K_TEC.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_K_TEC, 9, 12, 1, 1)

        self.label_STA = QLabel(self.gridLayoutWidget)
        self.label_STA.setObjectName(u"label_STA")
        self.label_STA.setFont(font2)
        self.label_STA.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_STA, 0, 5, 1, 1)

        self.label_QB = QLabel(self.gridLayoutWidget)
        self.label_QB.setObjectName(u"label_QB")
        self.label_QB.setFont(font2)
        self.label_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_QB, 1, 0, 1, 1)

        self.checkBox_RB_DUR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_RB_DUR.setObjectName(u"checkBox_RB_DUR")
        sizePolicy1.setHeightForWidth(self.checkBox_RB_DUR.sizePolicy().hasHeightForWidth())
        self.checkBox_RB_DUR.setSizePolicy(sizePolicy1)
        self.checkBox_RB_DUR.setFont(font1)
        self.checkBox_RB_DUR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_RB_DUR.setIconSize(QSize(16, 16))
        self.checkBox_RB_DUR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_RB_DUR, 2, 3, 1, 1)

        self.label_GI = QLabel(self.gridLayoutWidget)
        self.label_GI.setObjectName(u"label_GI")
        self.label_GI.setFont(font2)
        self.label_GI.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_GI, 0, 10, 1, 1)

        self.label_DUR = QLabel(self.gridLayoutWidget)
        self.label_DUR.setObjectName(u"label_DUR")
        self.label_DUR.setFont(font2)
        self.label_DUR.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_DUR, 0, 3, 1, 1)

        self.checkBox_P_TEC = QCheckBox(self.gridLayoutWidget)
        self.checkBox_P_TEC.setObjectName(u"checkBox_P_TEC")
        sizePolicy1.setHeightForWidth(self.checkBox_P_TEC.sizePolicy().hasHeightForWidth())
        self.checkBox_P_TEC.setSizePolicy(sizePolicy1)
        self.checkBox_P_TEC.setFont(font1)
        self.checkBox_P_TEC.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_P_TEC.setIconSize(QSize(16, 16))
        self.checkBox_P_TEC.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_P_TEC, 10, 12, 1, 1)

        self.checkBox_QB_STR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_QB_STR.setObjectName(u"checkBox_QB_STR")
        sizePolicy1.setHeightForWidth(self.checkBox_QB_STR.sizePolicy().hasHeightForWidth())
        self.checkBox_QB_STR.setSizePolicy(sizePolicy1)
        self.checkBox_QB_STR.setFont(font1)
        self.checkBox_QB_STR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_QB_STR.setIconSize(QSize(16, 16))
        self.checkBox_QB_STR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_QB_STR, 1, 6, 1, 1)

        self.label_TEC = QLabel(self.gridLayoutWidget)
        self.label_TEC.setObjectName(u"label_TEC")
        self.label_TEC.setFont(font2)
        self.label_TEC.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_TEC, 0, 12, 1, 1)

        self.checkBox_WR_TKL = QCheckBox(self.gridLayoutWidget)
        self.checkBox_WR_TKL.setObjectName(u"checkBox_WR_TKL")
        sizePolicy1.setHeightForWidth(self.checkBox_WR_TKL.sizePolicy().hasHeightForWidth())
        self.checkBox_WR_TKL.setSizePolicy(sizePolicy1)
        self.checkBox_WR_TKL.setFont(font1)
        self.checkBox_WR_TKL.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_WR_TKL.setIconSize(QSize(20, 20))
        self.checkBox_WR_TKL.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_WR_TKL, 3, 8, 1, 1)

        self.checkBox_RB_WE = QCheckBox(self.gridLayoutWidget)
        self.checkBox_RB_WE.setObjectName(u"checkBox_RB_WE")
        sizePolicy1.setHeightForWidth(self.checkBox_RB_WE.sizePolicy().hasHeightForWidth())
        self.checkBox_RB_WE.setSizePolicy(sizePolicy1)
        self.checkBox_RB_WE.setFont(font1)
        self.checkBox_RB_WE.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_RB_WE.setIconSize(QSize(16, 16))
        self.checkBox_RB_WE.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_RB_WE, 2, 4, 1, 1)

        self.checkBox_WR_ATH = QCheckBox(self.gridLayoutWidget)
        self.checkBox_WR_ATH.setObjectName(u"checkBox_WR_ATH")
        sizePolicy.setHeightForWidth(self.checkBox_WR_ATH.sizePolicy().hasHeightForWidth())
        self.checkBox_WR_ATH.setSizePolicy(sizePolicy)
        self.checkBox_WR_ATH.setFont(font1)
        self.checkBox_WR_ATH.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_WR_ATH.setIconSize(QSize(20, 20))
        self.checkBox_WR_ATH.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_WR_ATH, 3, 1, 1, 1)

        self.checkBox_LB_TKL = QCheckBox(self.gridLayoutWidget)
        self.checkBox_LB_TKL.setObjectName(u"checkBox_LB_TKL")
        sizePolicy1.setHeightForWidth(self.checkBox_LB_TKL.sizePolicy().hasHeightForWidth())
        self.checkBox_LB_TKL.setSizePolicy(sizePolicy1)
        self.checkBox_LB_TKL.setFont(font1)
        self.checkBox_LB_TKL.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_LB_TKL.setIconSize(QSize(16, 16))
        self.checkBox_LB_TKL.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_LB_TKL, 7, 8, 1, 1)

        self.checkBox_TE_GI = QCheckBox(self.gridLayoutWidget)
        self.checkBox_TE_GI.setObjectName(u"checkBox_TE_GI")
        sizePolicy1.setHeightForWidth(self.checkBox_TE_GI.sizePolicy().hasHeightForWidth())
        self.checkBox_TE_GI.setSizePolicy(sizePolicy1)
        self.checkBox_TE_GI.setFont(font1)
        self.checkBox_TE_GI.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_TE_GI.setIconSize(QSize(16, 16))
        self.checkBox_TE_GI.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_TE_GI, 4, 10, 1, 1)

        self.checkBox_K_ELU = QCheckBox(self.gridLayoutWidget)
        self.checkBox_K_ELU.setObjectName(u"checkBox_K_ELU")
        sizePolicy1.setHeightForWidth(self.checkBox_K_ELU.sizePolicy().hasHeightForWidth())
        self.checkBox_K_ELU.setSizePolicy(sizePolicy1)
        self.checkBox_K_ELU.setFont(font1)
        self.checkBox_K_ELU.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_K_ELU.setIconSize(QSize(16, 16))
        self.checkBox_K_ELU.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_K_ELU, 9, 11, 1, 1)

        self.label_STR = QLabel(self.gridLayoutWidget)
        self.label_STR.setObjectName(u"label_STR")
        self.label_STR.setFont(font2)
        self.label_STR.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_STR, 0, 6, 1, 1)

        self.checkBox_RB_SPD = QCheckBox(self.gridLayoutWidget)
        self.checkBox_RB_SPD.setObjectName(u"checkBox_RB_SPD")
        sizePolicy1.setHeightForWidth(self.checkBox_RB_SPD.sizePolicy().hasHeightForWidth())
        self.checkBox_RB_SPD.setSizePolicy(sizePolicy1)
        self.checkBox_RB_SPD.setFont(font1)
        self.checkBox_RB_SPD.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_RB_SPD.setIconSize(QSize(16, 16))
        self.checkBox_RB_SPD.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_RB_SPD, 2, 2, 1, 1)

        self.checkBox_K_TKL = QCheckBox(self.gridLayoutWidget)
        self.checkBox_K_TKL.setObjectName(u"checkBox_K_TKL")
        sizePolicy1.setHeightForWidth(self.checkBox_K_TKL.sizePolicy().hasHeightForWidth())
        self.checkBox_K_TKL.setSizePolicy(sizePolicy1)
        self.checkBox_K_TKL.setFont(font1)
        self.checkBox_K_TKL.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_K_TKL.setIconSize(QSize(16, 16))
        self.checkBox_K_TKL.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_K_TKL, 9, 8, 1, 1)

        self.checkBox_LB_ATH = QCheckBox(self.gridLayoutWidget)
        self.checkBox_LB_ATH.setObjectName(u"checkBox_LB_ATH")
        sizePolicy1.setHeightForWidth(self.checkBox_LB_ATH.sizePolicy().hasHeightForWidth())
        self.checkBox_LB_ATH.setSizePolicy(sizePolicy1)
        self.checkBox_LB_ATH.setFont(font1)
        self.checkBox_LB_ATH.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_LB_ATH.setIconSize(QSize(16, 16))
        self.checkBox_LB_ATH.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_LB_ATH, 7, 1, 1, 1)

        self.checkBox_K_STA = QCheckBox(self.gridLayoutWidget)
        self.checkBox_K_STA.setObjectName(u"checkBox_K_STA")
        sizePolicy1.setHeightForWidth(self.checkBox_K_STA.sizePolicy().hasHeightForWidth())
        self.checkBox_K_STA.setSizePolicy(sizePolicy1)
        self.checkBox_K_STA.setFont(font1)
        self.checkBox_K_STA.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_K_STA.setIconSize(QSize(16, 16))
        self.checkBox_K_STA.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_K_STA, 9, 5, 1, 1)

        self.checkBox_LB_ELU = QCheckBox(self.gridLayoutWidget)
        self.checkBox_LB_ELU.setObjectName(u"checkBox_LB_ELU")
        sizePolicy1.setHeightForWidth(self.checkBox_LB_ELU.sizePolicy().hasHeightForWidth())
        self.checkBox_LB_ELU.setSizePolicy(sizePolicy1)
        self.checkBox_LB_ELU.setFont(font1)
        self.checkBox_LB_ELU.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_LB_ELU.setIconSize(QSize(16, 16))
        self.checkBox_LB_ELU.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_LB_ELU, 7, 11, 1, 1)

        self.checkBox_P_GI = QCheckBox(self.gridLayoutWidget)
        self.checkBox_P_GI.setObjectName(u"checkBox_P_GI")
        sizePolicy1.setHeightForWidth(self.checkBox_P_GI.sizePolicy().hasHeightForWidth())
        self.checkBox_P_GI.setSizePolicy(sizePolicy1)
        self.checkBox_P_GI.setFont(font1)
        self.checkBox_P_GI.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_P_GI.setIconSize(QSize(16, 16))
        self.checkBox_P_GI.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_P_GI, 10, 10, 1, 1)

        self.checkBox_P_TKL = QCheckBox(self.gridLayoutWidget)
        self.checkBox_P_TKL.setObjectName(u"checkBox_P_TKL")
        sizePolicy1.setHeightForWidth(self.checkBox_P_TKL.sizePolicy().hasHeightForWidth())
        self.checkBox_P_TKL.setSizePolicy(sizePolicy1)
        self.checkBox_P_TKL.setFont(font1)
        self.checkBox_P_TKL.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_P_TKL.setIconSize(QSize(16, 16))
        self.checkBox_P_TKL.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_P_TKL, 10, 8, 1, 1)

        self.checkBox_TE_BLK = QCheckBox(self.gridLayoutWidget)
        self.checkBox_TE_BLK.setObjectName(u"checkBox_TE_BLK")
        sizePolicy1.setHeightForWidth(self.checkBox_TE_BLK.sizePolicy().hasHeightForWidth())
        self.checkBox_TE_BLK.setSizePolicy(sizePolicy1)
        self.checkBox_TE_BLK.setFont(font1)
        self.checkBox_TE_BLK.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_TE_BLK.setIconSize(QSize(16, 16))
        self.checkBox_TE_BLK.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_TE_BLK, 4, 7, 1, 1)

        self.checkBox_TE_STA = QCheckBox(self.gridLayoutWidget)
        self.checkBox_TE_STA.setObjectName(u"checkBox_TE_STA")
        sizePolicy.setHeightForWidth(self.checkBox_TE_STA.sizePolicy().hasHeightForWidth())
        self.checkBox_TE_STA.setSizePolicy(sizePolicy)
        self.checkBox_TE_STA.setFont(font1)
        self.checkBox_TE_STA.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_TE_STA.setIconSize(QSize(20, 20))
        self.checkBox_TE_STA.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_TE_STA, 4, 5, 1, 1)

        self.checkBox_DB_TKL = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DB_TKL.setObjectName(u"checkBox_DB_TKL")
        sizePolicy.setHeightForWidth(self.checkBox_DB_TKL.sizePolicy().hasHeightForWidth())
        self.checkBox_DB_TKL.setSizePolicy(sizePolicy)
        self.checkBox_DB_TKL.setFont(font1)
        self.checkBox_DB_TKL.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DB_TKL.setIconSize(QSize(20, 20))
        self.checkBox_DB_TKL.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DB_TKL, 8, 8, 1, 1)

        self.checkBox_OL_HAN = QCheckBox(self.gridLayoutWidget)
        self.checkBox_OL_HAN.setObjectName(u"checkBox_OL_HAN")
        sizePolicy1.setHeightForWidth(self.checkBox_OL_HAN.sizePolicy().hasHeightForWidth())
        self.checkBox_OL_HAN.setSizePolicy(sizePolicy1)
        self.checkBox_OL_HAN.setFont(font1)
        self.checkBox_OL_HAN.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_OL_HAN.setIconSize(QSize(16, 16))
        self.checkBox_OL_HAN.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_OL_HAN, 5, 9, 1, 1)

        self.checkBox_DL_GI = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DL_GI.setObjectName(u"checkBox_DL_GI")
        sizePolicy1.setHeightForWidth(self.checkBox_DL_GI.sizePolicy().hasHeightForWidth())
        self.checkBox_DL_GI.setSizePolicy(sizePolicy1)
        self.checkBox_DL_GI.setFont(font1)
        self.checkBox_DL_GI.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DL_GI.setIconSize(QSize(16, 16))
        self.checkBox_DL_GI.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DL_GI, 6, 10, 1, 1)

        self.checkBox_K_STR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_K_STR.setObjectName(u"checkBox_K_STR")
        sizePolicy1.setHeightForWidth(self.checkBox_K_STR.sizePolicy().hasHeightForWidth())
        self.checkBox_K_STR.setSizePolicy(sizePolicy1)
        self.checkBox_K_STR.setFont(font1)
        self.checkBox_K_STR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_K_STR.setIconSize(QSize(16, 16))
        self.checkBox_K_STR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_K_STR, 9, 6, 1, 1)

        self.checkBox_LB_GI = QCheckBox(self.gridLayoutWidget)
        self.checkBox_LB_GI.setObjectName(u"checkBox_LB_GI")
        sizePolicy1.setHeightForWidth(self.checkBox_LB_GI.sizePolicy().hasHeightForWidth())
        self.checkBox_LB_GI.setSizePolicy(sizePolicy1)
        self.checkBox_LB_GI.setFont(font1)
        self.checkBox_LB_GI.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_LB_GI.setIconSize(QSize(16, 16))
        self.checkBox_LB_GI.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_LB_GI, 7, 10, 1, 1)

        self.checkBox_OL_TKL = QCheckBox(self.gridLayoutWidget)
        self.checkBox_OL_TKL.setObjectName(u"checkBox_OL_TKL")
        sizePolicy1.setHeightForWidth(self.checkBox_OL_TKL.sizePolicy().hasHeightForWidth())
        self.checkBox_OL_TKL.setSizePolicy(sizePolicy1)
        self.checkBox_OL_TKL.setFont(font1)
        self.checkBox_OL_TKL.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_OL_TKL.setIconSize(QSize(16, 16))
        self.checkBox_OL_TKL.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_OL_TKL, 5, 8, 1, 1)

        self.checkBox_QB_HAN = QCheckBox(self.gridLayoutWidget)
        self.checkBox_QB_HAN.setObjectName(u"checkBox_QB_HAN")
        sizePolicy1.setHeightForWidth(self.checkBox_QB_HAN.sizePolicy().hasHeightForWidth())
        self.checkBox_QB_HAN.setSizePolicy(sizePolicy1)
        self.checkBox_QB_HAN.setFont(font1)
        self.checkBox_QB_HAN.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_QB_HAN.setIconSize(QSize(16, 16))
        self.checkBox_QB_HAN.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_QB_HAN, 1, 9, 1, 1)

        self.checkBox_QB_STA = QCheckBox(self.gridLayoutWidget)
        self.checkBox_QB_STA.setObjectName(u"checkBox_QB_STA")
        sizePolicy1.setHeightForWidth(self.checkBox_QB_STA.sizePolicy().hasHeightForWidth())
        self.checkBox_QB_STA.setSizePolicy(sizePolicy1)
        self.checkBox_QB_STA.setFont(font1)
        self.checkBox_QB_STA.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_QB_STA.setIconSize(QSize(16, 16))
        self.checkBox_QB_STA.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_QB_STA, 1, 5, 1, 1)

        self.checkBox_DB_BLK = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DB_BLK.setObjectName(u"checkBox_DB_BLK")
        sizePolicy1.setHeightForWidth(self.checkBox_DB_BLK.sizePolicy().hasHeightForWidth())
        self.checkBox_DB_BLK.setSizePolicy(sizePolicy1)
        self.checkBox_DB_BLK.setFont(font1)
        self.checkBox_DB_BLK.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DB_BLK.setIconSize(QSize(16, 16))
        self.checkBox_DB_BLK.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DB_BLK, 8, 7, 1, 1)

        self.checkBox_K_HAN = QCheckBox(self.gridLayoutWidget)
        self.checkBox_K_HAN.setObjectName(u"checkBox_K_HAN")
        sizePolicy1.setHeightForWidth(self.checkBox_K_HAN.sizePolicy().hasHeightForWidth())
        self.checkBox_K_HAN.setSizePolicy(sizePolicy1)
        self.checkBox_K_HAN.setFont(font1)
        self.checkBox_K_HAN.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_K_HAN.setIconSize(QSize(16, 16))
        self.checkBox_K_HAN.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_K_HAN, 9, 9, 1, 1)

        self.checkBox_DB_WE = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DB_WE.setObjectName(u"checkBox_DB_WE")
        sizePolicy1.setHeightForWidth(self.checkBox_DB_WE.sizePolicy().hasHeightForWidth())
        self.checkBox_DB_WE.setSizePolicy(sizePolicy1)
        self.checkBox_DB_WE.setFont(font1)
        self.checkBox_DB_WE.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DB_WE.setIconSize(QSize(16, 16))
        self.checkBox_DB_WE.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DB_WE, 8, 4, 1, 1)

        self.checkBox_QB_DUR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_QB_DUR.setObjectName(u"checkBox_QB_DUR")
        sizePolicy1.setHeightForWidth(self.checkBox_QB_DUR.sizePolicy().hasHeightForWidth())
        self.checkBox_QB_DUR.setSizePolicy(sizePolicy1)
        self.checkBox_QB_DUR.setFont(font1)
        self.checkBox_QB_DUR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_QB_DUR.setIconSize(QSize(16, 16))
        self.checkBox_QB_DUR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_QB_DUR, 1, 3, 1, 1)

        self.checkBox_TE_ELU = QCheckBox(self.gridLayoutWidget)
        self.checkBox_TE_ELU.setObjectName(u"checkBox_TE_ELU")
        sizePolicy1.setHeightForWidth(self.checkBox_TE_ELU.sizePolicy().hasHeightForWidth())
        self.checkBox_TE_ELU.setSizePolicy(sizePolicy1)
        self.checkBox_TE_ELU.setFont(font1)
        self.checkBox_TE_ELU.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_TE_ELU.setIconSize(QSize(16, 16))
        self.checkBox_TE_ELU.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_TE_ELU, 4, 11, 1, 1)

        self.label_OL = QLabel(self.gridLayoutWidget)
        self.label_OL.setObjectName(u"label_OL")
        self.label_OL.setFont(font2)
        self.label_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_OL, 5, 0, 1, 1)

        self.label_SPD = QLabel(self.gridLayoutWidget)
        self.label_SPD.setObjectName(u"label_SPD")
        self.label_SPD.setFont(font2)
        self.label_SPD.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_SPD, 0, 2, 1, 1)

        self.label_TKL = QLabel(self.gridLayoutWidget)
        self.label_TKL.setObjectName(u"label_TKL")
        self.label_TKL.setFont(font2)
        self.label_TKL.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_TKL, 0, 8, 1, 1)

        self.checkBox_DB_ELU = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DB_ELU.setObjectName(u"checkBox_DB_ELU")
        sizePolicy1.setHeightForWidth(self.checkBox_DB_ELU.sizePolicy().hasHeightForWidth())
        self.checkBox_DB_ELU.setSizePolicy(sizePolicy1)
        self.checkBox_DB_ELU.setFont(font1)
        self.checkBox_DB_ELU.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DB_ELU.setIconSize(QSize(16, 16))
        self.checkBox_DB_ELU.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DB_ELU, 8, 11, 1, 1)

        self.checkBox_QB_BLK = QCheckBox(self.gridLayoutWidget)
        self.checkBox_QB_BLK.setObjectName(u"checkBox_QB_BLK")
        sizePolicy1.setHeightForWidth(self.checkBox_QB_BLK.sizePolicy().hasHeightForWidth())
        self.checkBox_QB_BLK.setSizePolicy(sizePolicy1)
        self.checkBox_QB_BLK.setFont(font1)
        self.checkBox_QB_BLK.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_QB_BLK.setIconSize(QSize(16, 16))
        self.checkBox_QB_BLK.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_QB_BLK, 1, 7, 1, 1)

        self.checkBox_RB_HAN = QCheckBox(self.gridLayoutWidget)
        self.checkBox_RB_HAN.setObjectName(u"checkBox_RB_HAN")
        sizePolicy1.setHeightForWidth(self.checkBox_RB_HAN.sizePolicy().hasHeightForWidth())
        self.checkBox_RB_HAN.setSizePolicy(sizePolicy1)
        self.checkBox_RB_HAN.setFont(font1)
        self.checkBox_RB_HAN.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_RB_HAN.setIconSize(QSize(16, 16))
        self.checkBox_RB_HAN.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_RB_HAN, 2, 9, 1, 1)

        self.checkBox_OL_SPD = QCheckBox(self.gridLayoutWidget)
        self.checkBox_OL_SPD.setObjectName(u"checkBox_OL_SPD")
        sizePolicy1.setHeightForWidth(self.checkBox_OL_SPD.sizePolicy().hasHeightForWidth())
        self.checkBox_OL_SPD.setSizePolicy(sizePolicy1)
        self.checkBox_OL_SPD.setFont(font1)
        self.checkBox_OL_SPD.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_OL_SPD.setIconSize(QSize(16, 16))
        self.checkBox_OL_SPD.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_OL_SPD, 5, 2, 1, 1)

        self.checkBox_LB_STR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_LB_STR.setObjectName(u"checkBox_LB_STR")
        sizePolicy1.setHeightForWidth(self.checkBox_LB_STR.sizePolicy().hasHeightForWidth())
        self.checkBox_LB_STR.setSizePolicy(sizePolicy1)
        self.checkBox_LB_STR.setFont(font1)
        self.checkBox_LB_STR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_LB_STR.setIconSize(QSize(16, 16))
        self.checkBox_LB_STR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_LB_STR, 7, 6, 1, 1)

        self.checkBox_K_GI = QCheckBox(self.gridLayoutWidget)
        self.checkBox_K_GI.setObjectName(u"checkBox_K_GI")
        sizePolicy1.setHeightForWidth(self.checkBox_K_GI.sizePolicy().hasHeightForWidth())
        self.checkBox_K_GI.setSizePolicy(sizePolicy1)
        self.checkBox_K_GI.setFont(font1)
        self.checkBox_K_GI.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_K_GI.setIconSize(QSize(16, 16))
        self.checkBox_K_GI.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_K_GI, 9, 10, 1, 1)

        self.checkBox_OL_WE = QCheckBox(self.gridLayoutWidget)
        self.checkBox_OL_WE.setObjectName(u"checkBox_OL_WE")
        sizePolicy1.setHeightForWidth(self.checkBox_OL_WE.sizePolicy().hasHeightForWidth())
        self.checkBox_OL_WE.setSizePolicy(sizePolicy1)
        self.checkBox_OL_WE.setFont(font1)
        self.checkBox_OL_WE.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_OL_WE.setIconSize(QSize(16, 16))
        self.checkBox_OL_WE.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_OL_WE, 5, 4, 1, 1)

        self.label_DL = QLabel(self.gridLayoutWidget)
        self.label_DL.setObjectName(u"label_DL")
        self.label_DL.setFont(font2)
        self.label_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_DL, 6, 0, 1, 1)

        self.label_K = QLabel(self.gridLayoutWidget)
        self.label_K.setObjectName(u"label_K")
        self.label_K.setFont(font2)
        self.label_K.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_K, 9, 0, 1, 1)

        self.checkBox_TE_STR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_TE_STR.setObjectName(u"checkBox_TE_STR")
        sizePolicy1.setHeightForWidth(self.checkBox_TE_STR.sizePolicy().hasHeightForWidth())
        self.checkBox_TE_STR.setSizePolicy(sizePolicy1)
        self.checkBox_TE_STR.setFont(font1)
        self.checkBox_TE_STR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_TE_STR.setIconSize(QSize(16, 16))
        self.checkBox_TE_STR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_TE_STR, 4, 6, 1, 1)

        self.checkBox_RB_STR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_RB_STR.setObjectName(u"checkBox_RB_STR")
        sizePolicy1.setHeightForWidth(self.checkBox_RB_STR.sizePolicy().hasHeightForWidth())
        self.checkBox_RB_STR.setSizePolicy(sizePolicy1)
        self.checkBox_RB_STR.setFont(font1)
        self.checkBox_RB_STR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_RB_STR.setIconSize(QSize(16, 16))
        self.checkBox_RB_STR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_RB_STR, 2, 6, 1, 1)

        self.checkBox_TE_WE = QCheckBox(self.gridLayoutWidget)
        self.checkBox_TE_WE.setObjectName(u"checkBox_TE_WE")
        sizePolicy1.setHeightForWidth(self.checkBox_TE_WE.sizePolicy().hasHeightForWidth())
        self.checkBox_TE_WE.setSizePolicy(sizePolicy1)
        self.checkBox_TE_WE.setFont(font1)
        self.checkBox_TE_WE.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_TE_WE.setIconSize(QSize(16, 16))
        self.checkBox_TE_WE.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_TE_WE, 4, 4, 1, 1)

        self.checkBox_WR_BLK = QCheckBox(self.gridLayoutWidget)
        self.checkBox_WR_BLK.setObjectName(u"checkBox_WR_BLK")
        sizePolicy1.setHeightForWidth(self.checkBox_WR_BLK.sizePolicy().hasHeightForWidth())
        self.checkBox_WR_BLK.setSizePolicy(sizePolicy1)
        self.checkBox_WR_BLK.setFont(font1)
        self.checkBox_WR_BLK.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_WR_BLK.setIconSize(QSize(16, 16))
        self.checkBox_WR_BLK.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_WR_BLK, 3, 7, 1, 1)

        self.checkBox_K_ATH = QCheckBox(self.gridLayoutWidget)
        self.checkBox_K_ATH.setObjectName(u"checkBox_K_ATH")
        sizePolicy1.setHeightForWidth(self.checkBox_K_ATH.sizePolicy().hasHeightForWidth())
        self.checkBox_K_ATH.setSizePolicy(sizePolicy1)
        self.checkBox_K_ATH.setFont(font1)
        self.checkBox_K_ATH.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_K_ATH.setIconSize(QSize(16, 16))
        self.checkBox_K_ATH.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_K_ATH, 9, 1, 1, 1)

        self.checkBox_QB_WE = QCheckBox(self.gridLayoutWidget)
        self.checkBox_QB_WE.setObjectName(u"checkBox_QB_WE")
        sizePolicy1.setHeightForWidth(self.checkBox_QB_WE.sizePolicy().hasHeightForWidth())
        self.checkBox_QB_WE.setSizePolicy(sizePolicy1)
        self.checkBox_QB_WE.setFont(font1)
        self.checkBox_QB_WE.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_QB_WE.setIconSize(QSize(16, 16))
        self.checkBox_QB_WE.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_QB_WE, 1, 4, 1, 1)

        self.checkBox_LB_WE = QCheckBox(self.gridLayoutWidget)
        self.checkBox_LB_WE.setObjectName(u"checkBox_LB_WE")
        sizePolicy1.setHeightForWidth(self.checkBox_LB_WE.sizePolicy().hasHeightForWidth())
        self.checkBox_LB_WE.setSizePolicy(sizePolicy1)
        self.checkBox_LB_WE.setFont(font1)
        self.checkBox_LB_WE.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_LB_WE.setIconSize(QSize(16, 16))
        self.checkBox_LB_WE.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_LB_WE, 7, 4, 1, 1)

        self.checkBox_DL_BLK = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DL_BLK.setObjectName(u"checkBox_DL_BLK")
        sizePolicy.setHeightForWidth(self.checkBox_DL_BLK.sizePolicy().hasHeightForWidth())
        self.checkBox_DL_BLK.setSizePolicy(sizePolicy)
        self.checkBox_DL_BLK.setFont(font1)
        self.checkBox_DL_BLK.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DL_BLK.setIconSize(QSize(20, 20))
        self.checkBox_DL_BLK.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DL_BLK, 6, 7, 1, 1)

        self.checkBox_LB_SPD = QCheckBox(self.gridLayoutWidget)
        self.checkBox_LB_SPD.setObjectName(u"checkBox_LB_SPD")
        sizePolicy1.setHeightForWidth(self.checkBox_LB_SPD.sizePolicy().hasHeightForWidth())
        self.checkBox_LB_SPD.setSizePolicy(sizePolicy1)
        self.checkBox_LB_SPD.setFont(font1)
        self.checkBox_LB_SPD.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_LB_SPD.setIconSize(QSize(16, 16))
        self.checkBox_LB_SPD.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_LB_SPD, 7, 2, 1, 1)

        self.checkBox_WR_WE = QCheckBox(self.gridLayoutWidget)
        self.checkBox_WR_WE.setObjectName(u"checkBox_WR_WE")
        sizePolicy1.setHeightForWidth(self.checkBox_WR_WE.sizePolicy().hasHeightForWidth())
        self.checkBox_WR_WE.setSizePolicy(sizePolicy1)
        self.checkBox_WR_WE.setFont(font1)
        self.checkBox_WR_WE.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_WR_WE.setIconSize(QSize(16, 16))
        self.checkBox_WR_WE.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_WR_WE, 3, 4, 1, 1)

        self.checkBox_P_SPD = QCheckBox(self.gridLayoutWidget)
        self.checkBox_P_SPD.setObjectName(u"checkBox_P_SPD")
        sizePolicy1.setHeightForWidth(self.checkBox_P_SPD.sizePolicy().hasHeightForWidth())
        self.checkBox_P_SPD.setSizePolicy(sizePolicy1)
        self.checkBox_P_SPD.setFont(font1)
        self.checkBox_P_SPD.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_P_SPD.setIconSize(QSize(16, 16))
        self.checkBox_P_SPD.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_P_SPD, 10, 2, 1, 1)

        self.checkBox_WR_STA = QCheckBox(self.gridLayoutWidget)
        self.checkBox_WR_STA.setObjectName(u"checkBox_WR_STA")
        sizePolicy1.setHeightForWidth(self.checkBox_WR_STA.sizePolicy().hasHeightForWidth())
        self.checkBox_WR_STA.setSizePolicy(sizePolicy1)
        self.checkBox_WR_STA.setFont(font1)
        self.checkBox_WR_STA.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_WR_STA.setIconSize(QSize(16, 16))
        self.checkBox_WR_STA.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_WR_STA, 3, 5, 1, 1)

        self.checkBox_P_ELU = QCheckBox(self.gridLayoutWidget)
        self.checkBox_P_ELU.setObjectName(u"checkBox_P_ELU")
        sizePolicy1.setHeightForWidth(self.checkBox_P_ELU.sizePolicy().hasHeightForWidth())
        self.checkBox_P_ELU.setSizePolicy(sizePolicy1)
        self.checkBox_P_ELU.setFont(font1)
        self.checkBox_P_ELU.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_P_ELU.setIconSize(QSize(16, 16))
        self.checkBox_P_ELU.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_P_ELU, 10, 11, 1, 1)

        self.label_HAN = QLabel(self.gridLayoutWidget)
        self.label_HAN.setObjectName(u"label_HAN")
        self.label_HAN.setFont(font2)
        self.label_HAN.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_HAN, 0, 9, 1, 1)

        self.checkBox_WR_TEC = QCheckBox(self.gridLayoutWidget)
        self.checkBox_WR_TEC.setObjectName(u"checkBox_WR_TEC")
        sizePolicy1.setHeightForWidth(self.checkBox_WR_TEC.sizePolicy().hasHeightForWidth())
        self.checkBox_WR_TEC.setSizePolicy(sizePolicy1)
        self.checkBox_WR_TEC.setFont(font1)
        self.checkBox_WR_TEC.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_WR_TEC.setIconSize(QSize(16, 16))
        self.checkBox_WR_TEC.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_WR_TEC, 3, 12, 1, 1)

        self.checkBox_OL_GI = QCheckBox(self.gridLayoutWidget)
        self.checkBox_OL_GI.setObjectName(u"checkBox_OL_GI")
        sizePolicy1.setHeightForWidth(self.checkBox_OL_GI.sizePolicy().hasHeightForWidth())
        self.checkBox_OL_GI.setSizePolicy(sizePolicy1)
        self.checkBox_OL_GI.setFont(font1)
        self.checkBox_OL_GI.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_OL_GI.setIconSize(QSize(16, 16))
        self.checkBox_OL_GI.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_OL_GI, 5, 10, 1, 1)

        self.checkBox_RB_BLK = QCheckBox(self.gridLayoutWidget)
        self.checkBox_RB_BLK.setObjectName(u"checkBox_RB_BLK")
        sizePolicy1.setHeightForWidth(self.checkBox_RB_BLK.sizePolicy().hasHeightForWidth())
        self.checkBox_RB_BLK.setSizePolicy(sizePolicy1)
        self.checkBox_RB_BLK.setFont(font1)
        self.checkBox_RB_BLK.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_RB_BLK.setIconSize(QSize(16, 16))
        self.checkBox_RB_BLK.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_RB_BLK, 2, 7, 1, 1)

        self.checkBox_K_DUR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_K_DUR.setObjectName(u"checkBox_K_DUR")
        sizePolicy1.setHeightForWidth(self.checkBox_K_DUR.sizePolicy().hasHeightForWidth())
        self.checkBox_K_DUR.setSizePolicy(sizePolicy1)
        self.checkBox_K_DUR.setFont(font1)
        self.checkBox_K_DUR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_K_DUR.setIconSize(QSize(16, 16))
        self.checkBox_K_DUR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_K_DUR, 9, 3, 1, 1)

        self.checkBox_WR_SPD = QCheckBox(self.gridLayoutWidget)
        self.checkBox_WR_SPD.setObjectName(u"checkBox_WR_SPD")
        sizePolicy1.setHeightForWidth(self.checkBox_WR_SPD.sizePolicy().hasHeightForWidth())
        self.checkBox_WR_SPD.setSizePolicy(sizePolicy1)
        self.checkBox_WR_SPD.setFont(font1)
        self.checkBox_WR_SPD.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_WR_SPD.setIconSize(QSize(16, 16))
        self.checkBox_WR_SPD.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_WR_SPD, 3, 2, 1, 1)

        self.checkBox_P_STA = QCheckBox(self.gridLayoutWidget)
        self.checkBox_P_STA.setObjectName(u"checkBox_P_STA")
        sizePolicy1.setHeightForWidth(self.checkBox_P_STA.sizePolicy().hasHeightForWidth())
        self.checkBox_P_STA.setSizePolicy(sizePolicy1)
        self.checkBox_P_STA.setFont(font1)
        self.checkBox_P_STA.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_P_STA.setIconSize(QSize(16, 16))
        self.checkBox_P_STA.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_P_STA, 10, 5, 1, 1)

        self.checkBox_K_SPD = QCheckBox(self.gridLayoutWidget)
        self.checkBox_K_SPD.setObjectName(u"checkBox_K_SPD")
        sizePolicy1.setHeightForWidth(self.checkBox_K_SPD.sizePolicy().hasHeightForWidth())
        self.checkBox_K_SPD.setSizePolicy(sizePolicy1)
        self.checkBox_K_SPD.setFont(font1)
        self.checkBox_K_SPD.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_K_SPD.setIconSize(QSize(16, 16))
        self.checkBox_K_SPD.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_K_SPD, 9, 2, 1, 1)

        self.checkBox_TE_SPD = QCheckBox(self.gridLayoutWidget)
        self.checkBox_TE_SPD.setObjectName(u"checkBox_TE_SPD")
        sizePolicy1.setHeightForWidth(self.checkBox_TE_SPD.sizePolicy().hasHeightForWidth())
        self.checkBox_TE_SPD.setSizePolicy(sizePolicy1)
        self.checkBox_TE_SPD.setFont(font1)
        self.checkBox_TE_SPD.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_TE_SPD.setIconSize(QSize(16, 16))
        self.checkBox_TE_SPD.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_TE_SPD, 4, 2, 1, 1)

        self.label_P = QLabel(self.gridLayoutWidget)
        self.label_P.setObjectName(u"label_P")
        self.label_P.setFont(font2)
        self.label_P.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_P, 10, 0, 1, 1)

        self.checkBox_DB_STR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DB_STR.setObjectName(u"checkBox_DB_STR")
        sizePolicy1.setHeightForWidth(self.checkBox_DB_STR.sizePolicy().hasHeightForWidth())
        self.checkBox_DB_STR.setSizePolicy(sizePolicy1)
        self.checkBox_DB_STR.setFont(font1)
        self.checkBox_DB_STR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DB_STR.setIconSize(QSize(16, 16))
        self.checkBox_DB_STR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DB_STR, 8, 6, 1, 1)

        self.checkBox_P_BLK = QCheckBox(self.gridLayoutWidget)
        self.checkBox_P_BLK.setObjectName(u"checkBox_P_BLK")
        sizePolicy.setHeightForWidth(self.checkBox_P_BLK.sizePolicy().hasHeightForWidth())
        self.checkBox_P_BLK.setSizePolicy(sizePolicy)
        self.checkBox_P_BLK.setFont(font1)
        self.checkBox_P_BLK.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_P_BLK.setIconSize(QSize(20, 20))
        self.checkBox_P_BLK.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_P_BLK, 10, 7, 1, 1)

        self.label_LB = QLabel(self.gridLayoutWidget)
        self.label_LB.setObjectName(u"label_LB")
        self.label_LB.setFont(font2)
        self.label_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_LB, 7, 0, 1, 1)

        self.checkBox_OL_BLK = QCheckBox(self.gridLayoutWidget)
        self.checkBox_OL_BLK.setObjectName(u"checkBox_OL_BLK")
        sizePolicy1.setHeightForWidth(self.checkBox_OL_BLK.sizePolicy().hasHeightForWidth())
        self.checkBox_OL_BLK.setSizePolicy(sizePolicy1)
        self.checkBox_OL_BLK.setFont(font1)
        self.checkBox_OL_BLK.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_OL_BLK.setIconSize(QSize(16, 16))
        self.checkBox_OL_BLK.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_OL_BLK, 5, 7, 1, 1)

        self.checkBox_WR_GI = QCheckBox(self.gridLayoutWidget)
        self.checkBox_WR_GI.setObjectName(u"checkBox_WR_GI")
        sizePolicy1.setHeightForWidth(self.checkBox_WR_GI.sizePolicy().hasHeightForWidth())
        self.checkBox_WR_GI.setSizePolicy(sizePolicy1)
        self.checkBox_WR_GI.setFont(font1)
        self.checkBox_WR_GI.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_WR_GI.setIconSize(QSize(16, 16))
        self.checkBox_WR_GI.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_WR_GI, 3, 10, 1, 1)

        self.checkBox_DB_ATH = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DB_ATH.setObjectName(u"checkBox_DB_ATH")
        sizePolicy1.setHeightForWidth(self.checkBox_DB_ATH.sizePolicy().hasHeightForWidth())
        self.checkBox_DB_ATH.setSizePolicy(sizePolicy1)
        self.checkBox_DB_ATH.setFont(font1)
        self.checkBox_DB_ATH.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DB_ATH.setIconSize(QSize(16, 16))
        self.checkBox_DB_ATH.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DB_ATH, 8, 1, 1, 1)

        self.checkBox_RB_STA = QCheckBox(self.gridLayoutWidget)
        self.checkBox_RB_STA.setObjectName(u"checkBox_RB_STA")
        sizePolicy1.setHeightForWidth(self.checkBox_RB_STA.sizePolicy().hasHeightForWidth())
        self.checkBox_RB_STA.setSizePolicy(sizePolicy1)
        self.checkBox_RB_STA.setFont(font1)
        self.checkBox_RB_STA.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_RB_STA.setIconSize(QSize(16, 16))
        self.checkBox_RB_STA.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_RB_STA, 2, 5, 1, 1)

        self.checkBox_DL_TEC = QCheckBox(self.gridLayoutWidget)
        self.checkBox_DL_TEC.setObjectName(u"checkBox_DL_TEC")
        sizePolicy1.setHeightForWidth(self.checkBox_DL_TEC.sizePolicy().hasHeightForWidth())
        self.checkBox_DL_TEC.setSizePolicy(sizePolicy1)
        self.checkBox_DL_TEC.setFont(font1)
        self.checkBox_DL_TEC.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_DL_TEC.setIconSize(QSize(16, 16))
        self.checkBox_DL_TEC.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_DL_TEC, 6, 12, 1, 1)

        self.checkBox_QB_TKL = QCheckBox(self.gridLayoutWidget)
        self.checkBox_QB_TKL.setObjectName(u"checkBox_QB_TKL")
        sizePolicy1.setHeightForWidth(self.checkBox_QB_TKL.sizePolicy().hasHeightForWidth())
        self.checkBox_QB_TKL.setSizePolicy(sizePolicy1)
        self.checkBox_QB_TKL.setFont(font1)
        self.checkBox_QB_TKL.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_QB_TKL.setIconSize(QSize(16, 16))
        self.checkBox_QB_TKL.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_QB_TKL, 1, 8, 1, 1)

        self.checkBox_RB_ATH = QCheckBox(self.gridLayoutWidget)
        self.checkBox_RB_ATH.setObjectName(u"checkBox_RB_ATH")
        sizePolicy.setHeightForWidth(self.checkBox_RB_ATH.sizePolicy().hasHeightForWidth())
        self.checkBox_RB_ATH.setSizePolicy(sizePolicy)
        self.checkBox_RB_ATH.setFont(font1)
        self.checkBox_RB_ATH.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_RB_ATH.setIconSize(QSize(16, 16))
        self.checkBox_RB_ATH.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_RB_ATH, 2, 1, 1, 1)

        self.checkBox_OL_TEC = QCheckBox(self.gridLayoutWidget)
        self.checkBox_OL_TEC.setObjectName(u"checkBox_OL_TEC")
        sizePolicy.setHeightForWidth(self.checkBox_OL_TEC.sizePolicy().hasHeightForWidth())
        self.checkBox_OL_TEC.setSizePolicy(sizePolicy)
        self.checkBox_OL_TEC.setFont(font1)
        self.checkBox_OL_TEC.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_OL_TEC.setIconSize(QSize(20, 20))
        self.checkBox_OL_TEC.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_OL_TEC, 5, 12, 1, 1)

        self.label_WE = QLabel(self.gridLayoutWidget)
        self.label_WE.setObjectName(u"label_WE")
        self.label_WE.setFont(font2)
        self.label_WE.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_WE, 0, 4, 1, 1)

        self.label_TE = QLabel(self.gridLayoutWidget)
        self.label_TE.setObjectName(u"label_TE")
        self.label_TE.setFont(font2)
        self.label_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_TE, 4, 0, 1, 1)

        self.checkBox_P_STR = QCheckBox(self.gridLayoutWidget)
        self.checkBox_P_STR.setObjectName(u"checkBox_P_STR")
        sizePolicy1.setHeightForWidth(self.checkBox_P_STR.sizePolicy().hasHeightForWidth())
        self.checkBox_P_STR.setSizePolicy(sizePolicy1)
        self.checkBox_P_STR.setFont(font1)
        self.checkBox_P_STR.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_P_STR.setIconSize(QSize(16, 16))
        self.checkBox_P_STR.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_P_STR, 10, 6, 1, 1)

        self.checkBox_QB_ATH = QCheckBox(self.gridLayoutWidget)
        self.checkBox_QB_ATH.setObjectName(u"checkBox_QB_ATH")
        sizePolicy.setHeightForWidth(self.checkBox_QB_ATH.sizePolicy().hasHeightForWidth())
        self.checkBox_QB_ATH.setSizePolicy(sizePolicy)
        self.checkBox_QB_ATH.setFont(font1)
        self.checkBox_QB_ATH.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_QB_ATH.setStyleSheet(u"margin-left:10%;\n"
"margin-right:10%;")
        self.checkBox_QB_ATH.setIconSize(QSize(20, 20))
        self.checkBox_QB_ATH.setChecked(False)

        self.gridLayout.addWidget(self.checkBox_QB_ATH, 1, 1, 1, 1)


        self.retranslateUi(DialogBoldAttributes)
        self.buttonBox.accepted.connect(DialogBoldAttributes.accept)
        self.buttonBox.rejected.connect(DialogBoldAttributes.reject)

        QMetaObject.connectSlotsByName(DialogBoldAttributes)
    # setupUi

    def retranslateUi(self, DialogBoldAttributes):
        DialogBoldAttributes.setWindowTitle(QCoreApplication.translate("DialogBoldAttributes", u"Bold Attributes Config", None))
        self.label.setText(QCoreApplication.translate("DialogBoldAttributes", u"Check the box for each attribute you want in Bold text by position:", None))
        self.checkBox_DB_DUR.setText("")
        self.label_BLK.setText(QCoreApplication.translate("DialogBoldAttributes", u"BLK", None))
        self.checkBox_WR_ELU.setText("")
        self.checkBox_DB_GI.setText("")
        self.checkBox_TE_DUR.setText("")
        self.label_ELU.setText(QCoreApplication.translate("DialogBoldAttributes", u"ELU", None))
        self.checkBox_P_WE.setText("")
        self.checkBox_OL_ATH.setText("")
        self.checkBox_P_DUR.setText("")
        self.checkBox_WR_DUR.setText("")
        self.checkBox_DL_ATH.setText("")
        self.checkBox_LB_DUR.setText("")
        self.checkBox_OL_DUR.setText("")
        self.checkBox_RB_TEC.setText("")
        self.checkBox_LB_TEC.setText("")
        self.checkBox_QB_TEC.setText("")
        self.checkBox_LB_HAN.setText("")
        self.checkBox_QB_ELU.setText("")
        self.checkBox_K_WE.setText("")
        self.label_WR.setText(QCoreApplication.translate("DialogBoldAttributes", u"WR", None))
        self.checkBox_DL_STR.setText("")
        self.checkBox_DL_HAN.setText("")
        self.checkBox_RB_ELU.setText("")
        self.checkBox_DB_TEC.setText("")
        self.checkBox_OL_STR.setText("")
        self.checkBox_RB_GI.setText("")
        self.checkBox_WR_HAN.setText("")
        self.checkBox_TE_HAN.setText("")
        self.checkBox_DL_DUR.setText("")
        self.checkBox_DB_HAN.setText("")
        self.checkBox_OL_ELU.setText("")
        self.checkBox_WR_STR.setText("")
        self.checkBox_DL_STA.setText("")
        self.checkBox_DB_STA.setText("")
        self.checkBox_P_ATH.setText("")
        self.checkBox_QB_GI.setText("")
        self.checkBox_DL_SPD.setText("")
        self.checkBox_P_HAN.setText("")
        self.checkBox_DL_ELU.setText("")
        self.checkBox_TE_ATH.setText("")
        self.checkBox_DL_TKL.setText("")
        self.checkBox_OL_STA.setText("")
        self.checkBox_QB_SPD.setText("")
        self.checkBox_K_BLK.setText("")
        self.checkBox_TE_TEC.setText("")
        self.label_RB.setText(QCoreApplication.translate("DialogBoldAttributes", u"RB", None))
        self.checkBox_DB_SPD.setText("")
        self.checkBox_RB_TKL.setText("")
        self.checkBox_TE_TKL.setText("")
        self.label_DB.setText(QCoreApplication.translate("DialogBoldAttributes", u"DB", None))
        self.checkBox_LB_STA.setText("")
        self.checkBox_DL_WE.setText("")
        self.checkBox_LB_BLK.setText("")
        self.label_ATH.setText(QCoreApplication.translate("DialogBoldAttributes", u"ATH", None))
        self.checkBox_K_TEC.setText("")
        self.label_STA.setText(QCoreApplication.translate("DialogBoldAttributes", u"STA", None))
        self.label_QB.setText(QCoreApplication.translate("DialogBoldAttributes", u"QB", None))
        self.checkBox_RB_DUR.setText("")
        self.label_GI.setText(QCoreApplication.translate("DialogBoldAttributes", u"GI", None))
        self.label_DUR.setText(QCoreApplication.translate("DialogBoldAttributes", u"DUR", None))
        self.checkBox_P_TEC.setText("")
        self.checkBox_QB_STR.setText("")
        self.label_TEC.setText(QCoreApplication.translate("DialogBoldAttributes", u"TEC", None))
        self.checkBox_WR_TKL.setText("")
        self.checkBox_RB_WE.setText("")
        self.checkBox_WR_ATH.setText("")
        self.checkBox_LB_TKL.setText("")
        self.checkBox_TE_GI.setText("")
        self.checkBox_K_ELU.setText("")
        self.label_STR.setText(QCoreApplication.translate("DialogBoldAttributes", u"STR", None))
        self.checkBox_RB_SPD.setText("")
        self.checkBox_K_TKL.setText("")
        self.checkBox_LB_ATH.setText("")
        self.checkBox_K_STA.setText("")
        self.checkBox_LB_ELU.setText("")
        self.checkBox_P_GI.setText("")
        self.checkBox_P_TKL.setText("")
        self.checkBox_TE_BLK.setText("")
        self.checkBox_TE_STA.setText("")
        self.checkBox_DB_TKL.setText("")
        self.checkBox_OL_HAN.setText("")
        self.checkBox_DL_GI.setText("")
        self.checkBox_K_STR.setText("")
        self.checkBox_LB_GI.setText("")
        self.checkBox_OL_TKL.setText("")
        self.checkBox_QB_HAN.setText("")
        self.checkBox_QB_STA.setText("")
        self.checkBox_DB_BLK.setText("")
        self.checkBox_K_HAN.setText("")
        self.checkBox_DB_WE.setText("")
        self.checkBox_QB_DUR.setText("")
        self.checkBox_TE_ELU.setText("")
        self.label_OL.setText(QCoreApplication.translate("DialogBoldAttributes", u"OL", None))
        self.label_SPD.setText(QCoreApplication.translate("DialogBoldAttributes", u"SPD", None))
        self.label_TKL.setText(QCoreApplication.translate("DialogBoldAttributes", u"TKL", None))
        self.checkBox_DB_ELU.setText("")
        self.checkBox_QB_BLK.setText("")
        self.checkBox_RB_HAN.setText("")
        self.checkBox_OL_SPD.setText("")
        self.checkBox_LB_STR.setText("")
        self.checkBox_K_GI.setText("")
        self.checkBox_OL_WE.setText("")
        self.label_DL.setText(QCoreApplication.translate("DialogBoldAttributes", u"DL", None))
        self.label_K.setText(QCoreApplication.translate("DialogBoldAttributes", u"K", None))
        self.checkBox_TE_STR.setText("")
        self.checkBox_RB_STR.setText("")
        self.checkBox_TE_WE.setText("")
        self.checkBox_WR_BLK.setText("")
        self.checkBox_K_ATH.setText("")
        self.checkBox_QB_WE.setText("")
        self.checkBox_LB_WE.setText("")
        self.checkBox_DL_BLK.setText("")
        self.checkBox_LB_SPD.setText("")
        self.checkBox_WR_WE.setText("")
        self.checkBox_P_SPD.setText("")
        self.checkBox_WR_STA.setText("")
        self.checkBox_P_ELU.setText("")
        self.label_HAN.setText(QCoreApplication.translate("DialogBoldAttributes", u"HAN", None))
        self.checkBox_WR_TEC.setText("")
        self.checkBox_OL_GI.setText("")
        self.checkBox_RB_BLK.setText("")
        self.checkBox_K_DUR.setText("")
        self.checkBox_WR_SPD.setText("")
        self.checkBox_P_STA.setText("")
        self.checkBox_K_SPD.setText("")
        self.checkBox_TE_SPD.setText("")
        self.label_P.setText(QCoreApplication.translate("DialogBoldAttributes", u"P", None))
        self.checkBox_DB_STR.setText("")
        self.checkBox_P_BLK.setText("")
        self.label_LB.setText(QCoreApplication.translate("DialogBoldAttributes", u"LB", None))
        self.checkBox_OL_BLK.setText("")
        self.checkBox_WR_GI.setText("")
        self.checkBox_DB_ATH.setText("")
        self.checkBox_RB_STA.setText("")
        self.checkBox_DL_TEC.setText("")
        self.checkBox_QB_TKL.setText("")
        self.checkBox_RB_ATH.setText("")
        self.checkBox_OL_TEC.setText("")
        self.label_WE.setText(QCoreApplication.translate("DialogBoldAttributes", u"WE", None))
        self.label_TE.setText(QCoreApplication.translate("DialogBoldAttributes", u"TE", None))
        self.checkBox_P_STR.setText("")
        self.checkBox_QB_ATH.setText("")
    # retranslateUi

