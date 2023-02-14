from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_DialogRoleRatings(object):
    def setupUi(self, DialogRoleRatings):
        if not DialogRoleRatings.objectName():
            DialogRoleRatings.setObjectName(u"DialogRoleRatings")
        DialogRoleRatings.setWindowModality(Qt.ApplicationModal)
        DialogRoleRatings.resize(1245, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogRoleRatings.sizePolicy().hasHeightForWidth())
        DialogRoleRatings.setSizePolicy(sizePolicy)
        DialogRoleRatings.setMinimumSize(QSize(1245, 460))
        DialogRoleRatings.setMaximumSize(QSize(1245, 460))
        self.buttonBox = QDialogButtonBox(DialogRoleRatings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(1010, 400, 211, 32))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.tabWidgetRoleRatings = QTabWidget(DialogRoleRatings)
        self.tabWidgetRoleRatings.setObjectName(u"tabWidgetRoleRatings")
        self.tabWidgetRoleRatings.setGeometry(QRect(0, 60, 1231, 321))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        self.tabWidgetRoleRatings.setFont(font1)
        self.QB = QWidget()
        self.QB.setObjectName(u"QB")
        self.gridLayoutWidget = QWidget(self.QB)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 10, 1215, 261))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_ATH_Header_QB = QLabel(self.gridLayoutWidget)
        self.label_ATH_Header_QB.setObjectName(u"label_ATH_Header_QB")
        self.label_ATH_Header_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_ATH_Header_QB, 0, 2, 1, 1)

        self.spinBox_R2_TKL_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R2_TKL_QB.setObjectName(u"spinBox_R2_TKL_QB")
        self.spinBox_R2_TKL_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TKL_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R2_TKL_QB, 2, 9, 1, 1)

        self.spinBox_R3_DUR_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R3_DUR_QB.setObjectName(u"spinBox_R3_DUR_QB")
        self.spinBox_R3_DUR_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_DUR_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R3_DUR_QB, 3, 4, 1, 1)

        self.spinBox_R3_STR_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R3_STR_QB.setObjectName(u"spinBox_R3_STR_QB")
        self.spinBox_R3_STR_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STR_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R3_STR_QB, 3, 7, 1, 1)

        self.spinBox_R2_TEC_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R2_TEC_QB.setObjectName(u"spinBox_R2_TEC_QB")
        self.spinBox_R2_TEC_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TEC_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R2_TEC_QB, 2, 13, 1, 1)

        self.spinBox_R2_WE_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R2_WE_QB.setObjectName(u"spinBox_R2_WE_QB")
        self.spinBox_R2_WE_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_WE_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R2_WE_QB, 2, 5, 1, 1)

        self.spinBox_R1_SPD_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R1_SPD_QB.setObjectName(u"spinBox_R1_SPD_QB")
        self.spinBox_R1_SPD_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_SPD_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R1_SPD_QB, 1, 3, 1, 1)

        self.label_TEC_Header_QB = QLabel(self.gridLayoutWidget)
        self.label_TEC_Header_QB.setObjectName(u"label_TEC_Header_QB")
        self.label_TEC_Header_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_TEC_Header_QB, 0, 13, 1, 1)

        self.spinBox_R1_BLK_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R1_BLK_QB.setObjectName(u"spinBox_R1_BLK_QB")
        self.spinBox_R1_BLK_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_BLK_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R1_BLK_QB, 1, 8, 1, 1)

        self.spinBox_R1_STA_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R1_STA_QB.setObjectName(u"spinBox_R1_STA_QB")
        self.spinBox_R1_STA_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STA_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R1_STA_QB, 1, 6, 1, 1)

        self.label_WE_Header_QB = QLabel(self.gridLayoutWidget)
        self.label_WE_Header_QB.setObjectName(u"label_WE_Header_QB")
        self.label_WE_Header_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_WE_Header_QB, 0, 5, 1, 1)

        self.label_TKL_Header_QB = QLabel(self.gridLayoutWidget)
        self.label_TKL_Header_QB.setObjectName(u"label_TKL_Header_QB")
        self.label_TKL_Header_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_TKL_Header_QB, 0, 9, 1, 1)

        self.label_STR_Header_QB = QLabel(self.gridLayoutWidget)
        self.label_STR_Header_QB.setObjectName(u"label_STR_Header_QB")
        self.label_STR_Header_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_STR_Header_QB, 0, 7, 1, 1)

        self.spinBox_R1_WE_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R1_WE_QB.setObjectName(u"spinBox_R1_WE_QB")
        self.spinBox_R1_WE_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_WE_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R1_WE_QB, 1, 5, 1, 1)

        self.spinBox_R2_SPD_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R2_SPD_QB.setObjectName(u"spinBox_R2_SPD_QB")
        self.spinBox_R2_SPD_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_SPD_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R2_SPD_QB, 2, 3, 1, 1)

        self.label_R1_QB = QLabel(self.gridLayoutWidget)
        self.label_R1_QB.setObjectName(u"label_R1_QB")
        self.label_R1_QB.setFont(font1)
        self.label_R1_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_R1_QB, 1, 0, 1, 1)

        self.label_RoleHeader_QB = QLabel(self.gridLayoutWidget)
        self.label_RoleHeader_QB.setObjectName(u"label_RoleHeader_QB")
        self.label_RoleHeader_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_RoleHeader_QB, 0, 0, 1, 1)

        self.label_Total_Header_QB = QLabel(self.gridLayoutWidget)
        self.label_Total_Header_QB.setObjectName(u"label_Total_Header_QB")

        self.gridLayout.addWidget(self.label_Total_Header_QB, 0, 14, 1, 1)

        self.spinBox_R3_STA_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R3_STA_QB.setObjectName(u"spinBox_R3_STA_QB")
        self.spinBox_R3_STA_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STA_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R3_STA_QB, 3, 6, 1, 1)

        self.label_R5_QB = QLabel(self.gridLayoutWidget)
        self.label_R5_QB.setObjectName(u"label_R5_QB")
        self.label_R5_QB.setFont(font1)
        self.label_R5_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_R5_QB, 5, 0, 1, 1)

        self.label_BLK_Header_QB = QLabel(self.gridLayoutWidget)
        self.label_BLK_Header_QB.setObjectName(u"label_BLK_Header_QB")
        self.label_BLK_Header_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_BLK_Header_QB, 0, 8, 1, 1)

        self.label_ELU_Header_QB = QLabel(self.gridLayoutWidget)
        self.label_ELU_Header_QB.setObjectName(u"label_ELU_Header_QB")
        self.label_ELU_Header_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_ELU_Header_QB, 0, 12, 1, 1)

        self.spinBox_R2_BLK_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R2_BLK_QB.setObjectName(u"spinBox_R2_BLK_QB")
        self.spinBox_R2_BLK_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_BLK_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R2_BLK_QB, 2, 8, 1, 1)

        self.label_LabelHeader_QB = QLabel(self.gridLayoutWidget)
        self.label_LabelHeader_QB.setObjectName(u"label_LabelHeader_QB")
        self.label_LabelHeader_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_LabelHeader_QB, 0, 1, 1, 1)

        self.spinBox_R2_HAN_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R2_HAN_QB.setObjectName(u"spinBox_R2_HAN_QB")
        self.spinBox_R2_HAN_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_HAN_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R2_HAN_QB, 2, 10, 1, 1)

        self.label_R2_QB = QLabel(self.gridLayoutWidget)
        self.label_R2_QB.setObjectName(u"label_R2_QB")
        self.label_R2_QB.setFont(font1)
        self.label_R2_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_R2_QB, 2, 0, 1, 1)

        self.spinBox_R1_GI_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R1_GI_QB.setObjectName(u"spinBox_R1_GI_QB")
        self.spinBox_R1_GI_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_GI_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R1_GI_QB, 1, 11, 1, 1)

        self.label_DUR_Header_QB = QLabel(self.gridLayoutWidget)
        self.label_DUR_Header_QB.setObjectName(u"label_DUR_Header_QB")
        self.label_DUR_Header_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_DUR_Header_QB, 0, 4, 1, 1)

        self.spinBox_R1_HAN_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R1_HAN_QB.setObjectName(u"spinBox_R1_HAN_QB")
        self.spinBox_R1_HAN_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_HAN_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R1_HAN_QB, 1, 10, 1, 1)

        self.label_R3_QB = QLabel(self.gridLayoutWidget)
        self.label_R3_QB.setObjectName(u"label_R3_QB")
        self.label_R3_QB.setFont(font1)
        self.label_R3_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_R3_QB, 3, 0, 1, 1)

        self.label_GI_Header_QB = QLabel(self.gridLayoutWidget)
        self.label_GI_Header_QB.setObjectName(u"label_GI_Header_QB")
        self.label_GI_Header_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_GI_Header_QB, 0, 11, 1, 1)

        self.spinBox_R1_TEC_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R1_TEC_QB.setObjectName(u"spinBox_R1_TEC_QB")
        self.spinBox_R1_TEC_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TEC_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R1_TEC_QB, 1, 13, 1, 1)

        self.spinBox_R1_ATH_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R1_ATH_QB.setObjectName(u"spinBox_R1_ATH_QB")
        self.spinBox_R1_ATH_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ATH_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R1_ATH_QB, 1, 2, 1, 1)

        self.spinBox_R1_DUR_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R1_DUR_QB.setObjectName(u"spinBox_R1_DUR_QB")
        self.spinBox_R1_DUR_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_DUR_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R1_DUR_QB, 1, 4, 1, 1)

        self.spinBox_R2_ELU_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R2_ELU_QB.setObjectName(u"spinBox_R2_ELU_QB")
        self.spinBox_R2_ELU_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ELU_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R2_ELU_QB, 2, 12, 1, 1)

        self.spinBox_R2_ATH_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R2_ATH_QB.setObjectName(u"spinBox_R2_ATH_QB")
        self.spinBox_R2_ATH_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ATH_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R2_ATH_QB, 2, 2, 1, 1)

        self.spinBox_R2_STR_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R2_STR_QB.setObjectName(u"spinBox_R2_STR_QB")
        self.spinBox_R2_STR_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STR_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R2_STR_QB, 2, 7, 1, 1)

        self.spinBox_R3_ATH_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R3_ATH_QB.setObjectName(u"spinBox_R3_ATH_QB")
        self.spinBox_R3_ATH_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ATH_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R3_ATH_QB, 3, 2, 1, 1)

        self.spinBox_R1_ELU_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R1_ELU_QB.setObjectName(u"spinBox_R1_ELU_QB")
        self.spinBox_R1_ELU_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ELU_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R1_ELU_QB, 1, 12, 1, 1)

        self.label_STA_Header_QB = QLabel(self.gridLayoutWidget)
        self.label_STA_Header_QB.setObjectName(u"label_STA_Header_QB")
        self.label_STA_Header_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_STA_Header_QB, 0, 6, 1, 1)

        self.spinBox_R1_STR_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R1_STR_QB.setObjectName(u"spinBox_R1_STR_QB")
        self.spinBox_R1_STR_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STR_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R1_STR_QB, 1, 7, 1, 1)

        self.label_SPD_Header_QB = QLabel(self.gridLayoutWidget)
        self.label_SPD_Header_QB.setObjectName(u"label_SPD_Header_QB")
        self.label_SPD_Header_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_SPD_Header_QB, 0, 3, 1, 1)

        self.spinBox_R2_DUR_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R2_DUR_QB.setObjectName(u"spinBox_R2_DUR_QB")
        self.spinBox_R2_DUR_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_DUR_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R2_DUR_QB, 2, 4, 1, 1)

        self.label_HAN_Header_QB = QLabel(self.gridLayoutWidget)
        self.label_HAN_Header_QB.setObjectName(u"label_HAN_Header_QB")
        self.label_HAN_Header_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_HAN_Header_QB, 0, 10, 1, 1)

        self.label_R4_QB = QLabel(self.gridLayoutWidget)
        self.label_R4_QB.setObjectName(u"label_R4_QB")
        self.label_R4_QB.setFont(font1)
        self.label_R4_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_R4_QB, 4, 0, 1, 1)

        self.spinBox_R1_TKL_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R1_TKL_QB.setObjectName(u"spinBox_R1_TKL_QB")
        self.spinBox_R1_TKL_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TKL_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R1_TKL_QB, 1, 9, 1, 1)

        self.spinBox_R2_GI_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R2_GI_QB.setObjectName(u"spinBox_R2_GI_QB")
        self.spinBox_R2_GI_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_GI_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R2_GI_QB, 2, 11, 1, 1)

        self.spinBox_R3_WE_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R3_WE_QB.setObjectName(u"spinBox_R3_WE_QB")
        self.spinBox_R3_WE_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_WE_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R3_WE_QB, 3, 5, 1, 1)

        self.spinBox_R3_SPD_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R3_SPD_QB.setObjectName(u"spinBox_R3_SPD_QB")
        self.spinBox_R3_SPD_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_SPD_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R3_SPD_QB, 3, 3, 1, 1)

        self.label_R6_QB = QLabel(self.gridLayoutWidget)
        self.label_R6_QB.setObjectName(u"label_R6_QB")
        self.label_R6_QB.setFont(font1)
        self.label_R6_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_R6_QB, 6, 0, 1, 1)

        self.spinBox_R2_STA_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R2_STA_QB.setObjectName(u"spinBox_R2_STA_QB")
        self.spinBox_R2_STA_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STA_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R2_STA_QB, 2, 6, 1, 1)

        self.spinBox_R3_BLK_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R3_BLK_QB.setObjectName(u"spinBox_R3_BLK_QB")
        self.spinBox_R3_BLK_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_BLK_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R3_BLK_QB, 3, 8, 1, 1)

        self.spinBox_R3_TKL_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R3_TKL_QB.setObjectName(u"spinBox_R3_TKL_QB")
        self.spinBox_R3_TKL_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TKL_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R3_TKL_QB, 3, 9, 1, 1)

        self.spinBox_R3_HAN_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R3_HAN_QB.setObjectName(u"spinBox_R3_HAN_QB")
        self.spinBox_R3_HAN_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_HAN_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R3_HAN_QB, 3, 10, 1, 1)

        self.spinBox_R3_GI_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R3_GI_QB.setObjectName(u"spinBox_R3_GI_QB")
        self.spinBox_R3_GI_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_GI_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R3_GI_QB, 3, 11, 1, 1)

        self.spinBox_R3_ELU_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R3_ELU_QB.setObjectName(u"spinBox_R3_ELU_QB")
        self.spinBox_R3_ELU_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ELU_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R3_ELU_QB, 3, 12, 1, 1)

        self.spinBox_R3_TEC_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R3_TEC_QB.setObjectName(u"spinBox_R3_TEC_QB")
        self.spinBox_R3_TEC_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TEC_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R3_TEC_QB, 3, 13, 1, 1)

        self.spinBox_R4_ATH_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R4_ATH_QB.setObjectName(u"spinBox_R4_ATH_QB")
        self.spinBox_R4_ATH_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ATH_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R4_ATH_QB, 4, 2, 1, 1)

        self.spinBox_R4_SPD_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R4_SPD_QB.setObjectName(u"spinBox_R4_SPD_QB")
        self.spinBox_R4_SPD_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_SPD_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R4_SPD_QB, 4, 3, 1, 1)

        self.spinBox_R4_DUR_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R4_DUR_QB.setObjectName(u"spinBox_R4_DUR_QB")
        self.spinBox_R4_DUR_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_DUR_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R4_DUR_QB, 4, 4, 1, 1)

        self.spinBox_R4_WE_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R4_WE_QB.setObjectName(u"spinBox_R4_WE_QB")
        self.spinBox_R4_WE_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_WE_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R4_WE_QB, 4, 5, 1, 1)

        self.spinBox_R4_STA_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R4_STA_QB.setObjectName(u"spinBox_R4_STA_QB")
        self.spinBox_R4_STA_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STA_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R4_STA_QB, 4, 6, 1, 1)

        self.spinBox_R4_STR_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R4_STR_QB.setObjectName(u"spinBox_R4_STR_QB")
        self.spinBox_R4_STR_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STR_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R4_STR_QB, 4, 7, 1, 1)

        self.spinBox_R4_BLK_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R4_BLK_QB.setObjectName(u"spinBox_R4_BLK_QB")
        self.spinBox_R4_BLK_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_BLK_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R4_BLK_QB, 4, 8, 1, 1)

        self.spinBox_R4_TKL_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R4_TKL_QB.setObjectName(u"spinBox_R4_TKL_QB")
        self.spinBox_R4_TKL_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TKL_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R4_TKL_QB, 4, 9, 1, 1)

        self.spinBox_R4_HAN_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R4_HAN_QB.setObjectName(u"spinBox_R4_HAN_QB")
        self.spinBox_R4_HAN_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_HAN_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R4_HAN_QB, 4, 10, 1, 1)

        self.spinBox_R4_GI_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R4_GI_QB.setObjectName(u"spinBox_R4_GI_QB")
        self.spinBox_R4_GI_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_GI_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R4_GI_QB, 4, 11, 1, 1)

        self.spinBox_R4_ELU_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R4_ELU_QB.setObjectName(u"spinBox_R4_ELU_QB")
        self.spinBox_R4_ELU_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ELU_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R4_ELU_QB, 4, 12, 1, 1)

        self.spinBox_R4_TEC_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R4_TEC_QB.setObjectName(u"spinBox_R4_TEC_QB")
        self.spinBox_R4_TEC_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TEC_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R4_TEC_QB, 4, 13, 1, 1)

        self.spinBox_R5_ATH_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R5_ATH_QB.setObjectName(u"spinBox_R5_ATH_QB")
        self.spinBox_R5_ATH_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ATH_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R5_ATH_QB, 5, 2, 1, 1)

        self.spinBox_R5_SPD_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R5_SPD_QB.setObjectName(u"spinBox_R5_SPD_QB")
        self.spinBox_R5_SPD_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_SPD_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R5_SPD_QB, 5, 3, 1, 1)

        self.spinBox_R5_DUR_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R5_DUR_QB.setObjectName(u"spinBox_R5_DUR_QB")
        self.spinBox_R5_DUR_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_DUR_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R5_DUR_QB, 5, 4, 1, 1)

        self.spinBox_R5_WE_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R5_WE_QB.setObjectName(u"spinBox_R5_WE_QB")
        self.spinBox_R5_WE_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_WE_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R5_WE_QB, 5, 5, 1, 1)

        self.spinBox_R5_STA_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R5_STA_QB.setObjectName(u"spinBox_R5_STA_QB")
        self.spinBox_R5_STA_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STA_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R5_STA_QB, 5, 6, 1, 1)

        self.spinBox_R5_STR_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R5_STR_QB.setObjectName(u"spinBox_R5_STR_QB")
        self.spinBox_R5_STR_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STR_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R5_STR_QB, 5, 7, 1, 1)

        self.spinBox_R5_BLK_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R5_BLK_QB.setObjectName(u"spinBox_R5_BLK_QB")
        self.spinBox_R5_BLK_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_BLK_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R5_BLK_QB, 5, 8, 1, 1)

        self.spinBox_R5_TKL_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R5_TKL_QB.setObjectName(u"spinBox_R5_TKL_QB")
        self.spinBox_R5_TKL_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TKL_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R5_TKL_QB, 5, 9, 1, 1)

        self.spinBox_R5_HAN_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R5_HAN_QB.setObjectName(u"spinBox_R5_HAN_QB")
        self.spinBox_R5_HAN_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_HAN_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R5_HAN_QB, 5, 10, 1, 1)

        self.spinBox_R5_GI_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R5_GI_QB.setObjectName(u"spinBox_R5_GI_QB")
        self.spinBox_R5_GI_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_GI_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R5_GI_QB, 5, 11, 1, 1)

        self.spinBox_R5_ELU_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R5_ELU_QB.setObjectName(u"spinBox_R5_ELU_QB")
        self.spinBox_R5_ELU_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ELU_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R5_ELU_QB, 5, 12, 1, 1)

        self.spinBox_R5_TEC_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R5_TEC_QB.setObjectName(u"spinBox_R5_TEC_QB")
        self.spinBox_R5_TEC_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TEC_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R5_TEC_QB, 5, 13, 1, 1)

        self.spinBox_R6_ATH_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R6_ATH_QB.setObjectName(u"spinBox_R6_ATH_QB")
        self.spinBox_R6_ATH_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ATH_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R6_ATH_QB, 6, 2, 1, 1)

        self.spinBox_R6_SPD_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R6_SPD_QB.setObjectName(u"spinBox_R6_SPD_QB")
        self.spinBox_R6_SPD_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_SPD_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R6_SPD_QB, 6, 3, 1, 1)

        self.spinBox_R6_DUR_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R6_DUR_QB.setObjectName(u"spinBox_R6_DUR_QB")
        self.spinBox_R6_DUR_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_DUR_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R6_DUR_QB, 6, 4, 1, 1)

        self.spinBox_R6_WE_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R6_WE_QB.setObjectName(u"spinBox_R6_WE_QB")
        self.spinBox_R6_WE_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_WE_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R6_WE_QB, 6, 5, 1, 1)

        self.spinBox_R6_STA_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R6_STA_QB.setObjectName(u"spinBox_R6_STA_QB")
        self.spinBox_R6_STA_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STA_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R6_STA_QB, 6, 6, 1, 1)

        self.spinBox_R6_STR_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R6_STR_QB.setObjectName(u"spinBox_R6_STR_QB")
        self.spinBox_R6_STR_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STR_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R6_STR_QB, 6, 7, 1, 1)

        self.spinBox_R6_BLK_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R6_BLK_QB.setObjectName(u"spinBox_R6_BLK_QB")
        self.spinBox_R6_BLK_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_BLK_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R6_BLK_QB, 6, 8, 1, 1)

        self.spinBox_R6_TKL_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R6_TKL_QB.setObjectName(u"spinBox_R6_TKL_QB")
        self.spinBox_R6_TKL_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TKL_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R6_TKL_QB, 6, 9, 1, 1)

        self.spinBox_R6_HAN_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R6_HAN_QB.setObjectName(u"spinBox_R6_HAN_QB")
        self.spinBox_R6_HAN_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_HAN_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R6_HAN_QB, 6, 10, 1, 1)

        self.spinBox_R6_GI_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R6_GI_QB.setObjectName(u"spinBox_R6_GI_QB")
        self.spinBox_R6_GI_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_GI_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R6_GI_QB, 6, 11, 1, 1)

        self.spinBox_R6_ELU_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R6_ELU_QB.setObjectName(u"spinBox_R6_ELU_QB")
        self.spinBox_R6_ELU_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ELU_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R6_ELU_QB, 6, 12, 1, 1)

        self.spinBox_R6_TEC_QB = QSpinBox(self.gridLayoutWidget)
        self.spinBox_R6_TEC_QB.setObjectName(u"spinBox_R6_TEC_QB")
        self.spinBox_R6_TEC_QB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TEC_QB.setMaximum(100)

        self.gridLayout.addWidget(self.spinBox_R6_TEC_QB, 6, 13, 1, 1)

        self.lineEdit_R1_QB = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_R1_QB.setObjectName(u"lineEdit_R1_QB")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        self.lineEdit_R1_QB.setFont(font2)
        self.lineEdit_R1_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_R1_QB, 1, 1, 1, 1)

        self.lineEdit_R2_QB = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_R2_QB.setObjectName(u"lineEdit_R2_QB")
        self.lineEdit_R2_QB.setFont(font2)
        self.lineEdit_R2_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_R2_QB, 2, 1, 1, 1)

        self.lineEdit_R3_QB = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_R3_QB.setObjectName(u"lineEdit_R3_QB")
        self.lineEdit_R3_QB.setFont(font2)
        self.lineEdit_R3_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_R3_QB, 3, 1, 1, 1)

        self.lineEdit_R4_QB = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_R4_QB.setObjectName(u"lineEdit_R4_QB")
        self.lineEdit_R4_QB.setFont(font2)
        self.lineEdit_R4_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_R4_QB, 4, 1, 1, 1)

        self.lineEdit_R5_QB = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_R5_QB.setObjectName(u"lineEdit_R5_QB")
        self.lineEdit_R5_QB.setFont(font2)
        self.lineEdit_R5_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_R5_QB, 5, 1, 1, 1)

        self.lineEdit_R6_QB = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_R6_QB.setObjectName(u"lineEdit_R6_QB")
        self.lineEdit_R6_QB.setFont(font2)
        self.lineEdit_R6_QB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_R6_QB, 6, 1, 1, 1)

        self.lcdNumber_R1_QB = QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_R1_QB.setObjectName(u"lcdNumber_R1_QB")
        self.lcdNumber_R1_QB.setDigitCount(3)
        self.lcdNumber_R1_QB.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.lcdNumber_R1_QB, 1, 14, 1, 1)

        self.lcdNumber_R2_QB = QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_R2_QB.setObjectName(u"lcdNumber_R2_QB")
        self.lcdNumber_R2_QB.setDigitCount(3)
        self.lcdNumber_R2_QB.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.lcdNumber_R2_QB, 2, 14, 1, 1)

        self.lcdNumber_R3_QB = QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_R3_QB.setObjectName(u"lcdNumber_R3_QB")
        self.lcdNumber_R3_QB.setDigitCount(3)
        self.lcdNumber_R3_QB.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.lcdNumber_R3_QB, 3, 14, 1, 1)

        self.lcdNumber_R4_QB = QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_R4_QB.setObjectName(u"lcdNumber_R4_QB")
        self.lcdNumber_R4_QB.setDigitCount(3)
        self.lcdNumber_R4_QB.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.lcdNumber_R4_QB, 4, 14, 1, 1)

        self.lcdNumber_R5_QB = QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_R5_QB.setObjectName(u"lcdNumber_R5_QB")
        self.lcdNumber_R5_QB.setDigitCount(3)
        self.lcdNumber_R5_QB.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.lcdNumber_R5_QB, 5, 14, 1, 1)

        self.lcdNumber_R6_QB = QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_R6_QB.setObjectName(u"lcdNumber_R6_QB")
        self.lcdNumber_R6_QB.setDigitCount(3)
        self.lcdNumber_R6_QB.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.lcdNumber_R6_QB, 6, 14, 1, 1)

        self.tabWidgetRoleRatings.addTab(self.QB, "")
        self.RB = QWidget()
        self.RB.setObjectName(u"RB")
        self.gridLayoutWidget_2 = QWidget(self.RB)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 10, 1215, 261))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_ATH_Header_RB = QLabel(self.gridLayoutWidget_2)
        self.label_ATH_Header_RB.setObjectName(u"label_ATH_Header_RB")
        self.label_ATH_Header_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_ATH_Header_RB, 0, 2, 1, 1)

        self.spinBox_R2_TKL_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R2_TKL_RB.setObjectName(u"spinBox_R2_TKL_RB")
        self.spinBox_R2_TKL_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TKL_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R2_TKL_RB, 2, 9, 1, 1)

        self.spinBox_R3_DUR_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R3_DUR_RB.setObjectName(u"spinBox_R3_DUR_RB")
        self.spinBox_R3_DUR_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_DUR_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R3_DUR_RB, 3, 4, 1, 1)

        self.spinBox_R3_STR_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R3_STR_RB.setObjectName(u"spinBox_R3_STR_RB")
        self.spinBox_R3_STR_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STR_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R3_STR_RB, 3, 7, 1, 1)

        self.spinBox_R2_TEC_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R2_TEC_RB.setObjectName(u"spinBox_R2_TEC_RB")
        self.spinBox_R2_TEC_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TEC_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R2_TEC_RB, 2, 13, 1, 1)

        self.spinBox_R2_WE_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R2_WE_RB.setObjectName(u"spinBox_R2_WE_RB")
        self.spinBox_R2_WE_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_WE_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R2_WE_RB, 2, 5, 1, 1)

        self.spinBox_R1_SPD_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R1_SPD_RB.setObjectName(u"spinBox_R1_SPD_RB")
        self.spinBox_R1_SPD_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_SPD_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R1_SPD_RB, 1, 3, 1, 1)

        self.label_TEC_Header_RB = QLabel(self.gridLayoutWidget_2)
        self.label_TEC_Header_RB.setObjectName(u"label_TEC_Header_RB")
        self.label_TEC_Header_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_TEC_Header_RB, 0, 13, 1, 1)

        self.spinBox_R1_BLK_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R1_BLK_RB.setObjectName(u"spinBox_R1_BLK_RB")
        self.spinBox_R1_BLK_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_BLK_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R1_BLK_RB, 1, 8, 1, 1)

        self.spinBox_R1_STA_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R1_STA_RB.setObjectName(u"spinBox_R1_STA_RB")
        self.spinBox_R1_STA_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STA_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R1_STA_RB, 1, 6, 1, 1)

        self.label_WE_Header_RB = QLabel(self.gridLayoutWidget_2)
        self.label_WE_Header_RB.setObjectName(u"label_WE_Header_RB")
        self.label_WE_Header_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_WE_Header_RB, 0, 5, 1, 1)

        self.label_TKL_Header_RB = QLabel(self.gridLayoutWidget_2)
        self.label_TKL_Header_RB.setObjectName(u"label_TKL_Header_RB")
        self.label_TKL_Header_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_TKL_Header_RB, 0, 9, 1, 1)

        self.label_STR_Header_RB = QLabel(self.gridLayoutWidget_2)
        self.label_STR_Header_RB.setObjectName(u"label_STR_Header_RB")
        self.label_STR_Header_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_STR_Header_RB, 0, 7, 1, 1)

        self.spinBox_R1_WE_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R1_WE_RB.setObjectName(u"spinBox_R1_WE_RB")
        self.spinBox_R1_WE_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_WE_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R1_WE_RB, 1, 5, 1, 1)

        self.spinBox_R2_SPD_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R2_SPD_RB.setObjectName(u"spinBox_R2_SPD_RB")
        self.spinBox_R2_SPD_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_SPD_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R2_SPD_RB, 2, 3, 1, 1)

        self.label_R1_RB = QLabel(self.gridLayoutWidget_2)
        self.label_R1_RB.setObjectName(u"label_R1_RB")
        self.label_R1_RB.setFont(font1)
        self.label_R1_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_R1_RB, 1, 0, 1, 1)

        self.label_RoleHeader_RB = QLabel(self.gridLayoutWidget_2)
        self.label_RoleHeader_RB.setObjectName(u"label_RoleHeader_RB")
        self.label_RoleHeader_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_RoleHeader_RB, 0, 0, 1, 1)

        self.label_Total_Header_RB = QLabel(self.gridLayoutWidget_2)
        self.label_Total_Header_RB.setObjectName(u"label_Total_Header_RB")

        self.gridLayout_2.addWidget(self.label_Total_Header_RB, 0, 14, 1, 1)

        self.spinBox_R3_STA_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R3_STA_RB.setObjectName(u"spinBox_R3_STA_RB")
        self.spinBox_R3_STA_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STA_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R3_STA_RB, 3, 6, 1, 1)

        self.label_R5_RB = QLabel(self.gridLayoutWidget_2)
        self.label_R5_RB.setObjectName(u"label_R5_RB")
        self.label_R5_RB.setFont(font1)
        self.label_R5_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_R5_RB, 5, 0, 1, 1)

        self.label_BLK_Header_RB = QLabel(self.gridLayoutWidget_2)
        self.label_BLK_Header_RB.setObjectName(u"label_BLK_Header_RB")
        self.label_BLK_Header_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_BLK_Header_RB, 0, 8, 1, 1)

        self.label_ELU_Header_RB = QLabel(self.gridLayoutWidget_2)
        self.label_ELU_Header_RB.setObjectName(u"label_ELU_Header_RB")
        self.label_ELU_Header_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_ELU_Header_RB, 0, 12, 1, 1)

        self.spinBox_R2_BLK_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R2_BLK_RB.setObjectName(u"spinBox_R2_BLK_RB")
        self.spinBox_R2_BLK_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_BLK_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R2_BLK_RB, 2, 8, 1, 1)

        self.label_LabelHeader_RB = QLabel(self.gridLayoutWidget_2)
        self.label_LabelHeader_RB.setObjectName(u"label_LabelHeader_RB")
        self.label_LabelHeader_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_LabelHeader_RB, 0, 1, 1, 1)

        self.spinBox_R2_HAN_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R2_HAN_RB.setObjectName(u"spinBox_R2_HAN_RB")
        self.spinBox_R2_HAN_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_HAN_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R2_HAN_RB, 2, 10, 1, 1)

        self.label_R2_RB = QLabel(self.gridLayoutWidget_2)
        self.label_R2_RB.setObjectName(u"label_R2_RB")
        self.label_R2_RB.setFont(font1)
        self.label_R2_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_R2_RB, 2, 0, 1, 1)

        self.spinBox_R1_GI_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R1_GI_RB.setObjectName(u"spinBox_R1_GI_RB")
        self.spinBox_R1_GI_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_GI_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R1_GI_RB, 1, 11, 1, 1)

        self.label_DUR_Header_RB = QLabel(self.gridLayoutWidget_2)
        self.label_DUR_Header_RB.setObjectName(u"label_DUR_Header_RB")
        self.label_DUR_Header_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_DUR_Header_RB, 0, 4, 1, 1)

        self.spinBox_R1_HAN_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R1_HAN_RB.setObjectName(u"spinBox_R1_HAN_RB")
        self.spinBox_R1_HAN_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_HAN_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R1_HAN_RB, 1, 10, 1, 1)

        self.label_R3_RB = QLabel(self.gridLayoutWidget_2)
        self.label_R3_RB.setObjectName(u"label_R3_RB")
        self.label_R3_RB.setFont(font1)
        self.label_R3_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_R3_RB, 3, 0, 1, 1)

        self.label_GI_Header_RB = QLabel(self.gridLayoutWidget_2)
        self.label_GI_Header_RB.setObjectName(u"label_GI_Header_RB")
        self.label_GI_Header_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_GI_Header_RB, 0, 11, 1, 1)

        self.spinBox_R1_TEC_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R1_TEC_RB.setObjectName(u"spinBox_R1_TEC_RB")
        self.spinBox_R1_TEC_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TEC_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R1_TEC_RB, 1, 13, 1, 1)

        self.spinBox_R1_ATH_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R1_ATH_RB.setObjectName(u"spinBox_R1_ATH_RB")
        self.spinBox_R1_ATH_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ATH_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R1_ATH_RB, 1, 2, 1, 1)

        self.spinBox_R1_DUR_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R1_DUR_RB.setObjectName(u"spinBox_R1_DUR_RB")
        self.spinBox_R1_DUR_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_DUR_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R1_DUR_RB, 1, 4, 1, 1)

        self.spinBox_R2_ELU_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R2_ELU_RB.setObjectName(u"spinBox_R2_ELU_RB")
        self.spinBox_R2_ELU_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ELU_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R2_ELU_RB, 2, 12, 1, 1)

        self.spinBox_R2_ATH_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R2_ATH_RB.setObjectName(u"spinBox_R2_ATH_RB")
        self.spinBox_R2_ATH_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ATH_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R2_ATH_RB, 2, 2, 1, 1)

        self.spinBox_R2_STR_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R2_STR_RB.setObjectName(u"spinBox_R2_STR_RB")
        self.spinBox_R2_STR_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STR_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R2_STR_RB, 2, 7, 1, 1)

        self.spinBox_R3_ATH_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R3_ATH_RB.setObjectName(u"spinBox_R3_ATH_RB")
        self.spinBox_R3_ATH_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ATH_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R3_ATH_RB, 3, 2, 1, 1)

        self.spinBox_R1_ELU_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R1_ELU_RB.setObjectName(u"spinBox_R1_ELU_RB")
        self.spinBox_R1_ELU_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ELU_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R1_ELU_RB, 1, 12, 1, 1)

        self.label_STA_Header_RB = QLabel(self.gridLayoutWidget_2)
        self.label_STA_Header_RB.setObjectName(u"label_STA_Header_RB")
        self.label_STA_Header_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_STA_Header_RB, 0, 6, 1, 1)

        self.spinBox_R1_STR_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R1_STR_RB.setObjectName(u"spinBox_R1_STR_RB")
        self.spinBox_R1_STR_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STR_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R1_STR_RB, 1, 7, 1, 1)

        self.label_SPD_Header_RB = QLabel(self.gridLayoutWidget_2)
        self.label_SPD_Header_RB.setObjectName(u"label_SPD_Header_RB")
        self.label_SPD_Header_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_SPD_Header_RB, 0, 3, 1, 1)

        self.spinBox_R2_DUR_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R2_DUR_RB.setObjectName(u"spinBox_R2_DUR_RB")
        self.spinBox_R2_DUR_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_DUR_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R2_DUR_RB, 2, 4, 1, 1)

        self.label_HAN_Header_RB = QLabel(self.gridLayoutWidget_2)
        self.label_HAN_Header_RB.setObjectName(u"label_HAN_Header_RB")
        self.label_HAN_Header_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_HAN_Header_RB, 0, 10, 1, 1)

        self.label_R4_RB = QLabel(self.gridLayoutWidget_2)
        self.label_R4_RB.setObjectName(u"label_R4_RB")
        self.label_R4_RB.setFont(font1)
        self.label_R4_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_R4_RB, 4, 0, 1, 1)

        self.spinBox_R1_TKL_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R1_TKL_RB.setObjectName(u"spinBox_R1_TKL_RB")
        self.spinBox_R1_TKL_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TKL_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R1_TKL_RB, 1, 9, 1, 1)

        self.spinBox_R2_GI_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R2_GI_RB.setObjectName(u"spinBox_R2_GI_RB")
        self.spinBox_R2_GI_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_GI_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R2_GI_RB, 2, 11, 1, 1)

        self.spinBox_R3_WE_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R3_WE_RB.setObjectName(u"spinBox_R3_WE_RB")
        self.spinBox_R3_WE_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_WE_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R3_WE_RB, 3, 5, 1, 1)

        self.spinBox_R3_SPD_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R3_SPD_RB.setObjectName(u"spinBox_R3_SPD_RB")
        self.spinBox_R3_SPD_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_SPD_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R3_SPD_RB, 3, 3, 1, 1)

        self.label_R6_RB = QLabel(self.gridLayoutWidget_2)
        self.label_R6_RB.setObjectName(u"label_R6_RB")
        self.label_R6_RB.setFont(font1)
        self.label_R6_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_R6_RB, 6, 0, 1, 1)

        self.spinBox_R2_STA_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R2_STA_RB.setObjectName(u"spinBox_R2_STA_RB")
        self.spinBox_R2_STA_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STA_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R2_STA_RB, 2, 6, 1, 1)

        self.spinBox_R3_BLK_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R3_BLK_RB.setObjectName(u"spinBox_R3_BLK_RB")
        self.spinBox_R3_BLK_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_BLK_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R3_BLK_RB, 3, 8, 1, 1)

        self.spinBox_R3_TKL_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R3_TKL_RB.setObjectName(u"spinBox_R3_TKL_RB")
        self.spinBox_R3_TKL_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TKL_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R3_TKL_RB, 3, 9, 1, 1)

        self.spinBox_R3_HAN_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R3_HAN_RB.setObjectName(u"spinBox_R3_HAN_RB")
        self.spinBox_R3_HAN_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_HAN_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R3_HAN_RB, 3, 10, 1, 1)

        self.spinBox_R3_GI_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R3_GI_RB.setObjectName(u"spinBox_R3_GI_RB")
        self.spinBox_R3_GI_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_GI_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R3_GI_RB, 3, 11, 1, 1)

        self.spinBox_R3_ELU_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R3_ELU_RB.setObjectName(u"spinBox_R3_ELU_RB")
        self.spinBox_R3_ELU_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ELU_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R3_ELU_RB, 3, 12, 1, 1)

        self.spinBox_R3_TEC_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R3_TEC_RB.setObjectName(u"spinBox_R3_TEC_RB")
        self.spinBox_R3_TEC_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TEC_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R3_TEC_RB, 3, 13, 1, 1)

        self.spinBox_R4_ATH_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R4_ATH_RB.setObjectName(u"spinBox_R4_ATH_RB")
        self.spinBox_R4_ATH_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ATH_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R4_ATH_RB, 4, 2, 1, 1)

        self.spinBox_R4_SPD_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R4_SPD_RB.setObjectName(u"spinBox_R4_SPD_RB")
        self.spinBox_R4_SPD_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_SPD_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R4_SPD_RB, 4, 3, 1, 1)

        self.spinBox_R4_DUR_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R4_DUR_RB.setObjectName(u"spinBox_R4_DUR_RB")
        self.spinBox_R4_DUR_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_DUR_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R4_DUR_RB, 4, 4, 1, 1)

        self.spinBox_R4_WE_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R4_WE_RB.setObjectName(u"spinBox_R4_WE_RB")
        self.spinBox_R4_WE_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_WE_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R4_WE_RB, 4, 5, 1, 1)

        self.spinBox_R4_STA_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R4_STA_RB.setObjectName(u"spinBox_R4_STA_RB")
        self.spinBox_R4_STA_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STA_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R4_STA_RB, 4, 6, 1, 1)

        self.spinBox_R4_STR_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R4_STR_RB.setObjectName(u"spinBox_R4_STR_RB")
        self.spinBox_R4_STR_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STR_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R4_STR_RB, 4, 7, 1, 1)

        self.spinBox_R4_BLK_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R4_BLK_RB.setObjectName(u"spinBox_R4_BLK_RB")
        self.spinBox_R4_BLK_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_BLK_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R4_BLK_RB, 4, 8, 1, 1)

        self.spinBox_R4_TKL_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R4_TKL_RB.setObjectName(u"spinBox_R4_TKL_RB")
        self.spinBox_R4_TKL_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TKL_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R4_TKL_RB, 4, 9, 1, 1)

        self.spinBox_R4_HAN_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R4_HAN_RB.setObjectName(u"spinBox_R4_HAN_RB")
        self.spinBox_R4_HAN_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_HAN_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R4_HAN_RB, 4, 10, 1, 1)

        self.spinBox_R4_GI_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R4_GI_RB.setObjectName(u"spinBox_R4_GI_RB")
        self.spinBox_R4_GI_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_GI_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R4_GI_RB, 4, 11, 1, 1)

        self.spinBox_R4_ELU_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R4_ELU_RB.setObjectName(u"spinBox_R4_ELU_RB")
        self.spinBox_R4_ELU_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ELU_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R4_ELU_RB, 4, 12, 1, 1)

        self.spinBox_R4_TEC_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R4_TEC_RB.setObjectName(u"spinBox_R4_TEC_RB")
        self.spinBox_R4_TEC_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TEC_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R4_TEC_RB, 4, 13, 1, 1)

        self.spinBox_R5_ATH_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R5_ATH_RB.setObjectName(u"spinBox_R5_ATH_RB")
        self.spinBox_R5_ATH_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ATH_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R5_ATH_RB, 5, 2, 1, 1)

        self.spinBox_R5_SPD_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R5_SPD_RB.setObjectName(u"spinBox_R5_SPD_RB")
        self.spinBox_R5_SPD_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_SPD_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R5_SPD_RB, 5, 3, 1, 1)

        self.spinBox_R5_DUR_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R5_DUR_RB.setObjectName(u"spinBox_R5_DUR_RB")
        self.spinBox_R5_DUR_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_DUR_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R5_DUR_RB, 5, 4, 1, 1)

        self.spinBox_R5_WE_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R5_WE_RB.setObjectName(u"spinBox_R5_WE_RB")
        self.spinBox_R5_WE_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_WE_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R5_WE_RB, 5, 5, 1, 1)

        self.spinBox_R5_STA_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R5_STA_RB.setObjectName(u"spinBox_R5_STA_RB")
        self.spinBox_R5_STA_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STA_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R5_STA_RB, 5, 6, 1, 1)

        self.spinBox_R5_STR_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R5_STR_RB.setObjectName(u"spinBox_R5_STR_RB")
        self.spinBox_R5_STR_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STR_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R5_STR_RB, 5, 7, 1, 1)

        self.spinBox_R5_BLK_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R5_BLK_RB.setObjectName(u"spinBox_R5_BLK_RB")
        self.spinBox_R5_BLK_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_BLK_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R5_BLK_RB, 5, 8, 1, 1)

        self.spinBox_R5_TKL_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R5_TKL_RB.setObjectName(u"spinBox_R5_TKL_RB")
        self.spinBox_R5_TKL_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TKL_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R5_TKL_RB, 5, 9, 1, 1)

        self.spinBox_R5_HAN_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R5_HAN_RB.setObjectName(u"spinBox_R5_HAN_RB")
        self.spinBox_R5_HAN_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_HAN_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R5_HAN_RB, 5, 10, 1, 1)

        self.spinBox_R5_GI_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R5_GI_RB.setObjectName(u"spinBox_R5_GI_RB")
        self.spinBox_R5_GI_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_GI_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R5_GI_RB, 5, 11, 1, 1)

        self.spinBox_R5_ELU_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R5_ELU_RB.setObjectName(u"spinBox_R5_ELU_RB")
        self.spinBox_R5_ELU_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ELU_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R5_ELU_RB, 5, 12, 1, 1)

        self.spinBox_R5_TEC_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R5_TEC_RB.setObjectName(u"spinBox_R5_TEC_RB")
        self.spinBox_R5_TEC_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TEC_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R5_TEC_RB, 5, 13, 1, 1)

        self.spinBox_R6_ATH_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R6_ATH_RB.setObjectName(u"spinBox_R6_ATH_RB")
        self.spinBox_R6_ATH_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ATH_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R6_ATH_RB, 6, 2, 1, 1)

        self.spinBox_R6_SPD_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R6_SPD_RB.setObjectName(u"spinBox_R6_SPD_RB")
        self.spinBox_R6_SPD_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_SPD_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R6_SPD_RB, 6, 3, 1, 1)

        self.spinBox_R6_DUR_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R6_DUR_RB.setObjectName(u"spinBox_R6_DUR_RB")
        self.spinBox_R6_DUR_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_DUR_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R6_DUR_RB, 6, 4, 1, 1)

        self.spinBox_R6_WE_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R6_WE_RB.setObjectName(u"spinBox_R6_WE_RB")
        self.spinBox_R6_WE_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_WE_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R6_WE_RB, 6, 5, 1, 1)

        self.spinBox_R6_STA_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R6_STA_RB.setObjectName(u"spinBox_R6_STA_RB")
        self.spinBox_R6_STA_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STA_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R6_STA_RB, 6, 6, 1, 1)

        self.spinBox_R6_STR_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R6_STR_RB.setObjectName(u"spinBox_R6_STR_RB")
        self.spinBox_R6_STR_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STR_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R6_STR_RB, 6, 7, 1, 1)

        self.spinBox_R6_BLK_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R6_BLK_RB.setObjectName(u"spinBox_R6_BLK_RB")
        self.spinBox_R6_BLK_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_BLK_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R6_BLK_RB, 6, 8, 1, 1)

        self.spinBox_R6_TKL_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R6_TKL_RB.setObjectName(u"spinBox_R6_TKL_RB")
        self.spinBox_R6_TKL_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TKL_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R6_TKL_RB, 6, 9, 1, 1)

        self.spinBox_R6_HAN_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R6_HAN_RB.setObjectName(u"spinBox_R6_HAN_RB")
        self.spinBox_R6_HAN_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_HAN_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R6_HAN_RB, 6, 10, 1, 1)

        self.spinBox_R6_GI_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R6_GI_RB.setObjectName(u"spinBox_R6_GI_RB")
        self.spinBox_R6_GI_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_GI_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R6_GI_RB, 6, 11, 1, 1)

        self.spinBox_R6_ELU_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R6_ELU_RB.setObjectName(u"spinBox_R6_ELU_RB")
        self.spinBox_R6_ELU_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ELU_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R6_ELU_RB, 6, 12, 1, 1)

        self.spinBox_R6_TEC_RB = QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_R6_TEC_RB.setObjectName(u"spinBox_R6_TEC_RB")
        self.spinBox_R6_TEC_RB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TEC_RB.setMaximum(100)

        self.gridLayout_2.addWidget(self.spinBox_R6_TEC_RB, 6, 13, 1, 1)

        self.lineEdit_R1_RB = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_R1_RB.setObjectName(u"lineEdit_R1_RB")
        self.lineEdit_R1_RB.setFont(font2)
        self.lineEdit_R1_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_R1_RB, 1, 1, 1, 1)

        self.lineEdit_R2_RB = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_R2_RB.setObjectName(u"lineEdit_R2_RB")
        self.lineEdit_R2_RB.setFont(font2)
        self.lineEdit_R2_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_R2_RB, 2, 1, 1, 1)

        self.lineEdit_R3_RB = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_R3_RB.setObjectName(u"lineEdit_R3_RB")
        self.lineEdit_R3_RB.setFont(font2)
        self.lineEdit_R3_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_R3_RB, 3, 1, 1, 1)

        self.lineEdit_R4_RB = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_R4_RB.setObjectName(u"lineEdit_R4_RB")
        self.lineEdit_R4_RB.setFont(font2)
        self.lineEdit_R4_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_R4_RB, 4, 1, 1, 1)

        self.lineEdit_R5_RB = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_R5_RB.setObjectName(u"lineEdit_R5_RB")
        self.lineEdit_R5_RB.setFont(font2)
        self.lineEdit_R5_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_R5_RB, 5, 1, 1, 1)

        self.lineEdit_R6_RB = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_R6_RB.setObjectName(u"lineEdit_R6_RB")
        self.lineEdit_R6_RB.setFont(font2)
        self.lineEdit_R6_RB.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_R6_RB, 6, 1, 1, 1)

        self.lcdNumber_R1_RB = QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumber_R1_RB.setObjectName(u"lcdNumber_R1_RB")
        self.lcdNumber_R1_RB.setDigitCount(3)
        self.lcdNumber_R1_RB.setProperty("intValue", 0)

        self.gridLayout_2.addWidget(self.lcdNumber_R1_RB, 1, 14, 1, 1)

        self.lcdNumber_R2_RB = QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumber_R2_RB.setObjectName(u"lcdNumber_R2_RB")
        self.lcdNumber_R2_RB.setDigitCount(3)
        self.lcdNumber_R2_RB.setProperty("intValue", 0)

        self.gridLayout_2.addWidget(self.lcdNumber_R2_RB, 2, 14, 1, 1)

        self.lcdNumber_R3_RB = QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumber_R3_RB.setObjectName(u"lcdNumber_R3_RB")
        self.lcdNumber_R3_RB.setDigitCount(3)
        self.lcdNumber_R3_RB.setProperty("intValue", 0)

        self.gridLayout_2.addWidget(self.lcdNumber_R3_RB, 3, 14, 1, 1)

        self.lcdNumber_R4_RB = QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumber_R4_RB.setObjectName(u"lcdNumber_R4_RB")
        self.lcdNumber_R4_RB.setDigitCount(3)
        self.lcdNumber_R4_RB.setProperty("intValue", 0)

        self.gridLayout_2.addWidget(self.lcdNumber_R4_RB, 4, 14, 1, 1)

        self.lcdNumber_R5_RB = QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumber_R5_RB.setObjectName(u"lcdNumber_R5_RB")
        self.lcdNumber_R5_RB.setDigitCount(3)
        self.lcdNumber_R5_RB.setProperty("intValue", 0)

        self.gridLayout_2.addWidget(self.lcdNumber_R5_RB, 5, 14, 1, 1)

        self.lcdNumber_R6_RB = QLCDNumber(self.gridLayoutWidget_2)
        self.lcdNumber_R6_RB.setObjectName(u"lcdNumber_R6_RB")
        self.lcdNumber_R6_RB.setDigitCount(3)
        self.lcdNumber_R6_RB.setProperty("intValue", 0)

        self.gridLayout_2.addWidget(self.lcdNumber_R6_RB, 6, 14, 1, 1)

        self.tabWidgetRoleRatings.addTab(self.RB, "")
        self.WR = QWidget()
        self.WR.setObjectName(u"WR")
        self.gridLayoutWidget_3 = QWidget(self.WR)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 10, 1215, 261))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_ATH_Header_WR = QLabel(self.gridLayoutWidget_3)
        self.label_ATH_Header_WR.setObjectName(u"label_ATH_Header_WR")
        self.label_ATH_Header_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_ATH_Header_WR, 0, 2, 1, 1)

        self.spinBox_R2_TKL_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R2_TKL_WR.setObjectName(u"spinBox_R2_TKL_WR")
        self.spinBox_R2_TKL_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TKL_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R2_TKL_WR, 2, 9, 1, 1)

        self.spinBox_R3_DUR_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R3_DUR_WR.setObjectName(u"spinBox_R3_DUR_WR")
        self.spinBox_R3_DUR_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_DUR_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R3_DUR_WR, 3, 4, 1, 1)

        self.spinBox_R3_STR_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R3_STR_WR.setObjectName(u"spinBox_R3_STR_WR")
        self.spinBox_R3_STR_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STR_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R3_STR_WR, 3, 7, 1, 1)

        self.spinBox_R2_TEC_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R2_TEC_WR.setObjectName(u"spinBox_R2_TEC_WR")
        self.spinBox_R2_TEC_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TEC_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R2_TEC_WR, 2, 13, 1, 1)

        self.spinBox_R2_WE_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R2_WE_WR.setObjectName(u"spinBox_R2_WE_WR")
        self.spinBox_R2_WE_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_WE_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R2_WE_WR, 2, 5, 1, 1)

        self.spinBox_R1_SPD_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R1_SPD_WR.setObjectName(u"spinBox_R1_SPD_WR")
        self.spinBox_R1_SPD_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_SPD_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R1_SPD_WR, 1, 3, 1, 1)

        self.label_TEC_Header_WR = QLabel(self.gridLayoutWidget_3)
        self.label_TEC_Header_WR.setObjectName(u"label_TEC_Header_WR")
        self.label_TEC_Header_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_TEC_Header_WR, 0, 13, 1, 1)

        self.spinBox_R1_BLK_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R1_BLK_WR.setObjectName(u"spinBox_R1_BLK_WR")
        self.spinBox_R1_BLK_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_BLK_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R1_BLK_WR, 1, 8, 1, 1)

        self.spinBox_R1_STA_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R1_STA_WR.setObjectName(u"spinBox_R1_STA_WR")
        self.spinBox_R1_STA_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STA_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R1_STA_WR, 1, 6, 1, 1)

        self.label_WE_Header_WR = QLabel(self.gridLayoutWidget_3)
        self.label_WE_Header_WR.setObjectName(u"label_WE_Header_WR")
        self.label_WE_Header_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_WE_Header_WR, 0, 5, 1, 1)

        self.label_TKL_Header_WR = QLabel(self.gridLayoutWidget_3)
        self.label_TKL_Header_WR.setObjectName(u"label_TKL_Header_WR")
        self.label_TKL_Header_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_TKL_Header_WR, 0, 9, 1, 1)

        self.label_STR_Header_WR = QLabel(self.gridLayoutWidget_3)
        self.label_STR_Header_WR.setObjectName(u"label_STR_Header_WR")
        self.label_STR_Header_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_STR_Header_WR, 0, 7, 1, 1)

        self.spinBox_R1_WE_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R1_WE_WR.setObjectName(u"spinBox_R1_WE_WR")
        self.spinBox_R1_WE_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_WE_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R1_WE_WR, 1, 5, 1, 1)

        self.spinBox_R2_SPD_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R2_SPD_WR.setObjectName(u"spinBox_R2_SPD_WR")
        self.spinBox_R2_SPD_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_SPD_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R2_SPD_WR, 2, 3, 1, 1)

        self.label_R1_WR = QLabel(self.gridLayoutWidget_3)
        self.label_R1_WR.setObjectName(u"label_R1_WR")
        self.label_R1_WR.setFont(font1)
        self.label_R1_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_R1_WR, 1, 0, 1, 1)

        self.label_RoleHeader_WR = QLabel(self.gridLayoutWidget_3)
        self.label_RoleHeader_WR.setObjectName(u"label_RoleHeader_WR")
        self.label_RoleHeader_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_RoleHeader_WR, 0, 0, 1, 1)

        self.label_Total_Header_WR = QLabel(self.gridLayoutWidget_3)
        self.label_Total_Header_WR.setObjectName(u"label_Total_Header_WR")

        self.gridLayout_3.addWidget(self.label_Total_Header_WR, 0, 14, 1, 1)

        self.spinBox_R3_STA_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R3_STA_WR.setObjectName(u"spinBox_R3_STA_WR")
        self.spinBox_R3_STA_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STA_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R3_STA_WR, 3, 6, 1, 1)

        self.label_R5_WR = QLabel(self.gridLayoutWidget_3)
        self.label_R5_WR.setObjectName(u"label_R5_WR")
        self.label_R5_WR.setFont(font1)
        self.label_R5_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_R5_WR, 5, 0, 1, 1)

        self.label_BLK_Header_WR = QLabel(self.gridLayoutWidget_3)
        self.label_BLK_Header_WR.setObjectName(u"label_BLK_Header_WR")
        self.label_BLK_Header_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_BLK_Header_WR, 0, 8, 1, 1)

        self.label_ELU_Header_WR = QLabel(self.gridLayoutWidget_3)
        self.label_ELU_Header_WR.setObjectName(u"label_ELU_Header_WR")
        self.label_ELU_Header_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_ELU_Header_WR, 0, 12, 1, 1)

        self.spinBox_R2_BLK_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R2_BLK_WR.setObjectName(u"spinBox_R2_BLK_WR")
        self.spinBox_R2_BLK_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_BLK_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R2_BLK_WR, 2, 8, 1, 1)

        self.label_LabelHeader_WR = QLabel(self.gridLayoutWidget_3)
        self.label_LabelHeader_WR.setObjectName(u"label_LabelHeader_WR")
        self.label_LabelHeader_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_LabelHeader_WR, 0, 1, 1, 1)

        self.spinBox_R2_HAN_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R2_HAN_WR.setObjectName(u"spinBox_R2_HAN_WR")
        self.spinBox_R2_HAN_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_HAN_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R2_HAN_WR, 2, 10, 1, 1)

        self.label_R2_WR = QLabel(self.gridLayoutWidget_3)
        self.label_R2_WR.setObjectName(u"label_R2_WR")
        self.label_R2_WR.setFont(font1)
        self.label_R2_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_R2_WR, 2, 0, 1, 1)

        self.spinBox_R1_GI_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R1_GI_WR.setObjectName(u"spinBox_R1_GI_WR")
        self.spinBox_R1_GI_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_GI_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R1_GI_WR, 1, 11, 1, 1)

        self.label_DUR_Header_WR = QLabel(self.gridLayoutWidget_3)
        self.label_DUR_Header_WR.setObjectName(u"label_DUR_Header_WR")
        self.label_DUR_Header_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_DUR_Header_WR, 0, 4, 1, 1)

        self.spinBox_R1_HAN_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R1_HAN_WR.setObjectName(u"spinBox_R1_HAN_WR")
        self.spinBox_R1_HAN_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_HAN_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R1_HAN_WR, 1, 10, 1, 1)

        self.label_R3_WR = QLabel(self.gridLayoutWidget_3)
        self.label_R3_WR.setObjectName(u"label_R3_WR")
        self.label_R3_WR.setFont(font1)
        self.label_R3_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_R3_WR, 3, 0, 1, 1)

        self.label_GI_Header_WR = QLabel(self.gridLayoutWidget_3)
        self.label_GI_Header_WR.setObjectName(u"label_GI_Header_WR")
        self.label_GI_Header_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_GI_Header_WR, 0, 11, 1, 1)

        self.spinBox_R1_TEC_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R1_TEC_WR.setObjectName(u"spinBox_R1_TEC_WR")
        self.spinBox_R1_TEC_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TEC_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R1_TEC_WR, 1, 13, 1, 1)

        self.spinBox_R1_ATH_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R1_ATH_WR.setObjectName(u"spinBox_R1_ATH_WR")
        self.spinBox_R1_ATH_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ATH_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R1_ATH_WR, 1, 2, 1, 1)

        self.spinBox_R1_DUR_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R1_DUR_WR.setObjectName(u"spinBox_R1_DUR_WR")
        self.spinBox_R1_DUR_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_DUR_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R1_DUR_WR, 1, 4, 1, 1)

        self.spinBox_R2_ELU_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R2_ELU_WR.setObjectName(u"spinBox_R2_ELU_WR")
        self.spinBox_R2_ELU_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ELU_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R2_ELU_WR, 2, 12, 1, 1)

        self.spinBox_R2_ATH_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R2_ATH_WR.setObjectName(u"spinBox_R2_ATH_WR")
        self.spinBox_R2_ATH_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ATH_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R2_ATH_WR, 2, 2, 1, 1)

        self.spinBox_R2_STR_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R2_STR_WR.setObjectName(u"spinBox_R2_STR_WR")
        self.spinBox_R2_STR_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STR_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R2_STR_WR, 2, 7, 1, 1)

        self.spinBox_R3_ATH_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R3_ATH_WR.setObjectName(u"spinBox_R3_ATH_WR")
        self.spinBox_R3_ATH_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ATH_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R3_ATH_WR, 3, 2, 1, 1)

        self.spinBox_R1_ELU_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R1_ELU_WR.setObjectName(u"spinBox_R1_ELU_WR")
        self.spinBox_R1_ELU_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ELU_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R1_ELU_WR, 1, 12, 1, 1)

        self.label_STA_Header_WR = QLabel(self.gridLayoutWidget_3)
        self.label_STA_Header_WR.setObjectName(u"label_STA_Header_WR")
        self.label_STA_Header_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_STA_Header_WR, 0, 6, 1, 1)

        self.spinBox_R1_STR_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R1_STR_WR.setObjectName(u"spinBox_R1_STR_WR")
        self.spinBox_R1_STR_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STR_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R1_STR_WR, 1, 7, 1, 1)

        self.label_SPD_Header_WR = QLabel(self.gridLayoutWidget_3)
        self.label_SPD_Header_WR.setObjectName(u"label_SPD_Header_WR")
        self.label_SPD_Header_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_SPD_Header_WR, 0, 3, 1, 1)

        self.spinBox_R2_DUR_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R2_DUR_WR.setObjectName(u"spinBox_R2_DUR_WR")
        self.spinBox_R2_DUR_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_DUR_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R2_DUR_WR, 2, 4, 1, 1)

        self.label_HAN_Header_WR = QLabel(self.gridLayoutWidget_3)
        self.label_HAN_Header_WR.setObjectName(u"label_HAN_Header_WR")
        self.label_HAN_Header_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_HAN_Header_WR, 0, 10, 1, 1)

        self.label_R4_WR = QLabel(self.gridLayoutWidget_3)
        self.label_R4_WR.setObjectName(u"label_R4_WR")
        self.label_R4_WR.setFont(font1)
        self.label_R4_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_R4_WR, 4, 0, 1, 1)

        self.spinBox_R1_TKL_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R1_TKL_WR.setObjectName(u"spinBox_R1_TKL_WR")
        self.spinBox_R1_TKL_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TKL_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R1_TKL_WR, 1, 9, 1, 1)

        self.spinBox_R2_GI_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R2_GI_WR.setObjectName(u"spinBox_R2_GI_WR")
        self.spinBox_R2_GI_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_GI_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R2_GI_WR, 2, 11, 1, 1)

        self.spinBox_R3_WE_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R3_WE_WR.setObjectName(u"spinBox_R3_WE_WR")
        self.spinBox_R3_WE_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_WE_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R3_WE_WR, 3, 5, 1, 1)

        self.spinBox_R3_SPD_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R3_SPD_WR.setObjectName(u"spinBox_R3_SPD_WR")
        self.spinBox_R3_SPD_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_SPD_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R3_SPD_WR, 3, 3, 1, 1)

        self.label_R6_WR = QLabel(self.gridLayoutWidget_3)
        self.label_R6_WR.setObjectName(u"label_R6_WR")
        self.label_R6_WR.setFont(font1)
        self.label_R6_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_R6_WR, 6, 0, 1, 1)

        self.spinBox_R2_STA_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R2_STA_WR.setObjectName(u"spinBox_R2_STA_WR")
        self.spinBox_R2_STA_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STA_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R2_STA_WR, 2, 6, 1, 1)

        self.spinBox_R3_BLK_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R3_BLK_WR.setObjectName(u"spinBox_R3_BLK_WR")
        self.spinBox_R3_BLK_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_BLK_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R3_BLK_WR, 3, 8, 1, 1)

        self.spinBox_R3_TKL_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R3_TKL_WR.setObjectName(u"spinBox_R3_TKL_WR")
        self.spinBox_R3_TKL_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TKL_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R3_TKL_WR, 3, 9, 1, 1)

        self.spinBox_R3_HAN_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R3_HAN_WR.setObjectName(u"spinBox_R3_HAN_WR")
        self.spinBox_R3_HAN_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_HAN_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R3_HAN_WR, 3, 10, 1, 1)

        self.spinBox_R3_GI_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R3_GI_WR.setObjectName(u"spinBox_R3_GI_WR")
        self.spinBox_R3_GI_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_GI_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R3_GI_WR, 3, 11, 1, 1)

        self.spinBox_R3_ELU_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R3_ELU_WR.setObjectName(u"spinBox_R3_ELU_WR")
        self.spinBox_R3_ELU_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ELU_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R3_ELU_WR, 3, 12, 1, 1)

        self.spinBox_R3_TEC_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R3_TEC_WR.setObjectName(u"spinBox_R3_TEC_WR")
        self.spinBox_R3_TEC_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TEC_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R3_TEC_WR, 3, 13, 1, 1)

        self.spinBox_R4_ATH_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R4_ATH_WR.setObjectName(u"spinBox_R4_ATH_WR")
        self.spinBox_R4_ATH_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ATH_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R4_ATH_WR, 4, 2, 1, 1)

        self.spinBox_R4_SPD_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R4_SPD_WR.setObjectName(u"spinBox_R4_SPD_WR")
        self.spinBox_R4_SPD_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_SPD_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R4_SPD_WR, 4, 3, 1, 1)

        self.spinBox_R4_DUR_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R4_DUR_WR.setObjectName(u"spinBox_R4_DUR_WR")
        self.spinBox_R4_DUR_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_DUR_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R4_DUR_WR, 4, 4, 1, 1)

        self.spinBox_R4_WE_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R4_WE_WR.setObjectName(u"spinBox_R4_WE_WR")
        self.spinBox_R4_WE_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_WE_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R4_WE_WR, 4, 5, 1, 1)

        self.spinBox_R4_STA_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R4_STA_WR.setObjectName(u"spinBox_R4_STA_WR")
        self.spinBox_R4_STA_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STA_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R4_STA_WR, 4, 6, 1, 1)

        self.spinBox_R4_STR_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R4_STR_WR.setObjectName(u"spinBox_R4_STR_WR")
        self.spinBox_R4_STR_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STR_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R4_STR_WR, 4, 7, 1, 1)

        self.spinBox_R4_BLK_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R4_BLK_WR.setObjectName(u"spinBox_R4_BLK_WR")
        self.spinBox_R4_BLK_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_BLK_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R4_BLK_WR, 4, 8, 1, 1)

        self.spinBox_R4_TKL_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R4_TKL_WR.setObjectName(u"spinBox_R4_TKL_WR")
        self.spinBox_R4_TKL_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TKL_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R4_TKL_WR, 4, 9, 1, 1)

        self.spinBox_R4_HAN_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R4_HAN_WR.setObjectName(u"spinBox_R4_HAN_WR")
        self.spinBox_R4_HAN_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_HAN_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R4_HAN_WR, 4, 10, 1, 1)

        self.spinBox_R4_GI_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R4_GI_WR.setObjectName(u"spinBox_R4_GI_WR")
        self.spinBox_R4_GI_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_GI_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R4_GI_WR, 4, 11, 1, 1)

        self.spinBox_R4_ELU_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R4_ELU_WR.setObjectName(u"spinBox_R4_ELU_WR")
        self.spinBox_R4_ELU_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ELU_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R4_ELU_WR, 4, 12, 1, 1)

        self.spinBox_R4_TEC_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R4_TEC_WR.setObjectName(u"spinBox_R4_TEC_WR")
        self.spinBox_R4_TEC_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TEC_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R4_TEC_WR, 4, 13, 1, 1)

        self.spinBox_R5_ATH_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R5_ATH_WR.setObjectName(u"spinBox_R5_ATH_WR")
        self.spinBox_R5_ATH_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ATH_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R5_ATH_WR, 5, 2, 1, 1)

        self.spinBox_R5_SPD_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R5_SPD_WR.setObjectName(u"spinBox_R5_SPD_WR")
        self.spinBox_R5_SPD_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_SPD_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R5_SPD_WR, 5, 3, 1, 1)

        self.spinBox_R5_DUR_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R5_DUR_WR.setObjectName(u"spinBox_R5_DUR_WR")
        self.spinBox_R5_DUR_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_DUR_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R5_DUR_WR, 5, 4, 1, 1)

        self.spinBox_R5_WE_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R5_WE_WR.setObjectName(u"spinBox_R5_WE_WR")
        self.spinBox_R5_WE_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_WE_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R5_WE_WR, 5, 5, 1, 1)

        self.spinBox_R5_STA_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R5_STA_WR.setObjectName(u"spinBox_R5_STA_WR")
        self.spinBox_R5_STA_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STA_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R5_STA_WR, 5, 6, 1, 1)

        self.spinBox_R5_STR_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R5_STR_WR.setObjectName(u"spinBox_R5_STR_WR")
        self.spinBox_R5_STR_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STR_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R5_STR_WR, 5, 7, 1, 1)

        self.spinBox_R5_BLK_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R5_BLK_WR.setObjectName(u"spinBox_R5_BLK_WR")
        self.spinBox_R5_BLK_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_BLK_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R5_BLK_WR, 5, 8, 1, 1)

        self.spinBox_R5_TKL_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R5_TKL_WR.setObjectName(u"spinBox_R5_TKL_WR")
        self.spinBox_R5_TKL_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TKL_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R5_TKL_WR, 5, 9, 1, 1)

        self.spinBox_R5_HAN_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R5_HAN_WR.setObjectName(u"spinBox_R5_HAN_WR")
        self.spinBox_R5_HAN_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_HAN_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R5_HAN_WR, 5, 10, 1, 1)

        self.spinBox_R5_GI_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R5_GI_WR.setObjectName(u"spinBox_R5_GI_WR")
        self.spinBox_R5_GI_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_GI_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R5_GI_WR, 5, 11, 1, 1)

        self.spinBox_R5_ELU_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R5_ELU_WR.setObjectName(u"spinBox_R5_ELU_WR")
        self.spinBox_R5_ELU_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ELU_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R5_ELU_WR, 5, 12, 1, 1)

        self.spinBox_R5_TEC_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R5_TEC_WR.setObjectName(u"spinBox_R5_TEC_WR")
        self.spinBox_R5_TEC_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TEC_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R5_TEC_WR, 5, 13, 1, 1)

        self.spinBox_R6_ATH_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R6_ATH_WR.setObjectName(u"spinBox_R6_ATH_WR")
        self.spinBox_R6_ATH_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ATH_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R6_ATH_WR, 6, 2, 1, 1)

        self.spinBox_R6_SPD_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R6_SPD_WR.setObjectName(u"spinBox_R6_SPD_WR")
        self.spinBox_R6_SPD_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_SPD_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R6_SPD_WR, 6, 3, 1, 1)

        self.spinBox_R6_DUR_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R6_DUR_WR.setObjectName(u"spinBox_R6_DUR_WR")
        self.spinBox_R6_DUR_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_DUR_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R6_DUR_WR, 6, 4, 1, 1)

        self.spinBox_R6_WE_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R6_WE_WR.setObjectName(u"spinBox_R6_WE_WR")
        self.spinBox_R6_WE_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_WE_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R6_WE_WR, 6, 5, 1, 1)

        self.spinBox_R6_STA_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R6_STA_WR.setObjectName(u"spinBox_R6_STA_WR")
        self.spinBox_R6_STA_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STA_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R6_STA_WR, 6, 6, 1, 1)

        self.spinBox_R6_STR_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R6_STR_WR.setObjectName(u"spinBox_R6_STR_WR")
        self.spinBox_R6_STR_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STR_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R6_STR_WR, 6, 7, 1, 1)

        self.spinBox_R6_BLK_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R6_BLK_WR.setObjectName(u"spinBox_R6_BLK_WR")
        self.spinBox_R6_BLK_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_BLK_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R6_BLK_WR, 6, 8, 1, 1)

        self.spinBox_R6_TKL_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R6_TKL_WR.setObjectName(u"spinBox_R6_TKL_WR")
        self.spinBox_R6_TKL_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TKL_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R6_TKL_WR, 6, 9, 1, 1)

        self.spinBox_R6_HAN_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R6_HAN_WR.setObjectName(u"spinBox_R6_HAN_WR")
        self.spinBox_R6_HAN_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_HAN_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R6_HAN_WR, 6, 10, 1, 1)

        self.spinBox_R6_GI_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R6_GI_WR.setObjectName(u"spinBox_R6_GI_WR")
        self.spinBox_R6_GI_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_GI_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R6_GI_WR, 6, 11, 1, 1)

        self.spinBox_R6_ELU_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R6_ELU_WR.setObjectName(u"spinBox_R6_ELU_WR")
        self.spinBox_R6_ELU_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ELU_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R6_ELU_WR, 6, 12, 1, 1)

        self.spinBox_R6_TEC_WR = QSpinBox(self.gridLayoutWidget_3)
        self.spinBox_R6_TEC_WR.setObjectName(u"spinBox_R6_TEC_WR")
        self.spinBox_R6_TEC_WR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TEC_WR.setMaximum(100)

        self.gridLayout_3.addWidget(self.spinBox_R6_TEC_WR, 6, 13, 1, 1)

        self.lineEdit_R1_WR = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_R1_WR.setObjectName(u"lineEdit_R1_WR")
        self.lineEdit_R1_WR.setFont(font2)
        self.lineEdit_R1_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_R1_WR, 1, 1, 1, 1)

        self.lineEdit_R2_WR = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_R2_WR.setObjectName(u"lineEdit_R2_WR")
        self.lineEdit_R2_WR.setFont(font2)
        self.lineEdit_R2_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_R2_WR, 2, 1, 1, 1)

        self.lineEdit_R3_WR = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_R3_WR.setObjectName(u"lineEdit_R3_WR")
        self.lineEdit_R3_WR.setFont(font2)
        self.lineEdit_R3_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_R3_WR, 3, 1, 1, 1)

        self.lineEdit_R4_WR = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_R4_WR.setObjectName(u"lineEdit_R4_WR")
        self.lineEdit_R4_WR.setFont(font2)
        self.lineEdit_R4_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_R4_WR, 4, 1, 1, 1)

        self.lineEdit_R5_WR = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_R5_WR.setObjectName(u"lineEdit_R5_WR")
        self.lineEdit_R5_WR.setFont(font2)
        self.lineEdit_R5_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_R5_WR, 5, 1, 1, 1)

        self.lineEdit_R6_WR = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_R6_WR.setObjectName(u"lineEdit_R6_WR")
        self.lineEdit_R6_WR.setFont(font2)
        self.lineEdit_R6_WR.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_R6_WR, 6, 1, 1, 1)

        self.lcdNumber_R1_WR = QLCDNumber(self.gridLayoutWidget_3)
        self.lcdNumber_R1_WR.setObjectName(u"lcdNumber_R1_WR")
        self.lcdNumber_R1_WR.setDigitCount(3)
        self.lcdNumber_R1_WR.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.lcdNumber_R1_WR, 1, 14, 1, 1)

        self.lcdNumber_R2_WR = QLCDNumber(self.gridLayoutWidget_3)
        self.lcdNumber_R2_WR.setObjectName(u"lcdNumber_R2_WR")
        self.lcdNumber_R2_WR.setDigitCount(3)
        self.lcdNumber_R2_WR.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.lcdNumber_R2_WR, 2, 14, 1, 1)

        self.lcdNumber_R3_WR = QLCDNumber(self.gridLayoutWidget_3)
        self.lcdNumber_R3_WR.setObjectName(u"lcdNumber_R3_WR")
        self.lcdNumber_R3_WR.setDigitCount(3)
        self.lcdNumber_R3_WR.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.lcdNumber_R3_WR, 3, 14, 1, 1)

        self.lcdNumber_R4_WR = QLCDNumber(self.gridLayoutWidget_3)
        self.lcdNumber_R4_WR.setObjectName(u"lcdNumber_R4_WR")
        self.lcdNumber_R4_WR.setDigitCount(3)
        self.lcdNumber_R4_WR.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.lcdNumber_R4_WR, 4, 14, 1, 1)

        self.lcdNumber_R5_WR = QLCDNumber(self.gridLayoutWidget_3)
        self.lcdNumber_R5_WR.setObjectName(u"lcdNumber_R5_WR")
        self.lcdNumber_R5_WR.setDigitCount(3)
        self.lcdNumber_R5_WR.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.lcdNumber_R5_WR, 5, 14, 1, 1)

        self.lcdNumber_R6_WR = QLCDNumber(self.gridLayoutWidget_3)
        self.lcdNumber_R6_WR.setObjectName(u"lcdNumber_R6_WR")
        self.lcdNumber_R6_WR.setDigitCount(3)
        self.lcdNumber_R6_WR.setProperty("intValue", 0)

        self.gridLayout_3.addWidget(self.lcdNumber_R6_WR, 6, 14, 1, 1)

        self.tabWidgetRoleRatings.addTab(self.WR, "")
        self.TE = QWidget()
        self.TE.setObjectName(u"TE")
        self.gridLayoutWidget_4 = QWidget(self.TE)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 10, 1215, 261))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_ATH_Header_TE = QLabel(self.gridLayoutWidget_4)
        self.label_ATH_Header_TE.setObjectName(u"label_ATH_Header_TE")
        self.label_ATH_Header_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_ATH_Header_TE, 0, 2, 1, 1)

        self.spinBox_R2_TKL_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R2_TKL_TE.setObjectName(u"spinBox_R2_TKL_TE")
        self.spinBox_R2_TKL_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TKL_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R2_TKL_TE, 2, 9, 1, 1)

        self.spinBox_R3_DUR_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R3_DUR_TE.setObjectName(u"spinBox_R3_DUR_TE")
        self.spinBox_R3_DUR_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_DUR_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R3_DUR_TE, 3, 4, 1, 1)

        self.spinBox_R3_STR_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R3_STR_TE.setObjectName(u"spinBox_R3_STR_TE")
        self.spinBox_R3_STR_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STR_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R3_STR_TE, 3, 7, 1, 1)

        self.spinBox_R2_TEC_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R2_TEC_TE.setObjectName(u"spinBox_R2_TEC_TE")
        self.spinBox_R2_TEC_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TEC_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R2_TEC_TE, 2, 13, 1, 1)

        self.spinBox_R2_WE_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R2_WE_TE.setObjectName(u"spinBox_R2_WE_TE")
        self.spinBox_R2_WE_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_WE_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R2_WE_TE, 2, 5, 1, 1)

        self.spinBox_R1_SPD_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R1_SPD_TE.setObjectName(u"spinBox_R1_SPD_TE")
        self.spinBox_R1_SPD_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_SPD_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R1_SPD_TE, 1, 3, 1, 1)

        self.label_TEC_Header_TE = QLabel(self.gridLayoutWidget_4)
        self.label_TEC_Header_TE.setObjectName(u"label_TEC_Header_TE")
        self.label_TEC_Header_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_TEC_Header_TE, 0, 13, 1, 1)

        self.spinBox_R1_BLK_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R1_BLK_TE.setObjectName(u"spinBox_R1_BLK_TE")
        self.spinBox_R1_BLK_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_BLK_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R1_BLK_TE, 1, 8, 1, 1)

        self.spinBox_R1_STA_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R1_STA_TE.setObjectName(u"spinBox_R1_STA_TE")
        self.spinBox_R1_STA_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STA_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R1_STA_TE, 1, 6, 1, 1)

        self.label_WE_Header_TE = QLabel(self.gridLayoutWidget_4)
        self.label_WE_Header_TE.setObjectName(u"label_WE_Header_TE")
        self.label_WE_Header_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_WE_Header_TE, 0, 5, 1, 1)

        self.label_TKL_Header_TE = QLabel(self.gridLayoutWidget_4)
        self.label_TKL_Header_TE.setObjectName(u"label_TKL_Header_TE")
        self.label_TKL_Header_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_TKL_Header_TE, 0, 9, 1, 1)

        self.label_STR_Header_TE = QLabel(self.gridLayoutWidget_4)
        self.label_STR_Header_TE.setObjectName(u"label_STR_Header_TE")
        self.label_STR_Header_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_STR_Header_TE, 0, 7, 1, 1)

        self.spinBox_R1_WE_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R1_WE_TE.setObjectName(u"spinBox_R1_WE_TE")
        self.spinBox_R1_WE_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_WE_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R1_WE_TE, 1, 5, 1, 1)

        self.spinBox_R2_SPD_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R2_SPD_TE.setObjectName(u"spinBox_R2_SPD_TE")
        self.spinBox_R2_SPD_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_SPD_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R2_SPD_TE, 2, 3, 1, 1)

        self.label_R1_TE = QLabel(self.gridLayoutWidget_4)
        self.label_R1_TE.setObjectName(u"label_R1_TE")
        self.label_R1_TE.setFont(font1)
        self.label_R1_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_R1_TE, 1, 0, 1, 1)

        self.label_RoleHeader_TE = QLabel(self.gridLayoutWidget_4)
        self.label_RoleHeader_TE.setObjectName(u"label_RoleHeader_TE")
        self.label_RoleHeader_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_RoleHeader_TE, 0, 0, 1, 1)

        self.label_Total_Header_TE = QLabel(self.gridLayoutWidget_4)
        self.label_Total_Header_TE.setObjectName(u"label_Total_Header_TE")

        self.gridLayout_4.addWidget(self.label_Total_Header_TE, 0, 14, 1, 1)

        self.spinBox_R3_STA_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R3_STA_TE.setObjectName(u"spinBox_R3_STA_TE")
        self.spinBox_R3_STA_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STA_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R3_STA_TE, 3, 6, 1, 1)

        self.label_R5_TE = QLabel(self.gridLayoutWidget_4)
        self.label_R5_TE.setObjectName(u"label_R5_TE")
        self.label_R5_TE.setFont(font1)
        self.label_R5_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_R5_TE, 5, 0, 1, 1)

        self.label_BLK_Header_TE = QLabel(self.gridLayoutWidget_4)
        self.label_BLK_Header_TE.setObjectName(u"label_BLK_Header_TE")
        self.label_BLK_Header_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_BLK_Header_TE, 0, 8, 1, 1)

        self.label_ELU_Header_TE = QLabel(self.gridLayoutWidget_4)
        self.label_ELU_Header_TE.setObjectName(u"label_ELU_Header_TE")
        self.label_ELU_Header_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_ELU_Header_TE, 0, 12, 1, 1)

        self.spinBox_R2_BLK_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R2_BLK_TE.setObjectName(u"spinBox_R2_BLK_TE")
        self.spinBox_R2_BLK_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_BLK_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R2_BLK_TE, 2, 8, 1, 1)

        self.label_LabelHeader_TE = QLabel(self.gridLayoutWidget_4)
        self.label_LabelHeader_TE.setObjectName(u"label_LabelHeader_TE")
        self.label_LabelHeader_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_LabelHeader_TE, 0, 1, 1, 1)

        self.spinBox_R2_HAN_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R2_HAN_TE.setObjectName(u"spinBox_R2_HAN_TE")
        self.spinBox_R2_HAN_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_HAN_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R2_HAN_TE, 2, 10, 1, 1)

        self.label_R2_TE = QLabel(self.gridLayoutWidget_4)
        self.label_R2_TE.setObjectName(u"label_R2_TE")
        self.label_R2_TE.setFont(font1)
        self.label_R2_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_R2_TE, 2, 0, 1, 1)

        self.spinBox_R1_GI_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R1_GI_TE.setObjectName(u"spinBox_R1_GI_TE")
        self.spinBox_R1_GI_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_GI_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R1_GI_TE, 1, 11, 1, 1)

        self.label_DUR_Header_TE = QLabel(self.gridLayoutWidget_4)
        self.label_DUR_Header_TE.setObjectName(u"label_DUR_Header_TE")
        self.label_DUR_Header_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_DUR_Header_TE, 0, 4, 1, 1)

        self.spinBox_R1_HAN_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R1_HAN_TE.setObjectName(u"spinBox_R1_HAN_TE")
        self.spinBox_R1_HAN_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_HAN_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R1_HAN_TE, 1, 10, 1, 1)

        self.label_R3_TE = QLabel(self.gridLayoutWidget_4)
        self.label_R3_TE.setObjectName(u"label_R3_TE")
        self.label_R3_TE.setFont(font1)
        self.label_R3_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_R3_TE, 3, 0, 1, 1)

        self.label_GI_Header_TE = QLabel(self.gridLayoutWidget_4)
        self.label_GI_Header_TE.setObjectName(u"label_GI_Header_TE")
        self.label_GI_Header_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_GI_Header_TE, 0, 11, 1, 1)

        self.spinBox_R1_TEC_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R1_TEC_TE.setObjectName(u"spinBox_R1_TEC_TE")
        self.spinBox_R1_TEC_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TEC_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R1_TEC_TE, 1, 13, 1, 1)

        self.spinBox_R1_ATH_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R1_ATH_TE.setObjectName(u"spinBox_R1_ATH_TE")
        self.spinBox_R1_ATH_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ATH_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R1_ATH_TE, 1, 2, 1, 1)

        self.spinBox_R1_DUR_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R1_DUR_TE.setObjectName(u"spinBox_R1_DUR_TE")
        self.spinBox_R1_DUR_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_DUR_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R1_DUR_TE, 1, 4, 1, 1)

        self.spinBox_R2_ELU_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R2_ELU_TE.setObjectName(u"spinBox_R2_ELU_TE")
        self.spinBox_R2_ELU_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ELU_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R2_ELU_TE, 2, 12, 1, 1)

        self.spinBox_R2_ATH_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R2_ATH_TE.setObjectName(u"spinBox_R2_ATH_TE")
        self.spinBox_R2_ATH_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ATH_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R2_ATH_TE, 2, 2, 1, 1)

        self.spinBox_R2_STR_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R2_STR_TE.setObjectName(u"spinBox_R2_STR_TE")
        self.spinBox_R2_STR_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STR_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R2_STR_TE, 2, 7, 1, 1)

        self.spinBox_R3_ATH_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R3_ATH_TE.setObjectName(u"spinBox_R3_ATH_TE")
        self.spinBox_R3_ATH_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ATH_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R3_ATH_TE, 3, 2, 1, 1)

        self.spinBox_R1_ELU_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R1_ELU_TE.setObjectName(u"spinBox_R1_ELU_TE")
        self.spinBox_R1_ELU_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ELU_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R1_ELU_TE, 1, 12, 1, 1)

        self.label_STA_Header_TE = QLabel(self.gridLayoutWidget_4)
        self.label_STA_Header_TE.setObjectName(u"label_STA_Header_TE")
        self.label_STA_Header_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_STA_Header_TE, 0, 6, 1, 1)

        self.spinBox_R1_STR_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R1_STR_TE.setObjectName(u"spinBox_R1_STR_TE")
        self.spinBox_R1_STR_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STR_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R1_STR_TE, 1, 7, 1, 1)

        self.label_SPD_Header_TE = QLabel(self.gridLayoutWidget_4)
        self.label_SPD_Header_TE.setObjectName(u"label_SPD_Header_TE")
        self.label_SPD_Header_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_SPD_Header_TE, 0, 3, 1, 1)

        self.spinBox_R2_DUR_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R2_DUR_TE.setObjectName(u"spinBox_R2_DUR_TE")
        self.spinBox_R2_DUR_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_DUR_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R2_DUR_TE, 2, 4, 1, 1)

        self.label_HAN_Header_TE = QLabel(self.gridLayoutWidget_4)
        self.label_HAN_Header_TE.setObjectName(u"label_HAN_Header_TE")
        self.label_HAN_Header_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_HAN_Header_TE, 0, 10, 1, 1)

        self.label_R4_TE = QLabel(self.gridLayoutWidget_4)
        self.label_R4_TE.setObjectName(u"label_R4_TE")
        self.label_R4_TE.setFont(font1)
        self.label_R4_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_R4_TE, 4, 0, 1, 1)

        self.spinBox_R1_TKL_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R1_TKL_TE.setObjectName(u"spinBox_R1_TKL_TE")
        self.spinBox_R1_TKL_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TKL_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R1_TKL_TE, 1, 9, 1, 1)

        self.spinBox_R2_GI_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R2_GI_TE.setObjectName(u"spinBox_R2_GI_TE")
        self.spinBox_R2_GI_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_GI_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R2_GI_TE, 2, 11, 1, 1)

        self.spinBox_R3_WE_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R3_WE_TE.setObjectName(u"spinBox_R3_WE_TE")
        self.spinBox_R3_WE_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_WE_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R3_WE_TE, 3, 5, 1, 1)

        self.spinBox_R3_SPD_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R3_SPD_TE.setObjectName(u"spinBox_R3_SPD_TE")
        self.spinBox_R3_SPD_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_SPD_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R3_SPD_TE, 3, 3, 1, 1)

        self.label_R6_TE = QLabel(self.gridLayoutWidget_4)
        self.label_R6_TE.setObjectName(u"label_R6_TE")
        self.label_R6_TE.setFont(font1)
        self.label_R6_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_R6_TE, 6, 0, 1, 1)

        self.spinBox_R2_STA_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R2_STA_TE.setObjectName(u"spinBox_R2_STA_TE")
        self.spinBox_R2_STA_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STA_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R2_STA_TE, 2, 6, 1, 1)

        self.spinBox_R3_BLK_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R3_BLK_TE.setObjectName(u"spinBox_R3_BLK_TE")
        self.spinBox_R3_BLK_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_BLK_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R3_BLK_TE, 3, 8, 1, 1)

        self.spinBox_R3_TKL_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R3_TKL_TE.setObjectName(u"spinBox_R3_TKL_TE")
        self.spinBox_R3_TKL_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TKL_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R3_TKL_TE, 3, 9, 1, 1)

        self.spinBox_R3_HAN_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R3_HAN_TE.setObjectName(u"spinBox_R3_HAN_TE")
        self.spinBox_R3_HAN_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_HAN_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R3_HAN_TE, 3, 10, 1, 1)

        self.spinBox_R3_GI_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R3_GI_TE.setObjectName(u"spinBox_R3_GI_TE")
        self.spinBox_R3_GI_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_GI_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R3_GI_TE, 3, 11, 1, 1)

        self.spinBox_R3_ELU_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R3_ELU_TE.setObjectName(u"spinBox_R3_ELU_TE")
        self.spinBox_R3_ELU_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ELU_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R3_ELU_TE, 3, 12, 1, 1)

        self.spinBox_R3_TEC_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R3_TEC_TE.setObjectName(u"spinBox_R3_TEC_TE")
        self.spinBox_R3_TEC_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TEC_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R3_TEC_TE, 3, 13, 1, 1)

        self.spinBox_R4_ATH_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R4_ATH_TE.setObjectName(u"spinBox_R4_ATH_TE")
        self.spinBox_R4_ATH_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ATH_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R4_ATH_TE, 4, 2, 1, 1)

        self.spinBox_R4_SPD_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R4_SPD_TE.setObjectName(u"spinBox_R4_SPD_TE")
        self.spinBox_R4_SPD_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_SPD_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R4_SPD_TE, 4, 3, 1, 1)

        self.spinBox_R4_DUR_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R4_DUR_TE.setObjectName(u"spinBox_R4_DUR_TE")
        self.spinBox_R4_DUR_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_DUR_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R4_DUR_TE, 4, 4, 1, 1)

        self.spinBox_R4_WE_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R4_WE_TE.setObjectName(u"spinBox_R4_WE_TE")
        self.spinBox_R4_WE_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_WE_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R4_WE_TE, 4, 5, 1, 1)

        self.spinBox_R4_STA_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R4_STA_TE.setObjectName(u"spinBox_R4_STA_TE")
        self.spinBox_R4_STA_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STA_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R4_STA_TE, 4, 6, 1, 1)

        self.spinBox_R4_STR_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R4_STR_TE.setObjectName(u"spinBox_R4_STR_TE")
        self.spinBox_R4_STR_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STR_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R4_STR_TE, 4, 7, 1, 1)

        self.spinBox_R4_BLK_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R4_BLK_TE.setObjectName(u"spinBox_R4_BLK_TE")
        self.spinBox_R4_BLK_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_BLK_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R4_BLK_TE, 4, 8, 1, 1)

        self.spinBox_R4_TKL_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R4_TKL_TE.setObjectName(u"spinBox_R4_TKL_TE")
        self.spinBox_R4_TKL_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TKL_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R4_TKL_TE, 4, 9, 1, 1)

        self.spinBox_R4_HAN_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R4_HAN_TE.setObjectName(u"spinBox_R4_HAN_TE")
        self.spinBox_R4_HAN_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_HAN_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R4_HAN_TE, 4, 10, 1, 1)

        self.spinBox_R4_GI_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R4_GI_TE.setObjectName(u"spinBox_R4_GI_TE")
        self.spinBox_R4_GI_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_GI_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R4_GI_TE, 4, 11, 1, 1)

        self.spinBox_R4_ELU_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R4_ELU_TE.setObjectName(u"spinBox_R4_ELU_TE")
        self.spinBox_R4_ELU_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ELU_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R4_ELU_TE, 4, 12, 1, 1)

        self.spinBox_R4_TEC_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R4_TEC_TE.setObjectName(u"spinBox_R4_TEC_TE")
        self.spinBox_R4_TEC_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TEC_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R4_TEC_TE, 4, 13, 1, 1)

        self.spinBox_R5_ATH_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R5_ATH_TE.setObjectName(u"spinBox_R5_ATH_TE")
        self.spinBox_R5_ATH_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ATH_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R5_ATH_TE, 5, 2, 1, 1)

        self.spinBox_R5_SPD_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R5_SPD_TE.setObjectName(u"spinBox_R5_SPD_TE")
        self.spinBox_R5_SPD_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_SPD_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R5_SPD_TE, 5, 3, 1, 1)

        self.spinBox_R5_DUR_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R5_DUR_TE.setObjectName(u"spinBox_R5_DUR_TE")
        self.spinBox_R5_DUR_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_DUR_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R5_DUR_TE, 5, 4, 1, 1)

        self.spinBox_R5_WE_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R5_WE_TE.setObjectName(u"spinBox_R5_WE_TE")
        self.spinBox_R5_WE_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_WE_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R5_WE_TE, 5, 5, 1, 1)

        self.spinBox_R5_STA_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R5_STA_TE.setObjectName(u"spinBox_R5_STA_TE")
        self.spinBox_R5_STA_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STA_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R5_STA_TE, 5, 6, 1, 1)

        self.spinBox_R5_STR_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R5_STR_TE.setObjectName(u"spinBox_R5_STR_TE")
        self.spinBox_R5_STR_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STR_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R5_STR_TE, 5, 7, 1, 1)

        self.spinBox_R5_BLK_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R5_BLK_TE.setObjectName(u"spinBox_R5_BLK_TE")
        self.spinBox_R5_BLK_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_BLK_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R5_BLK_TE, 5, 8, 1, 1)

        self.spinBox_R5_TKL_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R5_TKL_TE.setObjectName(u"spinBox_R5_TKL_TE")
        self.spinBox_R5_TKL_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TKL_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R5_TKL_TE, 5, 9, 1, 1)

        self.spinBox_R5_HAN_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R5_HAN_TE.setObjectName(u"spinBox_R5_HAN_TE")
        self.spinBox_R5_HAN_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_HAN_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R5_HAN_TE, 5, 10, 1, 1)

        self.spinBox_R5_GI_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R5_GI_TE.setObjectName(u"spinBox_R5_GI_TE")
        self.spinBox_R5_GI_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_GI_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R5_GI_TE, 5, 11, 1, 1)

        self.spinBox_R5_ELU_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R5_ELU_TE.setObjectName(u"spinBox_R5_ELU_TE")
        self.spinBox_R5_ELU_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ELU_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R5_ELU_TE, 5, 12, 1, 1)

        self.spinBox_R5_TEC_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R5_TEC_TE.setObjectName(u"spinBox_R5_TEC_TE")
        self.spinBox_R5_TEC_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TEC_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R5_TEC_TE, 5, 13, 1, 1)

        self.spinBox_R6_ATH_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R6_ATH_TE.setObjectName(u"spinBox_R6_ATH_TE")
        self.spinBox_R6_ATH_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ATH_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R6_ATH_TE, 6, 2, 1, 1)

        self.spinBox_R6_SPD_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R6_SPD_TE.setObjectName(u"spinBox_R6_SPD_TE")
        self.spinBox_R6_SPD_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_SPD_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R6_SPD_TE, 6, 3, 1, 1)

        self.spinBox_R6_DUR_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R6_DUR_TE.setObjectName(u"spinBox_R6_DUR_TE")
        self.spinBox_R6_DUR_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_DUR_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R6_DUR_TE, 6, 4, 1, 1)

        self.spinBox_R6_WE_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R6_WE_TE.setObjectName(u"spinBox_R6_WE_TE")
        self.spinBox_R6_WE_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_WE_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R6_WE_TE, 6, 5, 1, 1)

        self.spinBox_R6_STA_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R6_STA_TE.setObjectName(u"spinBox_R6_STA_TE")
        self.spinBox_R6_STA_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STA_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R6_STA_TE, 6, 6, 1, 1)

        self.spinBox_R6_STR_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R6_STR_TE.setObjectName(u"spinBox_R6_STR_TE")
        self.spinBox_R6_STR_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STR_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R6_STR_TE, 6, 7, 1, 1)

        self.spinBox_R6_BLK_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R6_BLK_TE.setObjectName(u"spinBox_R6_BLK_TE")
        self.spinBox_R6_BLK_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_BLK_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R6_BLK_TE, 6, 8, 1, 1)

        self.spinBox_R6_TKL_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R6_TKL_TE.setObjectName(u"spinBox_R6_TKL_TE")
        self.spinBox_R6_TKL_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TKL_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R6_TKL_TE, 6, 9, 1, 1)

        self.spinBox_R6_HAN_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R6_HAN_TE.setObjectName(u"spinBox_R6_HAN_TE")
        self.spinBox_R6_HAN_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_HAN_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R6_HAN_TE, 6, 10, 1, 1)

        self.spinBox_R6_GI_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R6_GI_TE.setObjectName(u"spinBox_R6_GI_TE")
        self.spinBox_R6_GI_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_GI_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R6_GI_TE, 6, 11, 1, 1)

        self.spinBox_R6_ELU_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R6_ELU_TE.setObjectName(u"spinBox_R6_ELU_TE")
        self.spinBox_R6_ELU_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ELU_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R6_ELU_TE, 6, 12, 1, 1)

        self.spinBox_R6_TEC_TE = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_R6_TEC_TE.setObjectName(u"spinBox_R6_TEC_TE")
        self.spinBox_R6_TEC_TE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TEC_TE.setMaximum(100)

        self.gridLayout_4.addWidget(self.spinBox_R6_TEC_TE, 6, 13, 1, 1)

        self.lineEdit_R1_TE = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_R1_TE.setObjectName(u"lineEdit_R1_TE")
        self.lineEdit_R1_TE.setFont(font2)
        self.lineEdit_R1_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_R1_TE, 1, 1, 1, 1)

        self.lineEdit_R2_TE = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_R2_TE.setObjectName(u"lineEdit_R2_TE")
        self.lineEdit_R2_TE.setFont(font2)
        self.lineEdit_R2_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_R2_TE, 2, 1, 1, 1)

        self.lineEdit_R3_TE = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_R3_TE.setObjectName(u"lineEdit_R3_TE")
        self.lineEdit_R3_TE.setFont(font2)
        self.lineEdit_R3_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_R3_TE, 3, 1, 1, 1)

        self.lineEdit_R4_TE = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_R4_TE.setObjectName(u"lineEdit_R4_TE")
        self.lineEdit_R4_TE.setFont(font2)
        self.lineEdit_R4_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_R4_TE, 4, 1, 1, 1)

        self.lineEdit_R5_TE = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_R5_TE.setObjectName(u"lineEdit_R5_TE")
        self.lineEdit_R5_TE.setFont(font2)
        self.lineEdit_R5_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_R5_TE, 5, 1, 1, 1)

        self.lineEdit_R6_TE = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_R6_TE.setObjectName(u"lineEdit_R6_TE")
        self.lineEdit_R6_TE.setFont(font2)
        self.lineEdit_R6_TE.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lineEdit_R6_TE, 6, 1, 1, 1)

        self.lcdNumber_R1_TE = QLCDNumber(self.gridLayoutWidget_4)
        self.lcdNumber_R1_TE.setObjectName(u"lcdNumber_R1_TE")
        self.lcdNumber_R1_TE.setDigitCount(3)
        self.lcdNumber_R1_TE.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.lcdNumber_R1_TE, 1, 14, 1, 1)

        self.lcdNumber_R2_TE = QLCDNumber(self.gridLayoutWidget_4)
        self.lcdNumber_R2_TE.setObjectName(u"lcdNumber_R2_TE")
        self.lcdNumber_R2_TE.setDigitCount(3)
        self.lcdNumber_R2_TE.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.lcdNumber_R2_TE, 2, 14, 1, 1)

        self.lcdNumber_R3_TE = QLCDNumber(self.gridLayoutWidget_4)
        self.lcdNumber_R3_TE.setObjectName(u"lcdNumber_R3_TE")
        self.lcdNumber_R3_TE.setDigitCount(3)
        self.lcdNumber_R3_TE.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.lcdNumber_R3_TE, 3, 14, 1, 1)

        self.lcdNumber_R4_TE = QLCDNumber(self.gridLayoutWidget_4)
        self.lcdNumber_R4_TE.setObjectName(u"lcdNumber_R4_TE")
        self.lcdNumber_R4_TE.setDigitCount(3)
        self.lcdNumber_R4_TE.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.lcdNumber_R4_TE, 4, 14, 1, 1)

        self.lcdNumber_R5_TE = QLCDNumber(self.gridLayoutWidget_4)
        self.lcdNumber_R5_TE.setObjectName(u"lcdNumber_R5_TE")
        self.lcdNumber_R5_TE.setDigitCount(3)
        self.lcdNumber_R5_TE.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.lcdNumber_R5_TE, 5, 14, 1, 1)

        self.lcdNumber_R6_TE = QLCDNumber(self.gridLayoutWidget_4)
        self.lcdNumber_R6_TE.setObjectName(u"lcdNumber_R6_TE")
        self.lcdNumber_R6_TE.setDigitCount(3)
        self.lcdNumber_R6_TE.setProperty("intValue", 0)

        self.gridLayout_4.addWidget(self.lcdNumber_R6_TE, 6, 14, 1, 1)

        self.tabWidgetRoleRatings.addTab(self.TE, "")
        self.OL = QWidget()
        self.OL.setObjectName(u"OL")
        self.gridLayoutWidget_5 = QWidget(self.OL)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 10, 1215, 261))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_ATH_Header_OL = QLabel(self.gridLayoutWidget_5)
        self.label_ATH_Header_OL.setObjectName(u"label_ATH_Header_OL")
        self.label_ATH_Header_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_ATH_Header_OL, 0, 2, 1, 1)

        self.spinBox_R2_TKL_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R2_TKL_OL.setObjectName(u"spinBox_R2_TKL_OL")
        self.spinBox_R2_TKL_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TKL_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R2_TKL_OL, 2, 9, 1, 1)

        self.spinBox_R3_DUR_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R3_DUR_OL.setObjectName(u"spinBox_R3_DUR_OL")
        self.spinBox_R3_DUR_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_DUR_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R3_DUR_OL, 3, 4, 1, 1)

        self.spinBox_R3_STR_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R3_STR_OL.setObjectName(u"spinBox_R3_STR_OL")
        self.spinBox_R3_STR_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STR_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R3_STR_OL, 3, 7, 1, 1)

        self.spinBox_R2_TEC_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R2_TEC_OL.setObjectName(u"spinBox_R2_TEC_OL")
        self.spinBox_R2_TEC_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TEC_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R2_TEC_OL, 2, 13, 1, 1)

        self.spinBox_R2_WE_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R2_WE_OL.setObjectName(u"spinBox_R2_WE_OL")
        self.spinBox_R2_WE_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_WE_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R2_WE_OL, 2, 5, 1, 1)

        self.spinBox_R1_SPD_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R1_SPD_OL.setObjectName(u"spinBox_R1_SPD_OL")
        self.spinBox_R1_SPD_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_SPD_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R1_SPD_OL, 1, 3, 1, 1)

        self.label_TEC_Header_OL = QLabel(self.gridLayoutWidget_5)
        self.label_TEC_Header_OL.setObjectName(u"label_TEC_Header_OL")
        self.label_TEC_Header_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_TEC_Header_OL, 0, 13, 1, 1)

        self.spinBox_R1_BLK_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R1_BLK_OL.setObjectName(u"spinBox_R1_BLK_OL")
        self.spinBox_R1_BLK_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_BLK_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R1_BLK_OL, 1, 8, 1, 1)

        self.spinBox_R1_STA_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R1_STA_OL.setObjectName(u"spinBox_R1_STA_OL")
        self.spinBox_R1_STA_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STA_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R1_STA_OL, 1, 6, 1, 1)

        self.label_WE_Header_OL = QLabel(self.gridLayoutWidget_5)
        self.label_WE_Header_OL.setObjectName(u"label_WE_Header_OL")
        self.label_WE_Header_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_WE_Header_OL, 0, 5, 1, 1)

        self.label_TKL_Header_OL = QLabel(self.gridLayoutWidget_5)
        self.label_TKL_Header_OL.setObjectName(u"label_TKL_Header_OL")
        self.label_TKL_Header_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_TKL_Header_OL, 0, 9, 1, 1)

        self.label_STR_Header_OL = QLabel(self.gridLayoutWidget_5)
        self.label_STR_Header_OL.setObjectName(u"label_STR_Header_OL")
        self.label_STR_Header_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_STR_Header_OL, 0, 7, 1, 1)

        self.spinBox_R1_WE_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R1_WE_OL.setObjectName(u"spinBox_R1_WE_OL")
        self.spinBox_R1_WE_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_WE_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R1_WE_OL, 1, 5, 1, 1)

        self.spinBox_R2_SPD_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R2_SPD_OL.setObjectName(u"spinBox_R2_SPD_OL")
        self.spinBox_R2_SPD_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_SPD_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R2_SPD_OL, 2, 3, 1, 1)

        self.label_R1_OL = QLabel(self.gridLayoutWidget_5)
        self.label_R1_OL.setObjectName(u"label_R1_OL")
        self.label_R1_OL.setFont(font1)
        self.label_R1_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_R1_OL, 1, 0, 1, 1)

        self.label_RoleHeader_OL = QLabel(self.gridLayoutWidget_5)
        self.label_RoleHeader_OL.setObjectName(u"label_RoleHeader_OL")
        self.label_RoleHeader_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_RoleHeader_OL, 0, 0, 1, 1)

        self.label_Total_Header_OL = QLabel(self.gridLayoutWidget_5)
        self.label_Total_Header_OL.setObjectName(u"label_Total_Header_OL")

        self.gridLayout_5.addWidget(self.label_Total_Header_OL, 0, 14, 1, 1)

        self.spinBox_R3_STA_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R3_STA_OL.setObjectName(u"spinBox_R3_STA_OL")
        self.spinBox_R3_STA_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STA_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R3_STA_OL, 3, 6, 1, 1)

        self.label_R5_OL = QLabel(self.gridLayoutWidget_5)
        self.label_R5_OL.setObjectName(u"label_R5_OL")
        self.label_R5_OL.setFont(font1)
        self.label_R5_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_R5_OL, 5, 0, 1, 1)

        self.label_BLK_Header_OL = QLabel(self.gridLayoutWidget_5)
        self.label_BLK_Header_OL.setObjectName(u"label_BLK_Header_OL")
        self.label_BLK_Header_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_BLK_Header_OL, 0, 8, 1, 1)

        self.label_ELU_Header_OL = QLabel(self.gridLayoutWidget_5)
        self.label_ELU_Header_OL.setObjectName(u"label_ELU_Header_OL")
        self.label_ELU_Header_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_ELU_Header_OL, 0, 12, 1, 1)

        self.spinBox_R2_BLK_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R2_BLK_OL.setObjectName(u"spinBox_R2_BLK_OL")
        self.spinBox_R2_BLK_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_BLK_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R2_BLK_OL, 2, 8, 1, 1)

        self.label_LabelHeader_OL = QLabel(self.gridLayoutWidget_5)
        self.label_LabelHeader_OL.setObjectName(u"label_LabelHeader_OL")
        self.label_LabelHeader_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_LabelHeader_OL, 0, 1, 1, 1)

        self.spinBox_R2_HAN_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R2_HAN_OL.setObjectName(u"spinBox_R2_HAN_OL")
        self.spinBox_R2_HAN_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_HAN_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R2_HAN_OL, 2, 10, 1, 1)

        self.label_R2_OL = QLabel(self.gridLayoutWidget_5)
        self.label_R2_OL.setObjectName(u"label_R2_OL")
        self.label_R2_OL.setFont(font1)
        self.label_R2_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_R2_OL, 2, 0, 1, 1)

        self.spinBox_R1_GI_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R1_GI_OL.setObjectName(u"spinBox_R1_GI_OL")
        self.spinBox_R1_GI_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_GI_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R1_GI_OL, 1, 11, 1, 1)

        self.label_DUR_Header_OL = QLabel(self.gridLayoutWidget_5)
        self.label_DUR_Header_OL.setObjectName(u"label_DUR_Header_OL")
        self.label_DUR_Header_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_DUR_Header_OL, 0, 4, 1, 1)

        self.spinBox_R1_HAN_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R1_HAN_OL.setObjectName(u"spinBox_R1_HAN_OL")
        self.spinBox_R1_HAN_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_HAN_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R1_HAN_OL, 1, 10, 1, 1)

        self.label_R3_OL = QLabel(self.gridLayoutWidget_5)
        self.label_R3_OL.setObjectName(u"label_R3_OL")
        self.label_R3_OL.setFont(font1)
        self.label_R3_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_R3_OL, 3, 0, 1, 1)

        self.label_GI_Header_OL = QLabel(self.gridLayoutWidget_5)
        self.label_GI_Header_OL.setObjectName(u"label_GI_Header_OL")
        self.label_GI_Header_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_GI_Header_OL, 0, 11, 1, 1)

        self.spinBox_R1_TEC_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R1_TEC_OL.setObjectName(u"spinBox_R1_TEC_OL")
        self.spinBox_R1_TEC_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TEC_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R1_TEC_OL, 1, 13, 1, 1)

        self.spinBox_R1_ATH_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R1_ATH_OL.setObjectName(u"spinBox_R1_ATH_OL")
        self.spinBox_R1_ATH_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ATH_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R1_ATH_OL, 1, 2, 1, 1)

        self.spinBox_R1_DUR_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R1_DUR_OL.setObjectName(u"spinBox_R1_DUR_OL")
        self.spinBox_R1_DUR_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_DUR_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R1_DUR_OL, 1, 4, 1, 1)

        self.spinBox_R2_ELU_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R2_ELU_OL.setObjectName(u"spinBox_R2_ELU_OL")
        self.spinBox_R2_ELU_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ELU_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R2_ELU_OL, 2, 12, 1, 1)

        self.spinBox_R2_ATH_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R2_ATH_OL.setObjectName(u"spinBox_R2_ATH_OL")
        self.spinBox_R2_ATH_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ATH_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R2_ATH_OL, 2, 2, 1, 1)

        self.spinBox_R2_STR_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R2_STR_OL.setObjectName(u"spinBox_R2_STR_OL")
        self.spinBox_R2_STR_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STR_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R2_STR_OL, 2, 7, 1, 1)

        self.spinBox_R3_ATH_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R3_ATH_OL.setObjectName(u"spinBox_R3_ATH_OL")
        self.spinBox_R3_ATH_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ATH_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R3_ATH_OL, 3, 2, 1, 1)

        self.spinBox_R1_ELU_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R1_ELU_OL.setObjectName(u"spinBox_R1_ELU_OL")
        self.spinBox_R1_ELU_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ELU_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R1_ELU_OL, 1, 12, 1, 1)

        self.label_STA_Header_OL = QLabel(self.gridLayoutWidget_5)
        self.label_STA_Header_OL.setObjectName(u"label_STA_Header_OL")
        self.label_STA_Header_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_STA_Header_OL, 0, 6, 1, 1)

        self.spinBox_R1_STR_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R1_STR_OL.setObjectName(u"spinBox_R1_STR_OL")
        self.spinBox_R1_STR_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STR_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R1_STR_OL, 1, 7, 1, 1)

        self.label_SPD_Header_OL = QLabel(self.gridLayoutWidget_5)
        self.label_SPD_Header_OL.setObjectName(u"label_SPD_Header_OL")
        self.label_SPD_Header_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_SPD_Header_OL, 0, 3, 1, 1)

        self.spinBox_R2_DUR_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R2_DUR_OL.setObjectName(u"spinBox_R2_DUR_OL")
        self.spinBox_R2_DUR_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_DUR_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R2_DUR_OL, 2, 4, 1, 1)

        self.label_HAN_Header_OL = QLabel(self.gridLayoutWidget_5)
        self.label_HAN_Header_OL.setObjectName(u"label_HAN_Header_OL")
        self.label_HAN_Header_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_HAN_Header_OL, 0, 10, 1, 1)

        self.label_R4_OL = QLabel(self.gridLayoutWidget_5)
        self.label_R4_OL.setObjectName(u"label_R4_OL")
        self.label_R4_OL.setFont(font1)
        self.label_R4_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_R4_OL, 4, 0, 1, 1)

        self.spinBox_R1_TKL_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R1_TKL_OL.setObjectName(u"spinBox_R1_TKL_OL")
        self.spinBox_R1_TKL_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TKL_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R1_TKL_OL, 1, 9, 1, 1)

        self.spinBox_R2_GI_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R2_GI_OL.setObjectName(u"spinBox_R2_GI_OL")
        self.spinBox_R2_GI_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_GI_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R2_GI_OL, 2, 11, 1, 1)

        self.spinBox_R3_WE_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R3_WE_OL.setObjectName(u"spinBox_R3_WE_OL")
        self.spinBox_R3_WE_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_WE_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R3_WE_OL, 3, 5, 1, 1)

        self.spinBox_R3_SPD_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R3_SPD_OL.setObjectName(u"spinBox_R3_SPD_OL")
        self.spinBox_R3_SPD_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_SPD_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R3_SPD_OL, 3, 3, 1, 1)

        self.label_R6_OL = QLabel(self.gridLayoutWidget_5)
        self.label_R6_OL.setObjectName(u"label_R6_OL")
        self.label_R6_OL.setFont(font1)
        self.label_R6_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_R6_OL, 6, 0, 1, 1)

        self.spinBox_R2_STA_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R2_STA_OL.setObjectName(u"spinBox_R2_STA_OL")
        self.spinBox_R2_STA_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STA_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R2_STA_OL, 2, 6, 1, 1)

        self.spinBox_R3_BLK_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R3_BLK_OL.setObjectName(u"spinBox_R3_BLK_OL")
        self.spinBox_R3_BLK_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_BLK_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R3_BLK_OL, 3, 8, 1, 1)

        self.spinBox_R3_TKL_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R3_TKL_OL.setObjectName(u"spinBox_R3_TKL_OL")
        self.spinBox_R3_TKL_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TKL_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R3_TKL_OL, 3, 9, 1, 1)

        self.spinBox_R3_HAN_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R3_HAN_OL.setObjectName(u"spinBox_R3_HAN_OL")
        self.spinBox_R3_HAN_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_HAN_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R3_HAN_OL, 3, 10, 1, 1)

        self.spinBox_R3_GI_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R3_GI_OL.setObjectName(u"spinBox_R3_GI_OL")
        self.spinBox_R3_GI_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_GI_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R3_GI_OL, 3, 11, 1, 1)

        self.spinBox_R3_ELU_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R3_ELU_OL.setObjectName(u"spinBox_R3_ELU_OL")
        self.spinBox_R3_ELU_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ELU_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R3_ELU_OL, 3, 12, 1, 1)

        self.spinBox_R3_TEC_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R3_TEC_OL.setObjectName(u"spinBox_R3_TEC_OL")
        self.spinBox_R3_TEC_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TEC_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R3_TEC_OL, 3, 13, 1, 1)

        self.spinBox_R4_ATH_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R4_ATH_OL.setObjectName(u"spinBox_R4_ATH_OL")
        self.spinBox_R4_ATH_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ATH_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R4_ATH_OL, 4, 2, 1, 1)

        self.spinBox_R4_SPD_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R4_SPD_OL.setObjectName(u"spinBox_R4_SPD_OL")
        self.spinBox_R4_SPD_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_SPD_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R4_SPD_OL, 4, 3, 1, 1)

        self.spinBox_R4_DUR_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R4_DUR_OL.setObjectName(u"spinBox_R4_DUR_OL")
        self.spinBox_R4_DUR_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_DUR_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R4_DUR_OL, 4, 4, 1, 1)

        self.spinBox_R4_WE_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R4_WE_OL.setObjectName(u"spinBox_R4_WE_OL")
        self.spinBox_R4_WE_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_WE_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R4_WE_OL, 4, 5, 1, 1)

        self.spinBox_R4_STA_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R4_STA_OL.setObjectName(u"spinBox_R4_STA_OL")
        self.spinBox_R4_STA_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STA_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R4_STA_OL, 4, 6, 1, 1)

        self.spinBox_R4_STR_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R4_STR_OL.setObjectName(u"spinBox_R4_STR_OL")
        self.spinBox_R4_STR_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STR_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R4_STR_OL, 4, 7, 1, 1)

        self.spinBox_R4_BLK_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R4_BLK_OL.setObjectName(u"spinBox_R4_BLK_OL")
        self.spinBox_R4_BLK_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_BLK_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R4_BLK_OL, 4, 8, 1, 1)

        self.spinBox_R4_TKL_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R4_TKL_OL.setObjectName(u"spinBox_R4_TKL_OL")
        self.spinBox_R4_TKL_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TKL_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R4_TKL_OL, 4, 9, 1, 1)

        self.spinBox_R4_HAN_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R4_HAN_OL.setObjectName(u"spinBox_R4_HAN_OL")
        self.spinBox_R4_HAN_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_HAN_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R4_HAN_OL, 4, 10, 1, 1)

        self.spinBox_R4_GI_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R4_GI_OL.setObjectName(u"spinBox_R4_GI_OL")
        self.spinBox_R4_GI_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_GI_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R4_GI_OL, 4, 11, 1, 1)

        self.spinBox_R4_ELU_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R4_ELU_OL.setObjectName(u"spinBox_R4_ELU_OL")
        self.spinBox_R4_ELU_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ELU_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R4_ELU_OL, 4, 12, 1, 1)

        self.spinBox_R4_TEC_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R4_TEC_OL.setObjectName(u"spinBox_R4_TEC_OL")
        self.spinBox_R4_TEC_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TEC_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R4_TEC_OL, 4, 13, 1, 1)

        self.spinBox_R5_ATH_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R5_ATH_OL.setObjectName(u"spinBox_R5_ATH_OL")
        self.spinBox_R5_ATH_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ATH_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R5_ATH_OL, 5, 2, 1, 1)

        self.spinBox_R5_SPD_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R5_SPD_OL.setObjectName(u"spinBox_R5_SPD_OL")
        self.spinBox_R5_SPD_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_SPD_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R5_SPD_OL, 5, 3, 1, 1)

        self.spinBox_R5_DUR_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R5_DUR_OL.setObjectName(u"spinBox_R5_DUR_OL")
        self.spinBox_R5_DUR_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_DUR_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R5_DUR_OL, 5, 4, 1, 1)

        self.spinBox_R5_WE_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R5_WE_OL.setObjectName(u"spinBox_R5_WE_OL")
        self.spinBox_R5_WE_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_WE_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R5_WE_OL, 5, 5, 1, 1)

        self.spinBox_R5_STA_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R5_STA_OL.setObjectName(u"spinBox_R5_STA_OL")
        self.spinBox_R5_STA_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STA_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R5_STA_OL, 5, 6, 1, 1)

        self.spinBox_R5_STR_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R5_STR_OL.setObjectName(u"spinBox_R5_STR_OL")
        self.spinBox_R5_STR_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STR_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R5_STR_OL, 5, 7, 1, 1)

        self.spinBox_R5_BLK_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R5_BLK_OL.setObjectName(u"spinBox_R5_BLK_OL")
        self.spinBox_R5_BLK_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_BLK_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R5_BLK_OL, 5, 8, 1, 1)

        self.spinBox_R5_TKL_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R5_TKL_OL.setObjectName(u"spinBox_R5_TKL_OL")
        self.spinBox_R5_TKL_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TKL_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R5_TKL_OL, 5, 9, 1, 1)

        self.spinBox_R5_HAN_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R5_HAN_OL.setObjectName(u"spinBox_R5_HAN_OL")
        self.spinBox_R5_HAN_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_HAN_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R5_HAN_OL, 5, 10, 1, 1)

        self.spinBox_R5_GI_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R5_GI_OL.setObjectName(u"spinBox_R5_GI_OL")
        self.spinBox_R5_GI_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_GI_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R5_GI_OL, 5, 11, 1, 1)

        self.spinBox_R5_ELU_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R5_ELU_OL.setObjectName(u"spinBox_R5_ELU_OL")
        self.spinBox_R5_ELU_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ELU_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R5_ELU_OL, 5, 12, 1, 1)

        self.spinBox_R5_TEC_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R5_TEC_OL.setObjectName(u"spinBox_R5_TEC_OL")
        self.spinBox_R5_TEC_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TEC_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R5_TEC_OL, 5, 13, 1, 1)

        self.spinBox_R6_ATH_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R6_ATH_OL.setObjectName(u"spinBox_R6_ATH_OL")
        self.spinBox_R6_ATH_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ATH_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R6_ATH_OL, 6, 2, 1, 1)

        self.spinBox_R6_SPD_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R6_SPD_OL.setObjectName(u"spinBox_R6_SPD_OL")
        self.spinBox_R6_SPD_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_SPD_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R6_SPD_OL, 6, 3, 1, 1)

        self.spinBox_R6_DUR_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R6_DUR_OL.setObjectName(u"spinBox_R6_DUR_OL")
        self.spinBox_R6_DUR_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_DUR_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R6_DUR_OL, 6, 4, 1, 1)

        self.spinBox_R6_WE_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R6_WE_OL.setObjectName(u"spinBox_R6_WE_OL")
        self.spinBox_R6_WE_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_WE_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R6_WE_OL, 6, 5, 1, 1)

        self.spinBox_R6_STA_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R6_STA_OL.setObjectName(u"spinBox_R6_STA_OL")
        self.spinBox_R6_STA_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STA_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R6_STA_OL, 6, 6, 1, 1)

        self.spinBox_R6_STR_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R6_STR_OL.setObjectName(u"spinBox_R6_STR_OL")
        self.spinBox_R6_STR_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STR_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R6_STR_OL, 6, 7, 1, 1)

        self.spinBox_R6_BLK_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R6_BLK_OL.setObjectName(u"spinBox_R6_BLK_OL")
        self.spinBox_R6_BLK_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_BLK_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R6_BLK_OL, 6, 8, 1, 1)

        self.spinBox_R6_TKL_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R6_TKL_OL.setObjectName(u"spinBox_R6_TKL_OL")
        self.spinBox_R6_TKL_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TKL_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R6_TKL_OL, 6, 9, 1, 1)

        self.spinBox_R6_HAN_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R6_HAN_OL.setObjectName(u"spinBox_R6_HAN_OL")
        self.spinBox_R6_HAN_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_HAN_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R6_HAN_OL, 6, 10, 1, 1)

        self.spinBox_R6_GI_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R6_GI_OL.setObjectName(u"spinBox_R6_GI_OL")
        self.spinBox_R6_GI_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_GI_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R6_GI_OL, 6, 11, 1, 1)

        self.spinBox_R6_ELU_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R6_ELU_OL.setObjectName(u"spinBox_R6_ELU_OL")
        self.spinBox_R6_ELU_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ELU_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R6_ELU_OL, 6, 12, 1, 1)

        self.spinBox_R6_TEC_OL = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_R6_TEC_OL.setObjectName(u"spinBox_R6_TEC_OL")
        self.spinBox_R6_TEC_OL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TEC_OL.setMaximum(100)

        self.gridLayout_5.addWidget(self.spinBox_R6_TEC_OL, 6, 13, 1, 1)

        self.lineEdit_R1_OL = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_R1_OL.setObjectName(u"lineEdit_R1_OL")
        self.lineEdit_R1_OL.setFont(font2)
        self.lineEdit_R1_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lineEdit_R1_OL, 1, 1, 1, 1)

        self.lineEdit_R2_OL = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_R2_OL.setObjectName(u"lineEdit_R2_OL")
        self.lineEdit_R2_OL.setFont(font2)
        self.lineEdit_R2_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lineEdit_R2_OL, 2, 1, 1, 1)

        self.lineEdit_R3_OL = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_R3_OL.setObjectName(u"lineEdit_R3_OL")
        self.lineEdit_R3_OL.setFont(font2)
        self.lineEdit_R3_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lineEdit_R3_OL, 3, 1, 1, 1)

        self.lineEdit_R4_OL = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_R4_OL.setObjectName(u"lineEdit_R4_OL")
        self.lineEdit_R4_OL.setFont(font2)
        self.lineEdit_R4_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lineEdit_R4_OL, 4, 1, 1, 1)

        self.lineEdit_R5_OL = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_R5_OL.setObjectName(u"lineEdit_R5_OL")
        self.lineEdit_R5_OL.setFont(font2)
        self.lineEdit_R5_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lineEdit_R5_OL, 5, 1, 1, 1)

        self.lineEdit_R6_OL = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_R6_OL.setObjectName(u"lineEdit_R6_OL")
        self.lineEdit_R6_OL.setFont(font2)
        self.lineEdit_R6_OL.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lineEdit_R6_OL, 6, 1, 1, 1)

        self.lcdNumber_R1_OL = QLCDNumber(self.gridLayoutWidget_5)
        self.lcdNumber_R1_OL.setObjectName(u"lcdNumber_R1_OL")
        self.lcdNumber_R1_OL.setDigitCount(3)
        self.lcdNumber_R1_OL.setProperty("intValue", 0)

        self.gridLayout_5.addWidget(self.lcdNumber_R1_OL, 1, 14, 1, 1)

        self.lcdNumber_R2_OL = QLCDNumber(self.gridLayoutWidget_5)
        self.lcdNumber_R2_OL.setObjectName(u"lcdNumber_R2_OL")
        self.lcdNumber_R2_OL.setDigitCount(3)
        self.lcdNumber_R2_OL.setProperty("intValue", 0)

        self.gridLayout_5.addWidget(self.lcdNumber_R2_OL, 2, 14, 1, 1)

        self.lcdNumber_R3_OL = QLCDNumber(self.gridLayoutWidget_5)
        self.lcdNumber_R3_OL.setObjectName(u"lcdNumber_R3_OL")
        self.lcdNumber_R3_OL.setDigitCount(3)
        self.lcdNumber_R3_OL.setProperty("intValue", 0)

        self.gridLayout_5.addWidget(self.lcdNumber_R3_OL, 3, 14, 1, 1)

        self.lcdNumber_R4_OL = QLCDNumber(self.gridLayoutWidget_5)
        self.lcdNumber_R4_OL.setObjectName(u"lcdNumber_R4_OL")
        self.lcdNumber_R4_OL.setDigitCount(3)
        self.lcdNumber_R4_OL.setProperty("intValue", 0)

        self.gridLayout_5.addWidget(self.lcdNumber_R4_OL, 4, 14, 1, 1)

        self.lcdNumber_R5_OL = QLCDNumber(self.gridLayoutWidget_5)
        self.lcdNumber_R5_OL.setObjectName(u"lcdNumber_R5_OL")
        self.lcdNumber_R5_OL.setDigitCount(3)
        self.lcdNumber_R5_OL.setProperty("intValue", 0)

        self.gridLayout_5.addWidget(self.lcdNumber_R5_OL, 5, 14, 1, 1)

        self.lcdNumber_R6_OL = QLCDNumber(self.gridLayoutWidget_5)
        self.lcdNumber_R6_OL.setObjectName(u"lcdNumber_R6_OL")
        self.lcdNumber_R6_OL.setDigitCount(3)
        self.lcdNumber_R6_OL.setProperty("intValue", 0)

        self.gridLayout_5.addWidget(self.lcdNumber_R6_OL, 6, 14, 1, 1)

        self.tabWidgetRoleRatings.addTab(self.OL, "")
        self.DL = QWidget()
        self.DL.setObjectName(u"DL")
        self.gridLayoutWidget_6 = QWidget(self.DL)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(0, 10, 1215, 261))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_ATH_Header_DL = QLabel(self.gridLayoutWidget_6)
        self.label_ATH_Header_DL.setObjectName(u"label_ATH_Header_DL")
        self.label_ATH_Header_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_ATH_Header_DL, 0, 2, 1, 1)

        self.spinBox_R2_TKL_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R2_TKL_DL.setObjectName(u"spinBox_R2_TKL_DL")
        self.spinBox_R2_TKL_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TKL_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R2_TKL_DL, 2, 9, 1, 1)

        self.spinBox_R3_DUR_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R3_DUR_DL.setObjectName(u"spinBox_R3_DUR_DL")
        self.spinBox_R3_DUR_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_DUR_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R3_DUR_DL, 3, 4, 1, 1)

        self.spinBox_R3_STR_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R3_STR_DL.setObjectName(u"spinBox_R3_STR_DL")
        self.spinBox_R3_STR_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STR_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R3_STR_DL, 3, 7, 1, 1)

        self.spinBox_R2_TEC_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R2_TEC_DL.setObjectName(u"spinBox_R2_TEC_DL")
        self.spinBox_R2_TEC_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TEC_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R2_TEC_DL, 2, 13, 1, 1)

        self.spinBox_R2_WE_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R2_WE_DL.setObjectName(u"spinBox_R2_WE_DL")
        self.spinBox_R2_WE_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_WE_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R2_WE_DL, 2, 5, 1, 1)

        self.spinBox_R1_SPD_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R1_SPD_DL.setObjectName(u"spinBox_R1_SPD_DL")
        self.spinBox_R1_SPD_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_SPD_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R1_SPD_DL, 1, 3, 1, 1)

        self.label_TEC_Header_DL = QLabel(self.gridLayoutWidget_6)
        self.label_TEC_Header_DL.setObjectName(u"label_TEC_Header_DL")
        self.label_TEC_Header_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_TEC_Header_DL, 0, 13, 1, 1)

        self.spinBox_R1_BLK_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R1_BLK_DL.setObjectName(u"spinBox_R1_BLK_DL")
        self.spinBox_R1_BLK_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_BLK_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R1_BLK_DL, 1, 8, 1, 1)

        self.spinBox_R1_STA_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R1_STA_DL.setObjectName(u"spinBox_R1_STA_DL")
        self.spinBox_R1_STA_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STA_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R1_STA_DL, 1, 6, 1, 1)

        self.label_WE_Header_DL = QLabel(self.gridLayoutWidget_6)
        self.label_WE_Header_DL.setObjectName(u"label_WE_Header_DL")
        self.label_WE_Header_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_WE_Header_DL, 0, 5, 1, 1)

        self.label_TKL_Header_DL = QLabel(self.gridLayoutWidget_6)
        self.label_TKL_Header_DL.setObjectName(u"label_TKL_Header_DL")
        self.label_TKL_Header_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_TKL_Header_DL, 0, 9, 1, 1)

        self.label_STR_Header_DL = QLabel(self.gridLayoutWidget_6)
        self.label_STR_Header_DL.setObjectName(u"label_STR_Header_DL")
        self.label_STR_Header_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_STR_Header_DL, 0, 7, 1, 1)

        self.spinBox_R1_WE_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R1_WE_DL.setObjectName(u"spinBox_R1_WE_DL")
        self.spinBox_R1_WE_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_WE_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R1_WE_DL, 1, 5, 1, 1)

        self.spinBox_R2_SPD_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R2_SPD_DL.setObjectName(u"spinBox_R2_SPD_DL")
        self.spinBox_R2_SPD_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_SPD_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R2_SPD_DL, 2, 3, 1, 1)

        self.label_R1_DL = QLabel(self.gridLayoutWidget_6)
        self.label_R1_DL.setObjectName(u"label_R1_DL")
        self.label_R1_DL.setFont(font1)
        self.label_R1_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_R1_DL, 1, 0, 1, 1)

        self.label_RoleHeader_DL = QLabel(self.gridLayoutWidget_6)
        self.label_RoleHeader_DL.setObjectName(u"label_RoleHeader_DL")
        self.label_RoleHeader_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_RoleHeader_DL, 0, 0, 1, 1)

        self.label_Total_Header_DL = QLabel(self.gridLayoutWidget_6)
        self.label_Total_Header_DL.setObjectName(u"label_Total_Header_DL")

        self.gridLayout_6.addWidget(self.label_Total_Header_DL, 0, 14, 1, 1)

        self.spinBox_R3_STA_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R3_STA_DL.setObjectName(u"spinBox_R3_STA_DL")
        self.spinBox_R3_STA_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STA_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R3_STA_DL, 3, 6, 1, 1)

        self.label_R5_DL = QLabel(self.gridLayoutWidget_6)
        self.label_R5_DL.setObjectName(u"label_R5_DL")
        self.label_R5_DL.setFont(font1)
        self.label_R5_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_R5_DL, 5, 0, 1, 1)

        self.label_BLK_Header_DL = QLabel(self.gridLayoutWidget_6)
        self.label_BLK_Header_DL.setObjectName(u"label_BLK_Header_DL")
        self.label_BLK_Header_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_BLK_Header_DL, 0, 8, 1, 1)

        self.label_ELU_Header_DL = QLabel(self.gridLayoutWidget_6)
        self.label_ELU_Header_DL.setObjectName(u"label_ELU_Header_DL")
        self.label_ELU_Header_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_ELU_Header_DL, 0, 12, 1, 1)

        self.spinBox_R2_BLK_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R2_BLK_DL.setObjectName(u"spinBox_R2_BLK_DL")
        self.spinBox_R2_BLK_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_BLK_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R2_BLK_DL, 2, 8, 1, 1)

        self.label_LabelHeader_DL = QLabel(self.gridLayoutWidget_6)
        self.label_LabelHeader_DL.setObjectName(u"label_LabelHeader_DL")
        self.label_LabelHeader_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_LabelHeader_DL, 0, 1, 1, 1)

        self.spinBox_R2_HAN_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R2_HAN_DL.setObjectName(u"spinBox_R2_HAN_DL")
        self.spinBox_R2_HAN_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_HAN_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R2_HAN_DL, 2, 10, 1, 1)

        self.label_R2_DL = QLabel(self.gridLayoutWidget_6)
        self.label_R2_DL.setObjectName(u"label_R2_DL")
        self.label_R2_DL.setFont(font1)
        self.label_R2_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_R2_DL, 2, 0, 1, 1)

        self.spinBox_R1_GI_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R1_GI_DL.setObjectName(u"spinBox_R1_GI_DL")
        self.spinBox_R1_GI_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_GI_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R1_GI_DL, 1, 11, 1, 1)

        self.label_DUR_Header_DL = QLabel(self.gridLayoutWidget_6)
        self.label_DUR_Header_DL.setObjectName(u"label_DUR_Header_DL")
        self.label_DUR_Header_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_DUR_Header_DL, 0, 4, 1, 1)

        self.spinBox_R1_HAN_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R1_HAN_DL.setObjectName(u"spinBox_R1_HAN_DL")
        self.spinBox_R1_HAN_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_HAN_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R1_HAN_DL, 1, 10, 1, 1)

        self.label_R3_DL = QLabel(self.gridLayoutWidget_6)
        self.label_R3_DL.setObjectName(u"label_R3_DL")
        self.label_R3_DL.setFont(font1)
        self.label_R3_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_R3_DL, 3, 0, 1, 1)

        self.label_GI_Header_DL = QLabel(self.gridLayoutWidget_6)
        self.label_GI_Header_DL.setObjectName(u"label_GI_Header_DL")
        self.label_GI_Header_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_GI_Header_DL, 0, 11, 1, 1)

        self.spinBox_R1_TEC_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R1_TEC_DL.setObjectName(u"spinBox_R1_TEC_DL")
        self.spinBox_R1_TEC_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TEC_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R1_TEC_DL, 1, 13, 1, 1)

        self.spinBox_R1_ATH_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R1_ATH_DL.setObjectName(u"spinBox_R1_ATH_DL")
        self.spinBox_R1_ATH_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ATH_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R1_ATH_DL, 1, 2, 1, 1)

        self.spinBox_R1_DUR_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R1_DUR_DL.setObjectName(u"spinBox_R1_DUR_DL")
        self.spinBox_R1_DUR_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_DUR_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R1_DUR_DL, 1, 4, 1, 1)

        self.spinBox_R2_ELU_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R2_ELU_DL.setObjectName(u"spinBox_R2_ELU_DL")
        self.spinBox_R2_ELU_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ELU_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R2_ELU_DL, 2, 12, 1, 1)

        self.spinBox_R2_ATH_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R2_ATH_DL.setObjectName(u"spinBox_R2_ATH_DL")
        self.spinBox_R2_ATH_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ATH_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R2_ATH_DL, 2, 2, 1, 1)

        self.spinBox_R2_STR_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R2_STR_DL.setObjectName(u"spinBox_R2_STR_DL")
        self.spinBox_R2_STR_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STR_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R2_STR_DL, 2, 7, 1, 1)

        self.spinBox_R3_ATH_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R3_ATH_DL.setObjectName(u"spinBox_R3_ATH_DL")
        self.spinBox_R3_ATH_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ATH_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R3_ATH_DL, 3, 2, 1, 1)

        self.spinBox_R1_ELU_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R1_ELU_DL.setObjectName(u"spinBox_R1_ELU_DL")
        self.spinBox_R1_ELU_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ELU_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R1_ELU_DL, 1, 12, 1, 1)

        self.label_STA_Header_DL = QLabel(self.gridLayoutWidget_6)
        self.label_STA_Header_DL.setObjectName(u"label_STA_Header_DL")
        self.label_STA_Header_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_STA_Header_DL, 0, 6, 1, 1)

        self.spinBox_R1_STR_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R1_STR_DL.setObjectName(u"spinBox_R1_STR_DL")
        self.spinBox_R1_STR_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STR_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R1_STR_DL, 1, 7, 1, 1)

        self.label_SPD_Header_DL = QLabel(self.gridLayoutWidget_6)
        self.label_SPD_Header_DL.setObjectName(u"label_SPD_Header_DL")
        self.label_SPD_Header_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_SPD_Header_DL, 0, 3, 1, 1)

        self.spinBox_R2_DUR_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R2_DUR_DL.setObjectName(u"spinBox_R2_DUR_DL")
        self.spinBox_R2_DUR_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_DUR_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R2_DUR_DL, 2, 4, 1, 1)

        self.label_HAN_Header_DL = QLabel(self.gridLayoutWidget_6)
        self.label_HAN_Header_DL.setObjectName(u"label_HAN_Header_DL")
        self.label_HAN_Header_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_HAN_Header_DL, 0, 10, 1, 1)

        self.label_R4_DL = QLabel(self.gridLayoutWidget_6)
        self.label_R4_DL.setObjectName(u"label_R4_DL")
        self.label_R4_DL.setFont(font1)
        self.label_R4_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_R4_DL, 4, 0, 1, 1)

        self.spinBox_R1_TKL_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R1_TKL_DL.setObjectName(u"spinBox_R1_TKL_DL")
        self.spinBox_R1_TKL_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TKL_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R1_TKL_DL, 1, 9, 1, 1)

        self.spinBox_R2_GI_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R2_GI_DL.setObjectName(u"spinBox_R2_GI_DL")
        self.spinBox_R2_GI_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_GI_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R2_GI_DL, 2, 11, 1, 1)

        self.spinBox_R3_WE_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R3_WE_DL.setObjectName(u"spinBox_R3_WE_DL")
        self.spinBox_R3_WE_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_WE_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R3_WE_DL, 3, 5, 1, 1)

        self.spinBox_R3_SPD_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R3_SPD_DL.setObjectName(u"spinBox_R3_SPD_DL")
        self.spinBox_R3_SPD_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_SPD_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R3_SPD_DL, 3, 3, 1, 1)

        self.label_R6_DL = QLabel(self.gridLayoutWidget_6)
        self.label_R6_DL.setObjectName(u"label_R6_DL")
        self.label_R6_DL.setFont(font1)
        self.label_R6_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_R6_DL, 6, 0, 1, 1)

        self.spinBox_R2_STA_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R2_STA_DL.setObjectName(u"spinBox_R2_STA_DL")
        self.spinBox_R2_STA_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STA_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R2_STA_DL, 2, 6, 1, 1)

        self.spinBox_R3_BLK_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R3_BLK_DL.setObjectName(u"spinBox_R3_BLK_DL")
        self.spinBox_R3_BLK_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_BLK_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R3_BLK_DL, 3, 8, 1, 1)

        self.spinBox_R3_TKL_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R3_TKL_DL.setObjectName(u"spinBox_R3_TKL_DL")
        self.spinBox_R3_TKL_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TKL_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R3_TKL_DL, 3, 9, 1, 1)

        self.spinBox_R3_HAN_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R3_HAN_DL.setObjectName(u"spinBox_R3_HAN_DL")
        self.spinBox_R3_HAN_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_HAN_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R3_HAN_DL, 3, 10, 1, 1)

        self.spinBox_R3_GI_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R3_GI_DL.setObjectName(u"spinBox_R3_GI_DL")
        self.spinBox_R3_GI_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_GI_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R3_GI_DL, 3, 11, 1, 1)

        self.spinBox_R3_ELU_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R3_ELU_DL.setObjectName(u"spinBox_R3_ELU_DL")
        self.spinBox_R3_ELU_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ELU_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R3_ELU_DL, 3, 12, 1, 1)

        self.spinBox_R3_TEC_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R3_TEC_DL.setObjectName(u"spinBox_R3_TEC_DL")
        self.spinBox_R3_TEC_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TEC_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R3_TEC_DL, 3, 13, 1, 1)

        self.spinBox_R4_ATH_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R4_ATH_DL.setObjectName(u"spinBox_R4_ATH_DL")
        self.spinBox_R4_ATH_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ATH_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R4_ATH_DL, 4, 2, 1, 1)

        self.spinBox_R4_SPD_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R4_SPD_DL.setObjectName(u"spinBox_R4_SPD_DL")
        self.spinBox_R4_SPD_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_SPD_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R4_SPD_DL, 4, 3, 1, 1)

        self.spinBox_R4_DUR_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R4_DUR_DL.setObjectName(u"spinBox_R4_DUR_DL")
        self.spinBox_R4_DUR_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_DUR_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R4_DUR_DL, 4, 4, 1, 1)

        self.spinBox_R4_WE_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R4_WE_DL.setObjectName(u"spinBox_R4_WE_DL")
        self.spinBox_R4_WE_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_WE_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R4_WE_DL, 4, 5, 1, 1)

        self.spinBox_R4_STA_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R4_STA_DL.setObjectName(u"spinBox_R4_STA_DL")
        self.spinBox_R4_STA_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STA_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R4_STA_DL, 4, 6, 1, 1)

        self.spinBox_R4_STR_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R4_STR_DL.setObjectName(u"spinBox_R4_STR_DL")
        self.spinBox_R4_STR_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STR_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R4_STR_DL, 4, 7, 1, 1)

        self.spinBox_R4_BLK_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R4_BLK_DL.setObjectName(u"spinBox_R4_BLK_DL")
        self.spinBox_R4_BLK_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_BLK_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R4_BLK_DL, 4, 8, 1, 1)

        self.spinBox_R4_TKL_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R4_TKL_DL.setObjectName(u"spinBox_R4_TKL_DL")
        self.spinBox_R4_TKL_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TKL_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R4_TKL_DL, 4, 9, 1, 1)

        self.spinBox_R4_HAN_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R4_HAN_DL.setObjectName(u"spinBox_R4_HAN_DL")
        self.spinBox_R4_HAN_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_HAN_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R4_HAN_DL, 4, 10, 1, 1)

        self.spinBox_R4_GI_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R4_GI_DL.setObjectName(u"spinBox_R4_GI_DL")
        self.spinBox_R4_GI_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_GI_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R4_GI_DL, 4, 11, 1, 1)

        self.spinBox_R4_ELU_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R4_ELU_DL.setObjectName(u"spinBox_R4_ELU_DL")
        self.spinBox_R4_ELU_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ELU_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R4_ELU_DL, 4, 12, 1, 1)

        self.spinBox_R4_TEC_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R4_TEC_DL.setObjectName(u"spinBox_R4_TEC_DL")
        self.spinBox_R4_TEC_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TEC_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R4_TEC_DL, 4, 13, 1, 1)

        self.spinBox_R5_ATH_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R5_ATH_DL.setObjectName(u"spinBox_R5_ATH_DL")
        self.spinBox_R5_ATH_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ATH_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R5_ATH_DL, 5, 2, 1, 1)

        self.spinBox_R5_SPD_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R5_SPD_DL.setObjectName(u"spinBox_R5_SPD_DL")
        self.spinBox_R5_SPD_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_SPD_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R5_SPD_DL, 5, 3, 1, 1)

        self.spinBox_R5_DUR_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R5_DUR_DL.setObjectName(u"spinBox_R5_DUR_DL")
        self.spinBox_R5_DUR_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_DUR_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R5_DUR_DL, 5, 4, 1, 1)

        self.spinBox_R5_WE_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R5_WE_DL.setObjectName(u"spinBox_R5_WE_DL")
        self.spinBox_R5_WE_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_WE_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R5_WE_DL, 5, 5, 1, 1)

        self.spinBox_R5_STA_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R5_STA_DL.setObjectName(u"spinBox_R5_STA_DL")
        self.spinBox_R5_STA_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STA_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R5_STA_DL, 5, 6, 1, 1)

        self.spinBox_R5_STR_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R5_STR_DL.setObjectName(u"spinBox_R5_STR_DL")
        self.spinBox_R5_STR_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STR_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R5_STR_DL, 5, 7, 1, 1)

        self.spinBox_R5_BLK_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R5_BLK_DL.setObjectName(u"spinBox_R5_BLK_DL")
        self.spinBox_R5_BLK_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_BLK_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R5_BLK_DL, 5, 8, 1, 1)

        self.spinBox_R5_TKL_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R5_TKL_DL.setObjectName(u"spinBox_R5_TKL_DL")
        self.spinBox_R5_TKL_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TKL_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R5_TKL_DL, 5, 9, 1, 1)

        self.spinBox_R5_HAN_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R5_HAN_DL.setObjectName(u"spinBox_R5_HAN_DL")
        self.spinBox_R5_HAN_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_HAN_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R5_HAN_DL, 5, 10, 1, 1)

        self.spinBox_R5_GI_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R5_GI_DL.setObjectName(u"spinBox_R5_GI_DL")
        self.spinBox_R5_GI_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_GI_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R5_GI_DL, 5, 11, 1, 1)

        self.spinBox_R5_ELU_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R5_ELU_DL.setObjectName(u"spinBox_R5_ELU_DL")
        self.spinBox_R5_ELU_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ELU_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R5_ELU_DL, 5, 12, 1, 1)

        self.spinBox_R5_TEC_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R5_TEC_DL.setObjectName(u"spinBox_R5_TEC_DL")
        self.spinBox_R5_TEC_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TEC_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R5_TEC_DL, 5, 13, 1, 1)

        self.spinBox_R6_ATH_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R6_ATH_DL.setObjectName(u"spinBox_R6_ATH_DL")
        self.spinBox_R6_ATH_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ATH_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R6_ATH_DL, 6, 2, 1, 1)

        self.spinBox_R6_SPD_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R6_SPD_DL.setObjectName(u"spinBox_R6_SPD_DL")
        self.spinBox_R6_SPD_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_SPD_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R6_SPD_DL, 6, 3, 1, 1)

        self.spinBox_R6_DUR_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R6_DUR_DL.setObjectName(u"spinBox_R6_DUR_DL")
        self.spinBox_R6_DUR_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_DUR_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R6_DUR_DL, 6, 4, 1, 1)

        self.spinBox_R6_WE_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R6_WE_DL.setObjectName(u"spinBox_R6_WE_DL")
        self.spinBox_R6_WE_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_WE_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R6_WE_DL, 6, 5, 1, 1)

        self.spinBox_R6_STA_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R6_STA_DL.setObjectName(u"spinBox_R6_STA_DL")
        self.spinBox_R6_STA_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STA_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R6_STA_DL, 6, 6, 1, 1)

        self.spinBox_R6_STR_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R6_STR_DL.setObjectName(u"spinBox_R6_STR_DL")
        self.spinBox_R6_STR_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STR_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R6_STR_DL, 6, 7, 1, 1)

        self.spinBox_R6_BLK_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R6_BLK_DL.setObjectName(u"spinBox_R6_BLK_DL")
        self.spinBox_R6_BLK_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_BLK_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R6_BLK_DL, 6, 8, 1, 1)

        self.spinBox_R6_TKL_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R6_TKL_DL.setObjectName(u"spinBox_R6_TKL_DL")
        self.spinBox_R6_TKL_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TKL_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R6_TKL_DL, 6, 9, 1, 1)

        self.spinBox_R6_HAN_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R6_HAN_DL.setObjectName(u"spinBox_R6_HAN_DL")
        self.spinBox_R6_HAN_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_HAN_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R6_HAN_DL, 6, 10, 1, 1)

        self.spinBox_R6_GI_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R6_GI_DL.setObjectName(u"spinBox_R6_GI_DL")
        self.spinBox_R6_GI_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_GI_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R6_GI_DL, 6, 11, 1, 1)

        self.spinBox_R6_ELU_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R6_ELU_DL.setObjectName(u"spinBox_R6_ELU_DL")
        self.spinBox_R6_ELU_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ELU_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R6_ELU_DL, 6, 12, 1, 1)

        self.spinBox_R6_TEC_DL = QSpinBox(self.gridLayoutWidget_6)
        self.spinBox_R6_TEC_DL.setObjectName(u"spinBox_R6_TEC_DL")
        self.spinBox_R6_TEC_DL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TEC_DL.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_R6_TEC_DL, 6, 13, 1, 1)

        self.lineEdit_R1_DL = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_R1_DL.setObjectName(u"lineEdit_R1_DL")
        self.lineEdit_R1_DL.setFont(font2)
        self.lineEdit_R1_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_R1_DL, 1, 1, 1, 1)

        self.lineEdit_R2_DL = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_R2_DL.setObjectName(u"lineEdit_R2_DL")
        self.lineEdit_R2_DL.setFont(font2)
        self.lineEdit_R2_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_R2_DL, 2, 1, 1, 1)

        self.lineEdit_R3_DL = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_R3_DL.setObjectName(u"lineEdit_R3_DL")
        self.lineEdit_R3_DL.setFont(font2)
        self.lineEdit_R3_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_R3_DL, 3, 1, 1, 1)

        self.lineEdit_R4_DL = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_R4_DL.setObjectName(u"lineEdit_R4_DL")
        self.lineEdit_R4_DL.setFont(font2)
        self.lineEdit_R4_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_R4_DL, 4, 1, 1, 1)

        self.lineEdit_R5_DL = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_R5_DL.setObjectName(u"lineEdit_R5_DL")
        self.lineEdit_R5_DL.setFont(font2)
        self.lineEdit_R5_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_R5_DL, 5, 1, 1, 1)

        self.lineEdit_R6_DL = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_R6_DL.setObjectName(u"lineEdit_R6_DL")
        self.lineEdit_R6_DL.setFont(font2)
        self.lineEdit_R6_DL.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lineEdit_R6_DL, 6, 1, 1, 1)

        self.lcdNumber_R1_DL = QLCDNumber(self.gridLayoutWidget_6)
        self.lcdNumber_R1_DL.setObjectName(u"lcdNumber_R1_DL")
        self.lcdNumber_R1_DL.setDigitCount(3)
        self.lcdNumber_R1_DL.setProperty("intValue", 0)

        self.gridLayout_6.addWidget(self.lcdNumber_R1_DL, 1, 14, 1, 1)

        self.lcdNumber_R2_DL = QLCDNumber(self.gridLayoutWidget_6)
        self.lcdNumber_R2_DL.setObjectName(u"lcdNumber_R2_DL")
        self.lcdNumber_R2_DL.setDigitCount(3)
        self.lcdNumber_R2_DL.setProperty("intValue", 0)

        self.gridLayout_6.addWidget(self.lcdNumber_R2_DL, 2, 14, 1, 1)

        self.lcdNumber_R3_DL = QLCDNumber(self.gridLayoutWidget_6)
        self.lcdNumber_R3_DL.setObjectName(u"lcdNumber_R3_DL")
        self.lcdNumber_R3_DL.setDigitCount(3)
        self.lcdNumber_R3_DL.setProperty("intValue", 0)

        self.gridLayout_6.addWidget(self.lcdNumber_R3_DL, 3, 14, 1, 1)

        self.lcdNumber_R4_DL = QLCDNumber(self.gridLayoutWidget_6)
        self.lcdNumber_R4_DL.setObjectName(u"lcdNumber_R4_DL")
        self.lcdNumber_R4_DL.setDigitCount(3)
        self.lcdNumber_R4_DL.setProperty("intValue", 0)

        self.gridLayout_6.addWidget(self.lcdNumber_R4_DL, 4, 14, 1, 1)

        self.lcdNumber_R5_DL = QLCDNumber(self.gridLayoutWidget_6)
        self.lcdNumber_R5_DL.setObjectName(u"lcdNumber_R5_DL")
        self.lcdNumber_R5_DL.setDigitCount(3)
        self.lcdNumber_R5_DL.setProperty("intValue", 0)

        self.gridLayout_6.addWidget(self.lcdNumber_R5_DL, 5, 14, 1, 1)

        self.lcdNumber_R6_DL = QLCDNumber(self.gridLayoutWidget_6)
        self.lcdNumber_R6_DL.setObjectName(u"lcdNumber_R6_DL")
        self.lcdNumber_R6_DL.setDigitCount(3)
        self.lcdNumber_R6_DL.setProperty("intValue", 0)

        self.gridLayout_6.addWidget(self.lcdNumber_R6_DL, 6, 14, 1, 1)

        self.tabWidgetRoleRatings.addTab(self.DL, "")
        self.LB = QWidget()
        self.LB.setObjectName(u"LB")
        self.gridLayoutWidget_7 = QWidget(self.LB)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(0, 10, 1215, 261))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_ATH_Header_LB = QLabel(self.gridLayoutWidget_7)
        self.label_ATH_Header_LB.setObjectName(u"label_ATH_Header_LB")
        self.label_ATH_Header_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_ATH_Header_LB, 0, 2, 1, 1)

        self.spinBox_R2_TKL_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R2_TKL_LB.setObjectName(u"spinBox_R2_TKL_LB")
        self.spinBox_R2_TKL_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TKL_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R2_TKL_LB, 2, 9, 1, 1)

        self.spinBox_R3_DUR_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R3_DUR_LB.setObjectName(u"spinBox_R3_DUR_LB")
        self.spinBox_R3_DUR_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_DUR_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R3_DUR_LB, 3, 4, 1, 1)

        self.spinBox_R3_STR_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R3_STR_LB.setObjectName(u"spinBox_R3_STR_LB")
        self.spinBox_R3_STR_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STR_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R3_STR_LB, 3, 7, 1, 1)

        self.spinBox_R2_TEC_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R2_TEC_LB.setObjectName(u"spinBox_R2_TEC_LB")
        self.spinBox_R2_TEC_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TEC_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R2_TEC_LB, 2, 13, 1, 1)

        self.spinBox_R2_WE_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R2_WE_LB.setObjectName(u"spinBox_R2_WE_LB")
        self.spinBox_R2_WE_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_WE_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R2_WE_LB, 2, 5, 1, 1)

        self.spinBox_R1_SPD_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R1_SPD_LB.setObjectName(u"spinBox_R1_SPD_LB")
        self.spinBox_R1_SPD_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_SPD_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R1_SPD_LB, 1, 3, 1, 1)

        self.label_TEC_Header_LB = QLabel(self.gridLayoutWidget_7)
        self.label_TEC_Header_LB.setObjectName(u"label_TEC_Header_LB")
        self.label_TEC_Header_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_TEC_Header_LB, 0, 13, 1, 1)

        self.spinBox_R1_BLK_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R1_BLK_LB.setObjectName(u"spinBox_R1_BLK_LB")
        self.spinBox_R1_BLK_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_BLK_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R1_BLK_LB, 1, 8, 1, 1)

        self.spinBox_R1_STA_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R1_STA_LB.setObjectName(u"spinBox_R1_STA_LB")
        self.spinBox_R1_STA_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STA_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R1_STA_LB, 1, 6, 1, 1)

        self.label_WE_Header_LB = QLabel(self.gridLayoutWidget_7)
        self.label_WE_Header_LB.setObjectName(u"label_WE_Header_LB")
        self.label_WE_Header_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_WE_Header_LB, 0, 5, 1, 1)

        self.label_TKL_Header_LB = QLabel(self.gridLayoutWidget_7)
        self.label_TKL_Header_LB.setObjectName(u"label_TKL_Header_LB")
        self.label_TKL_Header_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_TKL_Header_LB, 0, 9, 1, 1)

        self.label_STR_Header_LB = QLabel(self.gridLayoutWidget_7)
        self.label_STR_Header_LB.setObjectName(u"label_STR_Header_LB")
        self.label_STR_Header_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_STR_Header_LB, 0, 7, 1, 1)

        self.spinBox_R1_WE_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R1_WE_LB.setObjectName(u"spinBox_R1_WE_LB")
        self.spinBox_R1_WE_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_WE_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R1_WE_LB, 1, 5, 1, 1)

        self.spinBox_R2_SPD_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R2_SPD_LB.setObjectName(u"spinBox_R2_SPD_LB")
        self.spinBox_R2_SPD_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_SPD_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R2_SPD_LB, 2, 3, 1, 1)

        self.label_R1_LB = QLabel(self.gridLayoutWidget_7)
        self.label_R1_LB.setObjectName(u"label_R1_LB")
        self.label_R1_LB.setFont(font1)
        self.label_R1_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_R1_LB, 1, 0, 1, 1)

        self.label_RoleHeader_LB = QLabel(self.gridLayoutWidget_7)
        self.label_RoleHeader_LB.setObjectName(u"label_RoleHeader_LB")
        self.label_RoleHeader_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_RoleHeader_LB, 0, 0, 1, 1)

        self.label_Total_Header_LB = QLabel(self.gridLayoutWidget_7)
        self.label_Total_Header_LB.setObjectName(u"label_Total_Header_LB")

        self.gridLayout_7.addWidget(self.label_Total_Header_LB, 0, 14, 1, 1)

        self.spinBox_R3_STA_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R3_STA_LB.setObjectName(u"spinBox_R3_STA_LB")
        self.spinBox_R3_STA_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STA_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R3_STA_LB, 3, 6, 1, 1)

        self.label_R5_LB = QLabel(self.gridLayoutWidget_7)
        self.label_R5_LB.setObjectName(u"label_R5_LB")
        self.label_R5_LB.setFont(font1)
        self.label_R5_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_R5_LB, 5, 0, 1, 1)

        self.label_BLK_Header_LB = QLabel(self.gridLayoutWidget_7)
        self.label_BLK_Header_LB.setObjectName(u"label_BLK_Header_LB")
        self.label_BLK_Header_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_BLK_Header_LB, 0, 8, 1, 1)

        self.label_ELU_Header_LB = QLabel(self.gridLayoutWidget_7)
        self.label_ELU_Header_LB.setObjectName(u"label_ELU_Header_LB")
        self.label_ELU_Header_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_ELU_Header_LB, 0, 12, 1, 1)

        self.spinBox_R2_BLK_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R2_BLK_LB.setObjectName(u"spinBox_R2_BLK_LB")
        self.spinBox_R2_BLK_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_BLK_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R2_BLK_LB, 2, 8, 1, 1)

        self.label_LabelHeader_LB = QLabel(self.gridLayoutWidget_7)
        self.label_LabelHeader_LB.setObjectName(u"label_LabelHeader_LB")
        self.label_LabelHeader_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_LabelHeader_LB, 0, 1, 1, 1)

        self.spinBox_R2_HAN_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R2_HAN_LB.setObjectName(u"spinBox_R2_HAN_LB")
        self.spinBox_R2_HAN_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_HAN_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R2_HAN_LB, 2, 10, 1, 1)

        self.label_R2_LB = QLabel(self.gridLayoutWidget_7)
        self.label_R2_LB.setObjectName(u"label_R2_LB")
        self.label_R2_LB.setFont(font1)
        self.label_R2_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_R2_LB, 2, 0, 1, 1)

        self.spinBox_R1_GI_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R1_GI_LB.setObjectName(u"spinBox_R1_GI_LB")
        self.spinBox_R1_GI_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_GI_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R1_GI_LB, 1, 11, 1, 1)

        self.label_DUR_Header_LB = QLabel(self.gridLayoutWidget_7)
        self.label_DUR_Header_LB.setObjectName(u"label_DUR_Header_LB")
        self.label_DUR_Header_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_DUR_Header_LB, 0, 4, 1, 1)

        self.spinBox_R1_HAN_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R1_HAN_LB.setObjectName(u"spinBox_R1_HAN_LB")
        self.spinBox_R1_HAN_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_HAN_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R1_HAN_LB, 1, 10, 1, 1)

        self.label_R3_LB = QLabel(self.gridLayoutWidget_7)
        self.label_R3_LB.setObjectName(u"label_R3_LB")
        self.label_R3_LB.setFont(font1)
        self.label_R3_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_R3_LB, 3, 0, 1, 1)

        self.label_GI_Header_LB = QLabel(self.gridLayoutWidget_7)
        self.label_GI_Header_LB.setObjectName(u"label_GI_Header_LB")
        self.label_GI_Header_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_GI_Header_LB, 0, 11, 1, 1)

        self.spinBox_R1_TEC_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R1_TEC_LB.setObjectName(u"spinBox_R1_TEC_LB")
        self.spinBox_R1_TEC_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TEC_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R1_TEC_LB, 1, 13, 1, 1)

        self.spinBox_R1_ATH_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R1_ATH_LB.setObjectName(u"spinBox_R1_ATH_LB")
        self.spinBox_R1_ATH_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ATH_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R1_ATH_LB, 1, 2, 1, 1)

        self.spinBox_R1_DUR_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R1_DUR_LB.setObjectName(u"spinBox_R1_DUR_LB")
        self.spinBox_R1_DUR_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_DUR_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R1_DUR_LB, 1, 4, 1, 1)

        self.spinBox_R2_ELU_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R2_ELU_LB.setObjectName(u"spinBox_R2_ELU_LB")
        self.spinBox_R2_ELU_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ELU_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R2_ELU_LB, 2, 12, 1, 1)

        self.spinBox_R2_ATH_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R2_ATH_LB.setObjectName(u"spinBox_R2_ATH_LB")
        self.spinBox_R2_ATH_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ATH_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R2_ATH_LB, 2, 2, 1, 1)

        self.spinBox_R2_STR_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R2_STR_LB.setObjectName(u"spinBox_R2_STR_LB")
        self.spinBox_R2_STR_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STR_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R2_STR_LB, 2, 7, 1, 1)

        self.spinBox_R3_ATH_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R3_ATH_LB.setObjectName(u"spinBox_R3_ATH_LB")
        self.spinBox_R3_ATH_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ATH_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R3_ATH_LB, 3, 2, 1, 1)

        self.spinBox_R1_ELU_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R1_ELU_LB.setObjectName(u"spinBox_R1_ELU_LB")
        self.spinBox_R1_ELU_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ELU_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R1_ELU_LB, 1, 12, 1, 1)

        self.label_STA_Header_LB = QLabel(self.gridLayoutWidget_7)
        self.label_STA_Header_LB.setObjectName(u"label_STA_Header_LB")
        self.label_STA_Header_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_STA_Header_LB, 0, 6, 1, 1)

        self.spinBox_R1_STR_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R1_STR_LB.setObjectName(u"spinBox_R1_STR_LB")
        self.spinBox_R1_STR_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STR_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R1_STR_LB, 1, 7, 1, 1)

        self.label_SPD_Header_LB = QLabel(self.gridLayoutWidget_7)
        self.label_SPD_Header_LB.setObjectName(u"label_SPD_Header_LB")
        self.label_SPD_Header_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_SPD_Header_LB, 0, 3, 1, 1)

        self.spinBox_R2_DUR_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R2_DUR_LB.setObjectName(u"spinBox_R2_DUR_LB")
        self.spinBox_R2_DUR_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_DUR_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R2_DUR_LB, 2, 4, 1, 1)

        self.label_HAN_Header_LB = QLabel(self.gridLayoutWidget_7)
        self.label_HAN_Header_LB.setObjectName(u"label_HAN_Header_LB")
        self.label_HAN_Header_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_HAN_Header_LB, 0, 10, 1, 1)

        self.label_R4_LB = QLabel(self.gridLayoutWidget_7)
        self.label_R4_LB.setObjectName(u"label_R4_LB")
        self.label_R4_LB.setFont(font1)
        self.label_R4_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_R4_LB, 4, 0, 1, 1)

        self.spinBox_R1_TKL_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R1_TKL_LB.setObjectName(u"spinBox_R1_TKL_LB")
        self.spinBox_R1_TKL_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TKL_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R1_TKL_LB, 1, 9, 1, 1)

        self.spinBox_R2_GI_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R2_GI_LB.setObjectName(u"spinBox_R2_GI_LB")
        self.spinBox_R2_GI_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_GI_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R2_GI_LB, 2, 11, 1, 1)

        self.spinBox_R3_WE_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R3_WE_LB.setObjectName(u"spinBox_R3_WE_LB")
        self.spinBox_R3_WE_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_WE_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R3_WE_LB, 3, 5, 1, 1)

        self.spinBox_R3_SPD_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R3_SPD_LB.setObjectName(u"spinBox_R3_SPD_LB")
        self.spinBox_R3_SPD_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_SPD_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R3_SPD_LB, 3, 3, 1, 1)

        self.label_R6_LB = QLabel(self.gridLayoutWidget_7)
        self.label_R6_LB.setObjectName(u"label_R6_LB")
        self.label_R6_LB.setFont(font1)
        self.label_R6_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_R6_LB, 6, 0, 1, 1)

        self.spinBox_R2_STA_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R2_STA_LB.setObjectName(u"spinBox_R2_STA_LB")
        self.spinBox_R2_STA_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STA_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R2_STA_LB, 2, 6, 1, 1)

        self.spinBox_R3_BLK_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R3_BLK_LB.setObjectName(u"spinBox_R3_BLK_LB")
        self.spinBox_R3_BLK_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_BLK_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R3_BLK_LB, 3, 8, 1, 1)

        self.spinBox_R3_TKL_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R3_TKL_LB.setObjectName(u"spinBox_R3_TKL_LB")
        self.spinBox_R3_TKL_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TKL_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R3_TKL_LB, 3, 9, 1, 1)

        self.spinBox_R3_HAN_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R3_HAN_LB.setObjectName(u"spinBox_R3_HAN_LB")
        self.spinBox_R3_HAN_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_HAN_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R3_HAN_LB, 3, 10, 1, 1)

        self.spinBox_R3_GI_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R3_GI_LB.setObjectName(u"spinBox_R3_GI_LB")
        self.spinBox_R3_GI_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_GI_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R3_GI_LB, 3, 11, 1, 1)

        self.spinBox_R3_ELU_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R3_ELU_LB.setObjectName(u"spinBox_R3_ELU_LB")
        self.spinBox_R3_ELU_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ELU_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R3_ELU_LB, 3, 12, 1, 1)

        self.spinBox_R3_TEC_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R3_TEC_LB.setObjectName(u"spinBox_R3_TEC_LB")
        self.spinBox_R3_TEC_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TEC_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R3_TEC_LB, 3, 13, 1, 1)

        self.spinBox_R4_ATH_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R4_ATH_LB.setObjectName(u"spinBox_R4_ATH_LB")
        self.spinBox_R4_ATH_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ATH_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R4_ATH_LB, 4, 2, 1, 1)

        self.spinBox_R4_SPD_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R4_SPD_LB.setObjectName(u"spinBox_R4_SPD_LB")
        self.spinBox_R4_SPD_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_SPD_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R4_SPD_LB, 4, 3, 1, 1)

        self.spinBox_R4_DUR_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R4_DUR_LB.setObjectName(u"spinBox_R4_DUR_LB")
        self.spinBox_R4_DUR_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_DUR_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R4_DUR_LB, 4, 4, 1, 1)

        self.spinBox_R4_WE_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R4_WE_LB.setObjectName(u"spinBox_R4_WE_LB")
        self.spinBox_R4_WE_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_WE_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R4_WE_LB, 4, 5, 1, 1)

        self.spinBox_R4_STA_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R4_STA_LB.setObjectName(u"spinBox_R4_STA_LB")
        self.spinBox_R4_STA_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STA_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R4_STA_LB, 4, 6, 1, 1)

        self.spinBox_R4_STR_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R4_STR_LB.setObjectName(u"spinBox_R4_STR_LB")
        self.spinBox_R4_STR_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STR_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R4_STR_LB, 4, 7, 1, 1)

        self.spinBox_R4_BLK_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R4_BLK_LB.setObjectName(u"spinBox_R4_BLK_LB")
        self.spinBox_R4_BLK_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_BLK_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R4_BLK_LB, 4, 8, 1, 1)

        self.spinBox_R4_TKL_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R4_TKL_LB.setObjectName(u"spinBox_R4_TKL_LB")
        self.spinBox_R4_TKL_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TKL_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R4_TKL_LB, 4, 9, 1, 1)

        self.spinBox_R4_HAN_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R4_HAN_LB.setObjectName(u"spinBox_R4_HAN_LB")
        self.spinBox_R4_HAN_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_HAN_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R4_HAN_LB, 4, 10, 1, 1)

        self.spinBox_R4_GI_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R4_GI_LB.setObjectName(u"spinBox_R4_GI_LB")
        self.spinBox_R4_GI_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_GI_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R4_GI_LB, 4, 11, 1, 1)

        self.spinBox_R4_ELU_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R4_ELU_LB.setObjectName(u"spinBox_R4_ELU_LB")
        self.spinBox_R4_ELU_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ELU_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R4_ELU_LB, 4, 12, 1, 1)

        self.spinBox_R4_TEC_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R4_TEC_LB.setObjectName(u"spinBox_R4_TEC_LB")
        self.spinBox_R4_TEC_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TEC_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R4_TEC_LB, 4, 13, 1, 1)

        self.spinBox_R5_ATH_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R5_ATH_LB.setObjectName(u"spinBox_R5_ATH_LB")
        self.spinBox_R5_ATH_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ATH_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R5_ATH_LB, 5, 2, 1, 1)

        self.spinBox_R5_SPD_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R5_SPD_LB.setObjectName(u"spinBox_R5_SPD_LB")
        self.spinBox_R5_SPD_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_SPD_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R5_SPD_LB, 5, 3, 1, 1)

        self.spinBox_R5_DUR_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R5_DUR_LB.setObjectName(u"spinBox_R5_DUR_LB")
        self.spinBox_R5_DUR_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_DUR_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R5_DUR_LB, 5, 4, 1, 1)

        self.spinBox_R5_WE_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R5_WE_LB.setObjectName(u"spinBox_R5_WE_LB")
        self.spinBox_R5_WE_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_WE_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R5_WE_LB, 5, 5, 1, 1)

        self.spinBox_R5_STA_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R5_STA_LB.setObjectName(u"spinBox_R5_STA_LB")
        self.spinBox_R5_STA_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STA_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R5_STA_LB, 5, 6, 1, 1)

        self.spinBox_R5_STR_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R5_STR_LB.setObjectName(u"spinBox_R5_STR_LB")
        self.spinBox_R5_STR_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STR_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R5_STR_LB, 5, 7, 1, 1)

        self.spinBox_R5_BLK_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R5_BLK_LB.setObjectName(u"spinBox_R5_BLK_LB")
        self.spinBox_R5_BLK_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_BLK_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R5_BLK_LB, 5, 8, 1, 1)

        self.spinBox_R5_TKL_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R5_TKL_LB.setObjectName(u"spinBox_R5_TKL_LB")
        self.spinBox_R5_TKL_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TKL_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R5_TKL_LB, 5, 9, 1, 1)

        self.spinBox_R5_HAN_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R5_HAN_LB.setObjectName(u"spinBox_R5_HAN_LB")
        self.spinBox_R5_HAN_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_HAN_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R5_HAN_LB, 5, 10, 1, 1)

        self.spinBox_R5_GI_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R5_GI_LB.setObjectName(u"spinBox_R5_GI_LB")
        self.spinBox_R5_GI_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_GI_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R5_GI_LB, 5, 11, 1, 1)

        self.spinBox_R5_ELU_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R5_ELU_LB.setObjectName(u"spinBox_R5_ELU_LB")
        self.spinBox_R5_ELU_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ELU_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R5_ELU_LB, 5, 12, 1, 1)

        self.spinBox_R5_TEC_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R5_TEC_LB.setObjectName(u"spinBox_R5_TEC_LB")
        self.spinBox_R5_TEC_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TEC_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R5_TEC_LB, 5, 13, 1, 1)

        self.spinBox_R6_ATH_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R6_ATH_LB.setObjectName(u"spinBox_R6_ATH_LB")
        self.spinBox_R6_ATH_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ATH_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R6_ATH_LB, 6, 2, 1, 1)

        self.spinBox_R6_SPD_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R6_SPD_LB.setObjectName(u"spinBox_R6_SPD_LB")
        self.spinBox_R6_SPD_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_SPD_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R6_SPD_LB, 6, 3, 1, 1)

        self.spinBox_R6_DUR_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R6_DUR_LB.setObjectName(u"spinBox_R6_DUR_LB")
        self.spinBox_R6_DUR_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_DUR_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R6_DUR_LB, 6, 4, 1, 1)

        self.spinBox_R6_WE_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R6_WE_LB.setObjectName(u"spinBox_R6_WE_LB")
        self.spinBox_R6_WE_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_WE_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R6_WE_LB, 6, 5, 1, 1)

        self.spinBox_R6_STA_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R6_STA_LB.setObjectName(u"spinBox_R6_STA_LB")
        self.spinBox_R6_STA_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STA_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R6_STA_LB, 6, 6, 1, 1)

        self.spinBox_R6_STR_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R6_STR_LB.setObjectName(u"spinBox_R6_STR_LB")
        self.spinBox_R6_STR_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STR_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R6_STR_LB, 6, 7, 1, 1)

        self.spinBox_R6_BLK_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R6_BLK_LB.setObjectName(u"spinBox_R6_BLK_LB")
        self.spinBox_R6_BLK_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_BLK_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R6_BLK_LB, 6, 8, 1, 1)

        self.spinBox_R6_TKL_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R6_TKL_LB.setObjectName(u"spinBox_R6_TKL_LB")
        self.spinBox_R6_TKL_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TKL_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R6_TKL_LB, 6, 9, 1, 1)

        self.spinBox_R6_HAN_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R6_HAN_LB.setObjectName(u"spinBox_R6_HAN_LB")
        self.spinBox_R6_HAN_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_HAN_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R6_HAN_LB, 6, 10, 1, 1)

        self.spinBox_R6_GI_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R6_GI_LB.setObjectName(u"spinBox_R6_GI_LB")
        self.spinBox_R6_GI_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_GI_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R6_GI_LB, 6, 11, 1, 1)

        self.spinBox_R6_ELU_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R6_ELU_LB.setObjectName(u"spinBox_R6_ELU_LB")
        self.spinBox_R6_ELU_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ELU_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R6_ELU_LB, 6, 12, 1, 1)

        self.spinBox_R6_TEC_LB = QSpinBox(self.gridLayoutWidget_7)
        self.spinBox_R6_TEC_LB.setObjectName(u"spinBox_R6_TEC_LB")
        self.spinBox_R6_TEC_LB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TEC_LB.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_R6_TEC_LB, 6, 13, 1, 1)

        self.lineEdit_R1_LB = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_R1_LB.setObjectName(u"lineEdit_R1_LB")
        self.lineEdit_R1_LB.setFont(font2)
        self.lineEdit_R1_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_R1_LB, 1, 1, 1, 1)

        self.lineEdit_R2_LB = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_R2_LB.setObjectName(u"lineEdit_R2_LB")
        self.lineEdit_R2_LB.setFont(font2)
        self.lineEdit_R2_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_R2_LB, 2, 1, 1, 1)

        self.lineEdit_R3_LB = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_R3_LB.setObjectName(u"lineEdit_R3_LB")
        self.lineEdit_R3_LB.setFont(font2)
        self.lineEdit_R3_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_R3_LB, 3, 1, 1, 1)

        self.lineEdit_R4_LB = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_R4_LB.setObjectName(u"lineEdit_R4_LB")
        self.lineEdit_R4_LB.setFont(font2)
        self.lineEdit_R4_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_R4_LB, 4, 1, 1, 1)

        self.lineEdit_R5_LB = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_R5_LB.setObjectName(u"lineEdit_R5_LB")
        self.lineEdit_R5_LB.setFont(font2)
        self.lineEdit_R5_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_R5_LB, 5, 1, 1, 1)

        self.lineEdit_R6_LB = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_R6_LB.setObjectName(u"lineEdit_R6_LB")
        self.lineEdit_R6_LB.setFont(font2)
        self.lineEdit_R6_LB.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_R6_LB, 6, 1, 1, 1)

        self.lcdNumber_R1_LB = QLCDNumber(self.gridLayoutWidget_7)
        self.lcdNumber_R1_LB.setObjectName(u"lcdNumber_R1_LB")
        self.lcdNumber_R1_LB.setDigitCount(3)
        self.lcdNumber_R1_LB.setProperty("intValue", 0)

        self.gridLayout_7.addWidget(self.lcdNumber_R1_LB, 1, 14, 1, 1)

        self.lcdNumber_R2_LB = QLCDNumber(self.gridLayoutWidget_7)
        self.lcdNumber_R2_LB.setObjectName(u"lcdNumber_R2_LB")
        self.lcdNumber_R2_LB.setDigitCount(3)
        self.lcdNumber_R2_LB.setProperty("intValue", 0)

        self.gridLayout_7.addWidget(self.lcdNumber_R2_LB, 2, 14, 1, 1)

        self.lcdNumber_R3_LB = QLCDNumber(self.gridLayoutWidget_7)
        self.lcdNumber_R3_LB.setObjectName(u"lcdNumber_R3_LB")
        self.lcdNumber_R3_LB.setDigitCount(3)
        self.lcdNumber_R3_LB.setProperty("intValue", 0)

        self.gridLayout_7.addWidget(self.lcdNumber_R3_LB, 3, 14, 1, 1)

        self.lcdNumber_R4_LB = QLCDNumber(self.gridLayoutWidget_7)
        self.lcdNumber_R4_LB.setObjectName(u"lcdNumber_R4_LB")
        self.lcdNumber_R4_LB.setDigitCount(3)
        self.lcdNumber_R4_LB.setProperty("intValue", 0)

        self.gridLayout_7.addWidget(self.lcdNumber_R4_LB, 4, 14, 1, 1)

        self.lcdNumber_R5_LB = QLCDNumber(self.gridLayoutWidget_7)
        self.lcdNumber_R5_LB.setObjectName(u"lcdNumber_R5_LB")
        self.lcdNumber_R5_LB.setDigitCount(3)
        self.lcdNumber_R5_LB.setProperty("intValue", 0)

        self.gridLayout_7.addWidget(self.lcdNumber_R5_LB, 5, 14, 1, 1)

        self.lcdNumber_R6_LB = QLCDNumber(self.gridLayoutWidget_7)
        self.lcdNumber_R6_LB.setObjectName(u"lcdNumber_R6_LB")
        self.lcdNumber_R6_LB.setDigitCount(3)
        self.lcdNumber_R6_LB.setProperty("intValue", 0)

        self.gridLayout_7.addWidget(self.lcdNumber_R6_LB, 6, 14, 1, 1)

        self.tabWidgetRoleRatings.addTab(self.LB, "")
        self.DB = QWidget()
        self.DB.setObjectName(u"DB")
        self.gridLayoutWidget_8 = QWidget(self.DB)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(0, 10, 1215, 261))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_ATH_Header_DB = QLabel(self.gridLayoutWidget_8)
        self.label_ATH_Header_DB.setObjectName(u"label_ATH_Header_DB")
        self.label_ATH_Header_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_ATH_Header_DB, 0, 2, 1, 1)

        self.spinBox_R2_TKL_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R2_TKL_DB.setObjectName(u"spinBox_R2_TKL_DB")
        self.spinBox_R2_TKL_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TKL_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R2_TKL_DB, 2, 9, 1, 1)

        self.spinBox_R3_DUR_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R3_DUR_DB.setObjectName(u"spinBox_R3_DUR_DB")
        self.spinBox_R3_DUR_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_DUR_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R3_DUR_DB, 3, 4, 1, 1)

        self.spinBox_R3_STR_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R3_STR_DB.setObjectName(u"spinBox_R3_STR_DB")
        self.spinBox_R3_STR_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STR_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R3_STR_DB, 3, 7, 1, 1)

        self.spinBox_R2_TEC_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R2_TEC_DB.setObjectName(u"spinBox_R2_TEC_DB")
        self.spinBox_R2_TEC_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TEC_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R2_TEC_DB, 2, 13, 1, 1)

        self.spinBox_R2_WE_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R2_WE_DB.setObjectName(u"spinBox_R2_WE_DB")
        self.spinBox_R2_WE_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_WE_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R2_WE_DB, 2, 5, 1, 1)

        self.spinBox_R1_SPD_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R1_SPD_DB.setObjectName(u"spinBox_R1_SPD_DB")
        self.spinBox_R1_SPD_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_SPD_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R1_SPD_DB, 1, 3, 1, 1)

        self.label_TEC_Header_DB = QLabel(self.gridLayoutWidget_8)
        self.label_TEC_Header_DB.setObjectName(u"label_TEC_Header_DB")
        self.label_TEC_Header_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_TEC_Header_DB, 0, 13, 1, 1)

        self.spinBox_R1_BLK_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R1_BLK_DB.setObjectName(u"spinBox_R1_BLK_DB")
        self.spinBox_R1_BLK_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_BLK_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R1_BLK_DB, 1, 8, 1, 1)

        self.spinBox_R1_STA_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R1_STA_DB.setObjectName(u"spinBox_R1_STA_DB")
        self.spinBox_R1_STA_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STA_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R1_STA_DB, 1, 6, 1, 1)

        self.label_WE_Header_DB = QLabel(self.gridLayoutWidget_8)
        self.label_WE_Header_DB.setObjectName(u"label_WE_Header_DB")
        self.label_WE_Header_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_WE_Header_DB, 0, 5, 1, 1)

        self.label_TKL_Header_DB = QLabel(self.gridLayoutWidget_8)
        self.label_TKL_Header_DB.setObjectName(u"label_TKL_Header_DB")
        self.label_TKL_Header_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_TKL_Header_DB, 0, 9, 1, 1)

        self.label_STR_Header_DB = QLabel(self.gridLayoutWidget_8)
        self.label_STR_Header_DB.setObjectName(u"label_STR_Header_DB")
        self.label_STR_Header_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_STR_Header_DB, 0, 7, 1, 1)

        self.spinBox_R1_WE_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R1_WE_DB.setObjectName(u"spinBox_R1_WE_DB")
        self.spinBox_R1_WE_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_WE_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R1_WE_DB, 1, 5, 1, 1)

        self.spinBox_R2_SPD_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R2_SPD_DB.setObjectName(u"spinBox_R2_SPD_DB")
        self.spinBox_R2_SPD_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_SPD_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R2_SPD_DB, 2, 3, 1, 1)

        self.label_R1_DB = QLabel(self.gridLayoutWidget_8)
        self.label_R1_DB.setObjectName(u"label_R1_DB")
        self.label_R1_DB.setFont(font1)
        self.label_R1_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_R1_DB, 1, 0, 1, 1)

        self.label_RoleHeader_DB = QLabel(self.gridLayoutWidget_8)
        self.label_RoleHeader_DB.setObjectName(u"label_RoleHeader_DB")
        self.label_RoleHeader_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_RoleHeader_DB, 0, 0, 1, 1)

        self.label_Total_Header_DB = QLabel(self.gridLayoutWidget_8)
        self.label_Total_Header_DB.setObjectName(u"label_Total_Header_DB")

        self.gridLayout_8.addWidget(self.label_Total_Header_DB, 0, 14, 1, 1)

        self.spinBox_R3_STA_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R3_STA_DB.setObjectName(u"spinBox_R3_STA_DB")
        self.spinBox_R3_STA_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STA_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R3_STA_DB, 3, 6, 1, 1)

        self.label_R5_DB = QLabel(self.gridLayoutWidget_8)
        self.label_R5_DB.setObjectName(u"label_R5_DB")
        self.label_R5_DB.setFont(font1)
        self.label_R5_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_R5_DB, 5, 0, 1, 1)

        self.label_BLK_Header_DB = QLabel(self.gridLayoutWidget_8)
        self.label_BLK_Header_DB.setObjectName(u"label_BLK_Header_DB")
        self.label_BLK_Header_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_BLK_Header_DB, 0, 8, 1, 1)

        self.label_ELU_Header_DB = QLabel(self.gridLayoutWidget_8)
        self.label_ELU_Header_DB.setObjectName(u"label_ELU_Header_DB")
        self.label_ELU_Header_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_ELU_Header_DB, 0, 12, 1, 1)

        self.spinBox_R2_BLK_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R2_BLK_DB.setObjectName(u"spinBox_R2_BLK_DB")
        self.spinBox_R2_BLK_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_BLK_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R2_BLK_DB, 2, 8, 1, 1)

        self.label_LabelHeader_DB = QLabel(self.gridLayoutWidget_8)
        self.label_LabelHeader_DB.setObjectName(u"label_LabelHeader_DB")
        self.label_LabelHeader_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_LabelHeader_DB, 0, 1, 1, 1)

        self.spinBox_R2_HAN_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R2_HAN_DB.setObjectName(u"spinBox_R2_HAN_DB")
        self.spinBox_R2_HAN_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_HAN_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R2_HAN_DB, 2, 10, 1, 1)

        self.label_R2_DB = QLabel(self.gridLayoutWidget_8)
        self.label_R2_DB.setObjectName(u"label_R2_DB")
        self.label_R2_DB.setFont(font1)
        self.label_R2_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_R2_DB, 2, 0, 1, 1)

        self.spinBox_R1_GI_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R1_GI_DB.setObjectName(u"spinBox_R1_GI_DB")
        self.spinBox_R1_GI_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_GI_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R1_GI_DB, 1, 11, 1, 1)

        self.label_DUR_Header_DB = QLabel(self.gridLayoutWidget_8)
        self.label_DUR_Header_DB.setObjectName(u"label_DUR_Header_DB")
        self.label_DUR_Header_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_DUR_Header_DB, 0, 4, 1, 1)

        self.spinBox_R1_HAN_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R1_HAN_DB.setObjectName(u"spinBox_R1_HAN_DB")
        self.spinBox_R1_HAN_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_HAN_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R1_HAN_DB, 1, 10, 1, 1)

        self.label_R3_DB = QLabel(self.gridLayoutWidget_8)
        self.label_R3_DB.setObjectName(u"label_R3_DB")
        self.label_R3_DB.setFont(font1)
        self.label_R3_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_R3_DB, 3, 0, 1, 1)

        self.label_GI_Header_DB = QLabel(self.gridLayoutWidget_8)
        self.label_GI_Header_DB.setObjectName(u"label_GI_Header_DB")
        self.label_GI_Header_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_GI_Header_DB, 0, 11, 1, 1)

        self.spinBox_R1_TEC_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R1_TEC_DB.setObjectName(u"spinBox_R1_TEC_DB")
        self.spinBox_R1_TEC_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TEC_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R1_TEC_DB, 1, 13, 1, 1)

        self.spinBox_R1_ATH_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R1_ATH_DB.setObjectName(u"spinBox_R1_ATH_DB")
        self.spinBox_R1_ATH_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ATH_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R1_ATH_DB, 1, 2, 1, 1)

        self.spinBox_R1_DUR_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R1_DUR_DB.setObjectName(u"spinBox_R1_DUR_DB")
        self.spinBox_R1_DUR_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_DUR_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R1_DUR_DB, 1, 4, 1, 1)

        self.spinBox_R2_ELU_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R2_ELU_DB.setObjectName(u"spinBox_R2_ELU_DB")
        self.spinBox_R2_ELU_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ELU_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R2_ELU_DB, 2, 12, 1, 1)

        self.spinBox_R2_ATH_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R2_ATH_DB.setObjectName(u"spinBox_R2_ATH_DB")
        self.spinBox_R2_ATH_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ATH_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R2_ATH_DB, 2, 2, 1, 1)

        self.spinBox_R2_STR_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R2_STR_DB.setObjectName(u"spinBox_R2_STR_DB")
        self.spinBox_R2_STR_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STR_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R2_STR_DB, 2, 7, 1, 1)

        self.spinBox_R3_ATH_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R3_ATH_DB.setObjectName(u"spinBox_R3_ATH_DB")
        self.spinBox_R3_ATH_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ATH_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R3_ATH_DB, 3, 2, 1, 1)

        self.spinBox_R1_ELU_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R1_ELU_DB.setObjectName(u"spinBox_R1_ELU_DB")
        self.spinBox_R1_ELU_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ELU_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R1_ELU_DB, 1, 12, 1, 1)

        self.label_STA_Header_DB = QLabel(self.gridLayoutWidget_8)
        self.label_STA_Header_DB.setObjectName(u"label_STA_Header_DB")
        self.label_STA_Header_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_STA_Header_DB, 0, 6, 1, 1)

        self.spinBox_R1_STR_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R1_STR_DB.setObjectName(u"spinBox_R1_STR_DB")
        self.spinBox_R1_STR_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STR_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R1_STR_DB, 1, 7, 1, 1)

        self.label_SPD_Header_DB = QLabel(self.gridLayoutWidget_8)
        self.label_SPD_Header_DB.setObjectName(u"label_SPD_Header_DB")
        self.label_SPD_Header_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_SPD_Header_DB, 0, 3, 1, 1)

        self.spinBox_R2_DUR_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R2_DUR_DB.setObjectName(u"spinBox_R2_DUR_DB")
        self.spinBox_R2_DUR_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_DUR_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R2_DUR_DB, 2, 4, 1, 1)

        self.label_HAN_Header_DB = QLabel(self.gridLayoutWidget_8)
        self.label_HAN_Header_DB.setObjectName(u"label_HAN_Header_DB")
        self.label_HAN_Header_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_HAN_Header_DB, 0, 10, 1, 1)

        self.label_R4_DB = QLabel(self.gridLayoutWidget_8)
        self.label_R4_DB.setObjectName(u"label_R4_DB")
        self.label_R4_DB.setFont(font1)
        self.label_R4_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_R4_DB, 4, 0, 1, 1)

        self.spinBox_R1_TKL_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R1_TKL_DB.setObjectName(u"spinBox_R1_TKL_DB")
        self.spinBox_R1_TKL_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TKL_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R1_TKL_DB, 1, 9, 1, 1)

        self.spinBox_R2_GI_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R2_GI_DB.setObjectName(u"spinBox_R2_GI_DB")
        self.spinBox_R2_GI_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_GI_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R2_GI_DB, 2, 11, 1, 1)

        self.spinBox_R3_WE_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R3_WE_DB.setObjectName(u"spinBox_R3_WE_DB")
        self.spinBox_R3_WE_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_WE_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R3_WE_DB, 3, 5, 1, 1)

        self.spinBox_R3_SPD_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R3_SPD_DB.setObjectName(u"spinBox_R3_SPD_DB")
        self.spinBox_R3_SPD_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_SPD_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R3_SPD_DB, 3, 3, 1, 1)

        self.label_R6_DB = QLabel(self.gridLayoutWidget_8)
        self.label_R6_DB.setObjectName(u"label_R6_DB")
        self.label_R6_DB.setFont(font1)
        self.label_R6_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_R6_DB, 6, 0, 1, 1)

        self.spinBox_R2_STA_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R2_STA_DB.setObjectName(u"spinBox_R2_STA_DB")
        self.spinBox_R2_STA_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STA_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R2_STA_DB, 2, 6, 1, 1)

        self.spinBox_R3_BLK_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R3_BLK_DB.setObjectName(u"spinBox_R3_BLK_DB")
        self.spinBox_R3_BLK_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_BLK_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R3_BLK_DB, 3, 8, 1, 1)

        self.spinBox_R3_TKL_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R3_TKL_DB.setObjectName(u"spinBox_R3_TKL_DB")
        self.spinBox_R3_TKL_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TKL_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R3_TKL_DB, 3, 9, 1, 1)

        self.spinBox_R3_HAN_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R3_HAN_DB.setObjectName(u"spinBox_R3_HAN_DB")
        self.spinBox_R3_HAN_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_HAN_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R3_HAN_DB, 3, 10, 1, 1)

        self.spinBox_R3_GI_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R3_GI_DB.setObjectName(u"spinBox_R3_GI_DB")
        self.spinBox_R3_GI_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_GI_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R3_GI_DB, 3, 11, 1, 1)

        self.spinBox_R3_ELU_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R3_ELU_DB.setObjectName(u"spinBox_R3_ELU_DB")
        self.spinBox_R3_ELU_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ELU_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R3_ELU_DB, 3, 12, 1, 1)

        self.spinBox_R3_TEC_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R3_TEC_DB.setObjectName(u"spinBox_R3_TEC_DB")
        self.spinBox_R3_TEC_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TEC_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R3_TEC_DB, 3, 13, 1, 1)

        self.spinBox_R4_ATH_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R4_ATH_DB.setObjectName(u"spinBox_R4_ATH_DB")
        self.spinBox_R4_ATH_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ATH_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R4_ATH_DB, 4, 2, 1, 1)

        self.spinBox_R4_SPD_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R4_SPD_DB.setObjectName(u"spinBox_R4_SPD_DB")
        self.spinBox_R4_SPD_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_SPD_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R4_SPD_DB, 4, 3, 1, 1)

        self.spinBox_R4_DUR_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R4_DUR_DB.setObjectName(u"spinBox_R4_DUR_DB")
        self.spinBox_R4_DUR_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_DUR_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R4_DUR_DB, 4, 4, 1, 1)

        self.spinBox_R4_WE_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R4_WE_DB.setObjectName(u"spinBox_R4_WE_DB")
        self.spinBox_R4_WE_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_WE_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R4_WE_DB, 4, 5, 1, 1)

        self.spinBox_R4_STA_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R4_STA_DB.setObjectName(u"spinBox_R4_STA_DB")
        self.spinBox_R4_STA_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STA_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R4_STA_DB, 4, 6, 1, 1)

        self.spinBox_R4_STR_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R4_STR_DB.setObjectName(u"spinBox_R4_STR_DB")
        self.spinBox_R4_STR_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STR_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R4_STR_DB, 4, 7, 1, 1)

        self.spinBox_R4_BLK_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R4_BLK_DB.setObjectName(u"spinBox_R4_BLK_DB")
        self.spinBox_R4_BLK_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_BLK_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R4_BLK_DB, 4, 8, 1, 1)

        self.spinBox_R4_TKL_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R4_TKL_DB.setObjectName(u"spinBox_R4_TKL_DB")
        self.spinBox_R4_TKL_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TKL_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R4_TKL_DB, 4, 9, 1, 1)

        self.spinBox_R4_HAN_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R4_HAN_DB.setObjectName(u"spinBox_R4_HAN_DB")
        self.spinBox_R4_HAN_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_HAN_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R4_HAN_DB, 4, 10, 1, 1)

        self.spinBox_R4_GI_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R4_GI_DB.setObjectName(u"spinBox_R4_GI_DB")
        self.spinBox_R4_GI_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_GI_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R4_GI_DB, 4, 11, 1, 1)

        self.spinBox_R4_ELU_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R4_ELU_DB.setObjectName(u"spinBox_R4_ELU_DB")
        self.spinBox_R4_ELU_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ELU_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R4_ELU_DB, 4, 12, 1, 1)

        self.spinBox_R4_TEC_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R4_TEC_DB.setObjectName(u"spinBox_R4_TEC_DB")
        self.spinBox_R4_TEC_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TEC_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R4_TEC_DB, 4, 13, 1, 1)

        self.spinBox_R5_ATH_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R5_ATH_DB.setObjectName(u"spinBox_R5_ATH_DB")
        self.spinBox_R5_ATH_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ATH_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R5_ATH_DB, 5, 2, 1, 1)

        self.spinBox_R5_SPD_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R5_SPD_DB.setObjectName(u"spinBox_R5_SPD_DB")
        self.spinBox_R5_SPD_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_SPD_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R5_SPD_DB, 5, 3, 1, 1)

        self.spinBox_R5_DUR_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R5_DUR_DB.setObjectName(u"spinBox_R5_DUR_DB")
        self.spinBox_R5_DUR_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_DUR_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R5_DUR_DB, 5, 4, 1, 1)

        self.spinBox_R5_WE_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R5_WE_DB.setObjectName(u"spinBox_R5_WE_DB")
        self.spinBox_R5_WE_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_WE_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R5_WE_DB, 5, 5, 1, 1)

        self.spinBox_R5_STA_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R5_STA_DB.setObjectName(u"spinBox_R5_STA_DB")
        self.spinBox_R5_STA_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STA_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R5_STA_DB, 5, 6, 1, 1)

        self.spinBox_R5_STR_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R5_STR_DB.setObjectName(u"spinBox_R5_STR_DB")
        self.spinBox_R5_STR_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STR_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R5_STR_DB, 5, 7, 1, 1)

        self.spinBox_R5_BLK_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R5_BLK_DB.setObjectName(u"spinBox_R5_BLK_DB")
        self.spinBox_R5_BLK_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_BLK_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R5_BLK_DB, 5, 8, 1, 1)

        self.spinBox_R5_TKL_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R5_TKL_DB.setObjectName(u"spinBox_R5_TKL_DB")
        self.spinBox_R5_TKL_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TKL_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R5_TKL_DB, 5, 9, 1, 1)

        self.spinBox_R5_HAN_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R5_HAN_DB.setObjectName(u"spinBox_R5_HAN_DB")
        self.spinBox_R5_HAN_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_HAN_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R5_HAN_DB, 5, 10, 1, 1)

        self.spinBox_R5_GI_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R5_GI_DB.setObjectName(u"spinBox_R5_GI_DB")
        self.spinBox_R5_GI_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_GI_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R5_GI_DB, 5, 11, 1, 1)

        self.spinBox_R5_ELU_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R5_ELU_DB.setObjectName(u"spinBox_R5_ELU_DB")
        self.spinBox_R5_ELU_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ELU_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R5_ELU_DB, 5, 12, 1, 1)

        self.spinBox_R5_TEC_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R5_TEC_DB.setObjectName(u"spinBox_R5_TEC_DB")
        self.spinBox_R5_TEC_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TEC_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R5_TEC_DB, 5, 13, 1, 1)

        self.spinBox_R6_ATH_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R6_ATH_DB.setObjectName(u"spinBox_R6_ATH_DB")
        self.spinBox_R6_ATH_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ATH_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R6_ATH_DB, 6, 2, 1, 1)

        self.spinBox_R6_SPD_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R6_SPD_DB.setObjectName(u"spinBox_R6_SPD_DB")
        self.spinBox_R6_SPD_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_SPD_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R6_SPD_DB, 6, 3, 1, 1)

        self.spinBox_R6_DUR_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R6_DUR_DB.setObjectName(u"spinBox_R6_DUR_DB")
        self.spinBox_R6_DUR_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_DUR_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R6_DUR_DB, 6, 4, 1, 1)

        self.spinBox_R6_WE_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R6_WE_DB.setObjectName(u"spinBox_R6_WE_DB")
        self.spinBox_R6_WE_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_WE_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R6_WE_DB, 6, 5, 1, 1)

        self.spinBox_R6_STA_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R6_STA_DB.setObjectName(u"spinBox_R6_STA_DB")
        self.spinBox_R6_STA_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STA_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R6_STA_DB, 6, 6, 1, 1)

        self.spinBox_R6_STR_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R6_STR_DB.setObjectName(u"spinBox_R6_STR_DB")
        self.spinBox_R6_STR_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STR_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R6_STR_DB, 6, 7, 1, 1)

        self.spinBox_R6_BLK_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R6_BLK_DB.setObjectName(u"spinBox_R6_BLK_DB")
        self.spinBox_R6_BLK_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_BLK_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R6_BLK_DB, 6, 8, 1, 1)

        self.spinBox_R6_TKL_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R6_TKL_DB.setObjectName(u"spinBox_R6_TKL_DB")
        self.spinBox_R6_TKL_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TKL_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R6_TKL_DB, 6, 9, 1, 1)

        self.spinBox_R6_HAN_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R6_HAN_DB.setObjectName(u"spinBox_R6_HAN_DB")
        self.spinBox_R6_HAN_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_HAN_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R6_HAN_DB, 6, 10, 1, 1)

        self.spinBox_R6_GI_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R6_GI_DB.setObjectName(u"spinBox_R6_GI_DB")
        self.spinBox_R6_GI_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_GI_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R6_GI_DB, 6, 11, 1, 1)

        self.spinBox_R6_ELU_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R6_ELU_DB.setObjectName(u"spinBox_R6_ELU_DB")
        self.spinBox_R6_ELU_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ELU_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R6_ELU_DB, 6, 12, 1, 1)

        self.spinBox_R6_TEC_DB = QSpinBox(self.gridLayoutWidget_8)
        self.spinBox_R6_TEC_DB.setObjectName(u"spinBox_R6_TEC_DB")
        self.spinBox_R6_TEC_DB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TEC_DB.setMaximum(100)

        self.gridLayout_8.addWidget(self.spinBox_R6_TEC_DB, 6, 13, 1, 1)

        self.lineEdit_R1_DB = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_R1_DB.setObjectName(u"lineEdit_R1_DB")
        self.lineEdit_R1_DB.setFont(font2)
        self.lineEdit_R1_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lineEdit_R1_DB, 1, 1, 1, 1)

        self.lineEdit_R2_DB = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_R2_DB.setObjectName(u"lineEdit_R2_DB")
        self.lineEdit_R2_DB.setFont(font2)
        self.lineEdit_R2_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lineEdit_R2_DB, 2, 1, 1, 1)

        self.lineEdit_R3_DB = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_R3_DB.setObjectName(u"lineEdit_R3_DB")
        self.lineEdit_R3_DB.setFont(font2)
        self.lineEdit_R3_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lineEdit_R3_DB, 3, 1, 1, 1)

        self.lineEdit_R4_DB = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_R4_DB.setObjectName(u"lineEdit_R4_DB")
        self.lineEdit_R4_DB.setFont(font2)
        self.lineEdit_R4_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lineEdit_R4_DB, 4, 1, 1, 1)

        self.lineEdit_R5_DB = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_R5_DB.setObjectName(u"lineEdit_R5_DB")
        self.lineEdit_R5_DB.setFont(font2)
        self.lineEdit_R5_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lineEdit_R5_DB, 5, 1, 1, 1)

        self.lineEdit_R6_DB = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_R6_DB.setObjectName(u"lineEdit_R6_DB")
        self.lineEdit_R6_DB.setFont(font2)
        self.lineEdit_R6_DB.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.lineEdit_R6_DB, 6, 1, 1, 1)

        self.lcdNumber_R1_DB = QLCDNumber(self.gridLayoutWidget_8)
        self.lcdNumber_R1_DB.setObjectName(u"lcdNumber_R1_DB")
        self.lcdNumber_R1_DB.setDigitCount(3)
        self.lcdNumber_R1_DB.setProperty("intValue", 0)

        self.gridLayout_8.addWidget(self.lcdNumber_R1_DB, 1, 14, 1, 1)

        self.lcdNumber_R2_DB = QLCDNumber(self.gridLayoutWidget_8)
        self.lcdNumber_R2_DB.setObjectName(u"lcdNumber_R2_DB")
        self.lcdNumber_R2_DB.setDigitCount(3)
        self.lcdNumber_R2_DB.setProperty("intValue", 0)

        self.gridLayout_8.addWidget(self.lcdNumber_R2_DB, 2, 14, 1, 1)

        self.lcdNumber_R3_DB = QLCDNumber(self.gridLayoutWidget_8)
        self.lcdNumber_R3_DB.setObjectName(u"lcdNumber_R3_DB")
        self.lcdNumber_R3_DB.setDigitCount(3)
        self.lcdNumber_R3_DB.setProperty("intValue", 0)

        self.gridLayout_8.addWidget(self.lcdNumber_R3_DB, 3, 14, 1, 1)

        self.lcdNumber_R4_DB = QLCDNumber(self.gridLayoutWidget_8)
        self.lcdNumber_R4_DB.setObjectName(u"lcdNumber_R4_DB")
        self.lcdNumber_R4_DB.setDigitCount(3)
        self.lcdNumber_R4_DB.setProperty("intValue", 0)

        self.gridLayout_8.addWidget(self.lcdNumber_R4_DB, 4, 14, 1, 1)

        self.lcdNumber_R5_DB = QLCDNumber(self.gridLayoutWidget_8)
        self.lcdNumber_R5_DB.setObjectName(u"lcdNumber_R5_DB")
        self.lcdNumber_R5_DB.setDigitCount(3)
        self.lcdNumber_R5_DB.setProperty("intValue", 0)

        self.gridLayout_8.addWidget(self.lcdNumber_R5_DB, 5, 14, 1, 1)

        self.lcdNumber_R6_DB = QLCDNumber(self.gridLayoutWidget_8)
        self.lcdNumber_R6_DB.setObjectName(u"lcdNumber_R6_DB")
        self.lcdNumber_R6_DB.setDigitCount(3)
        self.lcdNumber_R6_DB.setProperty("intValue", 0)

        self.gridLayout_8.addWidget(self.lcdNumber_R6_DB, 6, 14, 1, 1)

        self.tabWidgetRoleRatings.addTab(self.DB, "")
        self.K = QWidget()
        self.K.setObjectName(u"K")
        self.gridLayoutWidget_9 = QWidget(self.K)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(0, 10, 1215, 261))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_ATH_Header_K = QLabel(self.gridLayoutWidget_9)
        self.label_ATH_Header_K.setObjectName(u"label_ATH_Header_K")
        self.label_ATH_Header_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_ATH_Header_K, 0, 2, 1, 1)

        self.spinBox_R2_TKL_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R2_TKL_K.setObjectName(u"spinBox_R2_TKL_K")
        self.spinBox_R2_TKL_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TKL_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R2_TKL_K, 2, 9, 1, 1)

        self.spinBox_R3_DUR_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R3_DUR_K.setObjectName(u"spinBox_R3_DUR_K")
        self.spinBox_R3_DUR_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_DUR_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R3_DUR_K, 3, 4, 1, 1)

        self.spinBox_R3_STR_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R3_STR_K.setObjectName(u"spinBox_R3_STR_K")
        self.spinBox_R3_STR_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STR_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R3_STR_K, 3, 7, 1, 1)

        self.spinBox_R2_TEC_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R2_TEC_K.setObjectName(u"spinBox_R2_TEC_K")
        self.spinBox_R2_TEC_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TEC_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R2_TEC_K, 2, 13, 1, 1)

        self.spinBox_R2_WE_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R2_WE_K.setObjectName(u"spinBox_R2_WE_K")
        self.spinBox_R2_WE_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_WE_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R2_WE_K, 2, 5, 1, 1)

        self.spinBox_R1_SPD_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R1_SPD_K.setObjectName(u"spinBox_R1_SPD_K")
        self.spinBox_R1_SPD_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_SPD_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R1_SPD_K, 1, 3, 1, 1)

        self.label_TEC_Header_K = QLabel(self.gridLayoutWidget_9)
        self.label_TEC_Header_K.setObjectName(u"label_TEC_Header_K")
        self.label_TEC_Header_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_TEC_Header_K, 0, 13, 1, 1)

        self.spinBox_R1_BLK_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R1_BLK_K.setObjectName(u"spinBox_R1_BLK_K")
        self.spinBox_R1_BLK_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_BLK_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R1_BLK_K, 1, 8, 1, 1)

        self.spinBox_R1_STA_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R1_STA_K.setObjectName(u"spinBox_R1_STA_K")
        self.spinBox_R1_STA_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STA_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R1_STA_K, 1, 6, 1, 1)

        self.label_WE_Header_K = QLabel(self.gridLayoutWidget_9)
        self.label_WE_Header_K.setObjectName(u"label_WE_Header_K")
        self.label_WE_Header_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_WE_Header_K, 0, 5, 1, 1)

        self.label_TKL_Header_K = QLabel(self.gridLayoutWidget_9)
        self.label_TKL_Header_K.setObjectName(u"label_TKL_Header_K")
        self.label_TKL_Header_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_TKL_Header_K, 0, 9, 1, 1)

        self.label_STR_Header_K = QLabel(self.gridLayoutWidget_9)
        self.label_STR_Header_K.setObjectName(u"label_STR_Header_K")
        self.label_STR_Header_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_STR_Header_K, 0, 7, 1, 1)

        self.spinBox_R1_WE_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R1_WE_K.setObjectName(u"spinBox_R1_WE_K")
        self.spinBox_R1_WE_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_WE_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R1_WE_K, 1, 5, 1, 1)

        self.spinBox_R2_SPD_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R2_SPD_K.setObjectName(u"spinBox_R2_SPD_K")
        self.spinBox_R2_SPD_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_SPD_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R2_SPD_K, 2, 3, 1, 1)

        self.label_R1_K = QLabel(self.gridLayoutWidget_9)
        self.label_R1_K.setObjectName(u"label_R1_K")
        self.label_R1_K.setFont(font1)
        self.label_R1_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_R1_K, 1, 0, 1, 1)

        self.label_RoleHeader_K = QLabel(self.gridLayoutWidget_9)
        self.label_RoleHeader_K.setObjectName(u"label_RoleHeader_K")
        self.label_RoleHeader_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_RoleHeader_K, 0, 0, 1, 1)

        self.label_Total_Header_K = QLabel(self.gridLayoutWidget_9)
        self.label_Total_Header_K.setObjectName(u"label_Total_Header_K")

        self.gridLayout_9.addWidget(self.label_Total_Header_K, 0, 14, 1, 1)

        self.spinBox_R3_STA_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R3_STA_K.setObjectName(u"spinBox_R3_STA_K")
        self.spinBox_R3_STA_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STA_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R3_STA_K, 3, 6, 1, 1)

        self.label_R5_K = QLabel(self.gridLayoutWidget_9)
        self.label_R5_K.setObjectName(u"label_R5_K")
        self.label_R5_K.setFont(font1)
        self.label_R5_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_R5_K, 5, 0, 1, 1)

        self.label_BLK_Header_K = QLabel(self.gridLayoutWidget_9)
        self.label_BLK_Header_K.setObjectName(u"label_BLK_Header_K")
        self.label_BLK_Header_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_BLK_Header_K, 0, 8, 1, 1)

        self.label_ELU_Header_K = QLabel(self.gridLayoutWidget_9)
        self.label_ELU_Header_K.setObjectName(u"label_ELU_Header_K")
        self.label_ELU_Header_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_ELU_Header_K, 0, 12, 1, 1)

        self.spinBox_R2_BLK_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R2_BLK_K.setObjectName(u"spinBox_R2_BLK_K")
        self.spinBox_R2_BLK_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_BLK_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R2_BLK_K, 2, 8, 1, 1)

        self.label_LabelHeader_K = QLabel(self.gridLayoutWidget_9)
        self.label_LabelHeader_K.setObjectName(u"label_LabelHeader_K")
        self.label_LabelHeader_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_LabelHeader_K, 0, 1, 1, 1)

        self.spinBox_R2_HAN_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R2_HAN_K.setObjectName(u"spinBox_R2_HAN_K")
        self.spinBox_R2_HAN_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_HAN_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R2_HAN_K, 2, 10, 1, 1)

        self.label_R2_K = QLabel(self.gridLayoutWidget_9)
        self.label_R2_K.setObjectName(u"label_R2_K")
        self.label_R2_K.setFont(font1)
        self.label_R2_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_R2_K, 2, 0, 1, 1)

        self.spinBox_R1_GI_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R1_GI_K.setObjectName(u"spinBox_R1_GI_K")
        self.spinBox_R1_GI_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_GI_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R1_GI_K, 1, 11, 1, 1)

        self.label_DUR_Header_K = QLabel(self.gridLayoutWidget_9)
        self.label_DUR_Header_K.setObjectName(u"label_DUR_Header_K")
        self.label_DUR_Header_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_DUR_Header_K, 0, 4, 1, 1)

        self.spinBox_R1_HAN_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R1_HAN_K.setObjectName(u"spinBox_R1_HAN_K")
        self.spinBox_R1_HAN_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_HAN_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R1_HAN_K, 1, 10, 1, 1)

        self.label_R3_K = QLabel(self.gridLayoutWidget_9)
        self.label_R3_K.setObjectName(u"label_R3_K")
        self.label_R3_K.setFont(font1)
        self.label_R3_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_R3_K, 3, 0, 1, 1)

        self.label_GI_Header_K = QLabel(self.gridLayoutWidget_9)
        self.label_GI_Header_K.setObjectName(u"label_GI_Header_K")
        self.label_GI_Header_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_GI_Header_K, 0, 11, 1, 1)

        self.spinBox_R1_TEC_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R1_TEC_K.setObjectName(u"spinBox_R1_TEC_K")
        self.spinBox_R1_TEC_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TEC_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R1_TEC_K, 1, 13, 1, 1)

        self.spinBox_R1_ATH_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R1_ATH_K.setObjectName(u"spinBox_R1_ATH_K")
        self.spinBox_R1_ATH_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ATH_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R1_ATH_K, 1, 2, 1, 1)

        self.spinBox_R1_DUR_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R1_DUR_K.setObjectName(u"spinBox_R1_DUR_K")
        self.spinBox_R1_DUR_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_DUR_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R1_DUR_K, 1, 4, 1, 1)

        self.spinBox_R2_ELU_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R2_ELU_K.setObjectName(u"spinBox_R2_ELU_K")
        self.spinBox_R2_ELU_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ELU_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R2_ELU_K, 2, 12, 1, 1)

        self.spinBox_R2_ATH_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R2_ATH_K.setObjectName(u"spinBox_R2_ATH_K")
        self.spinBox_R2_ATH_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ATH_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R2_ATH_K, 2, 2, 1, 1)

        self.spinBox_R2_STR_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R2_STR_K.setObjectName(u"spinBox_R2_STR_K")
        self.spinBox_R2_STR_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STR_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R2_STR_K, 2, 7, 1, 1)

        self.spinBox_R3_ATH_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R3_ATH_K.setObjectName(u"spinBox_R3_ATH_K")
        self.spinBox_R3_ATH_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ATH_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R3_ATH_K, 3, 2, 1, 1)

        self.spinBox_R1_ELU_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R1_ELU_K.setObjectName(u"spinBox_R1_ELU_K")
        self.spinBox_R1_ELU_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ELU_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R1_ELU_K, 1, 12, 1, 1)

        self.label_STA_Header_K = QLabel(self.gridLayoutWidget_9)
        self.label_STA_Header_K.setObjectName(u"label_STA_Header_K")
        self.label_STA_Header_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_STA_Header_K, 0, 6, 1, 1)

        self.spinBox_R1_STR_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R1_STR_K.setObjectName(u"spinBox_R1_STR_K")
        self.spinBox_R1_STR_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STR_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R1_STR_K, 1, 7, 1, 1)

        self.label_SPD_Header_K = QLabel(self.gridLayoutWidget_9)
        self.label_SPD_Header_K.setObjectName(u"label_SPD_Header_K")
        self.label_SPD_Header_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_SPD_Header_K, 0, 3, 1, 1)

        self.spinBox_R2_DUR_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R2_DUR_K.setObjectName(u"spinBox_R2_DUR_K")
        self.spinBox_R2_DUR_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_DUR_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R2_DUR_K, 2, 4, 1, 1)

        self.label_HAN_Header_K = QLabel(self.gridLayoutWidget_9)
        self.label_HAN_Header_K.setObjectName(u"label_HAN_Header_K")
        self.label_HAN_Header_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_HAN_Header_K, 0, 10, 1, 1)

        self.label_R4_K = QLabel(self.gridLayoutWidget_9)
        self.label_R4_K.setObjectName(u"label_R4_K")
        self.label_R4_K.setFont(font1)
        self.label_R4_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_R4_K, 4, 0, 1, 1)

        self.spinBox_R1_TKL_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R1_TKL_K.setObjectName(u"spinBox_R1_TKL_K")
        self.spinBox_R1_TKL_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TKL_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R1_TKL_K, 1, 9, 1, 1)

        self.spinBox_R2_GI_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R2_GI_K.setObjectName(u"spinBox_R2_GI_K")
        self.spinBox_R2_GI_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_GI_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R2_GI_K, 2, 11, 1, 1)

        self.spinBox_R3_WE_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R3_WE_K.setObjectName(u"spinBox_R3_WE_K")
        self.spinBox_R3_WE_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_WE_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R3_WE_K, 3, 5, 1, 1)

        self.spinBox_R3_SPD_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R3_SPD_K.setObjectName(u"spinBox_R3_SPD_K")
        self.spinBox_R3_SPD_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_SPD_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R3_SPD_K, 3, 3, 1, 1)

        self.label_R6_K = QLabel(self.gridLayoutWidget_9)
        self.label_R6_K.setObjectName(u"label_R6_K")
        self.label_R6_K.setFont(font1)
        self.label_R6_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_R6_K, 6, 0, 1, 1)

        self.spinBox_R2_STA_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R2_STA_K.setObjectName(u"spinBox_R2_STA_K")
        self.spinBox_R2_STA_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STA_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R2_STA_K, 2, 6, 1, 1)

        self.spinBox_R3_BLK_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R3_BLK_K.setObjectName(u"spinBox_R3_BLK_K")
        self.spinBox_R3_BLK_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_BLK_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R3_BLK_K, 3, 8, 1, 1)

        self.spinBox_R3_TKL_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R3_TKL_K.setObjectName(u"spinBox_R3_TKL_K")
        self.spinBox_R3_TKL_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TKL_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R3_TKL_K, 3, 9, 1, 1)

        self.spinBox_R3_HAN_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R3_HAN_K.setObjectName(u"spinBox_R3_HAN_K")
        self.spinBox_R3_HAN_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_HAN_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R3_HAN_K, 3, 10, 1, 1)

        self.spinBox_R3_GI_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R3_GI_K.setObjectName(u"spinBox_R3_GI_K")
        self.spinBox_R3_GI_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_GI_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R3_GI_K, 3, 11, 1, 1)

        self.spinBox_R3_ELU_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R3_ELU_K.setObjectName(u"spinBox_R3_ELU_K")
        self.spinBox_R3_ELU_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ELU_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R3_ELU_K, 3, 12, 1, 1)

        self.spinBox_R3_TEC_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R3_TEC_K.setObjectName(u"spinBox_R3_TEC_K")
        self.spinBox_R3_TEC_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TEC_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R3_TEC_K, 3, 13, 1, 1)

        self.spinBox_R4_ATH_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R4_ATH_K.setObjectName(u"spinBox_R4_ATH_K")
        self.spinBox_R4_ATH_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ATH_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R4_ATH_K, 4, 2, 1, 1)

        self.spinBox_R4_SPD_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R4_SPD_K.setObjectName(u"spinBox_R4_SPD_K")
        self.spinBox_R4_SPD_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_SPD_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R4_SPD_K, 4, 3, 1, 1)

        self.spinBox_R4_DUR_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R4_DUR_K.setObjectName(u"spinBox_R4_DUR_K")
        self.spinBox_R4_DUR_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_DUR_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R4_DUR_K, 4, 4, 1, 1)

        self.spinBox_R4_WE_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R4_WE_K.setObjectName(u"spinBox_R4_WE_K")
        self.spinBox_R4_WE_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_WE_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R4_WE_K, 4, 5, 1, 1)

        self.spinBox_R4_STA_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R4_STA_K.setObjectName(u"spinBox_R4_STA_K")
        self.spinBox_R4_STA_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STA_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R4_STA_K, 4, 6, 1, 1)

        self.spinBox_R4_STR_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R4_STR_K.setObjectName(u"spinBox_R4_STR_K")
        self.spinBox_R4_STR_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STR_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R4_STR_K, 4, 7, 1, 1)

        self.spinBox_R4_BLK_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R4_BLK_K.setObjectName(u"spinBox_R4_BLK_K")
        self.spinBox_R4_BLK_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_BLK_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R4_BLK_K, 4, 8, 1, 1)

        self.spinBox_R4_TKL_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R4_TKL_K.setObjectName(u"spinBox_R4_TKL_K")
        self.spinBox_R4_TKL_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TKL_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R4_TKL_K, 4, 9, 1, 1)

        self.spinBox_R4_HAN_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R4_HAN_K.setObjectName(u"spinBox_R4_HAN_K")
        self.spinBox_R4_HAN_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_HAN_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R4_HAN_K, 4, 10, 1, 1)

        self.spinBox_R4_GI_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R4_GI_K.setObjectName(u"spinBox_R4_GI_K")
        self.spinBox_R4_GI_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_GI_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R4_GI_K, 4, 11, 1, 1)

        self.spinBox_R4_ELU_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R4_ELU_K.setObjectName(u"spinBox_R4_ELU_K")
        self.spinBox_R4_ELU_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ELU_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R4_ELU_K, 4, 12, 1, 1)

        self.spinBox_R4_TEC_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R4_TEC_K.setObjectName(u"spinBox_R4_TEC_K")
        self.spinBox_R4_TEC_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TEC_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R4_TEC_K, 4, 13, 1, 1)

        self.spinBox_R5_ATH_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R5_ATH_K.setObjectName(u"spinBox_R5_ATH_K")
        self.spinBox_R5_ATH_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ATH_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R5_ATH_K, 5, 2, 1, 1)

        self.spinBox_R5_SPD_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R5_SPD_K.setObjectName(u"spinBox_R5_SPD_K")
        self.spinBox_R5_SPD_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_SPD_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R5_SPD_K, 5, 3, 1, 1)

        self.spinBox_R5_DUR_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R5_DUR_K.setObjectName(u"spinBox_R5_DUR_K")
        self.spinBox_R5_DUR_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_DUR_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R5_DUR_K, 5, 4, 1, 1)

        self.spinBox_R5_WE_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R5_WE_K.setObjectName(u"spinBox_R5_WE_K")
        self.spinBox_R5_WE_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_WE_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R5_WE_K, 5, 5, 1, 1)

        self.spinBox_R5_STA_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R5_STA_K.setObjectName(u"spinBox_R5_STA_K")
        self.spinBox_R5_STA_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STA_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R5_STA_K, 5, 6, 1, 1)

        self.spinBox_R5_STR_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R5_STR_K.setObjectName(u"spinBox_R5_STR_K")
        self.spinBox_R5_STR_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STR_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R5_STR_K, 5, 7, 1, 1)

        self.spinBox_R5_BLK_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R5_BLK_K.setObjectName(u"spinBox_R5_BLK_K")
        self.spinBox_R5_BLK_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_BLK_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R5_BLK_K, 5, 8, 1, 1)

        self.spinBox_R5_TKL_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R5_TKL_K.setObjectName(u"spinBox_R5_TKL_K")
        self.spinBox_R5_TKL_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TKL_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R5_TKL_K, 5, 9, 1, 1)

        self.spinBox_R5_HAN_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R5_HAN_K.setObjectName(u"spinBox_R5_HAN_K")
        self.spinBox_R5_HAN_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_HAN_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R5_HAN_K, 5, 10, 1, 1)

        self.spinBox_R5_GI_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R5_GI_K.setObjectName(u"spinBox_R5_GI_K")
        self.spinBox_R5_GI_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_GI_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R5_GI_K, 5, 11, 1, 1)

        self.spinBox_R5_ELU_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R5_ELU_K.setObjectName(u"spinBox_R5_ELU_K")
        self.spinBox_R5_ELU_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ELU_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R5_ELU_K, 5, 12, 1, 1)

        self.spinBox_R5_TEC_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R5_TEC_K.setObjectName(u"spinBox_R5_TEC_K")
        self.spinBox_R5_TEC_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TEC_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R5_TEC_K, 5, 13, 1, 1)

        self.spinBox_R6_ATH_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R6_ATH_K.setObjectName(u"spinBox_R6_ATH_K")
        self.spinBox_R6_ATH_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ATH_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R6_ATH_K, 6, 2, 1, 1)

        self.spinBox_R6_SPD_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R6_SPD_K.setObjectName(u"spinBox_R6_SPD_K")
        self.spinBox_R6_SPD_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_SPD_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R6_SPD_K, 6, 3, 1, 1)

        self.spinBox_R6_DUR_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R6_DUR_K.setObjectName(u"spinBox_R6_DUR_K")
        self.spinBox_R6_DUR_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_DUR_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R6_DUR_K, 6, 4, 1, 1)

        self.spinBox_R6_WE_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R6_WE_K.setObjectName(u"spinBox_R6_WE_K")
        self.spinBox_R6_WE_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_WE_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R6_WE_K, 6, 5, 1, 1)

        self.spinBox_R6_STA_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R6_STA_K.setObjectName(u"spinBox_R6_STA_K")
        self.spinBox_R6_STA_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STA_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R6_STA_K, 6, 6, 1, 1)

        self.spinBox_R6_STR_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R6_STR_K.setObjectName(u"spinBox_R6_STR_K")
        self.spinBox_R6_STR_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STR_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R6_STR_K, 6, 7, 1, 1)

        self.spinBox_R6_BLK_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R6_BLK_K.setObjectName(u"spinBox_R6_BLK_K")
        self.spinBox_R6_BLK_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_BLK_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R6_BLK_K, 6, 8, 1, 1)

        self.spinBox_R6_TKL_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R6_TKL_K.setObjectName(u"spinBox_R6_TKL_K")
        self.spinBox_R6_TKL_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TKL_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R6_TKL_K, 6, 9, 1, 1)

        self.spinBox_R6_HAN_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R6_HAN_K.setObjectName(u"spinBox_R6_HAN_K")
        self.spinBox_R6_HAN_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_HAN_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R6_HAN_K, 6, 10, 1, 1)

        self.spinBox_R6_GI_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R6_GI_K.setObjectName(u"spinBox_R6_GI_K")
        self.spinBox_R6_GI_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_GI_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R6_GI_K, 6, 11, 1, 1)

        self.spinBox_R6_ELU_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R6_ELU_K.setObjectName(u"spinBox_R6_ELU_K")
        self.spinBox_R6_ELU_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ELU_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R6_ELU_K, 6, 12, 1, 1)

        self.spinBox_R6_TEC_K = QSpinBox(self.gridLayoutWidget_9)
        self.spinBox_R6_TEC_K.setObjectName(u"spinBox_R6_TEC_K")
        self.spinBox_R6_TEC_K.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TEC_K.setMaximum(100)

        self.gridLayout_9.addWidget(self.spinBox_R6_TEC_K, 6, 13, 1, 1)

        self.lineEdit_R1_K = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_R1_K.setObjectName(u"lineEdit_R1_K")
        self.lineEdit_R1_K.setFont(font2)
        self.lineEdit_R1_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.lineEdit_R1_K, 1, 1, 1, 1)

        self.lineEdit_R2_K = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_R2_K.setObjectName(u"lineEdit_R2_K")
        self.lineEdit_R2_K.setFont(font2)
        self.lineEdit_R2_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.lineEdit_R2_K, 2, 1, 1, 1)

        self.lineEdit_R3_K = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_R3_K.setObjectName(u"lineEdit_R3_K")
        self.lineEdit_R3_K.setFont(font2)
        self.lineEdit_R3_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.lineEdit_R3_K, 3, 1, 1, 1)

        self.lineEdit_R4_K = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_R4_K.setObjectName(u"lineEdit_R4_K")
        self.lineEdit_R4_K.setFont(font2)
        self.lineEdit_R4_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.lineEdit_R4_K, 4, 1, 1, 1)

        self.lineEdit_R5_K = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_R5_K.setObjectName(u"lineEdit_R5_K")
        self.lineEdit_R5_K.setFont(font2)
        self.lineEdit_R5_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.lineEdit_R5_K, 5, 1, 1, 1)

        self.lineEdit_R6_K = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_R6_K.setObjectName(u"lineEdit_R6_K")
        self.lineEdit_R6_K.setFont(font2)
        self.lineEdit_R6_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.lineEdit_R6_K, 6, 1, 1, 1)

        self.lcdNumber_R1_K = QLCDNumber(self.gridLayoutWidget_9)
        self.lcdNumber_R1_K.setObjectName(u"lcdNumber_R1_K")
        self.lcdNumber_R1_K.setDigitCount(3)
        self.lcdNumber_R1_K.setProperty("intValue", 0)

        self.gridLayout_9.addWidget(self.lcdNumber_R1_K, 1, 14, 1, 1)

        self.lcdNumber_R2_K = QLCDNumber(self.gridLayoutWidget_9)
        self.lcdNumber_R2_K.setObjectName(u"lcdNumber_R2_K")
        self.lcdNumber_R2_K.setDigitCount(3)
        self.lcdNumber_R2_K.setProperty("intValue", 0)

        self.gridLayout_9.addWidget(self.lcdNumber_R2_K, 2, 14, 1, 1)

        self.lcdNumber_R3_K = QLCDNumber(self.gridLayoutWidget_9)
        self.lcdNumber_R3_K.setObjectName(u"lcdNumber_R3_K")
        self.lcdNumber_R3_K.setDigitCount(3)
        self.lcdNumber_R3_K.setProperty("intValue", 0)

        self.gridLayout_9.addWidget(self.lcdNumber_R3_K, 3, 14, 1, 1)

        self.lcdNumber_R4_K = QLCDNumber(self.gridLayoutWidget_9)
        self.lcdNumber_R4_K.setObjectName(u"lcdNumber_R4_K")
        self.lcdNumber_R4_K.setDigitCount(3)
        self.lcdNumber_R4_K.setProperty("intValue", 0)

        self.gridLayout_9.addWidget(self.lcdNumber_R4_K, 4, 14, 1, 1)

        self.lcdNumber_R5_K = QLCDNumber(self.gridLayoutWidget_9)
        self.lcdNumber_R5_K.setObjectName(u"lcdNumber_R5_K")
        self.lcdNumber_R5_K.setDigitCount(3)
        self.lcdNumber_R5_K.setProperty("intValue", 0)

        self.gridLayout_9.addWidget(self.lcdNumber_R5_K, 5, 14, 1, 1)

        self.lcdNumber_R6_K = QLCDNumber(self.gridLayoutWidget_9)
        self.lcdNumber_R6_K.setObjectName(u"lcdNumber_R6_K")
        self.lcdNumber_R6_K.setDigitCount(3)
        self.lcdNumber_R6_K.setProperty("intValue", 0)

        self.gridLayout_9.addWidget(self.lcdNumber_R6_K, 6, 14, 1, 1)

        self.tabWidgetRoleRatings.addTab(self.K, "")
        self.P = QWidget()
        self.P.setObjectName(u"P")
        self.gridLayoutWidget_10 = QWidget(self.P)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(0, 10, 1215, 261))
        self.gridLayout_10 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_ATH_Header_P = QLabel(self.gridLayoutWidget_10)
        self.label_ATH_Header_P.setObjectName(u"label_ATH_Header_P")
        self.label_ATH_Header_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_ATH_Header_P, 0, 2, 1, 1)

        self.spinBox_R2_TKL_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R2_TKL_P.setObjectName(u"spinBox_R2_TKL_P")
        self.spinBox_R2_TKL_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TKL_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R2_TKL_P, 2, 9, 1, 1)

        self.spinBox_R3_DUR_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R3_DUR_P.setObjectName(u"spinBox_R3_DUR_P")
        self.spinBox_R3_DUR_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_DUR_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R3_DUR_P, 3, 4, 1, 1)

        self.spinBox_R3_STR_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R3_STR_P.setObjectName(u"spinBox_R3_STR_P")
        self.spinBox_R3_STR_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STR_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R3_STR_P, 3, 7, 1, 1)

        self.spinBox_R2_TEC_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R2_TEC_P.setObjectName(u"spinBox_R2_TEC_P")
        self.spinBox_R2_TEC_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_TEC_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R2_TEC_P, 2, 13, 1, 1)

        self.spinBox_R2_WE_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R2_WE_P.setObjectName(u"spinBox_R2_WE_P")
        self.spinBox_R2_WE_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_WE_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R2_WE_P, 2, 5, 1, 1)

        self.spinBox_R1_SPD_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R1_SPD_P.setObjectName(u"spinBox_R1_SPD_P")
        self.spinBox_R1_SPD_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_SPD_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R1_SPD_P, 1, 3, 1, 1)

        self.label_TEC_Header_P = QLabel(self.gridLayoutWidget_10)
        self.label_TEC_Header_P.setObjectName(u"label_TEC_Header_P")
        self.label_TEC_Header_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_TEC_Header_P, 0, 13, 1, 1)

        self.spinBox_R1_BLK_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R1_BLK_P.setObjectName(u"spinBox_R1_BLK_P")
        self.spinBox_R1_BLK_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_BLK_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R1_BLK_P, 1, 8, 1, 1)

        self.spinBox_R1_STA_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R1_STA_P.setObjectName(u"spinBox_R1_STA_P")
        self.spinBox_R1_STA_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STA_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R1_STA_P, 1, 6, 1, 1)

        self.label_WE_Header_P = QLabel(self.gridLayoutWidget_10)
        self.label_WE_Header_P.setObjectName(u"label_WE_Header_P")
        self.label_WE_Header_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_WE_Header_P, 0, 5, 1, 1)

        self.label_TKL_Header_P = QLabel(self.gridLayoutWidget_10)
        self.label_TKL_Header_P.setObjectName(u"label_TKL_Header_P")
        self.label_TKL_Header_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_TKL_Header_P, 0, 9, 1, 1)

        self.label_STR_Header_P = QLabel(self.gridLayoutWidget_10)
        self.label_STR_Header_P.setObjectName(u"label_STR_Header_P")
        self.label_STR_Header_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_STR_Header_P, 0, 7, 1, 1)

        self.spinBox_R1_WE_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R1_WE_P.setObjectName(u"spinBox_R1_WE_P")
        self.spinBox_R1_WE_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_WE_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R1_WE_P, 1, 5, 1, 1)

        self.spinBox_R2_SPD_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R2_SPD_P.setObjectName(u"spinBox_R2_SPD_P")
        self.spinBox_R2_SPD_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_SPD_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R2_SPD_P, 2, 3, 1, 1)

        self.label_R1_P = QLabel(self.gridLayoutWidget_10)
        self.label_R1_P.setObjectName(u"label_R1_P")
        self.label_R1_P.setFont(font1)
        self.label_R1_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_R1_P, 1, 0, 1, 1)

        self.label_RoleHeader_P = QLabel(self.gridLayoutWidget_10)
        self.label_RoleHeader_P.setObjectName(u"label_RoleHeader_P")
        self.label_RoleHeader_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_RoleHeader_P, 0, 0, 1, 1)

        self.label_Total_Header_P = QLabel(self.gridLayoutWidget_10)
        self.label_Total_Header_P.setObjectName(u"label_Total_Header_P")

        self.gridLayout_10.addWidget(self.label_Total_Header_P, 0, 14, 1, 1)

        self.spinBox_R3_STA_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R3_STA_P.setObjectName(u"spinBox_R3_STA_P")
        self.spinBox_R3_STA_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_STA_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R3_STA_P, 3, 6, 1, 1)

        self.label_R5_P = QLabel(self.gridLayoutWidget_10)
        self.label_R5_P.setObjectName(u"label_R5_P")
        self.label_R5_P.setFont(font1)
        self.label_R5_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_R5_P, 5, 0, 1, 1)

        self.label_BLK_Header_P = QLabel(self.gridLayoutWidget_10)
        self.label_BLK_Header_P.setObjectName(u"label_BLK_Header_P")
        self.label_BLK_Header_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_BLK_Header_P, 0, 8, 1, 1)

        self.label_ELU_Header_P = QLabel(self.gridLayoutWidget_10)
        self.label_ELU_Header_P.setObjectName(u"label_ELU_Header_P")
        self.label_ELU_Header_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_ELU_Header_P, 0, 12, 1, 1)

        self.spinBox_R2_BLK_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R2_BLK_P.setObjectName(u"spinBox_R2_BLK_P")
        self.spinBox_R2_BLK_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_BLK_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R2_BLK_P, 2, 8, 1, 1)

        self.label_LabelHeader_P = QLabel(self.gridLayoutWidget_10)
        self.label_LabelHeader_P.setObjectName(u"label_LabelHeader_P")
        self.label_LabelHeader_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_LabelHeader_P, 0, 1, 1, 1)

        self.spinBox_R2_HAN_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R2_HAN_P.setObjectName(u"spinBox_R2_HAN_P")
        self.spinBox_R2_HAN_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_HAN_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R2_HAN_P, 2, 10, 1, 1)

        self.label_R2_P = QLabel(self.gridLayoutWidget_10)
        self.label_R2_P.setObjectName(u"label_R2_P")
        self.label_R2_P.setFont(font1)
        self.label_R2_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_R2_P, 2, 0, 1, 1)

        self.spinBox_R1_GI_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R1_GI_P.setObjectName(u"spinBox_R1_GI_P")
        self.spinBox_R1_GI_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_GI_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R1_GI_P, 1, 11, 1, 1)

        self.label_DUR_Header_P = QLabel(self.gridLayoutWidget_10)
        self.label_DUR_Header_P.setObjectName(u"label_DUR_Header_P")
        self.label_DUR_Header_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_DUR_Header_P, 0, 4, 1, 1)

        self.spinBox_R1_HAN_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R1_HAN_P.setObjectName(u"spinBox_R1_HAN_P")
        self.spinBox_R1_HAN_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_HAN_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R1_HAN_P, 1, 10, 1, 1)

        self.label_R3_P = QLabel(self.gridLayoutWidget_10)
        self.label_R3_P.setObjectName(u"label_R3_P")
        self.label_R3_P.setFont(font1)
        self.label_R3_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_R3_P, 3, 0, 1, 1)

        self.label_GI_Header_P = QLabel(self.gridLayoutWidget_10)
        self.label_GI_Header_P.setObjectName(u"label_GI_Header_P")
        self.label_GI_Header_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_GI_Header_P, 0, 11, 1, 1)

        self.spinBox_R1_TEC_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R1_TEC_P.setObjectName(u"spinBox_R1_TEC_P")
        self.spinBox_R1_TEC_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TEC_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R1_TEC_P, 1, 13, 1, 1)

        self.spinBox_R1_ATH_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R1_ATH_P.setObjectName(u"spinBox_R1_ATH_P")
        self.spinBox_R1_ATH_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ATH_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R1_ATH_P, 1, 2, 1, 1)

        self.spinBox_R1_DUR_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R1_DUR_P.setObjectName(u"spinBox_R1_DUR_P")
        self.spinBox_R1_DUR_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_DUR_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R1_DUR_P, 1, 4, 1, 1)

        self.spinBox_R2_ELU_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R2_ELU_P.setObjectName(u"spinBox_R2_ELU_P")
        self.spinBox_R2_ELU_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ELU_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R2_ELU_P, 2, 12, 1, 1)

        self.spinBox_R2_ATH_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R2_ATH_P.setObjectName(u"spinBox_R2_ATH_P")
        self.spinBox_R2_ATH_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_ATH_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R2_ATH_P, 2, 2, 1, 1)

        self.spinBox_R2_STR_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R2_STR_P.setObjectName(u"spinBox_R2_STR_P")
        self.spinBox_R2_STR_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STR_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R2_STR_P, 2, 7, 1, 1)

        self.spinBox_R3_ATH_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R3_ATH_P.setObjectName(u"spinBox_R3_ATH_P")
        self.spinBox_R3_ATH_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ATH_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R3_ATH_P, 3, 2, 1, 1)

        self.spinBox_R1_ELU_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R1_ELU_P.setObjectName(u"spinBox_R1_ELU_P")
        self.spinBox_R1_ELU_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_ELU_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R1_ELU_P, 1, 12, 1, 1)

        self.label_STA_Header_P = QLabel(self.gridLayoutWidget_10)
        self.label_STA_Header_P.setObjectName(u"label_STA_Header_P")
        self.label_STA_Header_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_STA_Header_P, 0, 6, 1, 1)

        self.spinBox_R1_STR_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R1_STR_P.setObjectName(u"spinBox_R1_STR_P")
        self.spinBox_R1_STR_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_STR_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R1_STR_P, 1, 7, 1, 1)

        self.label_SPD_Header_P = QLabel(self.gridLayoutWidget_10)
        self.label_SPD_Header_P.setObjectName(u"label_SPD_Header_P")
        self.label_SPD_Header_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_SPD_Header_P, 0, 3, 1, 1)

        self.spinBox_R2_DUR_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R2_DUR_P.setObjectName(u"spinBox_R2_DUR_P")
        self.spinBox_R2_DUR_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_DUR_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R2_DUR_P, 2, 4, 1, 1)

        self.label_HAN_Header_P = QLabel(self.gridLayoutWidget_10)
        self.label_HAN_Header_P.setObjectName(u"label_HAN_Header_P")
        self.label_HAN_Header_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_HAN_Header_P, 0, 10, 1, 1)

        self.label_R4_P = QLabel(self.gridLayoutWidget_10)
        self.label_R4_P.setObjectName(u"label_R4_P")
        self.label_R4_P.setFont(font1)
        self.label_R4_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_R4_P, 4, 0, 1, 1)

        self.spinBox_R1_TKL_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R1_TKL_P.setObjectName(u"spinBox_R1_TKL_P")
        self.spinBox_R1_TKL_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R1_TKL_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R1_TKL_P, 1, 9, 1, 1)

        self.spinBox_R2_GI_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R2_GI_P.setObjectName(u"spinBox_R2_GI_P")
        self.spinBox_R2_GI_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_GI_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R2_GI_P, 2, 11, 1, 1)

        self.spinBox_R3_WE_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R3_WE_P.setObjectName(u"spinBox_R3_WE_P")
        self.spinBox_R3_WE_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_WE_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R3_WE_P, 3, 5, 1, 1)

        self.spinBox_R3_SPD_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R3_SPD_P.setObjectName(u"spinBox_R3_SPD_P")
        self.spinBox_R3_SPD_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_SPD_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R3_SPD_P, 3, 3, 1, 1)

        self.label_R6_P = QLabel(self.gridLayoutWidget_10)
        self.label_R6_P.setObjectName(u"label_R6_P")
        self.label_R6_P.setFont(font1)
        self.label_R6_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_R6_P, 6, 0, 1, 1)

        self.spinBox_R2_STA_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R2_STA_P.setObjectName(u"spinBox_R2_STA_P")
        self.spinBox_R2_STA_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R2_STA_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R2_STA_P, 2, 6, 1, 1)

        self.spinBox_R3_BLK_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R3_BLK_P.setObjectName(u"spinBox_R3_BLK_P")
        self.spinBox_R3_BLK_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_BLK_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R3_BLK_P, 3, 8, 1, 1)

        self.spinBox_R3_TKL_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R3_TKL_P.setObjectName(u"spinBox_R3_TKL_P")
        self.spinBox_R3_TKL_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TKL_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R3_TKL_P, 3, 9, 1, 1)

        self.spinBox_R3_HAN_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R3_HAN_P.setObjectName(u"spinBox_R3_HAN_P")
        self.spinBox_R3_HAN_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_HAN_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R3_HAN_P, 3, 10, 1, 1)

        self.spinBox_R3_GI_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R3_GI_P.setObjectName(u"spinBox_R3_GI_P")
        self.spinBox_R3_GI_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_GI_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R3_GI_P, 3, 11, 1, 1)

        self.spinBox_R3_ELU_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R3_ELU_P.setObjectName(u"spinBox_R3_ELU_P")
        self.spinBox_R3_ELU_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_ELU_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R3_ELU_P, 3, 12, 1, 1)

        self.spinBox_R3_TEC_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R3_TEC_P.setObjectName(u"spinBox_R3_TEC_P")
        self.spinBox_R3_TEC_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R3_TEC_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R3_TEC_P, 3, 13, 1, 1)

        self.spinBox_R4_ATH_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R4_ATH_P.setObjectName(u"spinBox_R4_ATH_P")
        self.spinBox_R4_ATH_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ATH_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R4_ATH_P, 4, 2, 1, 1)

        self.spinBox_R4_SPD_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R4_SPD_P.setObjectName(u"spinBox_R4_SPD_P")
        self.spinBox_R4_SPD_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_SPD_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R4_SPD_P, 4, 3, 1, 1)

        self.spinBox_R4_DUR_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R4_DUR_P.setObjectName(u"spinBox_R4_DUR_P")
        self.spinBox_R4_DUR_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_DUR_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R4_DUR_P, 4, 4, 1, 1)

        self.spinBox_R4_WE_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R4_WE_P.setObjectName(u"spinBox_R4_WE_P")
        self.spinBox_R4_WE_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_WE_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R4_WE_P, 4, 5, 1, 1)

        self.spinBox_R4_STA_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R4_STA_P.setObjectName(u"spinBox_R4_STA_P")
        self.spinBox_R4_STA_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STA_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R4_STA_P, 4, 6, 1, 1)

        self.spinBox_R4_STR_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R4_STR_P.setObjectName(u"spinBox_R4_STR_P")
        self.spinBox_R4_STR_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_STR_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R4_STR_P, 4, 7, 1, 1)

        self.spinBox_R4_BLK_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R4_BLK_P.setObjectName(u"spinBox_R4_BLK_P")
        self.spinBox_R4_BLK_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_BLK_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R4_BLK_P, 4, 8, 1, 1)

        self.spinBox_R4_TKL_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R4_TKL_P.setObjectName(u"spinBox_R4_TKL_P")
        self.spinBox_R4_TKL_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TKL_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R4_TKL_P, 4, 9, 1, 1)

        self.spinBox_R4_HAN_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R4_HAN_P.setObjectName(u"spinBox_R4_HAN_P")
        self.spinBox_R4_HAN_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_HAN_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R4_HAN_P, 4, 10, 1, 1)

        self.spinBox_R4_GI_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R4_GI_P.setObjectName(u"spinBox_R4_GI_P")
        self.spinBox_R4_GI_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_GI_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R4_GI_P, 4, 11, 1, 1)

        self.spinBox_R4_ELU_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R4_ELU_P.setObjectName(u"spinBox_R4_ELU_P")
        self.spinBox_R4_ELU_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_ELU_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R4_ELU_P, 4, 12, 1, 1)

        self.spinBox_R4_TEC_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R4_TEC_P.setObjectName(u"spinBox_R4_TEC_P")
        self.spinBox_R4_TEC_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R4_TEC_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R4_TEC_P, 4, 13, 1, 1)

        self.spinBox_R5_ATH_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R5_ATH_P.setObjectName(u"spinBox_R5_ATH_P")
        self.spinBox_R5_ATH_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ATH_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R5_ATH_P, 5, 2, 1, 1)

        self.spinBox_R5_SPD_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R5_SPD_P.setObjectName(u"spinBox_R5_SPD_P")
        self.spinBox_R5_SPD_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_SPD_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R5_SPD_P, 5, 3, 1, 1)

        self.spinBox_R5_DUR_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R5_DUR_P.setObjectName(u"spinBox_R5_DUR_P")
        self.spinBox_R5_DUR_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_DUR_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R5_DUR_P, 5, 4, 1, 1)

        self.spinBox_R5_WE_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R5_WE_P.setObjectName(u"spinBox_R5_WE_P")
        self.spinBox_R5_WE_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_WE_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R5_WE_P, 5, 5, 1, 1)

        self.spinBox_R5_STA_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R5_STA_P.setObjectName(u"spinBox_R5_STA_P")
        self.spinBox_R5_STA_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STA_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R5_STA_P, 5, 6, 1, 1)

        self.spinBox_R5_STR_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R5_STR_P.setObjectName(u"spinBox_R5_STR_P")
        self.spinBox_R5_STR_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_STR_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R5_STR_P, 5, 7, 1, 1)

        self.spinBox_R5_BLK_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R5_BLK_P.setObjectName(u"spinBox_R5_BLK_P")
        self.spinBox_R5_BLK_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_BLK_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R5_BLK_P, 5, 8, 1, 1)

        self.spinBox_R5_TKL_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R5_TKL_P.setObjectName(u"spinBox_R5_TKL_P")
        self.spinBox_R5_TKL_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TKL_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R5_TKL_P, 5, 9, 1, 1)

        self.spinBox_R5_HAN_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R5_HAN_P.setObjectName(u"spinBox_R5_HAN_P")
        self.spinBox_R5_HAN_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_HAN_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R5_HAN_P, 5, 10, 1, 1)

        self.spinBox_R5_GI_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R5_GI_P.setObjectName(u"spinBox_R5_GI_P")
        self.spinBox_R5_GI_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_GI_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R5_GI_P, 5, 11, 1, 1)

        self.spinBox_R5_ELU_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R5_ELU_P.setObjectName(u"spinBox_R5_ELU_P")
        self.spinBox_R5_ELU_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_ELU_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R5_ELU_P, 5, 12, 1, 1)

        self.spinBox_R5_TEC_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R5_TEC_P.setObjectName(u"spinBox_R5_TEC_P")
        self.spinBox_R5_TEC_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R5_TEC_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R5_TEC_P, 5, 13, 1, 1)

        self.spinBox_R6_ATH_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R6_ATH_P.setObjectName(u"spinBox_R6_ATH_P")
        self.spinBox_R6_ATH_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ATH_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R6_ATH_P, 6, 2, 1, 1)

        self.spinBox_R6_SPD_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R6_SPD_P.setObjectName(u"spinBox_R6_SPD_P")
        self.spinBox_R6_SPD_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_SPD_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R6_SPD_P, 6, 3, 1, 1)

        self.spinBox_R6_DUR_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R6_DUR_P.setObjectName(u"spinBox_R6_DUR_P")
        self.spinBox_R6_DUR_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_DUR_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R6_DUR_P, 6, 4, 1, 1)

        self.spinBox_R6_WE_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R6_WE_P.setObjectName(u"spinBox_R6_WE_P")
        self.spinBox_R6_WE_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_WE_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R6_WE_P, 6, 5, 1, 1)

        self.spinBox_R6_STA_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R6_STA_P.setObjectName(u"spinBox_R6_STA_P")
        self.spinBox_R6_STA_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STA_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R6_STA_P, 6, 6, 1, 1)

        self.spinBox_R6_STR_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R6_STR_P.setObjectName(u"spinBox_R6_STR_P")
        self.spinBox_R6_STR_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_STR_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R6_STR_P, 6, 7, 1, 1)

        self.spinBox_R6_BLK_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R6_BLK_P.setObjectName(u"spinBox_R6_BLK_P")
        self.spinBox_R6_BLK_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_BLK_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R6_BLK_P, 6, 8, 1, 1)

        self.spinBox_R6_TKL_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R6_TKL_P.setObjectName(u"spinBox_R6_TKL_P")
        self.spinBox_R6_TKL_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TKL_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R6_TKL_P, 6, 9, 1, 1)

        self.spinBox_R6_HAN_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R6_HAN_P.setObjectName(u"spinBox_R6_HAN_P")
        self.spinBox_R6_HAN_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_HAN_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R6_HAN_P, 6, 10, 1, 1)

        self.spinBox_R6_GI_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R6_GI_P.setObjectName(u"spinBox_R6_GI_P")
        self.spinBox_R6_GI_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_GI_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R6_GI_P, 6, 11, 1, 1)

        self.spinBox_R6_ELU_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R6_ELU_P.setObjectName(u"spinBox_R6_ELU_P")
        self.spinBox_R6_ELU_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_ELU_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R6_ELU_P, 6, 12, 1, 1)

        self.spinBox_R6_TEC_P = QSpinBox(self.gridLayoutWidget_10)
        self.spinBox_R6_TEC_P.setObjectName(u"spinBox_R6_TEC_P")
        self.spinBox_R6_TEC_P.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_R6_TEC_P.setMaximum(100)

        self.gridLayout_10.addWidget(self.spinBox_R6_TEC_P, 6, 13, 1, 1)

        self.lineEdit_R1_P = QLineEdit(self.gridLayoutWidget_10)
        self.lineEdit_R1_P.setObjectName(u"lineEdit_R1_P")
        self.lineEdit_R1_P.setFont(font2)
        self.lineEdit_R1_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_R1_P, 1, 1, 1, 1)

        self.lineEdit_R2_P = QLineEdit(self.gridLayoutWidget_10)
        self.lineEdit_R2_P.setObjectName(u"lineEdit_R2_P")
        self.lineEdit_R2_P.setFont(font2)
        self.lineEdit_R2_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_R2_P, 2, 1, 1, 1)

        self.lineEdit_R3_P = QLineEdit(self.gridLayoutWidget_10)
        self.lineEdit_R3_P.setObjectName(u"lineEdit_R3_P")
        self.lineEdit_R3_P.setFont(font2)
        self.lineEdit_R3_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_R3_P, 3, 1, 1, 1)

        self.lineEdit_R4_P = QLineEdit(self.gridLayoutWidget_10)
        self.lineEdit_R4_P.setObjectName(u"lineEdit_R4_P")
        self.lineEdit_R4_P.setFont(font2)
        self.lineEdit_R4_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_R4_P, 4, 1, 1, 1)

        self.lineEdit_R5_P = QLineEdit(self.gridLayoutWidget_10)
        self.lineEdit_R5_P.setObjectName(u"lineEdit_R5_P")
        self.lineEdit_R5_P.setFont(font2)
        self.lineEdit_R5_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_R5_P, 5, 1, 1, 1)

        self.lineEdit_R6_P = QLineEdit(self.gridLayoutWidget_10)
        self.lineEdit_R6_P.setObjectName(u"lineEdit_R6_P")
        self.lineEdit_R6_P.setFont(font2)
        self.lineEdit_R6_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_R6_P, 6, 1, 1, 1)

        self.lcdNumber_R1_P = QLCDNumber(self.gridLayoutWidget_10)
        self.lcdNumber_R1_P.setObjectName(u"lcdNumber_R1_P")
        self.lcdNumber_R1_P.setDigitCount(3)
        self.lcdNumber_R1_P.setProperty("intValue", 0)

        self.gridLayout_10.addWidget(self.lcdNumber_R1_P, 1, 14, 1, 1)

        self.lcdNumber_R2_P = QLCDNumber(self.gridLayoutWidget_10)
        self.lcdNumber_R2_P.setObjectName(u"lcdNumber_R2_P")
        self.lcdNumber_R2_P.setDigitCount(3)
        self.lcdNumber_R2_P.setProperty("intValue", 0)

        self.gridLayout_10.addWidget(self.lcdNumber_R2_P, 2, 14, 1, 1)

        self.lcdNumber_R3_P = QLCDNumber(self.gridLayoutWidget_10)
        self.lcdNumber_R3_P.setObjectName(u"lcdNumber_R3_P")
        self.lcdNumber_R3_P.setDigitCount(3)
        self.lcdNumber_R3_P.setProperty("intValue", 0)

        self.gridLayout_10.addWidget(self.lcdNumber_R3_P, 3, 14, 1, 1)

        self.lcdNumber_R4_P = QLCDNumber(self.gridLayoutWidget_10)
        self.lcdNumber_R4_P.setObjectName(u"lcdNumber_R4_P")
        self.lcdNumber_R4_P.setDigitCount(3)
        self.lcdNumber_R4_P.setProperty("intValue", 0)

        self.gridLayout_10.addWidget(self.lcdNumber_R4_P, 4, 14, 1, 1)

        self.lcdNumber_R5_P = QLCDNumber(self.gridLayoutWidget_10)
        self.lcdNumber_R5_P.setObjectName(u"lcdNumber_R5_P")
        self.lcdNumber_R5_P.setDigitCount(3)
        self.lcdNumber_R5_P.setProperty("intValue", 0)

        self.gridLayout_10.addWidget(self.lcdNumber_R5_P, 5, 14, 1, 1)

        self.lcdNumber_R6_P = QLCDNumber(self.gridLayoutWidget_10)
        self.lcdNumber_R6_P.setObjectName(u"lcdNumber_R6_P")
        self.lcdNumber_R6_P.setDigitCount(3)
        self.lcdNumber_R6_P.setProperty("intValue", 0)

        self.gridLayout_10.addWidget(self.lcdNumber_R6_P, 6, 14, 1, 1)

        self.tabWidgetRoleRatings.addTab(self.P, "")
        self.label = QLabel(DialogRoleRatings)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 1041, 31))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: blue;")
        QWidget.setTabOrder(self.tabWidgetRoleRatings, self.lineEdit_R1_QB)
        QWidget.setTabOrder(self.lineEdit_R1_QB, self.spinBox_R1_ATH_QB)
        QWidget.setTabOrder(self.spinBox_R1_ATH_QB, self.spinBox_R1_SPD_QB)
        QWidget.setTabOrder(self.spinBox_R1_SPD_QB, self.spinBox_R1_DUR_QB)
        QWidget.setTabOrder(self.spinBox_R1_DUR_QB, self.spinBox_R1_WE_QB)
        QWidget.setTabOrder(self.spinBox_R1_WE_QB, self.spinBox_R1_STA_QB)
        QWidget.setTabOrder(self.spinBox_R1_STA_QB, self.spinBox_R1_STR_QB)
        QWidget.setTabOrder(self.spinBox_R1_STR_QB, self.spinBox_R1_BLK_QB)
        QWidget.setTabOrder(self.spinBox_R1_BLK_QB, self.spinBox_R1_TKL_QB)
        QWidget.setTabOrder(self.spinBox_R1_TKL_QB, self.spinBox_R1_HAN_QB)
        QWidget.setTabOrder(self.spinBox_R1_HAN_QB, self.spinBox_R1_GI_QB)
        QWidget.setTabOrder(self.spinBox_R1_GI_QB, self.spinBox_R1_ELU_QB)
        QWidget.setTabOrder(self.spinBox_R1_ELU_QB, self.spinBox_R1_TEC_QB)
        QWidget.setTabOrder(self.spinBox_R1_TEC_QB, self.lineEdit_R2_QB)
        QWidget.setTabOrder(self.lineEdit_R2_QB, self.spinBox_R2_ATH_QB)
        QWidget.setTabOrder(self.spinBox_R2_ATH_QB, self.spinBox_R2_SPD_QB)
        QWidget.setTabOrder(self.spinBox_R2_SPD_QB, self.spinBox_R2_DUR_QB)
        QWidget.setTabOrder(self.spinBox_R2_DUR_QB, self.spinBox_R2_WE_QB)
        QWidget.setTabOrder(self.spinBox_R2_WE_QB, self.spinBox_R2_STA_QB)
        QWidget.setTabOrder(self.spinBox_R2_STA_QB, self.spinBox_R2_STR_QB)
        QWidget.setTabOrder(self.spinBox_R2_STR_QB, self.spinBox_R2_BLK_QB)
        QWidget.setTabOrder(self.spinBox_R2_BLK_QB, self.spinBox_R2_TKL_QB)
        QWidget.setTabOrder(self.spinBox_R2_TKL_QB, self.spinBox_R2_HAN_QB)
        QWidget.setTabOrder(self.spinBox_R2_HAN_QB, self.spinBox_R2_GI_QB)
        QWidget.setTabOrder(self.spinBox_R2_GI_QB, self.spinBox_R2_ELU_QB)
        QWidget.setTabOrder(self.spinBox_R2_ELU_QB, self.spinBox_R2_TEC_QB)
        QWidget.setTabOrder(self.spinBox_R2_TEC_QB, self.lineEdit_R3_QB)
        QWidget.setTabOrder(self.lineEdit_R3_QB, self.spinBox_R3_ATH_QB)
        QWidget.setTabOrder(self.spinBox_R3_ATH_QB, self.spinBox_R3_SPD_QB)
        QWidget.setTabOrder(self.spinBox_R3_SPD_QB, self.spinBox_R3_DUR_QB)
        QWidget.setTabOrder(self.spinBox_R3_DUR_QB, self.spinBox_R3_WE_QB)
        QWidget.setTabOrder(self.spinBox_R3_WE_QB, self.spinBox_R3_STA_QB)
        QWidget.setTabOrder(self.spinBox_R3_STA_QB, self.spinBox_R3_STR_QB)
        QWidget.setTabOrder(self.spinBox_R3_STR_QB, self.spinBox_R3_BLK_QB)
        QWidget.setTabOrder(self.spinBox_R3_BLK_QB, self.spinBox_R3_TKL_QB)
        QWidget.setTabOrder(self.spinBox_R3_TKL_QB, self.spinBox_R3_HAN_QB)
        QWidget.setTabOrder(self.spinBox_R3_HAN_QB, self.spinBox_R3_GI_QB)
        QWidget.setTabOrder(self.spinBox_R3_GI_QB, self.spinBox_R3_ELU_QB)
        QWidget.setTabOrder(self.spinBox_R3_ELU_QB, self.spinBox_R3_TEC_QB)
        QWidget.setTabOrder(self.spinBox_R3_TEC_QB, self.lineEdit_R4_QB)
        QWidget.setTabOrder(self.lineEdit_R4_QB, self.spinBox_R4_ATH_QB)
        QWidget.setTabOrder(self.spinBox_R4_ATH_QB, self.spinBox_R4_SPD_QB)
        QWidget.setTabOrder(self.spinBox_R4_SPD_QB, self.spinBox_R4_DUR_QB)
        QWidget.setTabOrder(self.spinBox_R4_DUR_QB, self.spinBox_R4_WE_QB)
        QWidget.setTabOrder(self.spinBox_R4_WE_QB, self.spinBox_R4_STA_QB)
        QWidget.setTabOrder(self.spinBox_R4_STA_QB, self.spinBox_R4_STR_QB)
        QWidget.setTabOrder(self.spinBox_R4_STR_QB, self.spinBox_R4_BLK_QB)
        QWidget.setTabOrder(self.spinBox_R4_BLK_QB, self.spinBox_R4_TKL_QB)
        QWidget.setTabOrder(self.spinBox_R4_TKL_QB, self.spinBox_R4_HAN_QB)
        QWidget.setTabOrder(self.spinBox_R4_HAN_QB, self.spinBox_R4_GI_QB)
        QWidget.setTabOrder(self.spinBox_R4_GI_QB, self.spinBox_R4_ELU_QB)
        QWidget.setTabOrder(self.spinBox_R4_ELU_QB, self.spinBox_R4_TEC_QB)
        QWidget.setTabOrder(self.spinBox_R4_TEC_QB, self.lineEdit_R5_QB)
        QWidget.setTabOrder(self.lineEdit_R5_QB, self.spinBox_R5_ATH_QB)
        QWidget.setTabOrder(self.spinBox_R5_ATH_QB, self.spinBox_R5_SPD_QB)
        QWidget.setTabOrder(self.spinBox_R5_SPD_QB, self.spinBox_R5_DUR_QB)
        QWidget.setTabOrder(self.spinBox_R5_DUR_QB, self.spinBox_R5_WE_QB)
        QWidget.setTabOrder(self.spinBox_R5_WE_QB, self.spinBox_R5_STA_QB)
        QWidget.setTabOrder(self.spinBox_R5_STA_QB, self.spinBox_R5_STR_QB)
        QWidget.setTabOrder(self.spinBox_R5_STR_QB, self.spinBox_R5_BLK_QB)
        QWidget.setTabOrder(self.spinBox_R5_BLK_QB, self.spinBox_R5_TKL_QB)
        QWidget.setTabOrder(self.spinBox_R5_TKL_QB, self.spinBox_R5_HAN_QB)
        QWidget.setTabOrder(self.spinBox_R5_HAN_QB, self.spinBox_R5_GI_QB)
        QWidget.setTabOrder(self.spinBox_R5_GI_QB, self.spinBox_R5_ELU_QB)
        QWidget.setTabOrder(self.spinBox_R5_ELU_QB, self.spinBox_R5_TEC_QB)
        QWidget.setTabOrder(self.spinBox_R5_TEC_QB, self.lineEdit_R6_QB)
        QWidget.setTabOrder(self.lineEdit_R6_QB, self.spinBox_R6_ATH_QB)
        QWidget.setTabOrder(self.spinBox_R6_ATH_QB, self.spinBox_R6_SPD_QB)
        QWidget.setTabOrder(self.spinBox_R6_SPD_QB, self.spinBox_R6_DUR_QB)
        QWidget.setTabOrder(self.spinBox_R6_DUR_QB, self.spinBox_R6_WE_QB)
        QWidget.setTabOrder(self.spinBox_R6_WE_QB, self.spinBox_R6_STA_QB)
        QWidget.setTabOrder(self.spinBox_R6_STA_QB, self.spinBox_R6_STR_QB)
        QWidget.setTabOrder(self.spinBox_R6_STR_QB, self.spinBox_R6_BLK_QB)
        QWidget.setTabOrder(self.spinBox_R6_BLK_QB, self.spinBox_R6_TKL_QB)
        QWidget.setTabOrder(self.spinBox_R6_TKL_QB, self.spinBox_R6_HAN_QB)
        QWidget.setTabOrder(self.spinBox_R6_HAN_QB, self.spinBox_R6_GI_QB)
        QWidget.setTabOrder(self.spinBox_R6_GI_QB, self.spinBox_R6_ELU_QB)
        QWidget.setTabOrder(self.spinBox_R6_ELU_QB, self.spinBox_R6_TEC_QB)
        QWidget.setTabOrder(self.spinBox_R6_TEC_QB, self.lineEdit_R1_RB)
        QWidget.setTabOrder(self.lineEdit_R1_RB, self.spinBox_R1_ATH_RB)
        QWidget.setTabOrder(self.spinBox_R1_ATH_RB, self.spinBox_R1_SPD_RB)
        QWidget.setTabOrder(self.spinBox_R1_SPD_RB, self.spinBox_R1_DUR_RB)
        QWidget.setTabOrder(self.spinBox_R1_DUR_RB, self.spinBox_R1_WE_RB)
        QWidget.setTabOrder(self.spinBox_R1_WE_RB, self.spinBox_R1_STA_RB)
        QWidget.setTabOrder(self.spinBox_R1_STA_RB, self.spinBox_R1_STR_RB)
        QWidget.setTabOrder(self.spinBox_R1_STR_RB, self.spinBox_R1_BLK_RB)
        QWidget.setTabOrder(self.spinBox_R1_BLK_RB, self.spinBox_R1_TKL_RB)
        QWidget.setTabOrder(self.spinBox_R1_TKL_RB, self.spinBox_R1_HAN_RB)
        QWidget.setTabOrder(self.spinBox_R1_HAN_RB, self.spinBox_R1_GI_RB)
        QWidget.setTabOrder(self.spinBox_R1_GI_RB, self.spinBox_R1_ELU_RB)
        QWidget.setTabOrder(self.spinBox_R1_ELU_RB, self.spinBox_R1_TEC_RB)
        QWidget.setTabOrder(self.spinBox_R1_TEC_RB, self.lineEdit_R2_RB)
        QWidget.setTabOrder(self.lineEdit_R2_RB, self.spinBox_R2_ATH_RB)
        QWidget.setTabOrder(self.spinBox_R2_ATH_RB, self.spinBox_R2_SPD_RB)
        QWidget.setTabOrder(self.spinBox_R2_SPD_RB, self.spinBox_R2_DUR_RB)
        QWidget.setTabOrder(self.spinBox_R2_DUR_RB, self.spinBox_R2_WE_RB)
        QWidget.setTabOrder(self.spinBox_R2_WE_RB, self.spinBox_R2_STA_RB)
        QWidget.setTabOrder(self.spinBox_R2_STA_RB, self.spinBox_R2_STR_RB)
        QWidget.setTabOrder(self.spinBox_R2_STR_RB, self.spinBox_R2_BLK_RB)
        QWidget.setTabOrder(self.spinBox_R2_BLK_RB, self.spinBox_R2_TKL_RB)
        QWidget.setTabOrder(self.spinBox_R2_TKL_RB, self.spinBox_R2_HAN_RB)
        QWidget.setTabOrder(self.spinBox_R2_HAN_RB, self.spinBox_R2_GI_RB)
        QWidget.setTabOrder(self.spinBox_R2_GI_RB, self.spinBox_R2_ELU_RB)
        QWidget.setTabOrder(self.spinBox_R2_ELU_RB, self.spinBox_R2_TEC_RB)
        QWidget.setTabOrder(self.spinBox_R2_TEC_RB, self.lineEdit_R3_RB)
        QWidget.setTabOrder(self.lineEdit_R3_RB, self.spinBox_R3_ATH_RB)
        QWidget.setTabOrder(self.spinBox_R3_ATH_RB, self.spinBox_R3_SPD_RB)
        QWidget.setTabOrder(self.spinBox_R3_SPD_RB, self.spinBox_R3_DUR_RB)
        QWidget.setTabOrder(self.spinBox_R3_DUR_RB, self.spinBox_R3_WE_RB)
        QWidget.setTabOrder(self.spinBox_R3_WE_RB, self.spinBox_R3_STA_RB)
        QWidget.setTabOrder(self.spinBox_R3_STA_RB, self.spinBox_R3_STR_RB)
        QWidget.setTabOrder(self.spinBox_R3_STR_RB, self.spinBox_R3_BLK_RB)
        QWidget.setTabOrder(self.spinBox_R3_BLK_RB, self.spinBox_R3_TKL_RB)
        QWidget.setTabOrder(self.spinBox_R3_TKL_RB, self.spinBox_R3_HAN_RB)
        QWidget.setTabOrder(self.spinBox_R3_HAN_RB, self.spinBox_R3_GI_RB)
        QWidget.setTabOrder(self.spinBox_R3_GI_RB, self.spinBox_R3_ELU_RB)
        QWidget.setTabOrder(self.spinBox_R3_ELU_RB, self.spinBox_R3_TEC_RB)
        QWidget.setTabOrder(self.spinBox_R3_TEC_RB, self.lineEdit_R4_RB)
        QWidget.setTabOrder(self.lineEdit_R4_RB, self.spinBox_R4_ATH_RB)
        QWidget.setTabOrder(self.spinBox_R4_ATH_RB, self.spinBox_R4_SPD_RB)
        QWidget.setTabOrder(self.spinBox_R4_SPD_RB, self.spinBox_R4_DUR_RB)
        QWidget.setTabOrder(self.spinBox_R4_DUR_RB, self.spinBox_R4_WE_RB)
        QWidget.setTabOrder(self.spinBox_R4_WE_RB, self.spinBox_R4_STA_RB)
        QWidget.setTabOrder(self.spinBox_R4_STA_RB, self.spinBox_R4_STR_RB)
        QWidget.setTabOrder(self.spinBox_R4_STR_RB, self.spinBox_R4_BLK_RB)
        QWidget.setTabOrder(self.spinBox_R4_BLK_RB, self.spinBox_R4_TKL_RB)
        QWidget.setTabOrder(self.spinBox_R4_TKL_RB, self.spinBox_R4_HAN_RB)
        QWidget.setTabOrder(self.spinBox_R4_HAN_RB, self.spinBox_R4_GI_RB)
        QWidget.setTabOrder(self.spinBox_R4_GI_RB, self.spinBox_R4_ELU_RB)
        QWidget.setTabOrder(self.spinBox_R4_ELU_RB, self.spinBox_R4_TEC_RB)
        QWidget.setTabOrder(self.spinBox_R4_TEC_RB, self.lineEdit_R5_RB)
        QWidget.setTabOrder(self.lineEdit_R5_RB, self.spinBox_R5_ATH_RB)
        QWidget.setTabOrder(self.spinBox_R5_ATH_RB, self.spinBox_R5_SPD_RB)
        QWidget.setTabOrder(self.spinBox_R5_SPD_RB, self.spinBox_R5_DUR_RB)
        QWidget.setTabOrder(self.spinBox_R5_DUR_RB, self.spinBox_R5_WE_RB)
        QWidget.setTabOrder(self.spinBox_R5_WE_RB, self.spinBox_R5_STA_RB)
        QWidget.setTabOrder(self.spinBox_R5_STA_RB, self.spinBox_R5_STR_RB)
        QWidget.setTabOrder(self.spinBox_R5_STR_RB, self.spinBox_R5_BLK_RB)
        QWidget.setTabOrder(self.spinBox_R5_BLK_RB, self.spinBox_R5_TKL_RB)
        QWidget.setTabOrder(self.spinBox_R5_TKL_RB, self.spinBox_R5_HAN_RB)
        QWidget.setTabOrder(self.spinBox_R5_HAN_RB, self.spinBox_R5_GI_RB)
        QWidget.setTabOrder(self.spinBox_R5_GI_RB, self.spinBox_R5_ELU_RB)
        QWidget.setTabOrder(self.spinBox_R5_ELU_RB, self.spinBox_R5_TEC_RB)
        QWidget.setTabOrder(self.spinBox_R5_TEC_RB, self.lineEdit_R6_RB)
        QWidget.setTabOrder(self.lineEdit_R6_RB, self.spinBox_R6_ATH_RB)
        QWidget.setTabOrder(self.spinBox_R6_ATH_RB, self.spinBox_R6_SPD_RB)
        QWidget.setTabOrder(self.spinBox_R6_SPD_RB, self.spinBox_R6_DUR_RB)
        QWidget.setTabOrder(self.spinBox_R6_DUR_RB, self.spinBox_R6_WE_RB)
        QWidget.setTabOrder(self.spinBox_R6_WE_RB, self.spinBox_R6_STA_RB)
        QWidget.setTabOrder(self.spinBox_R6_STA_RB, self.spinBox_R6_STR_RB)
        QWidget.setTabOrder(self.spinBox_R6_STR_RB, self.spinBox_R6_BLK_RB)
        QWidget.setTabOrder(self.spinBox_R6_BLK_RB, self.spinBox_R6_TKL_RB)
        QWidget.setTabOrder(self.spinBox_R6_TKL_RB, self.spinBox_R6_HAN_RB)
        QWidget.setTabOrder(self.spinBox_R6_HAN_RB, self.spinBox_R6_GI_RB)
        QWidget.setTabOrder(self.spinBox_R6_GI_RB, self.spinBox_R6_ELU_RB)
        QWidget.setTabOrder(self.spinBox_R6_ELU_RB, self.spinBox_R6_TEC_RB)
        QWidget.setTabOrder(self.spinBox_R6_TEC_RB, self.lineEdit_R1_WR)
        QWidget.setTabOrder(self.lineEdit_R1_WR, self.spinBox_R1_ATH_WR)
        QWidget.setTabOrder(self.spinBox_R1_ATH_WR, self.spinBox_R1_SPD_WR)
        QWidget.setTabOrder(self.spinBox_R1_SPD_WR, self.spinBox_R1_DUR_WR)
        QWidget.setTabOrder(self.spinBox_R1_DUR_WR, self.spinBox_R1_WE_WR)
        QWidget.setTabOrder(self.spinBox_R1_WE_WR, self.spinBox_R1_STA_WR)
        QWidget.setTabOrder(self.spinBox_R1_STA_WR, self.spinBox_R1_STR_WR)
        QWidget.setTabOrder(self.spinBox_R1_STR_WR, self.spinBox_R1_BLK_WR)
        QWidget.setTabOrder(self.spinBox_R1_BLK_WR, self.spinBox_R1_TKL_WR)
        QWidget.setTabOrder(self.spinBox_R1_TKL_WR, self.spinBox_R1_HAN_WR)
        QWidget.setTabOrder(self.spinBox_R1_HAN_WR, self.spinBox_R1_GI_WR)
        QWidget.setTabOrder(self.spinBox_R1_GI_WR, self.spinBox_R1_ELU_WR)
        QWidget.setTabOrder(self.spinBox_R1_ELU_WR, self.spinBox_R1_TEC_WR)
        QWidget.setTabOrder(self.spinBox_R1_TEC_WR, self.lineEdit_R2_WR)
        QWidget.setTabOrder(self.lineEdit_R2_WR, self.spinBox_R2_ATH_WR)
        QWidget.setTabOrder(self.spinBox_R2_ATH_WR, self.spinBox_R2_SPD_WR)
        QWidget.setTabOrder(self.spinBox_R2_SPD_WR, self.spinBox_R2_DUR_WR)
        QWidget.setTabOrder(self.spinBox_R2_DUR_WR, self.spinBox_R2_WE_WR)
        QWidget.setTabOrder(self.spinBox_R2_WE_WR, self.spinBox_R2_STA_WR)
        QWidget.setTabOrder(self.spinBox_R2_STA_WR, self.spinBox_R2_STR_WR)
        QWidget.setTabOrder(self.spinBox_R2_STR_WR, self.spinBox_R2_BLK_WR)
        QWidget.setTabOrder(self.spinBox_R2_BLK_WR, self.spinBox_R2_TKL_WR)
        QWidget.setTabOrder(self.spinBox_R2_TKL_WR, self.spinBox_R2_HAN_WR)
        QWidget.setTabOrder(self.spinBox_R2_HAN_WR, self.spinBox_R2_GI_WR)
        QWidget.setTabOrder(self.spinBox_R2_GI_WR, self.spinBox_R2_ELU_WR)
        QWidget.setTabOrder(self.spinBox_R2_ELU_WR, self.spinBox_R2_TEC_WR)
        QWidget.setTabOrder(self.spinBox_R2_TEC_WR, self.lineEdit_R3_WR)
        QWidget.setTabOrder(self.lineEdit_R3_WR, self.spinBox_R3_ATH_WR)
        QWidget.setTabOrder(self.spinBox_R3_ATH_WR, self.spinBox_R3_SPD_WR)
        QWidget.setTabOrder(self.spinBox_R3_SPD_WR, self.spinBox_R3_DUR_WR)
        QWidget.setTabOrder(self.spinBox_R3_DUR_WR, self.spinBox_R3_WE_WR)
        QWidget.setTabOrder(self.spinBox_R3_WE_WR, self.spinBox_R3_STA_WR)
        QWidget.setTabOrder(self.spinBox_R3_STA_WR, self.spinBox_R3_STR_WR)
        QWidget.setTabOrder(self.spinBox_R3_STR_WR, self.spinBox_R3_BLK_WR)
        QWidget.setTabOrder(self.spinBox_R3_BLK_WR, self.spinBox_R3_TKL_WR)
        QWidget.setTabOrder(self.spinBox_R3_TKL_WR, self.spinBox_R3_HAN_WR)
        QWidget.setTabOrder(self.spinBox_R3_HAN_WR, self.spinBox_R3_GI_WR)
        QWidget.setTabOrder(self.spinBox_R3_GI_WR, self.spinBox_R3_ELU_WR)
        QWidget.setTabOrder(self.spinBox_R3_ELU_WR, self.spinBox_R3_TEC_WR)
        QWidget.setTabOrder(self.spinBox_R3_TEC_WR, self.lineEdit_R4_WR)
        QWidget.setTabOrder(self.lineEdit_R4_WR, self.spinBox_R4_ATH_WR)
        QWidget.setTabOrder(self.spinBox_R4_ATH_WR, self.spinBox_R4_SPD_WR)
        QWidget.setTabOrder(self.spinBox_R4_SPD_WR, self.spinBox_R4_DUR_WR)
        QWidget.setTabOrder(self.spinBox_R4_DUR_WR, self.spinBox_R4_WE_WR)
        QWidget.setTabOrder(self.spinBox_R4_WE_WR, self.spinBox_R4_STA_WR)
        QWidget.setTabOrder(self.spinBox_R4_STA_WR, self.spinBox_R4_STR_WR)
        QWidget.setTabOrder(self.spinBox_R4_STR_WR, self.spinBox_R4_BLK_WR)
        QWidget.setTabOrder(self.spinBox_R4_BLK_WR, self.spinBox_R4_TKL_WR)
        QWidget.setTabOrder(self.spinBox_R4_TKL_WR, self.spinBox_R4_HAN_WR)
        QWidget.setTabOrder(self.spinBox_R4_HAN_WR, self.spinBox_R4_GI_WR)
        QWidget.setTabOrder(self.spinBox_R4_GI_WR, self.spinBox_R4_ELU_WR)
        QWidget.setTabOrder(self.spinBox_R4_ELU_WR, self.spinBox_R4_TEC_WR)
        QWidget.setTabOrder(self.spinBox_R4_TEC_WR, self.lineEdit_R5_WR)
        QWidget.setTabOrder(self.lineEdit_R5_WR, self.spinBox_R5_ATH_WR)
        QWidget.setTabOrder(self.spinBox_R5_ATH_WR, self.spinBox_R5_SPD_WR)
        QWidget.setTabOrder(self.spinBox_R5_SPD_WR, self.spinBox_R5_DUR_WR)
        QWidget.setTabOrder(self.spinBox_R5_DUR_WR, self.spinBox_R5_WE_WR)
        QWidget.setTabOrder(self.spinBox_R5_WE_WR, self.spinBox_R5_STA_WR)
        QWidget.setTabOrder(self.spinBox_R5_STA_WR, self.spinBox_R5_STR_WR)
        QWidget.setTabOrder(self.spinBox_R5_STR_WR, self.spinBox_R5_BLK_WR)
        QWidget.setTabOrder(self.spinBox_R5_BLK_WR, self.spinBox_R5_TKL_WR)
        QWidget.setTabOrder(self.spinBox_R5_TKL_WR, self.spinBox_R5_HAN_WR)
        QWidget.setTabOrder(self.spinBox_R5_HAN_WR, self.spinBox_R5_GI_WR)
        QWidget.setTabOrder(self.spinBox_R5_GI_WR, self.spinBox_R5_ELU_WR)
        QWidget.setTabOrder(self.spinBox_R5_ELU_WR, self.spinBox_R5_TEC_WR)
        QWidget.setTabOrder(self.spinBox_R5_TEC_WR, self.lineEdit_R6_WR)
        QWidget.setTabOrder(self.lineEdit_R6_WR, self.spinBox_R6_ATH_WR)
        QWidget.setTabOrder(self.spinBox_R6_ATH_WR, self.spinBox_R6_SPD_WR)
        QWidget.setTabOrder(self.spinBox_R6_SPD_WR, self.spinBox_R6_DUR_WR)
        QWidget.setTabOrder(self.spinBox_R6_DUR_WR, self.spinBox_R6_WE_WR)
        QWidget.setTabOrder(self.spinBox_R6_WE_WR, self.spinBox_R6_STA_WR)
        QWidget.setTabOrder(self.spinBox_R6_STA_WR, self.spinBox_R6_STR_WR)
        QWidget.setTabOrder(self.spinBox_R6_STR_WR, self.spinBox_R6_BLK_WR)
        QWidget.setTabOrder(self.spinBox_R6_BLK_WR, self.spinBox_R6_TKL_WR)
        QWidget.setTabOrder(self.spinBox_R6_TKL_WR, self.spinBox_R6_HAN_WR)
        QWidget.setTabOrder(self.spinBox_R6_HAN_WR, self.spinBox_R6_GI_WR)
        QWidget.setTabOrder(self.spinBox_R6_GI_WR, self.spinBox_R6_ELU_WR)
        QWidget.setTabOrder(self.spinBox_R6_ELU_WR, self.spinBox_R6_TEC_WR)
        QWidget.setTabOrder(self.spinBox_R6_TEC_WR, self.lineEdit_R1_TE)
        QWidget.setTabOrder(self.lineEdit_R1_TE, self.spinBox_R1_ATH_TE)
        QWidget.setTabOrder(self.spinBox_R1_ATH_TE, self.spinBox_R1_SPD_TE)
        QWidget.setTabOrder(self.spinBox_R1_SPD_TE, self.spinBox_R1_DUR_TE)
        QWidget.setTabOrder(self.spinBox_R1_DUR_TE, self.spinBox_R1_WE_TE)
        QWidget.setTabOrder(self.spinBox_R1_WE_TE, self.spinBox_R1_STA_TE)
        QWidget.setTabOrder(self.spinBox_R1_STA_TE, self.spinBox_R1_STR_TE)
        QWidget.setTabOrder(self.spinBox_R1_STR_TE, self.spinBox_R1_BLK_TE)
        QWidget.setTabOrder(self.spinBox_R1_BLK_TE, self.spinBox_R1_TKL_TE)
        QWidget.setTabOrder(self.spinBox_R1_TKL_TE, self.spinBox_R1_HAN_TE)
        QWidget.setTabOrder(self.spinBox_R1_HAN_TE, self.spinBox_R1_GI_TE)
        QWidget.setTabOrder(self.spinBox_R1_GI_TE, self.spinBox_R1_ELU_TE)
        QWidget.setTabOrder(self.spinBox_R1_ELU_TE, self.spinBox_R1_TEC_TE)
        QWidget.setTabOrder(self.spinBox_R1_TEC_TE, self.lineEdit_R2_TE)
        QWidget.setTabOrder(self.lineEdit_R2_TE, self.spinBox_R2_ATH_TE)
        QWidget.setTabOrder(self.spinBox_R2_ATH_TE, self.spinBox_R2_SPD_TE)
        QWidget.setTabOrder(self.spinBox_R2_SPD_TE, self.spinBox_R2_DUR_TE)
        QWidget.setTabOrder(self.spinBox_R2_DUR_TE, self.spinBox_R2_WE_TE)
        QWidget.setTabOrder(self.spinBox_R2_WE_TE, self.spinBox_R2_STA_TE)
        QWidget.setTabOrder(self.spinBox_R2_STA_TE, self.spinBox_R2_STR_TE)
        QWidget.setTabOrder(self.spinBox_R2_STR_TE, self.spinBox_R2_BLK_TE)
        QWidget.setTabOrder(self.spinBox_R2_BLK_TE, self.spinBox_R2_TKL_TE)
        QWidget.setTabOrder(self.spinBox_R2_TKL_TE, self.spinBox_R2_HAN_TE)
        QWidget.setTabOrder(self.spinBox_R2_HAN_TE, self.spinBox_R2_GI_TE)
        QWidget.setTabOrder(self.spinBox_R2_GI_TE, self.spinBox_R2_ELU_TE)
        QWidget.setTabOrder(self.spinBox_R2_ELU_TE, self.spinBox_R2_TEC_TE)
        QWidget.setTabOrder(self.spinBox_R2_TEC_TE, self.lineEdit_R3_TE)
        QWidget.setTabOrder(self.lineEdit_R3_TE, self.spinBox_R3_ATH_TE)
        QWidget.setTabOrder(self.spinBox_R3_ATH_TE, self.spinBox_R3_SPD_TE)
        QWidget.setTabOrder(self.spinBox_R3_SPD_TE, self.spinBox_R3_DUR_TE)
        QWidget.setTabOrder(self.spinBox_R3_DUR_TE, self.spinBox_R3_WE_TE)
        QWidget.setTabOrder(self.spinBox_R3_WE_TE, self.spinBox_R3_STA_TE)
        QWidget.setTabOrder(self.spinBox_R3_STA_TE, self.spinBox_R3_STR_TE)
        QWidget.setTabOrder(self.spinBox_R3_STR_TE, self.spinBox_R3_BLK_TE)
        QWidget.setTabOrder(self.spinBox_R3_BLK_TE, self.spinBox_R3_TKL_TE)
        QWidget.setTabOrder(self.spinBox_R3_TKL_TE, self.spinBox_R3_HAN_TE)
        QWidget.setTabOrder(self.spinBox_R3_HAN_TE, self.spinBox_R3_GI_TE)
        QWidget.setTabOrder(self.spinBox_R3_GI_TE, self.spinBox_R3_ELU_TE)
        QWidget.setTabOrder(self.spinBox_R3_ELU_TE, self.spinBox_R3_TEC_TE)
        QWidget.setTabOrder(self.spinBox_R3_TEC_TE, self.lineEdit_R4_TE)
        QWidget.setTabOrder(self.lineEdit_R4_TE, self.spinBox_R4_ATH_TE)
        QWidget.setTabOrder(self.spinBox_R4_ATH_TE, self.spinBox_R4_SPD_TE)
        QWidget.setTabOrder(self.spinBox_R4_SPD_TE, self.spinBox_R4_DUR_TE)
        QWidget.setTabOrder(self.spinBox_R4_DUR_TE, self.spinBox_R4_WE_TE)
        QWidget.setTabOrder(self.spinBox_R4_WE_TE, self.spinBox_R4_STA_TE)
        QWidget.setTabOrder(self.spinBox_R4_STA_TE, self.spinBox_R4_STR_TE)
        QWidget.setTabOrder(self.spinBox_R4_STR_TE, self.spinBox_R4_BLK_TE)
        QWidget.setTabOrder(self.spinBox_R4_BLK_TE, self.spinBox_R4_TKL_TE)
        QWidget.setTabOrder(self.spinBox_R4_TKL_TE, self.spinBox_R4_HAN_TE)
        QWidget.setTabOrder(self.spinBox_R4_HAN_TE, self.spinBox_R4_GI_TE)
        QWidget.setTabOrder(self.spinBox_R4_GI_TE, self.spinBox_R4_ELU_TE)
        QWidget.setTabOrder(self.spinBox_R4_ELU_TE, self.spinBox_R4_TEC_TE)
        QWidget.setTabOrder(self.spinBox_R4_TEC_TE, self.lineEdit_R5_TE)
        QWidget.setTabOrder(self.lineEdit_R5_TE, self.spinBox_R5_ATH_TE)
        QWidget.setTabOrder(self.spinBox_R5_ATH_TE, self.spinBox_R5_SPD_TE)
        QWidget.setTabOrder(self.spinBox_R5_SPD_TE, self.spinBox_R5_DUR_TE)
        QWidget.setTabOrder(self.spinBox_R5_DUR_TE, self.spinBox_R5_WE_TE)
        QWidget.setTabOrder(self.spinBox_R5_WE_TE, self.spinBox_R5_STA_TE)
        QWidget.setTabOrder(self.spinBox_R5_STA_TE, self.spinBox_R5_STR_TE)
        QWidget.setTabOrder(self.spinBox_R5_STR_TE, self.spinBox_R5_BLK_TE)
        QWidget.setTabOrder(self.spinBox_R5_BLK_TE, self.spinBox_R5_TKL_TE)
        QWidget.setTabOrder(self.spinBox_R5_TKL_TE, self.spinBox_R5_HAN_TE)
        QWidget.setTabOrder(self.spinBox_R5_HAN_TE, self.spinBox_R5_GI_TE)
        QWidget.setTabOrder(self.spinBox_R5_GI_TE, self.spinBox_R5_ELU_TE)
        QWidget.setTabOrder(self.spinBox_R5_ELU_TE, self.spinBox_R5_TEC_TE)
        QWidget.setTabOrder(self.spinBox_R5_TEC_TE, self.lineEdit_R6_TE)
        QWidget.setTabOrder(self.lineEdit_R6_TE, self.spinBox_R6_ATH_TE)
        QWidget.setTabOrder(self.spinBox_R6_ATH_TE, self.spinBox_R6_SPD_TE)
        QWidget.setTabOrder(self.spinBox_R6_SPD_TE, self.spinBox_R6_DUR_TE)
        QWidget.setTabOrder(self.spinBox_R6_DUR_TE, self.spinBox_R6_WE_TE)
        QWidget.setTabOrder(self.spinBox_R6_WE_TE, self.spinBox_R6_STA_TE)
        QWidget.setTabOrder(self.spinBox_R6_STA_TE, self.spinBox_R6_STR_TE)
        QWidget.setTabOrder(self.spinBox_R6_STR_TE, self.spinBox_R6_BLK_TE)
        QWidget.setTabOrder(self.spinBox_R6_BLK_TE, self.spinBox_R6_TKL_TE)
        QWidget.setTabOrder(self.spinBox_R6_TKL_TE, self.spinBox_R6_HAN_TE)
        QWidget.setTabOrder(self.spinBox_R6_HAN_TE, self.spinBox_R6_GI_TE)
        QWidget.setTabOrder(self.spinBox_R6_GI_TE, self.spinBox_R6_ELU_TE)
        QWidget.setTabOrder(self.spinBox_R6_ELU_TE, self.spinBox_R6_TEC_TE)
        QWidget.setTabOrder(self.spinBox_R6_TEC_TE, self.lineEdit_R1_OL)
        QWidget.setTabOrder(self.lineEdit_R1_OL, self.spinBox_R1_ATH_OL)
        QWidget.setTabOrder(self.spinBox_R1_ATH_OL, self.spinBox_R1_SPD_OL)
        QWidget.setTabOrder(self.spinBox_R1_SPD_OL, self.spinBox_R1_DUR_OL)
        QWidget.setTabOrder(self.spinBox_R1_DUR_OL, self.spinBox_R1_WE_OL)
        QWidget.setTabOrder(self.spinBox_R1_WE_OL, self.spinBox_R1_STA_OL)
        QWidget.setTabOrder(self.spinBox_R1_STA_OL, self.spinBox_R1_STR_OL)
        QWidget.setTabOrder(self.spinBox_R1_STR_OL, self.spinBox_R1_BLK_OL)
        QWidget.setTabOrder(self.spinBox_R1_BLK_OL, self.spinBox_R1_TKL_OL)
        QWidget.setTabOrder(self.spinBox_R1_TKL_OL, self.spinBox_R1_HAN_OL)
        QWidget.setTabOrder(self.spinBox_R1_HAN_OL, self.spinBox_R1_GI_OL)
        QWidget.setTabOrder(self.spinBox_R1_GI_OL, self.spinBox_R1_ELU_OL)
        QWidget.setTabOrder(self.spinBox_R1_ELU_OL, self.spinBox_R1_TEC_OL)
        QWidget.setTabOrder(self.spinBox_R1_TEC_OL, self.lineEdit_R2_OL)
        QWidget.setTabOrder(self.lineEdit_R2_OL, self.spinBox_R2_ATH_OL)
        QWidget.setTabOrder(self.spinBox_R2_ATH_OL, self.spinBox_R2_SPD_OL)
        QWidget.setTabOrder(self.spinBox_R2_SPD_OL, self.spinBox_R2_DUR_OL)
        QWidget.setTabOrder(self.spinBox_R2_DUR_OL, self.spinBox_R2_WE_OL)
        QWidget.setTabOrder(self.spinBox_R2_WE_OL, self.spinBox_R2_STA_OL)
        QWidget.setTabOrder(self.spinBox_R2_STA_OL, self.spinBox_R2_STR_OL)
        QWidget.setTabOrder(self.spinBox_R2_STR_OL, self.spinBox_R2_BLK_OL)
        QWidget.setTabOrder(self.spinBox_R2_BLK_OL, self.spinBox_R2_TKL_OL)
        QWidget.setTabOrder(self.spinBox_R2_TKL_OL, self.spinBox_R2_HAN_OL)
        QWidget.setTabOrder(self.spinBox_R2_HAN_OL, self.spinBox_R2_GI_OL)
        QWidget.setTabOrder(self.spinBox_R2_GI_OL, self.spinBox_R2_ELU_OL)
        QWidget.setTabOrder(self.spinBox_R2_ELU_OL, self.spinBox_R2_TEC_OL)
        QWidget.setTabOrder(self.spinBox_R2_TEC_OL, self.lineEdit_R3_OL)
        QWidget.setTabOrder(self.lineEdit_R3_OL, self.spinBox_R3_ATH_OL)
        QWidget.setTabOrder(self.spinBox_R3_ATH_OL, self.spinBox_R3_SPD_OL)
        QWidget.setTabOrder(self.spinBox_R3_SPD_OL, self.spinBox_R3_DUR_OL)
        QWidget.setTabOrder(self.spinBox_R3_DUR_OL, self.spinBox_R3_WE_OL)
        QWidget.setTabOrder(self.spinBox_R3_WE_OL, self.spinBox_R3_STA_OL)
        QWidget.setTabOrder(self.spinBox_R3_STA_OL, self.spinBox_R3_STR_OL)
        QWidget.setTabOrder(self.spinBox_R3_STR_OL, self.spinBox_R3_BLK_OL)
        QWidget.setTabOrder(self.spinBox_R3_BLK_OL, self.spinBox_R3_TKL_OL)
        QWidget.setTabOrder(self.spinBox_R3_TKL_OL, self.spinBox_R3_HAN_OL)
        QWidget.setTabOrder(self.spinBox_R3_HAN_OL, self.spinBox_R3_GI_OL)
        QWidget.setTabOrder(self.spinBox_R3_GI_OL, self.spinBox_R3_ELU_OL)
        QWidget.setTabOrder(self.spinBox_R3_ELU_OL, self.spinBox_R3_TEC_OL)
        QWidget.setTabOrder(self.spinBox_R3_TEC_OL, self.lineEdit_R4_OL)
        QWidget.setTabOrder(self.lineEdit_R4_OL, self.spinBox_R4_ATH_OL)
        QWidget.setTabOrder(self.spinBox_R4_ATH_OL, self.spinBox_R4_SPD_OL)
        QWidget.setTabOrder(self.spinBox_R4_SPD_OL, self.spinBox_R4_DUR_OL)
        QWidget.setTabOrder(self.spinBox_R4_DUR_OL, self.spinBox_R4_WE_OL)
        QWidget.setTabOrder(self.spinBox_R4_WE_OL, self.spinBox_R4_STA_OL)
        QWidget.setTabOrder(self.spinBox_R4_STA_OL, self.spinBox_R4_STR_OL)
        QWidget.setTabOrder(self.spinBox_R4_STR_OL, self.spinBox_R4_BLK_OL)
        QWidget.setTabOrder(self.spinBox_R4_BLK_OL, self.spinBox_R4_TKL_OL)
        QWidget.setTabOrder(self.spinBox_R4_TKL_OL, self.spinBox_R4_HAN_OL)
        QWidget.setTabOrder(self.spinBox_R4_HAN_OL, self.spinBox_R4_GI_OL)
        QWidget.setTabOrder(self.spinBox_R4_GI_OL, self.spinBox_R4_ELU_OL)
        QWidget.setTabOrder(self.spinBox_R4_ELU_OL, self.spinBox_R4_TEC_OL)
        QWidget.setTabOrder(self.spinBox_R4_TEC_OL, self.lineEdit_R5_OL)
        QWidget.setTabOrder(self.lineEdit_R5_OL, self.spinBox_R5_ATH_OL)
        QWidget.setTabOrder(self.spinBox_R5_ATH_OL, self.spinBox_R5_SPD_OL)
        QWidget.setTabOrder(self.spinBox_R5_SPD_OL, self.spinBox_R5_DUR_OL)
        QWidget.setTabOrder(self.spinBox_R5_DUR_OL, self.spinBox_R5_WE_OL)
        QWidget.setTabOrder(self.spinBox_R5_WE_OL, self.spinBox_R5_STA_OL)
        QWidget.setTabOrder(self.spinBox_R5_STA_OL, self.spinBox_R5_STR_OL)
        QWidget.setTabOrder(self.spinBox_R5_STR_OL, self.spinBox_R5_BLK_OL)
        QWidget.setTabOrder(self.spinBox_R5_BLK_OL, self.spinBox_R5_TKL_OL)
        QWidget.setTabOrder(self.spinBox_R5_TKL_OL, self.spinBox_R5_HAN_OL)
        QWidget.setTabOrder(self.spinBox_R5_HAN_OL, self.spinBox_R5_GI_OL)
        QWidget.setTabOrder(self.spinBox_R5_GI_OL, self.spinBox_R5_ELU_OL)
        QWidget.setTabOrder(self.spinBox_R5_ELU_OL, self.spinBox_R5_TEC_OL)
        QWidget.setTabOrder(self.spinBox_R5_TEC_OL, self.lineEdit_R6_OL)
        QWidget.setTabOrder(self.lineEdit_R6_OL, self.spinBox_R6_ATH_OL)
        QWidget.setTabOrder(self.spinBox_R6_ATH_OL, self.spinBox_R6_SPD_OL)
        QWidget.setTabOrder(self.spinBox_R6_SPD_OL, self.spinBox_R6_DUR_OL)
        QWidget.setTabOrder(self.spinBox_R6_DUR_OL, self.spinBox_R6_WE_OL)
        QWidget.setTabOrder(self.spinBox_R6_WE_OL, self.spinBox_R6_STA_OL)
        QWidget.setTabOrder(self.spinBox_R6_STA_OL, self.spinBox_R6_STR_OL)
        QWidget.setTabOrder(self.spinBox_R6_STR_OL, self.spinBox_R6_BLK_OL)
        QWidget.setTabOrder(self.spinBox_R6_BLK_OL, self.spinBox_R6_TKL_OL)
        QWidget.setTabOrder(self.spinBox_R6_TKL_OL, self.spinBox_R6_HAN_OL)
        QWidget.setTabOrder(self.spinBox_R6_HAN_OL, self.spinBox_R6_GI_OL)
        QWidget.setTabOrder(self.spinBox_R6_GI_OL, self.spinBox_R6_ELU_OL)
        QWidget.setTabOrder(self.spinBox_R6_ELU_OL, self.spinBox_R6_TEC_OL)
        QWidget.setTabOrder(self.spinBox_R6_TEC_OL, self.lineEdit_R1_DL)
        QWidget.setTabOrder(self.lineEdit_R1_DL, self.spinBox_R1_ATH_DL)
        QWidget.setTabOrder(self.spinBox_R1_ATH_DL, self.spinBox_R1_SPD_DL)
        QWidget.setTabOrder(self.spinBox_R1_SPD_DL, self.spinBox_R1_DUR_DL)
        QWidget.setTabOrder(self.spinBox_R1_DUR_DL, self.spinBox_R1_WE_DL)
        QWidget.setTabOrder(self.spinBox_R1_WE_DL, self.spinBox_R1_STA_DL)
        QWidget.setTabOrder(self.spinBox_R1_STA_DL, self.spinBox_R1_STR_DL)
        QWidget.setTabOrder(self.spinBox_R1_STR_DL, self.spinBox_R1_BLK_DL)
        QWidget.setTabOrder(self.spinBox_R1_BLK_DL, self.spinBox_R1_TKL_DL)
        QWidget.setTabOrder(self.spinBox_R1_TKL_DL, self.spinBox_R1_HAN_DL)
        QWidget.setTabOrder(self.spinBox_R1_HAN_DL, self.spinBox_R1_GI_DL)
        QWidget.setTabOrder(self.spinBox_R1_GI_DL, self.spinBox_R1_ELU_DL)
        QWidget.setTabOrder(self.spinBox_R1_ELU_DL, self.spinBox_R1_TEC_DL)
        QWidget.setTabOrder(self.spinBox_R1_TEC_DL, self.lineEdit_R2_DL)
        QWidget.setTabOrder(self.lineEdit_R2_DL, self.spinBox_R2_ATH_DL)
        QWidget.setTabOrder(self.spinBox_R2_ATH_DL, self.spinBox_R2_SPD_DL)
        QWidget.setTabOrder(self.spinBox_R2_SPD_DL, self.spinBox_R2_DUR_DL)
        QWidget.setTabOrder(self.spinBox_R2_DUR_DL, self.spinBox_R2_WE_DL)
        QWidget.setTabOrder(self.spinBox_R2_WE_DL, self.spinBox_R2_STA_DL)
        QWidget.setTabOrder(self.spinBox_R2_STA_DL, self.spinBox_R2_STR_DL)
        QWidget.setTabOrder(self.spinBox_R2_STR_DL, self.spinBox_R2_BLK_DL)
        QWidget.setTabOrder(self.spinBox_R2_BLK_DL, self.spinBox_R2_TKL_DL)
        QWidget.setTabOrder(self.spinBox_R2_TKL_DL, self.spinBox_R2_HAN_DL)
        QWidget.setTabOrder(self.spinBox_R2_HAN_DL, self.spinBox_R2_GI_DL)
        QWidget.setTabOrder(self.spinBox_R2_GI_DL, self.spinBox_R2_ELU_DL)
        QWidget.setTabOrder(self.spinBox_R2_ELU_DL, self.spinBox_R2_TEC_DL)
        QWidget.setTabOrder(self.spinBox_R2_TEC_DL, self.lineEdit_R3_DL)
        QWidget.setTabOrder(self.lineEdit_R3_DL, self.spinBox_R3_ATH_DL)
        QWidget.setTabOrder(self.spinBox_R3_ATH_DL, self.spinBox_R3_SPD_DL)
        QWidget.setTabOrder(self.spinBox_R3_SPD_DL, self.spinBox_R3_DUR_DL)
        QWidget.setTabOrder(self.spinBox_R3_DUR_DL, self.spinBox_R3_WE_DL)
        QWidget.setTabOrder(self.spinBox_R3_WE_DL, self.spinBox_R3_STA_DL)
        QWidget.setTabOrder(self.spinBox_R3_STA_DL, self.spinBox_R3_STR_DL)
        QWidget.setTabOrder(self.spinBox_R3_STR_DL, self.spinBox_R3_BLK_DL)
        QWidget.setTabOrder(self.spinBox_R3_BLK_DL, self.spinBox_R3_TKL_DL)
        QWidget.setTabOrder(self.spinBox_R3_TKL_DL, self.spinBox_R3_HAN_DL)
        QWidget.setTabOrder(self.spinBox_R3_HAN_DL, self.spinBox_R3_GI_DL)
        QWidget.setTabOrder(self.spinBox_R3_GI_DL, self.spinBox_R3_ELU_DL)
        QWidget.setTabOrder(self.spinBox_R3_ELU_DL, self.spinBox_R3_TEC_DL)
        QWidget.setTabOrder(self.spinBox_R3_TEC_DL, self.lineEdit_R4_DL)
        QWidget.setTabOrder(self.lineEdit_R4_DL, self.spinBox_R4_ATH_DL)
        QWidget.setTabOrder(self.spinBox_R4_ATH_DL, self.spinBox_R4_SPD_DL)
        QWidget.setTabOrder(self.spinBox_R4_SPD_DL, self.spinBox_R4_DUR_DL)
        QWidget.setTabOrder(self.spinBox_R4_DUR_DL, self.spinBox_R4_WE_DL)
        QWidget.setTabOrder(self.spinBox_R4_WE_DL, self.spinBox_R4_STA_DL)
        QWidget.setTabOrder(self.spinBox_R4_STA_DL, self.spinBox_R4_STR_DL)
        QWidget.setTabOrder(self.spinBox_R4_STR_DL, self.spinBox_R4_BLK_DL)
        QWidget.setTabOrder(self.spinBox_R4_BLK_DL, self.spinBox_R4_TKL_DL)
        QWidget.setTabOrder(self.spinBox_R4_TKL_DL, self.spinBox_R4_HAN_DL)
        QWidget.setTabOrder(self.spinBox_R4_HAN_DL, self.spinBox_R4_GI_DL)
        QWidget.setTabOrder(self.spinBox_R4_GI_DL, self.spinBox_R4_ELU_DL)
        QWidget.setTabOrder(self.spinBox_R4_ELU_DL, self.spinBox_R4_TEC_DL)
        QWidget.setTabOrder(self.spinBox_R4_TEC_DL, self.lineEdit_R5_DL)
        QWidget.setTabOrder(self.lineEdit_R5_DL, self.spinBox_R5_ATH_DL)
        QWidget.setTabOrder(self.spinBox_R5_ATH_DL, self.spinBox_R5_SPD_DL)
        QWidget.setTabOrder(self.spinBox_R5_SPD_DL, self.spinBox_R5_DUR_DL)
        QWidget.setTabOrder(self.spinBox_R5_DUR_DL, self.spinBox_R5_WE_DL)
        QWidget.setTabOrder(self.spinBox_R5_WE_DL, self.spinBox_R5_STA_DL)
        QWidget.setTabOrder(self.spinBox_R5_STA_DL, self.spinBox_R5_STR_DL)
        QWidget.setTabOrder(self.spinBox_R5_STR_DL, self.spinBox_R5_BLK_DL)
        QWidget.setTabOrder(self.spinBox_R5_BLK_DL, self.spinBox_R5_TKL_DL)
        QWidget.setTabOrder(self.spinBox_R5_TKL_DL, self.spinBox_R5_HAN_DL)
        QWidget.setTabOrder(self.spinBox_R5_HAN_DL, self.spinBox_R5_GI_DL)
        QWidget.setTabOrder(self.spinBox_R5_GI_DL, self.spinBox_R5_ELU_DL)
        QWidget.setTabOrder(self.spinBox_R5_ELU_DL, self.spinBox_R5_TEC_DL)
        QWidget.setTabOrder(self.spinBox_R5_TEC_DL, self.lineEdit_R6_DL)
        QWidget.setTabOrder(self.lineEdit_R6_DL, self.spinBox_R6_ATH_DL)
        QWidget.setTabOrder(self.spinBox_R6_ATH_DL, self.spinBox_R6_SPD_DL)
        QWidget.setTabOrder(self.spinBox_R6_SPD_DL, self.spinBox_R6_DUR_DL)
        QWidget.setTabOrder(self.spinBox_R6_DUR_DL, self.spinBox_R6_WE_DL)
        QWidget.setTabOrder(self.spinBox_R6_WE_DL, self.spinBox_R6_STA_DL)
        QWidget.setTabOrder(self.spinBox_R6_STA_DL, self.spinBox_R6_STR_DL)
        QWidget.setTabOrder(self.spinBox_R6_STR_DL, self.spinBox_R6_BLK_DL)
        QWidget.setTabOrder(self.spinBox_R6_BLK_DL, self.spinBox_R6_TKL_DL)
        QWidget.setTabOrder(self.spinBox_R6_TKL_DL, self.spinBox_R6_HAN_DL)
        QWidget.setTabOrder(self.spinBox_R6_HAN_DL, self.spinBox_R6_GI_DL)
        QWidget.setTabOrder(self.spinBox_R6_GI_DL, self.spinBox_R6_ELU_DL)
        QWidget.setTabOrder(self.spinBox_R6_ELU_DL, self.spinBox_R6_TEC_DL)
        QWidget.setTabOrder(self.spinBox_R6_TEC_DL, self.lineEdit_R1_LB)
        QWidget.setTabOrder(self.lineEdit_R1_LB, self.spinBox_R1_ATH_LB)
        QWidget.setTabOrder(self.spinBox_R1_ATH_LB, self.spinBox_R1_SPD_LB)
        QWidget.setTabOrder(self.spinBox_R1_SPD_LB, self.spinBox_R1_DUR_LB)
        QWidget.setTabOrder(self.spinBox_R1_DUR_LB, self.spinBox_R1_WE_LB)
        QWidget.setTabOrder(self.spinBox_R1_WE_LB, self.spinBox_R1_STA_LB)
        QWidget.setTabOrder(self.spinBox_R1_STA_LB, self.spinBox_R1_STR_LB)
        QWidget.setTabOrder(self.spinBox_R1_STR_LB, self.spinBox_R1_BLK_LB)
        QWidget.setTabOrder(self.spinBox_R1_BLK_LB, self.spinBox_R1_TKL_LB)
        QWidget.setTabOrder(self.spinBox_R1_TKL_LB, self.spinBox_R1_HAN_LB)
        QWidget.setTabOrder(self.spinBox_R1_HAN_LB, self.spinBox_R1_GI_LB)
        QWidget.setTabOrder(self.spinBox_R1_GI_LB, self.spinBox_R1_ELU_LB)
        QWidget.setTabOrder(self.spinBox_R1_ELU_LB, self.spinBox_R1_TEC_LB)
        QWidget.setTabOrder(self.spinBox_R1_TEC_LB, self.lineEdit_R2_LB)
        QWidget.setTabOrder(self.lineEdit_R2_LB, self.spinBox_R2_ATH_LB)
        QWidget.setTabOrder(self.spinBox_R2_ATH_LB, self.spinBox_R2_SPD_LB)
        QWidget.setTabOrder(self.spinBox_R2_SPD_LB, self.spinBox_R2_DUR_LB)
        QWidget.setTabOrder(self.spinBox_R2_DUR_LB, self.spinBox_R2_WE_LB)
        QWidget.setTabOrder(self.spinBox_R2_WE_LB, self.spinBox_R2_STA_LB)
        QWidget.setTabOrder(self.spinBox_R2_STA_LB, self.spinBox_R2_STR_LB)
        QWidget.setTabOrder(self.spinBox_R2_STR_LB, self.spinBox_R2_BLK_LB)
        QWidget.setTabOrder(self.spinBox_R2_BLK_LB, self.spinBox_R2_TKL_LB)
        QWidget.setTabOrder(self.spinBox_R2_TKL_LB, self.spinBox_R2_HAN_LB)
        QWidget.setTabOrder(self.spinBox_R2_HAN_LB, self.spinBox_R2_GI_LB)
        QWidget.setTabOrder(self.spinBox_R2_GI_LB, self.spinBox_R2_ELU_LB)
        QWidget.setTabOrder(self.spinBox_R2_ELU_LB, self.spinBox_R2_TEC_LB)
        QWidget.setTabOrder(self.spinBox_R2_TEC_LB, self.lineEdit_R3_LB)
        QWidget.setTabOrder(self.lineEdit_R3_LB, self.spinBox_R3_ATH_LB)
        QWidget.setTabOrder(self.spinBox_R3_ATH_LB, self.spinBox_R3_SPD_LB)
        QWidget.setTabOrder(self.spinBox_R3_SPD_LB, self.spinBox_R3_DUR_LB)
        QWidget.setTabOrder(self.spinBox_R3_DUR_LB, self.spinBox_R3_WE_LB)
        QWidget.setTabOrder(self.spinBox_R3_WE_LB, self.spinBox_R3_STA_LB)
        QWidget.setTabOrder(self.spinBox_R3_STA_LB, self.spinBox_R3_STR_LB)
        QWidget.setTabOrder(self.spinBox_R3_STR_LB, self.spinBox_R3_BLK_LB)
        QWidget.setTabOrder(self.spinBox_R3_BLK_LB, self.spinBox_R3_TKL_LB)
        QWidget.setTabOrder(self.spinBox_R3_TKL_LB, self.spinBox_R3_HAN_LB)
        QWidget.setTabOrder(self.spinBox_R3_HAN_LB, self.spinBox_R3_GI_LB)
        QWidget.setTabOrder(self.spinBox_R3_GI_LB, self.spinBox_R3_ELU_LB)
        QWidget.setTabOrder(self.spinBox_R3_ELU_LB, self.spinBox_R3_TEC_LB)
        QWidget.setTabOrder(self.spinBox_R3_TEC_LB, self.lineEdit_R4_LB)
        QWidget.setTabOrder(self.lineEdit_R4_LB, self.spinBox_R4_ATH_LB)
        QWidget.setTabOrder(self.spinBox_R4_ATH_LB, self.spinBox_R4_SPD_LB)
        QWidget.setTabOrder(self.spinBox_R4_SPD_LB, self.spinBox_R4_DUR_LB)
        QWidget.setTabOrder(self.spinBox_R4_DUR_LB, self.spinBox_R4_WE_LB)
        QWidget.setTabOrder(self.spinBox_R4_WE_LB, self.spinBox_R4_STA_LB)
        QWidget.setTabOrder(self.spinBox_R4_STA_LB, self.spinBox_R4_STR_LB)
        QWidget.setTabOrder(self.spinBox_R4_STR_LB, self.spinBox_R4_BLK_LB)
        QWidget.setTabOrder(self.spinBox_R4_BLK_LB, self.spinBox_R4_TKL_LB)
        QWidget.setTabOrder(self.spinBox_R4_TKL_LB, self.spinBox_R4_HAN_LB)
        QWidget.setTabOrder(self.spinBox_R4_HAN_LB, self.spinBox_R4_GI_LB)
        QWidget.setTabOrder(self.spinBox_R4_GI_LB, self.spinBox_R4_ELU_LB)
        QWidget.setTabOrder(self.spinBox_R4_ELU_LB, self.spinBox_R4_TEC_LB)
        QWidget.setTabOrder(self.spinBox_R4_TEC_LB, self.lineEdit_R5_LB)
        QWidget.setTabOrder(self.lineEdit_R5_LB, self.spinBox_R5_ATH_LB)
        QWidget.setTabOrder(self.spinBox_R5_ATH_LB, self.spinBox_R5_SPD_LB)
        QWidget.setTabOrder(self.spinBox_R5_SPD_LB, self.spinBox_R5_DUR_LB)
        QWidget.setTabOrder(self.spinBox_R5_DUR_LB, self.spinBox_R5_WE_LB)
        QWidget.setTabOrder(self.spinBox_R5_WE_LB, self.spinBox_R5_STA_LB)
        QWidget.setTabOrder(self.spinBox_R5_STA_LB, self.spinBox_R5_STR_LB)
        QWidget.setTabOrder(self.spinBox_R5_STR_LB, self.spinBox_R5_BLK_LB)
        QWidget.setTabOrder(self.spinBox_R5_BLK_LB, self.spinBox_R5_TKL_LB)
        QWidget.setTabOrder(self.spinBox_R5_TKL_LB, self.spinBox_R5_HAN_LB)
        QWidget.setTabOrder(self.spinBox_R5_HAN_LB, self.spinBox_R5_GI_LB)
        QWidget.setTabOrder(self.spinBox_R5_GI_LB, self.spinBox_R5_ELU_LB)
        QWidget.setTabOrder(self.spinBox_R5_ELU_LB, self.spinBox_R5_TEC_LB)
        QWidget.setTabOrder(self.spinBox_R5_TEC_LB, self.lineEdit_R6_LB)
        QWidget.setTabOrder(self.lineEdit_R6_LB, self.spinBox_R6_ATH_LB)
        QWidget.setTabOrder(self.spinBox_R6_ATH_LB, self.spinBox_R6_SPD_LB)
        QWidget.setTabOrder(self.spinBox_R6_SPD_LB, self.spinBox_R6_DUR_LB)
        QWidget.setTabOrder(self.spinBox_R6_DUR_LB, self.spinBox_R6_WE_LB)
        QWidget.setTabOrder(self.spinBox_R6_WE_LB, self.spinBox_R6_STA_LB)
        QWidget.setTabOrder(self.spinBox_R6_STA_LB, self.spinBox_R6_STR_LB)
        QWidget.setTabOrder(self.spinBox_R6_STR_LB, self.spinBox_R6_BLK_LB)
        QWidget.setTabOrder(self.spinBox_R6_BLK_LB, self.spinBox_R6_TKL_LB)
        QWidget.setTabOrder(self.spinBox_R6_TKL_LB, self.spinBox_R6_HAN_LB)
        QWidget.setTabOrder(self.spinBox_R6_HAN_LB, self.spinBox_R6_GI_LB)
        QWidget.setTabOrder(self.spinBox_R6_GI_LB, self.spinBox_R6_ELU_LB)
        QWidget.setTabOrder(self.spinBox_R6_ELU_LB, self.spinBox_R6_TEC_LB)
        QWidget.setTabOrder(self.spinBox_R6_TEC_LB, self.lineEdit_R1_DB)
        QWidget.setTabOrder(self.lineEdit_R1_DB, self.spinBox_R1_ATH_DB)
        QWidget.setTabOrder(self.spinBox_R1_ATH_DB, self.spinBox_R1_SPD_DB)
        QWidget.setTabOrder(self.spinBox_R1_SPD_DB, self.spinBox_R1_DUR_DB)
        QWidget.setTabOrder(self.spinBox_R1_DUR_DB, self.spinBox_R1_WE_DB)
        QWidget.setTabOrder(self.spinBox_R1_WE_DB, self.spinBox_R1_STA_DB)
        QWidget.setTabOrder(self.spinBox_R1_STA_DB, self.spinBox_R1_STR_DB)
        QWidget.setTabOrder(self.spinBox_R1_STR_DB, self.spinBox_R1_BLK_DB)
        QWidget.setTabOrder(self.spinBox_R1_BLK_DB, self.spinBox_R1_TKL_DB)
        QWidget.setTabOrder(self.spinBox_R1_TKL_DB, self.spinBox_R1_HAN_DB)
        QWidget.setTabOrder(self.spinBox_R1_HAN_DB, self.spinBox_R1_GI_DB)
        QWidget.setTabOrder(self.spinBox_R1_GI_DB, self.spinBox_R1_ELU_DB)
        QWidget.setTabOrder(self.spinBox_R1_ELU_DB, self.spinBox_R1_TEC_DB)
        QWidget.setTabOrder(self.spinBox_R1_TEC_DB, self.lineEdit_R2_DB)
        QWidget.setTabOrder(self.lineEdit_R2_DB, self.spinBox_R2_ATH_DB)
        QWidget.setTabOrder(self.spinBox_R2_ATH_DB, self.spinBox_R2_SPD_DB)
        QWidget.setTabOrder(self.spinBox_R2_SPD_DB, self.spinBox_R2_DUR_DB)
        QWidget.setTabOrder(self.spinBox_R2_DUR_DB, self.spinBox_R2_WE_DB)
        QWidget.setTabOrder(self.spinBox_R2_WE_DB, self.spinBox_R2_STA_DB)
        QWidget.setTabOrder(self.spinBox_R2_STA_DB, self.spinBox_R2_STR_DB)
        QWidget.setTabOrder(self.spinBox_R2_STR_DB, self.spinBox_R2_BLK_DB)
        QWidget.setTabOrder(self.spinBox_R2_BLK_DB, self.spinBox_R2_TKL_DB)
        QWidget.setTabOrder(self.spinBox_R2_TKL_DB, self.spinBox_R2_HAN_DB)
        QWidget.setTabOrder(self.spinBox_R2_HAN_DB, self.spinBox_R2_GI_DB)
        QWidget.setTabOrder(self.spinBox_R2_GI_DB, self.spinBox_R2_ELU_DB)
        QWidget.setTabOrder(self.spinBox_R2_ELU_DB, self.spinBox_R2_TEC_DB)
        QWidget.setTabOrder(self.spinBox_R2_TEC_DB, self.lineEdit_R3_DB)
        QWidget.setTabOrder(self.lineEdit_R3_DB, self.spinBox_R3_ATH_DB)
        QWidget.setTabOrder(self.spinBox_R3_ATH_DB, self.spinBox_R3_SPD_DB)
        QWidget.setTabOrder(self.spinBox_R3_SPD_DB, self.spinBox_R3_DUR_DB)
        QWidget.setTabOrder(self.spinBox_R3_DUR_DB, self.spinBox_R3_WE_DB)
        QWidget.setTabOrder(self.spinBox_R3_WE_DB, self.spinBox_R3_STA_DB)
        QWidget.setTabOrder(self.spinBox_R3_STA_DB, self.spinBox_R3_STR_DB)
        QWidget.setTabOrder(self.spinBox_R3_STR_DB, self.spinBox_R3_BLK_DB)
        QWidget.setTabOrder(self.spinBox_R3_BLK_DB, self.spinBox_R3_TKL_DB)
        QWidget.setTabOrder(self.spinBox_R3_TKL_DB, self.spinBox_R3_HAN_DB)
        QWidget.setTabOrder(self.spinBox_R3_HAN_DB, self.spinBox_R3_GI_DB)
        QWidget.setTabOrder(self.spinBox_R3_GI_DB, self.spinBox_R3_ELU_DB)
        QWidget.setTabOrder(self.spinBox_R3_ELU_DB, self.spinBox_R3_TEC_DB)
        QWidget.setTabOrder(self.spinBox_R3_TEC_DB, self.lineEdit_R4_DB)
        QWidget.setTabOrder(self.lineEdit_R4_DB, self.spinBox_R4_ATH_DB)
        QWidget.setTabOrder(self.spinBox_R4_ATH_DB, self.spinBox_R4_SPD_DB)
        QWidget.setTabOrder(self.spinBox_R4_SPD_DB, self.spinBox_R4_DUR_DB)
        QWidget.setTabOrder(self.spinBox_R4_DUR_DB, self.spinBox_R4_WE_DB)
        QWidget.setTabOrder(self.spinBox_R4_WE_DB, self.spinBox_R4_STA_DB)
        QWidget.setTabOrder(self.spinBox_R4_STA_DB, self.spinBox_R4_STR_DB)
        QWidget.setTabOrder(self.spinBox_R4_STR_DB, self.spinBox_R4_BLK_DB)
        QWidget.setTabOrder(self.spinBox_R4_BLK_DB, self.spinBox_R4_TKL_DB)
        QWidget.setTabOrder(self.spinBox_R4_TKL_DB, self.spinBox_R4_HAN_DB)
        QWidget.setTabOrder(self.spinBox_R4_HAN_DB, self.spinBox_R4_GI_DB)
        QWidget.setTabOrder(self.spinBox_R4_GI_DB, self.spinBox_R4_ELU_DB)
        QWidget.setTabOrder(self.spinBox_R4_ELU_DB, self.spinBox_R4_TEC_DB)
        QWidget.setTabOrder(self.spinBox_R4_TEC_DB, self.lineEdit_R5_DB)
        QWidget.setTabOrder(self.lineEdit_R5_DB, self.spinBox_R5_ATH_DB)
        QWidget.setTabOrder(self.spinBox_R5_ATH_DB, self.spinBox_R5_SPD_DB)
        QWidget.setTabOrder(self.spinBox_R5_SPD_DB, self.spinBox_R5_DUR_DB)
        QWidget.setTabOrder(self.spinBox_R5_DUR_DB, self.spinBox_R5_WE_DB)
        QWidget.setTabOrder(self.spinBox_R5_WE_DB, self.spinBox_R5_STA_DB)
        QWidget.setTabOrder(self.spinBox_R5_STA_DB, self.spinBox_R5_STR_DB)
        QWidget.setTabOrder(self.spinBox_R5_STR_DB, self.spinBox_R5_BLK_DB)
        QWidget.setTabOrder(self.spinBox_R5_BLK_DB, self.spinBox_R5_TKL_DB)
        QWidget.setTabOrder(self.spinBox_R5_TKL_DB, self.spinBox_R5_HAN_DB)
        QWidget.setTabOrder(self.spinBox_R5_HAN_DB, self.spinBox_R5_GI_DB)
        QWidget.setTabOrder(self.spinBox_R5_GI_DB, self.spinBox_R5_ELU_DB)
        QWidget.setTabOrder(self.spinBox_R5_ELU_DB, self.spinBox_R5_TEC_DB)
        QWidget.setTabOrder(self.spinBox_R5_TEC_DB, self.lineEdit_R6_DB)
        QWidget.setTabOrder(self.lineEdit_R6_DB, self.spinBox_R6_ATH_DB)
        QWidget.setTabOrder(self.spinBox_R6_ATH_DB, self.spinBox_R6_SPD_DB)
        QWidget.setTabOrder(self.spinBox_R6_SPD_DB, self.spinBox_R6_DUR_DB)
        QWidget.setTabOrder(self.spinBox_R6_DUR_DB, self.spinBox_R6_WE_DB)
        QWidget.setTabOrder(self.spinBox_R6_WE_DB, self.spinBox_R6_STA_DB)
        QWidget.setTabOrder(self.spinBox_R6_STA_DB, self.spinBox_R6_STR_DB)
        QWidget.setTabOrder(self.spinBox_R6_STR_DB, self.spinBox_R6_BLK_DB)
        QWidget.setTabOrder(self.spinBox_R6_BLK_DB, self.spinBox_R6_TKL_DB)
        QWidget.setTabOrder(self.spinBox_R6_TKL_DB, self.spinBox_R6_HAN_DB)
        QWidget.setTabOrder(self.spinBox_R6_HAN_DB, self.spinBox_R6_GI_DB)
        QWidget.setTabOrder(self.spinBox_R6_GI_DB, self.spinBox_R6_ELU_DB)
        QWidget.setTabOrder(self.spinBox_R6_ELU_DB, self.spinBox_R6_TEC_DB)
        QWidget.setTabOrder(self.spinBox_R6_TEC_DB, self.lineEdit_R1_K)
        QWidget.setTabOrder(self.lineEdit_R1_K, self.spinBox_R1_ATH_K)
        QWidget.setTabOrder(self.spinBox_R1_ATH_K, self.spinBox_R1_SPD_K)
        QWidget.setTabOrder(self.spinBox_R1_SPD_K, self.spinBox_R1_DUR_K)
        QWidget.setTabOrder(self.spinBox_R1_DUR_K, self.spinBox_R1_WE_K)
        QWidget.setTabOrder(self.spinBox_R1_WE_K, self.spinBox_R1_STA_K)
        QWidget.setTabOrder(self.spinBox_R1_STA_K, self.spinBox_R1_STR_K)
        QWidget.setTabOrder(self.spinBox_R1_STR_K, self.spinBox_R1_BLK_K)
        QWidget.setTabOrder(self.spinBox_R1_BLK_K, self.spinBox_R1_TKL_K)
        QWidget.setTabOrder(self.spinBox_R1_TKL_K, self.spinBox_R1_HAN_K)
        QWidget.setTabOrder(self.spinBox_R1_HAN_K, self.spinBox_R1_GI_K)
        QWidget.setTabOrder(self.spinBox_R1_GI_K, self.spinBox_R1_ELU_K)
        QWidget.setTabOrder(self.spinBox_R1_ELU_K, self.spinBox_R1_TEC_K)
        QWidget.setTabOrder(self.spinBox_R1_TEC_K, self.lineEdit_R2_K)
        QWidget.setTabOrder(self.lineEdit_R2_K, self.spinBox_R2_ATH_K)
        QWidget.setTabOrder(self.spinBox_R2_ATH_K, self.spinBox_R2_SPD_K)
        QWidget.setTabOrder(self.spinBox_R2_SPD_K, self.spinBox_R2_DUR_K)
        QWidget.setTabOrder(self.spinBox_R2_DUR_K, self.spinBox_R2_WE_K)
        QWidget.setTabOrder(self.spinBox_R2_WE_K, self.spinBox_R2_STA_K)
        QWidget.setTabOrder(self.spinBox_R2_STA_K, self.spinBox_R2_STR_K)
        QWidget.setTabOrder(self.spinBox_R2_STR_K, self.spinBox_R2_BLK_K)
        QWidget.setTabOrder(self.spinBox_R2_BLK_K, self.spinBox_R2_TKL_K)
        QWidget.setTabOrder(self.spinBox_R2_TKL_K, self.spinBox_R2_HAN_K)
        QWidget.setTabOrder(self.spinBox_R2_HAN_K, self.spinBox_R2_GI_K)
        QWidget.setTabOrder(self.spinBox_R2_GI_K, self.spinBox_R2_ELU_K)
        QWidget.setTabOrder(self.spinBox_R2_ELU_K, self.spinBox_R2_TEC_K)
        QWidget.setTabOrder(self.spinBox_R2_TEC_K, self.lineEdit_R3_K)
        QWidget.setTabOrder(self.lineEdit_R3_K, self.spinBox_R3_ATH_K)
        QWidget.setTabOrder(self.spinBox_R3_ATH_K, self.spinBox_R3_SPD_K)
        QWidget.setTabOrder(self.spinBox_R3_SPD_K, self.spinBox_R3_DUR_K)
        QWidget.setTabOrder(self.spinBox_R3_DUR_K, self.spinBox_R3_WE_K)
        QWidget.setTabOrder(self.spinBox_R3_WE_K, self.spinBox_R3_STA_K)
        QWidget.setTabOrder(self.spinBox_R3_STA_K, self.spinBox_R3_STR_K)
        QWidget.setTabOrder(self.spinBox_R3_STR_K, self.spinBox_R3_BLK_K)
        QWidget.setTabOrder(self.spinBox_R3_BLK_K, self.spinBox_R3_TKL_K)
        QWidget.setTabOrder(self.spinBox_R3_TKL_K, self.spinBox_R3_HAN_K)
        QWidget.setTabOrder(self.spinBox_R3_HAN_K, self.spinBox_R3_GI_K)
        QWidget.setTabOrder(self.spinBox_R3_GI_K, self.spinBox_R3_ELU_K)
        QWidget.setTabOrder(self.spinBox_R3_ELU_K, self.spinBox_R3_TEC_K)
        QWidget.setTabOrder(self.spinBox_R3_TEC_K, self.lineEdit_R4_K)
        QWidget.setTabOrder(self.lineEdit_R4_K, self.spinBox_R4_ATH_K)
        QWidget.setTabOrder(self.spinBox_R4_ATH_K, self.spinBox_R4_SPD_K)
        QWidget.setTabOrder(self.spinBox_R4_SPD_K, self.spinBox_R4_DUR_K)
        QWidget.setTabOrder(self.spinBox_R4_DUR_K, self.spinBox_R4_WE_K)
        QWidget.setTabOrder(self.spinBox_R4_WE_K, self.spinBox_R4_STA_K)
        QWidget.setTabOrder(self.spinBox_R4_STA_K, self.spinBox_R4_STR_K)
        QWidget.setTabOrder(self.spinBox_R4_STR_K, self.spinBox_R4_BLK_K)
        QWidget.setTabOrder(self.spinBox_R4_BLK_K, self.spinBox_R4_TKL_K)
        QWidget.setTabOrder(self.spinBox_R4_TKL_K, self.spinBox_R4_HAN_K)
        QWidget.setTabOrder(self.spinBox_R4_HAN_K, self.spinBox_R4_GI_K)
        QWidget.setTabOrder(self.spinBox_R4_GI_K, self.spinBox_R4_ELU_K)
        QWidget.setTabOrder(self.spinBox_R4_ELU_K, self.spinBox_R4_TEC_K)
        QWidget.setTabOrder(self.spinBox_R4_TEC_K, self.lineEdit_R5_K)
        QWidget.setTabOrder(self.lineEdit_R5_K, self.spinBox_R5_ATH_K)
        QWidget.setTabOrder(self.spinBox_R5_ATH_K, self.spinBox_R5_SPD_K)
        QWidget.setTabOrder(self.spinBox_R5_SPD_K, self.spinBox_R5_DUR_K)
        QWidget.setTabOrder(self.spinBox_R5_DUR_K, self.spinBox_R5_WE_K)
        QWidget.setTabOrder(self.spinBox_R5_WE_K, self.spinBox_R5_STA_K)
        QWidget.setTabOrder(self.spinBox_R5_STA_K, self.spinBox_R5_STR_K)
        QWidget.setTabOrder(self.spinBox_R5_STR_K, self.spinBox_R5_BLK_K)
        QWidget.setTabOrder(self.spinBox_R5_BLK_K, self.spinBox_R5_TKL_K)
        QWidget.setTabOrder(self.spinBox_R5_TKL_K, self.spinBox_R5_HAN_K)
        QWidget.setTabOrder(self.spinBox_R5_HAN_K, self.spinBox_R5_GI_K)
        QWidget.setTabOrder(self.spinBox_R5_GI_K, self.spinBox_R5_ELU_K)
        QWidget.setTabOrder(self.spinBox_R5_ELU_K, self.spinBox_R5_TEC_K)
        QWidget.setTabOrder(self.spinBox_R5_TEC_K, self.lineEdit_R6_K)
        QWidget.setTabOrder(self.lineEdit_R6_K, self.spinBox_R6_ATH_K)
        QWidget.setTabOrder(self.spinBox_R6_ATH_K, self.spinBox_R6_SPD_K)
        QWidget.setTabOrder(self.spinBox_R6_SPD_K, self.spinBox_R6_DUR_K)
        QWidget.setTabOrder(self.spinBox_R6_DUR_K, self.spinBox_R6_WE_K)
        QWidget.setTabOrder(self.spinBox_R6_WE_K, self.spinBox_R6_STA_K)
        QWidget.setTabOrder(self.spinBox_R6_STA_K, self.spinBox_R6_STR_K)
        QWidget.setTabOrder(self.spinBox_R6_STR_K, self.spinBox_R6_BLK_K)
        QWidget.setTabOrder(self.spinBox_R6_BLK_K, self.spinBox_R6_TKL_K)
        QWidget.setTabOrder(self.spinBox_R6_TKL_K, self.spinBox_R6_HAN_K)
        QWidget.setTabOrder(self.spinBox_R6_HAN_K, self.spinBox_R6_GI_K)
        QWidget.setTabOrder(self.spinBox_R6_GI_K, self.spinBox_R6_ELU_K)
        QWidget.setTabOrder(self.spinBox_R6_ELU_K, self.spinBox_R6_TEC_K)
        QWidget.setTabOrder(self.spinBox_R6_TEC_K, self.lineEdit_R1_P)
        QWidget.setTabOrder(self.lineEdit_R1_P, self.spinBox_R1_ATH_P)
        QWidget.setTabOrder(self.spinBox_R1_ATH_P, self.spinBox_R1_SPD_P)
        QWidget.setTabOrder(self.spinBox_R1_SPD_P, self.spinBox_R1_DUR_P)
        QWidget.setTabOrder(self.spinBox_R1_DUR_P, self.spinBox_R1_WE_P)
        QWidget.setTabOrder(self.spinBox_R1_WE_P, self.spinBox_R1_STA_P)
        QWidget.setTabOrder(self.spinBox_R1_STA_P, self.spinBox_R1_STR_P)
        QWidget.setTabOrder(self.spinBox_R1_STR_P, self.spinBox_R1_BLK_P)
        QWidget.setTabOrder(self.spinBox_R1_BLK_P, self.spinBox_R1_TKL_P)
        QWidget.setTabOrder(self.spinBox_R1_TKL_P, self.spinBox_R1_HAN_P)
        QWidget.setTabOrder(self.spinBox_R1_HAN_P, self.spinBox_R1_GI_P)
        QWidget.setTabOrder(self.spinBox_R1_GI_P, self.spinBox_R1_ELU_P)
        QWidget.setTabOrder(self.spinBox_R1_ELU_P, self.spinBox_R1_TEC_P)
        QWidget.setTabOrder(self.spinBox_R1_TEC_P, self.lineEdit_R2_P)
        QWidget.setTabOrder(self.lineEdit_R2_P, self.spinBox_R2_ATH_P)
        QWidget.setTabOrder(self.spinBox_R2_ATH_P, self.spinBox_R2_SPD_P)
        QWidget.setTabOrder(self.spinBox_R2_SPD_P, self.spinBox_R2_DUR_P)
        QWidget.setTabOrder(self.spinBox_R2_DUR_P, self.spinBox_R2_WE_P)
        QWidget.setTabOrder(self.spinBox_R2_WE_P, self.spinBox_R2_STA_P)
        QWidget.setTabOrder(self.spinBox_R2_STA_P, self.spinBox_R2_STR_P)
        QWidget.setTabOrder(self.spinBox_R2_STR_P, self.spinBox_R2_BLK_P)
        QWidget.setTabOrder(self.spinBox_R2_BLK_P, self.spinBox_R2_TKL_P)
        QWidget.setTabOrder(self.spinBox_R2_TKL_P, self.spinBox_R2_HAN_P)
        QWidget.setTabOrder(self.spinBox_R2_HAN_P, self.spinBox_R2_GI_P)
        QWidget.setTabOrder(self.spinBox_R2_GI_P, self.spinBox_R2_ELU_P)
        QWidget.setTabOrder(self.spinBox_R2_ELU_P, self.spinBox_R2_TEC_P)
        QWidget.setTabOrder(self.spinBox_R2_TEC_P, self.lineEdit_R3_P)
        QWidget.setTabOrder(self.lineEdit_R3_P, self.spinBox_R3_ATH_P)
        QWidget.setTabOrder(self.spinBox_R3_ATH_P, self.spinBox_R3_SPD_P)
        QWidget.setTabOrder(self.spinBox_R3_SPD_P, self.spinBox_R3_DUR_P)
        QWidget.setTabOrder(self.spinBox_R3_DUR_P, self.spinBox_R3_WE_P)
        QWidget.setTabOrder(self.spinBox_R3_WE_P, self.spinBox_R3_STA_P)
        QWidget.setTabOrder(self.spinBox_R3_STA_P, self.spinBox_R3_STR_P)
        QWidget.setTabOrder(self.spinBox_R3_STR_P, self.spinBox_R3_BLK_P)
        QWidget.setTabOrder(self.spinBox_R3_BLK_P, self.spinBox_R3_TKL_P)
        QWidget.setTabOrder(self.spinBox_R3_TKL_P, self.spinBox_R3_HAN_P)
        QWidget.setTabOrder(self.spinBox_R3_HAN_P, self.spinBox_R3_GI_P)
        QWidget.setTabOrder(self.spinBox_R3_GI_P, self.spinBox_R3_ELU_P)
        QWidget.setTabOrder(self.spinBox_R3_ELU_P, self.spinBox_R3_TEC_P)
        QWidget.setTabOrder(self.spinBox_R3_TEC_P, self.lineEdit_R4_P)
        QWidget.setTabOrder(self.lineEdit_R4_P, self.spinBox_R4_ATH_P)
        QWidget.setTabOrder(self.spinBox_R4_ATH_P, self.spinBox_R4_SPD_P)
        QWidget.setTabOrder(self.spinBox_R4_SPD_P, self.spinBox_R4_DUR_P)
        QWidget.setTabOrder(self.spinBox_R4_DUR_P, self.spinBox_R4_WE_P)
        QWidget.setTabOrder(self.spinBox_R4_WE_P, self.spinBox_R4_STA_P)
        QWidget.setTabOrder(self.spinBox_R4_STA_P, self.spinBox_R4_STR_P)
        QWidget.setTabOrder(self.spinBox_R4_STR_P, self.spinBox_R4_BLK_P)
        QWidget.setTabOrder(self.spinBox_R4_BLK_P, self.spinBox_R4_TKL_P)
        QWidget.setTabOrder(self.spinBox_R4_TKL_P, self.spinBox_R4_HAN_P)
        QWidget.setTabOrder(self.spinBox_R4_HAN_P, self.spinBox_R4_GI_P)
        QWidget.setTabOrder(self.spinBox_R4_GI_P, self.spinBox_R4_ELU_P)
        QWidget.setTabOrder(self.spinBox_R4_ELU_P, self.spinBox_R4_TEC_P)
        QWidget.setTabOrder(self.spinBox_R4_TEC_P, self.lineEdit_R5_P)
        QWidget.setTabOrder(self.lineEdit_R5_P, self.spinBox_R5_ATH_P)
        QWidget.setTabOrder(self.spinBox_R5_ATH_P, self.spinBox_R5_SPD_P)
        QWidget.setTabOrder(self.spinBox_R5_SPD_P, self.spinBox_R5_DUR_P)
        QWidget.setTabOrder(self.spinBox_R5_DUR_P, self.spinBox_R5_WE_P)
        QWidget.setTabOrder(self.spinBox_R5_WE_P, self.spinBox_R5_STA_P)
        QWidget.setTabOrder(self.spinBox_R5_STA_P, self.spinBox_R5_STR_P)
        QWidget.setTabOrder(self.spinBox_R5_STR_P, self.spinBox_R5_BLK_P)
        QWidget.setTabOrder(self.spinBox_R5_BLK_P, self.spinBox_R5_TKL_P)
        QWidget.setTabOrder(self.spinBox_R5_TKL_P, self.spinBox_R5_HAN_P)
        QWidget.setTabOrder(self.spinBox_R5_HAN_P, self.spinBox_R5_GI_P)
        QWidget.setTabOrder(self.spinBox_R5_GI_P, self.spinBox_R5_ELU_P)
        QWidget.setTabOrder(self.spinBox_R5_ELU_P, self.spinBox_R5_TEC_P)
        QWidget.setTabOrder(self.spinBox_R5_TEC_P, self.lineEdit_R6_P)
        QWidget.setTabOrder(self.lineEdit_R6_P, self.spinBox_R6_ATH_P)
        QWidget.setTabOrder(self.spinBox_R6_ATH_P, self.spinBox_R6_SPD_P)
        QWidget.setTabOrder(self.spinBox_R6_SPD_P, self.spinBox_R6_DUR_P)
        QWidget.setTabOrder(self.spinBox_R6_DUR_P, self.spinBox_R6_WE_P)
        QWidget.setTabOrder(self.spinBox_R6_WE_P, self.spinBox_R6_STA_P)
        QWidget.setTabOrder(self.spinBox_R6_STA_P, self.spinBox_R6_STR_P)
        QWidget.setTabOrder(self.spinBox_R6_STR_P, self.spinBox_R6_BLK_P)
        QWidget.setTabOrder(self.spinBox_R6_BLK_P, self.spinBox_R6_TKL_P)
        QWidget.setTabOrder(self.spinBox_R6_TKL_P, self.spinBox_R6_HAN_P)
        QWidget.setTabOrder(self.spinBox_R6_HAN_P, self.spinBox_R6_GI_P)
        QWidget.setTabOrder(self.spinBox_R6_GI_P, self.spinBox_R6_ELU_P)
        QWidget.setTabOrder(self.spinBox_R6_ELU_P, self.spinBox_R6_TEC_P)

        self.retranslateUi(DialogRoleRatings)
        self.buttonBox.accepted.connect(DialogRoleRatings.accept)
        self.buttonBox.rejected.connect(DialogRoleRatings.reject)

        self.tabWidgetRoleRatings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DialogRoleRatings)
    # setupUi

    def retranslateUi(self, DialogRoleRatings):
        DialogRoleRatings.setWindowTitle(QCoreApplication.translate("DialogRoleRatings", u"Role Ratings", None))
        self.label_ATH_Header_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"ATH", None))
        self.spinBox_R2_TKL_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_DUR_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_STR_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_TEC_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_WE_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_SPD_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_TEC_Header_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"TEC", None))
        self.spinBox_R1_BLK_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_STA_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_WE_Header_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"WE", None))
        self.label_TKL_Header_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"TKL", None))
        self.label_STR_Header_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"STR", None))
        self.spinBox_R1_WE_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_SPD_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R1_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"R1", None))
        self.label_RoleHeader_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"Role", None))
        self.label_Total_Header_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"Total", None))
        self.spinBox_R3_STA_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R5_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"R5", None))
        self.label_BLK_Header_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"BLK", None))
        self.label_ELU_Header_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"ELU", None))
        self.spinBox_R2_BLK_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_LabelHeader_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"Label", None))
        self.spinBox_R2_HAN_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R2_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"R2", None))
        self.spinBox_R1_GI_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_DUR_Header_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"DUR", None))
        self.spinBox_R1_HAN_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R3_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"R3", None))
        self.label_GI_Header_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"GI", None))
        self.spinBox_R1_TEC_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ATH_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_DUR_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ELU_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ATH_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_STR_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ATH_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ELU_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_STA_Header_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"STA", None))
        self.spinBox_R1_STR_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_SPD_Header_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"SPD", None))
        self.spinBox_R2_DUR_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_HAN_Header_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"HAN", None))
        self.label_R4_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"R4", None))
        self.spinBox_R1_TKL_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_GI_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_WE_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_SPD_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R6_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"R6", None))
        self.spinBox_R2_STA_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_BLK_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TKL_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_HAN_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_GI_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ELU_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TEC_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ATH_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_SPD_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_DUR_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_WE_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STA_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STR_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_BLK_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TKL_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_HAN_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_GI_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ELU_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TEC_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ATH_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_SPD_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_DUR_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_WE_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STA_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STR_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_BLK_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TKL_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_HAN_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_GI_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ELU_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TEC_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ATH_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_SPD_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_DUR_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_WE_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STA_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STR_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_BLK_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TKL_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_HAN_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_GI_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ELU_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TEC_QB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.lineEdit_R1_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"QB", None))
        self.lineEdit_R2_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"QB Rush", None))
        self.lineEdit_R3_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"QB User1", None))
        self.lineEdit_R4_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"QB User2", None))
        self.lineEdit_R5_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"QB User3", None))
        self.lineEdit_R6_QB.setText(QCoreApplication.translate("DialogRoleRatings", u"QB User4", None))
        self.tabWidgetRoleRatings.setTabText(self.tabWidgetRoleRatings.indexOf(self.QB), QCoreApplication.translate("DialogRoleRatings", u"QB", None))
        self.label_ATH_Header_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"ATH", None))
        self.spinBox_R2_TKL_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_DUR_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_STR_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_TEC_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_WE_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_SPD_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_TEC_Header_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"TEC", None))
        self.spinBox_R1_BLK_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_STA_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_WE_Header_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"WE", None))
        self.label_TKL_Header_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"TKL", None))
        self.label_STR_Header_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"STR", None))
        self.spinBox_R1_WE_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_SPD_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R1_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"R1", None))
        self.label_RoleHeader_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"Role", None))
        self.label_Total_Header_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"Total", None))
        self.spinBox_R3_STA_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R5_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"R5", None))
        self.label_BLK_Header_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"BLK", None))
        self.label_ELU_Header_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"ELU", None))
        self.spinBox_R2_BLK_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_LabelHeader_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"Label", None))
        self.spinBox_R2_HAN_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R2_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"R2", None))
        self.spinBox_R1_GI_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_DUR_Header_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"DUR", None))
        self.spinBox_R1_HAN_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R3_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"R3", None))
        self.label_GI_Header_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"GI", None))
        self.spinBox_R1_TEC_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ATH_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_DUR_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ELU_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ATH_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_STR_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ATH_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ELU_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_STA_Header_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"STA", None))
        self.spinBox_R1_STR_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_SPD_Header_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"SPD", None))
        self.spinBox_R2_DUR_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_HAN_Header_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"HAN", None))
        self.label_R4_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"R4", None))
        self.spinBox_R1_TKL_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_GI_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_WE_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_SPD_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R6_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"R6", None))
        self.spinBox_R2_STA_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_BLK_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TKL_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_HAN_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_GI_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ELU_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TEC_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ATH_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_SPD_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_DUR_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_WE_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STA_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STR_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_BLK_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TKL_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_HAN_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_GI_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ELU_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TEC_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ATH_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_SPD_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_DUR_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_WE_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STA_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STR_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_BLK_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TKL_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_HAN_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_GI_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ELU_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TEC_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ATH_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_SPD_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_DUR_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_WE_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STA_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STR_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_BLK_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TKL_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_HAN_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_GI_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ELU_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TEC_RB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.lineEdit_R1_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"RB", None))
        self.lineEdit_R2_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"FB", None))
        self.lineEdit_R3_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"RBSpeed", None))
        self.lineEdit_R4_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"RBPower", None))
        self.lineEdit_R5_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"RBPoss", None))
        self.lineEdit_R6_RB.setText(QCoreApplication.translate("DialogRoleRatings", u"RBUser1", None))
        self.tabWidgetRoleRatings.setTabText(self.tabWidgetRoleRatings.indexOf(self.RB), QCoreApplication.translate("DialogRoleRatings", u"RB", None))
        self.label_ATH_Header_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"ATH", None))
        self.spinBox_R2_TKL_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_DUR_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_STR_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_TEC_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_WE_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_SPD_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_TEC_Header_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"TEC", None))
        self.spinBox_R1_BLK_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_STA_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_WE_Header_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"WE", None))
        self.label_TKL_Header_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"TKL", None))
        self.label_STR_Header_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"STR", None))
        self.spinBox_R1_WE_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_SPD_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R1_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"R1", None))
        self.label_RoleHeader_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"Role", None))
        self.label_Total_Header_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"Total", None))
        self.spinBox_R3_STA_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R5_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"R5", None))
        self.label_BLK_Header_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"BLK", None))
        self.label_ELU_Header_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"ELU", None))
        self.spinBox_R2_BLK_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_LabelHeader_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"Label", None))
        self.spinBox_R2_HAN_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R2_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"R2", None))
        self.spinBox_R1_GI_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_DUR_Header_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"DUR", None))
        self.spinBox_R1_HAN_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R3_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"R3", None))
        self.label_GI_Header_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"GI", None))
        self.spinBox_R1_TEC_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ATH_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_DUR_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ELU_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ATH_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_STR_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ATH_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ELU_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_STA_Header_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"STA", None))
        self.spinBox_R1_STR_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_SPD_Header_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"SPD", None))
        self.spinBox_R2_DUR_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_HAN_Header_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"HAN", None))
        self.label_R4_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"R4", None))
        self.spinBox_R1_TKL_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_GI_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_WE_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_SPD_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R6_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"R6", None))
        self.spinBox_R2_STA_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_BLK_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TKL_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_HAN_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_GI_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ELU_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TEC_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ATH_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_SPD_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_DUR_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_WE_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STA_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STR_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_BLK_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TKL_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_HAN_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_GI_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ELU_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TEC_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ATH_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_SPD_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_DUR_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_WE_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STA_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STR_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_BLK_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TKL_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_HAN_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_GI_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ELU_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TEC_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ATH_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_SPD_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_DUR_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_WE_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STA_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STR_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_BLK_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TKL_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_HAN_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_GI_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ELU_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TEC_WR.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.lineEdit_R1_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"WR", None))
        self.lineEdit_R2_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"WRPoss", None))
        self.lineEdit_R3_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"WRDeep", None))
        self.lineEdit_R4_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"WRUser1", None))
        self.lineEdit_R5_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"WRUser2", None))
        self.lineEdit_R6_WR.setText(QCoreApplication.translate("DialogRoleRatings", u"WRUser3", None))
        self.tabWidgetRoleRatings.setTabText(self.tabWidgetRoleRatings.indexOf(self.WR), QCoreApplication.translate("DialogRoleRatings", u"WR", None))
        self.label_ATH_Header_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"ATH", None))
        self.spinBox_R2_TKL_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_DUR_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_STR_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_TEC_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_WE_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_SPD_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_TEC_Header_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"TEC", None))
        self.spinBox_R1_BLK_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_STA_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_WE_Header_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"WE", None))
        self.label_TKL_Header_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"TKL", None))
        self.label_STR_Header_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"STR", None))
        self.spinBox_R1_WE_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_SPD_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R1_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"R1", None))
        self.label_RoleHeader_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"Role", None))
        self.label_Total_Header_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"Total", None))
        self.spinBox_R3_STA_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R5_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"R5", None))
        self.label_BLK_Header_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"BLK", None))
        self.label_ELU_Header_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"ELU", None))
        self.spinBox_R2_BLK_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_LabelHeader_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"Label", None))
        self.spinBox_R2_HAN_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R2_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"R2", None))
        self.spinBox_R1_GI_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_DUR_Header_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"DUR", None))
        self.spinBox_R1_HAN_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R3_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"R3", None))
        self.label_GI_Header_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"GI", None))
        self.spinBox_R1_TEC_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ATH_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_DUR_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ELU_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ATH_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_STR_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ATH_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ELU_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_STA_Header_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"STA", None))
        self.spinBox_R1_STR_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_SPD_Header_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"SPD", None))
        self.spinBox_R2_DUR_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_HAN_Header_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"HAN", None))
        self.label_R4_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"R4", None))
        self.spinBox_R1_TKL_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_GI_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_WE_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_SPD_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R6_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"R6", None))
        self.spinBox_R2_STA_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_BLK_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TKL_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_HAN_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_GI_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ELU_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TEC_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ATH_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_SPD_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_DUR_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_WE_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STA_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STR_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_BLK_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TKL_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_HAN_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_GI_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ELU_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TEC_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ATH_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_SPD_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_DUR_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_WE_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STA_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STR_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_BLK_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TKL_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_HAN_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_GI_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ELU_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TEC_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ATH_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_SPD_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_DUR_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_WE_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STA_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STR_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_BLK_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TKL_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_HAN_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_GI_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ELU_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TEC_TE.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.lineEdit_R1_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"TE", None))
        self.lineEdit_R2_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"TEBlock", None))
        self.lineEdit_R3_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"TEPoss", None))
        self.lineEdit_R4_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"TEUser1", None))
        self.lineEdit_R5_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"TEUser2", None))
        self.lineEdit_R6_TE.setText(QCoreApplication.translate("DialogRoleRatings", u"TEUser3", None))
        self.tabWidgetRoleRatings.setTabText(self.tabWidgetRoleRatings.indexOf(self.TE), QCoreApplication.translate("DialogRoleRatings", u"TE", None))
        self.label_ATH_Header_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"ATH", None))
        self.spinBox_R2_TKL_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_DUR_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_STR_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_TEC_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_WE_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_SPD_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_TEC_Header_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"TEC", None))
        self.spinBox_R1_BLK_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_STA_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_WE_Header_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"WE", None))
        self.label_TKL_Header_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"TKL", None))
        self.label_STR_Header_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"STR", None))
        self.spinBox_R1_WE_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_SPD_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R1_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"R1", None))
        self.label_RoleHeader_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"Role", None))
        self.label_Total_Header_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"Total", None))
        self.spinBox_R3_STA_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R5_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"R5", None))
        self.label_BLK_Header_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"BLK", None))
        self.label_ELU_Header_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"ELU", None))
        self.spinBox_R2_BLK_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_LabelHeader_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"Label", None))
        self.spinBox_R2_HAN_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R2_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"R2", None))
        self.spinBox_R1_GI_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_DUR_Header_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"DUR", None))
        self.spinBox_R1_HAN_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R3_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"R3", None))
        self.label_GI_Header_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"GI", None))
        self.spinBox_R1_TEC_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ATH_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_DUR_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ELU_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ATH_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_STR_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ATH_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ELU_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_STA_Header_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"STA", None))
        self.spinBox_R1_STR_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_SPD_Header_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"SPD", None))
        self.spinBox_R2_DUR_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_HAN_Header_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"HAN", None))
        self.label_R4_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"R4", None))
        self.spinBox_R1_TKL_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_GI_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_WE_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_SPD_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R6_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"R6", None))
        self.spinBox_R2_STA_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_BLK_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TKL_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_HAN_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_GI_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ELU_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TEC_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ATH_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_SPD_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_DUR_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_WE_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STA_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STR_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_BLK_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TKL_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_HAN_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_GI_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ELU_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TEC_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ATH_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_SPD_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_DUR_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_WE_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STA_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STR_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_BLK_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TKL_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_HAN_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_GI_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ELU_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TEC_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ATH_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_SPD_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_DUR_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_WE_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STA_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STR_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_BLK_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TKL_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_HAN_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_GI_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ELU_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TEC_OL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.lineEdit_R1_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"OL", None))
        self.lineEdit_R2_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"Tackle", None))
        self.lineEdit_R3_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"Grd-Cntr", None))
        self.lineEdit_R4_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"OLUser1", None))
        self.lineEdit_R5_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"OLUser2", None))
        self.lineEdit_R6_OL.setText(QCoreApplication.translate("DialogRoleRatings", u"OLUser3", None))
        self.tabWidgetRoleRatings.setTabText(self.tabWidgetRoleRatings.indexOf(self.OL), QCoreApplication.translate("DialogRoleRatings", u"OL", None))
        self.label_ATH_Header_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"ATH", None))
        self.spinBox_R2_TKL_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_DUR_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_STR_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_TEC_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_WE_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_SPD_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_TEC_Header_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"TEC", None))
        self.spinBox_R1_BLK_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_STA_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_WE_Header_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"WE", None))
        self.label_TKL_Header_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"TKL", None))
        self.label_STR_Header_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"STR", None))
        self.spinBox_R1_WE_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_SPD_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R1_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"R1", None))
        self.label_RoleHeader_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"Role", None))
        self.label_Total_Header_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"Total", None))
        self.spinBox_R3_STA_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R5_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"R5", None))
        self.label_BLK_Header_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"BLK", None))
        self.label_ELU_Header_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"ELU", None))
        self.spinBox_R2_BLK_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_LabelHeader_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"Label", None))
        self.spinBox_R2_HAN_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R2_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"R2", None))
        self.spinBox_R1_GI_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_DUR_Header_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"DUR", None))
        self.spinBox_R1_HAN_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R3_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"R3", None))
        self.label_GI_Header_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"GI", None))
        self.spinBox_R1_TEC_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ATH_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_DUR_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ELU_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ATH_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_STR_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ATH_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ELU_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_STA_Header_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"STA", None))
        self.spinBox_R1_STR_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_SPD_Header_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"SPD", None))
        self.spinBox_R2_DUR_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_HAN_Header_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"HAN", None))
        self.label_R4_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"R4", None))
        self.spinBox_R1_TKL_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_GI_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_WE_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_SPD_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R6_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"R6", None))
        self.spinBox_R2_STA_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_BLK_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TKL_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_HAN_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_GI_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ELU_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TEC_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ATH_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_SPD_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_DUR_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_WE_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STA_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STR_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_BLK_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TKL_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_HAN_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_GI_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ELU_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TEC_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ATH_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_SPD_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_DUR_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_WE_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STA_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STR_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_BLK_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TKL_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_HAN_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_GI_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ELU_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TEC_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ATH_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_SPD_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_DUR_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_WE_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STA_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STR_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_BLK_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TKL_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_HAN_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_GI_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ELU_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TEC_DL.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.lineEdit_R1_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"DL", None))
        self.lineEdit_R2_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"DT", None))
        self.lineEdit_R3_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"DE", None))
        self.lineEdit_R4_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"DLUser1", None))
        self.lineEdit_R5_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"DLUser2", None))
        self.lineEdit_R6_DL.setText(QCoreApplication.translate("DialogRoleRatings", u"DLUser3", None))
        self.tabWidgetRoleRatings.setTabText(self.tabWidgetRoleRatings.indexOf(self.DL), QCoreApplication.translate("DialogRoleRatings", u"DL", None))
        self.label_ATH_Header_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"ATH", None))
        self.spinBox_R2_TKL_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_DUR_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_STR_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_TEC_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_WE_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_SPD_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_TEC_Header_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"TEC", None))
        self.spinBox_R1_BLK_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_STA_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_WE_Header_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"WE", None))
        self.label_TKL_Header_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"TKL", None))
        self.label_STR_Header_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"STR", None))
        self.spinBox_R1_WE_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_SPD_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R1_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"R1", None))
        self.label_RoleHeader_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"Role", None))
        self.label_Total_Header_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"Total", None))
        self.spinBox_R3_STA_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R5_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"R5", None))
        self.label_BLK_Header_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"BLK", None))
        self.label_ELU_Header_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"ELU", None))
        self.spinBox_R2_BLK_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_LabelHeader_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"Label", None))
        self.spinBox_R2_HAN_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R2_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"R2", None))
        self.spinBox_R1_GI_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_DUR_Header_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"DUR", None))
        self.spinBox_R1_HAN_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R3_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"R3", None))
        self.label_GI_Header_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"GI", None))
        self.spinBox_R1_TEC_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ATH_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_DUR_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ELU_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ATH_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_STR_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ATH_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ELU_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_STA_Header_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"STA", None))
        self.spinBox_R1_STR_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_SPD_Header_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"SPD", None))
        self.spinBox_R2_DUR_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_HAN_Header_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"HAN", None))
        self.label_R4_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"R4", None))
        self.spinBox_R1_TKL_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_GI_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_WE_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_SPD_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R6_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"R6", None))
        self.spinBox_R2_STA_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_BLK_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TKL_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_HAN_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_GI_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ELU_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TEC_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ATH_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_SPD_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_DUR_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_WE_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STA_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STR_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_BLK_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TKL_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_HAN_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_GI_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ELU_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TEC_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ATH_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_SPD_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_DUR_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_WE_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STA_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STR_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_BLK_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TKL_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_HAN_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_GI_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ELU_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TEC_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ATH_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_SPD_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_DUR_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_WE_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STA_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STR_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_BLK_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TKL_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_HAN_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_GI_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ELU_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TEC_LB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.lineEdit_R1_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"LB", None))
        self.lineEdit_R2_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"ILB", None))
        self.lineEdit_R3_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"OLB", None))
        self.lineEdit_R4_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"LBUser1", None))
        self.lineEdit_R5_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"LBUser2", None))
        self.lineEdit_R6_LB.setText(QCoreApplication.translate("DialogRoleRatings", u"LBUser3", None))
        self.tabWidgetRoleRatings.setTabText(self.tabWidgetRoleRatings.indexOf(self.LB), QCoreApplication.translate("DialogRoleRatings", u"LB", None))
        self.label_ATH_Header_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"ATH", None))
        self.spinBox_R2_TKL_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_DUR_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_STR_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_TEC_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_WE_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_SPD_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_TEC_Header_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"TEC", None))
        self.spinBox_R1_BLK_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_STA_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_WE_Header_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"WE", None))
        self.label_TKL_Header_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"TKL", None))
        self.label_STR_Header_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"STR", None))
        self.spinBox_R1_WE_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_SPD_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R1_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"R1", None))
        self.label_RoleHeader_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"Role", None))
        self.label_Total_Header_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"Total", None))
        self.spinBox_R3_STA_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R5_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"R5", None))
        self.label_BLK_Header_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"BLK", None))
        self.label_ELU_Header_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"ELU", None))
        self.spinBox_R2_BLK_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_LabelHeader_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"Label", None))
        self.spinBox_R2_HAN_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R2_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"R2", None))
        self.spinBox_R1_GI_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_DUR_Header_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"DUR", None))
        self.spinBox_R1_HAN_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R3_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"R3", None))
        self.label_GI_Header_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"GI", None))
        self.spinBox_R1_TEC_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ATH_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_DUR_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ELU_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ATH_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_STR_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ATH_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ELU_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_STA_Header_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"STA", None))
        self.spinBox_R1_STR_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_SPD_Header_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"SPD", None))
        self.spinBox_R2_DUR_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_HAN_Header_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"HAN", None))
        self.label_R4_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"R4", None))
        self.spinBox_R1_TKL_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_GI_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_WE_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_SPD_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R6_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"R6", None))
        self.spinBox_R2_STA_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_BLK_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TKL_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_HAN_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_GI_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ELU_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TEC_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ATH_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_SPD_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_DUR_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_WE_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STA_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STR_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_BLK_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TKL_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_HAN_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_GI_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ELU_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TEC_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ATH_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_SPD_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_DUR_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_WE_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STA_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STR_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_BLK_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TKL_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_HAN_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_GI_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ELU_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TEC_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ATH_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_SPD_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_DUR_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_WE_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STA_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STR_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_BLK_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TKL_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_HAN_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_GI_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ELU_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TEC_DB.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.lineEdit_R1_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"DB", None))
        self.lineEdit_R2_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"Safety", None))
        self.lineEdit_R3_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"CB", None))
        self.lineEdit_R4_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"DBUser1", None))
        self.lineEdit_R5_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"DBUser2", None))
        self.lineEdit_R6_DB.setText(QCoreApplication.translate("DialogRoleRatings", u"DBUser3", None))
        self.tabWidgetRoleRatings.setTabText(self.tabWidgetRoleRatings.indexOf(self.DB), QCoreApplication.translate("DialogRoleRatings", u"DB", None))
        self.label_ATH_Header_K.setText(QCoreApplication.translate("DialogRoleRatings", u"ATH", None))
        self.spinBox_R2_TKL_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_DUR_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_STR_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_TEC_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_WE_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_SPD_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_TEC_Header_K.setText(QCoreApplication.translate("DialogRoleRatings", u"TEC", None))
        self.spinBox_R1_BLK_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_STA_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_WE_Header_K.setText(QCoreApplication.translate("DialogRoleRatings", u"WE", None))
        self.label_TKL_Header_K.setText(QCoreApplication.translate("DialogRoleRatings", u"TKL", None))
        self.label_STR_Header_K.setText(QCoreApplication.translate("DialogRoleRatings", u"STR", None))
        self.spinBox_R1_WE_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_SPD_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R1_K.setText(QCoreApplication.translate("DialogRoleRatings", u"R1", None))
        self.label_RoleHeader_K.setText(QCoreApplication.translate("DialogRoleRatings", u"Role", None))
        self.label_Total_Header_K.setText(QCoreApplication.translate("DialogRoleRatings", u"Total", None))
        self.spinBox_R3_STA_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R5_K.setText(QCoreApplication.translate("DialogRoleRatings", u"R5", None))
        self.label_BLK_Header_K.setText(QCoreApplication.translate("DialogRoleRatings", u"BLK", None))
        self.label_ELU_Header_K.setText(QCoreApplication.translate("DialogRoleRatings", u"ELU", None))
        self.spinBox_R2_BLK_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_LabelHeader_K.setText(QCoreApplication.translate("DialogRoleRatings", u"Label", None))
        self.spinBox_R2_HAN_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R2_K.setText(QCoreApplication.translate("DialogRoleRatings", u"R2", None))
        self.spinBox_R1_GI_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_DUR_Header_K.setText(QCoreApplication.translate("DialogRoleRatings", u"DUR", None))
        self.spinBox_R1_HAN_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R3_K.setText(QCoreApplication.translate("DialogRoleRatings", u"R3", None))
        self.label_GI_Header_K.setText(QCoreApplication.translate("DialogRoleRatings", u"GI", None))
        self.spinBox_R1_TEC_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ATH_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_DUR_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ELU_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ATH_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_STR_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ATH_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ELU_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_STA_Header_K.setText(QCoreApplication.translate("DialogRoleRatings", u"STA", None))
        self.spinBox_R1_STR_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_SPD_Header_K.setText(QCoreApplication.translate("DialogRoleRatings", u"SPD", None))
        self.spinBox_R2_DUR_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_HAN_Header_K.setText(QCoreApplication.translate("DialogRoleRatings", u"HAN", None))
        self.label_R4_K.setText(QCoreApplication.translate("DialogRoleRatings", u"R4", None))
        self.spinBox_R1_TKL_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_GI_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_WE_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_SPD_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R6_K.setText(QCoreApplication.translate("DialogRoleRatings", u"R6", None))
        self.spinBox_R2_STA_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_BLK_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TKL_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_HAN_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_GI_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ELU_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TEC_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ATH_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_SPD_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_DUR_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_WE_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STA_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STR_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_BLK_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TKL_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_HAN_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_GI_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ELU_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TEC_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ATH_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_SPD_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_DUR_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_WE_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STA_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STR_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_BLK_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TKL_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_HAN_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_GI_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ELU_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TEC_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ATH_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_SPD_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_DUR_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_WE_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STA_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STR_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_BLK_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TKL_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_HAN_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_GI_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ELU_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TEC_K.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.lineEdit_R1_K.setText(QCoreApplication.translate("DialogRoleRatings", u"K", None))
        self.lineEdit_R2_K.setText(QCoreApplication.translate("DialogRoleRatings", u"KUser1", None))
        self.lineEdit_R3_K.setText(QCoreApplication.translate("DialogRoleRatings", u"KUser2", None))
        self.lineEdit_R4_K.setText(QCoreApplication.translate("DialogRoleRatings", u"KUser3", None))
        self.lineEdit_R5_K.setText(QCoreApplication.translate("DialogRoleRatings", u"KUser4", None))
        self.lineEdit_R6_K.setText(QCoreApplication.translate("DialogRoleRatings", u"KUser5", None))
        self.tabWidgetRoleRatings.setTabText(self.tabWidgetRoleRatings.indexOf(self.K), QCoreApplication.translate("DialogRoleRatings", u"K", None))
        self.label_ATH_Header_P.setText(QCoreApplication.translate("DialogRoleRatings", u"ATH", None))
        self.spinBox_R2_TKL_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_DUR_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_STR_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_TEC_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_WE_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_SPD_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_TEC_Header_P.setText(QCoreApplication.translate("DialogRoleRatings", u"TEC", None))
        self.spinBox_R1_BLK_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_STA_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_WE_Header_P.setText(QCoreApplication.translate("DialogRoleRatings", u"WE", None))
        self.label_TKL_Header_P.setText(QCoreApplication.translate("DialogRoleRatings", u"TKL", None))
        self.label_STR_Header_P.setText(QCoreApplication.translate("DialogRoleRatings", u"STR", None))
        self.spinBox_R1_WE_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_SPD_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R1_P.setText(QCoreApplication.translate("DialogRoleRatings", u"R1", None))
        self.label_RoleHeader_P.setText(QCoreApplication.translate("DialogRoleRatings", u"Role", None))
        self.label_Total_Header_P.setText(QCoreApplication.translate("DialogRoleRatings", u"Total", None))
        self.spinBox_R3_STA_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R5_P.setText(QCoreApplication.translate("DialogRoleRatings", u"R5", None))
        self.label_BLK_Header_P.setText(QCoreApplication.translate("DialogRoleRatings", u"BLK", None))
        self.label_ELU_Header_P.setText(QCoreApplication.translate("DialogRoleRatings", u"ELU", None))
        self.spinBox_R2_BLK_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_LabelHeader_P.setText(QCoreApplication.translate("DialogRoleRatings", u"Label", None))
        self.spinBox_R2_HAN_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R2_P.setText(QCoreApplication.translate("DialogRoleRatings", u"R2", None))
        self.spinBox_R1_GI_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_DUR_Header_P.setText(QCoreApplication.translate("DialogRoleRatings", u"DUR", None))
        self.spinBox_R1_HAN_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R3_P.setText(QCoreApplication.translate("DialogRoleRatings", u"R3", None))
        self.label_GI_Header_P.setText(QCoreApplication.translate("DialogRoleRatings", u"GI", None))
        self.spinBox_R1_TEC_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ATH_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_DUR_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ELU_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_ATH_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_STR_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ATH_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R1_ELU_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_STA_Header_P.setText(QCoreApplication.translate("DialogRoleRatings", u"STA", None))
        self.spinBox_R1_STR_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_SPD_Header_P.setText(QCoreApplication.translate("DialogRoleRatings", u"SPD", None))
        self.spinBox_R2_DUR_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_HAN_Header_P.setText(QCoreApplication.translate("DialogRoleRatings", u"HAN", None))
        self.label_R4_P.setText(QCoreApplication.translate("DialogRoleRatings", u"R4", None))
        self.spinBox_R1_TKL_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R2_GI_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_WE_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_SPD_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.label_R6_P.setText(QCoreApplication.translate("DialogRoleRatings", u"R6", None))
        self.spinBox_R2_STA_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_BLK_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TKL_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_HAN_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_GI_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_ELU_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R3_TEC_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ATH_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_SPD_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_DUR_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_WE_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STA_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_STR_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_BLK_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TKL_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_HAN_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_GI_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_ELU_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R4_TEC_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ATH_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_SPD_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_DUR_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_WE_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STA_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_STR_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_BLK_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TKL_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_HAN_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_GI_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_ELU_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R5_TEC_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ATH_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_SPD_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_DUR_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_WE_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STA_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_STR_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_BLK_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TKL_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_HAN_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_GI_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_ELU_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.spinBox_R6_TEC_P.setSuffix(QCoreApplication.translate("DialogRoleRatings", u"%", None))
        self.lineEdit_R1_P.setText(QCoreApplication.translate("DialogRoleRatings", u"P", None))
        self.lineEdit_R2_P.setText(QCoreApplication.translate("DialogRoleRatings", u"PUser1", None))
        self.lineEdit_R3_P.setText(QCoreApplication.translate("DialogRoleRatings", u"PUser2", None))
        self.lineEdit_R4_P.setText(QCoreApplication.translate("DialogRoleRatings", u"PUser3", None))
        self.lineEdit_R5_P.setText(QCoreApplication.translate("DialogRoleRatings", u"PUser4", None))
        self.lineEdit_R6_P.setText(QCoreApplication.translate("DialogRoleRatings", u"PUser5", None))
        self.tabWidgetRoleRatings.setTabText(self.tabWidgetRoleRatings.indexOf(self.P), QCoreApplication.translate("DialogRoleRatings", u"P", None))
        self.label.setText(QCoreApplication.translate("DialogRoleRatings", u"Customize role ratings by position. Each row should add up to 100 for the calculations to work correctly.", None))
    # retranslateUi

