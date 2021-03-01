import sys
from PyQt5 import QtCore, QtGui, QtSql, QtWidgets
# from .sportsconnection import *

def initializeModel(model):
   model.setTable('recruits')
   # model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
   model.select()
   model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
   model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
   model.setHeaderData(2, QtCore.Qt.Horizontal, "Pos")
   model.setHeaderData(3, QtCore.Qt.Horizontal, "Height")
   model.setHeaderData(4, QtCore.Qt.Horizontal, "Weight")
   model.setHeaderData(5, QtCore.Qt.Horizontal, "Rating")
   model.setHeaderData(6, QtCore.Qt.Horizontal, "Rank")
   model.setHeaderData(7, QtCore.Qt.Horizontal, "Hometown")
   model.setHeaderData(8, QtCore.Qt.Horizontal, "Miles")
   model.setHeaderData(9, QtCore.Qt.Horizontal, "Considering")
   model.setHeaderData(10, QtCore.Qt.Horizontal, "ATH")
   model.setHeaderData(11, QtCore.Qt.Horizontal, "SPD")
   model.setHeaderData(12, QtCore.Qt.Horizontal, "DUR")
   model.setHeaderData(13, QtCore.Qt.Horizontal, "WE")
   model.setHeaderData(14, QtCore.Qt.Horizontal, "STA")
   model.setHeaderData(15, QtCore.Qt.Horizontal, "STR")
   model.setHeaderData(16, QtCore.Qt.Horizontal, "BLK")
   model.setHeaderData(17, QtCore.Qt.Horizontal, "TKL")
   model.setHeaderData(18, QtCore.Qt.Horizontal, "HAN")
   model.setHeaderData(19, QtCore.Qt.Horizontal, "GI")
   model.setHeaderData(20, QtCore.Qt.Horizontal, "ELU")
   model.setHeaderData(21, QtCore.Qt.Horizontal, "TEC")
   model.setHeaderData(22, QtCore.Qt.Horizontal, "TOT")
   model.setHeaderData(23, QtCore.Qt.Horizontal, "GPA")
   model.setHeaderData(24, QtCore.Qt.Horizontal, "Pot")
	
def createView(title, model):
   view = QtWidgets.QTableView()
   view.setModel(model)
   view.setWindowTitle(title)
   return view
	
def addrow():
   print(model.rowCount())
   ret = model.insertRows(model.rowCount(), 1)
   print(ret)
	
def findrow(i):
   delrow = i.row()
	
if __name__ == '__main__':

   app = QtWidgets.QApplication(sys.argv)
   db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('gddb_testing\\recruit.db')
   model = QtSql.QSqlTableModel()
   delrow = -1
   initializeModel(model)
	
   view1 = createView("Table Model (View 1)", model)
   view1.clicked.connect(findrow)
	
   dlg = QtWidgets.QDialog()
   layout = QtWidgets.QVBoxLayout()
   layout.addWidget(view1)
	
   button = QtWidgets.QPushButton("Add a row")
   #button.clicked.connect(addrow)
   layout.addWidget(button)
	
   btn1 = QtWidgets.QPushButton("del a row")
   #btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
   layout.addWidget(btn1)
	
   dlg.setLayout(layout)
   dlg.setWindowTitle("Recruit DB Demo")
   dlg.show()
   sys.exit(app.exec_())