# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created: Wed Dec 10 11:40:44 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#I added these imports...
import sys  #uses: sys.exit()


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(QtGui.QWidget):	#changed 'object' to 'QGui.QWidget'

	#I created this constructor 
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)

	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8("Form"))
		Form.resize(300, 130)
		self.verticalLayoutWidget = QtGui.QWidget(Form)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 300, 50))
		self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
		self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setMargin(0)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.PushButton = QtGui.QPushButton(self.verticalLayoutWidget)
		self.PushButton.setObjectName(_fromUtf8("PushButton"))
		self.verticalLayout.addWidget(self.PushButton)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate("Form", "Bacon Printer", None, QtGui.QApplication.UnicodeUTF8))
		self.PushButton.setText(QtGui.QApplication.translate("Form", "Print Bacon", None, QtGui.QApplication.UnicodeUTF8))
		#Here I connect the button to an event
		self.PushButton.clicked.connect(self.printBacon)

	def printBacon(self):
		print("Bacon!")

#I added this code which runs the app gui
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	mw = Ui_Form()
	mw.show()
	sys.exit(app.exec_())

#######
# END #
#######
