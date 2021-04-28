from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogRoleRatingUpdateDB_Progress(object):
    def setupUi(self, DialogRoleRatingUpdateDB_Progress):
        if not DialogRoleRatingUpdateDB_Progress.objectName():
            DialogRoleRatingUpdateDB_Progress.setObjectName(u"DialogRoleRatingUpdateDB_Progress")
        DialogRoleRatingUpdateDB_Progress.setWindowModality(Qt.ApplicationModal)
        DialogRoleRatingUpdateDB_Progress.resize(450, 230)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogRoleRatingUpdateDB_Progress.sizePolicy().hasHeightForWidth())
        DialogRoleRatingUpdateDB_Progress.setSizePolicy(sizePolicy)
        DialogRoleRatingUpdateDB_Progress.setMinimumSize(QSize(450, 230))
        DialogRoleRatingUpdateDB_Progress.setMaximumSize(QSize(450, 230))
        self.label = QLabel(DialogRoleRatingUpdateDB_Progress)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 421, 41))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.progressBar = QProgressBar(DialogRoleRatingUpdateDB_Progress)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 140, 401, 23))
        self.progressBar.setValue(24)

        self.retranslateUi(DialogRoleRatingUpdateDB_Progress)

        QMetaObject.connectSlotsByName(DialogRoleRatingUpdateDB_Progress)
    # setupUi

    def retranslateUi(self, DialogRoleRatingUpdateDB_Progress):
        DialogRoleRatingUpdateDB_Progress.setWindowTitle(QCoreApplication.translate("DialogRoleRatingUpdateDB_Progress", u"Role Ratings - Update Database", None))
        self.label.setText(QCoreApplication.translate("DialogRoleRatingUpdateDB_Progress", u"Updating Recruit Role Ratings in Database...", None))
    # retranslateUi


