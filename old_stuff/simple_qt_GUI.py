#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.make_grid()
		self.add_picture("dude.gif")
		self.setGeometry(300, 300, 200, 190)
		self.setWindowTitle('Toggle button')
		self.show()
	def make_square(self,x,y,color):
		self.square = QtGui.QFrame(self)
		self.square.setGeometry(x, y, 20, 20)
		self.square.setStyleSheet("QWidget { background-color: %s }" % 
			color.name())  
	def make_grid(self): 	
		color = QtGui.QColor(0, 100, 0) 
		color2 = QtGui.QColor(0, 255, 0) 
		for x in range(19):
			x*=20
			for y in range(20):	
				y*=20
				if((x/20+y/20)%2)==0:	
					self.make_square(x,y,color)
				else:
					self.make_square(x,y,color2)
	def add_picture(self,pic):
		pixmap = QtGui.QPixmap(pic)
		self.lbl = QtGui.QLabel(self)
		self.lbl.setPixmap(pixmap)
		self.lbl.setGeometry(20,15,50,50)
		self.lbl2=QtGui.QLabel(self)
		self.lbl2.setText("<font color=black size=2>Brendan missed two white pixels</font>")		
		self.lbl2.setGeometry(10,22,200,100)
		self.lbl2.show()
app = QtGui.QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())