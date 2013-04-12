#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.setGeometry(300, 300, 200, 190)
		self.setWindowTitle('Toggle button')
		self.show()
app = QtGui.QApplication(sys.argv)
ex=Example()
sys.exit(app.exec_())