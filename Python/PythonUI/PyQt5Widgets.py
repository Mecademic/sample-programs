#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,Qt
#from pubsub import pub 
import numpy as np
import time

class LCDNumber(QtWidgets.QLCDNumber):

    def __init__(self, parent=None):
        super(LCDNumber,self).__init__(parent)
        self.setMaximumWidth(500)
        self.setMaximumHeight(300)
        self.setStyleSheet("""QLCDNumber { background-color: black; color: black;}""")
        self.setDigitCount(7)
    def reset(self):
        self.display(0)
        self.setStyleSheet("""QLCDNumber { background-color: green; color: yellow;}""")
        
    def default(self):
        self.setStyleSheet("""QLCDNumber { background-color: white; color: black;}""")
        
    def overLoad(self):
        self.setStyleSheet("""QLCDNumber { background-color: red; color: white;}""")

class PushBut(QtWidgets.QPushButton):
    
    def __init__(self, parent=None):
        super(PushBut, self).__init__(parent)
        self.setMouseTracking(True)
        self.setStyleSheet("margin: 1px; padding: 7px; background-color:rgba(125,125,125,100); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
        self.setMaximumWidth(1000)
        self.setMaximumHeight(50)
        self.setIconSize(QtCore.QSize(50, 50))

    def enterEvent(self, event):
        if self.isEnabled() is True:
            self.setStyleSheet("margin: 1px; padding: 7px; background-color:rgba(255,255,255,255) ; color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
        if self.isEnabled() is False:
            pass
            #self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(255,255,255,255); color: black; border-style: solid;border-radius: 3px;border-width: 0.5px;border-color: black;")

    def leaveEvent(self, event):
        if self.isEnabled():
            self.setStyleSheet("margin: 1px; padding: 7px; background-color:rgba(125,125,125,100); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")



class jogBut(QtWidgets.QPushButton):
    
    def __init__(self, parent=None):
        super(jogBut, self).__init__(parent)
        self.setMouseTracking(True)
        self.setStyleSheet("margin: 1px; padding: 7px; background-color:rgba(125,125,125,100); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
        #self.setMaximumWidth(50)
        #self.setMaximumHeight(30)
        #self.setIconSize(QtCore.QSize(50, 50))
        self.setAutoRepeat(True)
        self.setAutoRepeatInterval(30)
        self.setAutoRepeatDelay(0) 

    def enterEvent(self, event):
        if self.isEnabled() is True:
            self.setStyleSheet("margin: 1px; padding: 7px; background-color:rgba(255,255,255,255) ; color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
        if self.isEnabled() is False:
            #self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(255,255,255,255); color: black; border-style: solid;border-radius: 3px;border-width: 0.5px;border-color: black;")
            pass

    def leaveEvent(self, event):
        if self.isEnabled():
            self.setStyleSheet("margin: 1px; padding: 7px; background-color:rgba(125,125,125,100); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")

class Label(QtWidgets.QLabel):
    
    def __init__(self, parent=None):
        super(Label, self).__init__(parent)
        self.setMaximumWidth(200)
        self.setFixedHeight(30)
        font_label = QtGui.QFont()
        font_label.setFamily('Helvetica')
        font_label.setPointSize(10)
        font_label.setWeight(25)
        self.setFont(font_label)
        self.setAlignment(Qt.AlignCenter)

class LCDPanel(QtWidgets.QWidget):
    trigger = pyqtSignal(bool)
    def __init__(self, parent=None):
        from ConfigHandler import ConfigHandler
        super(LCDPanel, self).__init__(parent)
        self.horizontalLayoutWidget = QtWidgets.QWidget()
        self.setFixedWidth(235)
        self.setFixedHeight(325)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = Label(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.label.setText('Fx')
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = Label(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setText('Fy')
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = Label(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setText('Fz')
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = Label(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setText('Tx')
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = Label(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setText('Ty')
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = Label(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.label_6.setText('Tz')
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_7 = Label(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.label_7.setText('N')
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_8 = Label(self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.label_8.setText('N')
        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)
        self.label_9 = Label(self.horizontalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.label_9.setText('N')
        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)
        self.label_10 = Label(self.horizontalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.label_10.setText('Nm')
        self.gridLayout.addWidget(self.label_10, 3, 3, 1, 1)
        self.label_11 = Label(self.horizontalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.label_11.setText('Nm')
        self.gridLayout.addWidget(self.label_11, 4, 3, 1, 1)
        self.label_12 = Label(self.horizontalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.label_12.setText('Nm')
        self.gridLayout.addWidget(self.label_12, 5, 3, 1, 1)
        
        self.lcdNumber = LCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 0, 1, 1, 2)

        self.lcdNumber_2 = LCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 1, 1, 1, 2)

        self.lcdNumber_3 = LCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout.addWidget(self.lcdNumber_3, 2, 1, 1, 2)

        self.lcdNumber_4 = LCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout.addWidget(self.lcdNumber_4, 3, 1, 1, 2)

        self.lcdNumber_5 = LCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.gridLayout.addWidget(self.lcdNumber_5, 4, 1, 1, 2)

        self.lcdNumber_6 = LCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.gridLayout.addWidget(self.lcdNumber_6, 5, 1, 1, 2)
       
        self.setLayout(self.gridLayout)
        self.config = ConfigHandler()
        self.readThreshold()
        
    def readThreshold(self):
        self.Fx = self.config.read_config('Fx')
        self.Fy = self.config.read_config('Fy')
        self.Fz = self.config.read_config('Fz')
        self.Tx = self.config.read_config('Tx')
        self.Ty = self.config.read_config('Ty')
        self.Tz = self.config.read_config('Tz')
        
    def reset(self):
        self.lcdNumber.display(0)
        self.lcdNumber.default()
        self.lcdNumber_2.display(0)
        self.lcdNumber_2.default()
        self.lcdNumber_3.display(0)
        self.lcdNumber_3.default()
        self.lcdNumber_4.display(0)
        self.lcdNumber_4.default()
        self.lcdNumber_5.display(0)
        self.lcdNumber_5.default()
        self.lcdNumber_6.display(0)
        self.lcdNumber_6.default()
        

    def update(self, info):
        self.lcdNumber.display(info[0])
        self.lcdNumber_2.display(info[1])
        self.lcdNumber_3.display(info[2])
        self.lcdNumber_4.display(info[3])
        self.lcdNumber_5.display(info[4])
        self.lcdNumber_6.display(info[5])

        if info[0] < -(self.Fx) or info[0] > self.Fx :
            self.trigger.emit(True)
            self.lcdNumber.overLoad()
            #pub.sendMessage("Force Threshold", string = "Fz Exceeded")
        else:
            self.lcdNumber.default()
            self.trigger.emit(False)

        if info[1] < -(self.Fy) or info[1] > self.Fy  :
            self.trigger.emit(True)
            self.lcdNumber_2.overLoad()
            #pub.sendMessage("Force Threshold", string = "Fy Exceeded")
        else:
            self.lcdNumber_2.default()
            self.trigger.emit(False)

        if info[2] < -(self.Fz) or info[2] > self.Fz  :
            self.trigger.emit(True)
            self.lcdNumber_3.overLoad()
            #pub.sendMessage("Force Threshold", string = "Fz Exceeded")
        else:
            self.lcdNumber_3.default()
            self.trigger.emit(False)

        if info[3] < -(self.Tx) or info[3] > self.Tx  :
            self.lcdNumber_4.overLoad()
            self.trigger.emit(True)
            #pub.sendMessage("Force Threshold", string = "Tx Exceeded")
        else:
            self.lcdNumber_4.default()
            self.trigger.emit(False)

        if info[4] < -(self.Ty) or info[4] > self.Ty  :
            self.lcdNumber_5.overLoad()
            self.trigger.emit(True)
            #pub.sendMessage("Force Threshold", string = "Ty Exceeded")
        else:
            self.lcdNumber_5.default()
            self.trigger.emit(False)

        if info[5] < -(self.Tz) or info[5] > self.Tz :
            self.lcdNumber_6.overLoad()
            self.trigger.emit(True)
            #pub.sendMessage("Force Threshold", string = "Tz Exceeded")
        else:
            self.lcdNumber_6.default()
            self.trigger.emit(False)


        
class OutputButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(OutputButton, self).__init__(parent)
        self.setStyleSheet("background-color:rgb(200,200,200)")

        self.clicked.connect(self.colorchange)

    def colorchange(self):
        if self.isChecked():
            self.setStyleSheet("background-color:rgb(0,255,0)")
        else:
            self.setStyleSheet("background-color:rgb(200,200,200)")
