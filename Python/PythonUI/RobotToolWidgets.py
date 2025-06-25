from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,Qt

import PyQt5Widgets
from PyQt5Widgets import PushBut, LCDNumber, Label, LCDPanel, jogBut
from functools import partial

class PoseWidget(QtWidgets.QWidget):
    def __init__(self,parent = None):
        super(PoseWidget,self).__init__(parent)
        self.horizontalLayoutWidget = QtWidgets.QWidget()
        #self.setFixedWidth(235)
        #self.setFixedHeight(325)
        self.gridLayout = QtWidgets.QGridLayout()

        self.lcdNumber_1 = LCDNumber(self)
        self.gridLayout.addWidget(self.lcdNumber_1, 0, 0, 1, 1)

        self.lcdNumber_2 = LCDNumber(self)
        self.gridLayout.addWidget(self.lcdNumber_2, 0, 1, 1, 1)

        self.lcdNumber_3 = LCDNumber(self)
        self.gridLayout.addWidget(self.lcdNumber_3, 0, 2, 1, 1)

        self.lcdNumber_4 = LCDNumber(self)
        self.gridLayout.addWidget(self.lcdNumber_4, 0, 3, 1, 1)

        self.lcdNumber_5 = LCDNumber(self)
        self.gridLayout.addWidget(self.lcdNumber_5, 0, 4, 1, 1)

        self.lcdNumber_6 = LCDNumber(self)
        self.gridLayout.addWidget(self.lcdNumber_6, 0, 5, 1, 1)

        self.label_1 = Label(self)
        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1)

        self.label_2 = Label(self)
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = Label(self)
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_4 = Label(self)
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)

        self.label_5 = Label(self)
        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1)

        self.label_6 = Label(self)
        self.gridLayout.addWidget(self.label_6, 1, 5, 1, 1)



        self.setLayout(self.gridLayout)

    def update(self,info):
        self.lcdNumber_1.display(info[0])
        self.lcdNumber_2.display(info[1])
        self.lcdNumber_3.display(info[2])
        self.lcdNumber_4.display(info[3])
        self.lcdNumber_5.display(info[4])
        self.lcdNumber_6.display(info[5])
            

    def reset(self):
        self.lcdNumber_1.display(0)
        self.lcdNumber_1.default()
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
            
    def set_label(self, info):
        self.label_1.setText(info[0])
        self.label_2.setText(info[1])
        self.label_3.setText(info[2])
        self.label_4.setText(info[3])
        self.label_5.setText(info[4])
        self.label_6.setText(info[5])

    
class JogPanel(QtWidgets.QWidget):
    mode = pyqtSignal(str)
    vel = pyqtSignal(int)
    delta = pyqtSignal(list)
    def __init__(self,parent = None):
        super (JogPanel,self).__init__(parent)
        self.hboxLayout = QtWidgets.QHBoxLayout()
        self.vboxLayout = QtWidgets.QVBoxLayout()
        self.gridLayout = QtWidgets.QGridLayout()
        
        self.jog = QtWidgets.QPushButton()
        self.jog.setMaximumHeight(50)
        self.jog.setText("Jogging Mode")
        self.jog.setCheckable(True)

        self.joymode = QtWidgets.QPushButton()
        self.joymode.setMaximumHeight(25)
        self.joymode.setText("Use Joystick")
        self.joymode.setCheckable(True)
        self.joymode.setEnabled(False)

        self.jointsMode = QtWidgets.QRadioButton("Joints")
        self.WRFMode = QtWidgets.QRadioButton("WRF")
        self.TRFMode = QtWidgets.QRadioButton("TRF")
        self.jointsMode.setEnabled(False)
        self.WRFMode.setEnabled(False)
        self.TRFMode.setEnabled(False)

        self.hboxLayout.addWidget(self.jointsMode)
        self.hboxLayout.addWidget(self.WRFMode)
        self.hboxLayout.addWidget(self.TRFMode)

        self.label_1 = QtWidgets.QLabel()
        self.gridLayout.addWidget(self.label_1,0,0,1,1)
        self.btn1 = jogBut()
        self.btn1.setText("-")
        self.gridLayout.addWidget(self.btn1,0,1,1,1)
        self.btn2 = jogBut()
        self.btn2.setText("+")
        self.gridLayout.addWidget(self.btn2,0,2,1,1)
        
        self.label_2= QtWidgets.QLabel()
        self.gridLayout.addWidget(self.label_2,1,0,1,1)
        self.btn3 = jogBut()
        self.btn3.setText("-")
        self.gridLayout.addWidget(self.btn3,1,1,1,1)
        self.btn4 = jogBut()
        self.btn4.setText("+")
        self.gridLayout.addWidget(self.btn4,1,2,1,1)
        
        
        self.label_3= QtWidgets.QLabel()
        self.gridLayout.addWidget(self.label_3,2,0,1,1)
        self.btn5 = jogBut()
        self.btn5.setText("-")
        self.gridLayout.addWidget(self.btn5,2,1,1,1)
        self.btn6 = jogBut()
        self.btn6.setText("+")
        self.gridLayout.addWidget(self.btn6,2,2,1,1)

        self.label_4= QtWidgets.QLabel()
        self.gridLayout.addWidget(self.label_4,3,0,1,1)
        self.btn7 = jogBut()
        self.btn7.setText("-")
        self.gridLayout.addWidget(self.btn7,3,1,1,1)
        self.btn8 = jogBut()
        self.btn8.setText("+")
        self.gridLayout.addWidget(self.btn8,3,2,1,1)
        
        self.label_5= QtWidgets.QLabel()
        self.gridLayout.addWidget(self.label_5,4,0,1,1)
        self.btn9 = jogBut()
        self.btn9.setText("-")
        self.gridLayout.addWidget(self.btn9,4,1,1,1)
        self.btn10 = jogBut()
        self.btn10.setText("+")
        self.gridLayout.addWidget(self.btn10,4,2,1,1)
        

        self.label_6= QtWidgets.QLabel()
        self.gridLayout.addWidget(self.label_6,5,0,1,1)
        self.btn11 = jogBut()
        self.btn11.setText("-")
        self.gridLayout.addWidget(self.btn11,5,1,1,1)
        self.btn12 = jogBut()
        self.btn12.setText("+")
        self.gridLayout.addWidget(self.btn12,5,2,1,1)
        self.btn1.setEnabled(False)
        self.btn2.setEnabled(False)
        self.btn3.setEnabled(False)
        self.btn4.setEnabled(False)
        self.btn5.setEnabled(False)
        self.btn6.setEnabled(False)
        self.btn7.setEnabled(False)
        self.btn8.setEnabled(False)
        self.btn9.setEnabled(False)
        self.btn10.setEnabled(False)
        self.btn11.setEnabled(False)
        self.btn12.setEnabled(False)

        self.speed_set_label = QtWidgets.QLabel("Speed Settings")
        self.speed_set_label.setMaximumHeight(50)

        self.slider_layout = QtWidgets.QHBoxLayout()
        
        self.speed = QtWidgets.QSlider(Qt.Horizontal)
        self.speed.setRange(0, 20)
        self.speed.setFocusPolicy(Qt.NoFocus)
        self.speed.setPageStep(5)
        self.speed.setValue(0)
        self.val = QtWidgets.QLabel('0')
        self.val.setMaximumHeight(50)
        self.val.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        self.slider_layout.addWidget(self.speed)
        self.slider_layout.addWidget(self.val)

        self.vboxLayout.addWidget(self.jog)
        self.vboxLayout.addWidget(self.joymode)
        self.vboxLayout.addLayout(self.hboxLayout)
        self.vboxLayout.addLayout(self.gridLayout)
        self.vboxLayout.addWidget(self.speed_set_label)
        self.vboxLayout.addLayout(self.slider_layout)
        
        self.setLayout(self.vboxLayout)

        self.jointsMode.toggled.connect(self.on_joints)
        self.WRFMode.toggled.connect(self.on_WRF)
        self.TRFMode.toggled.connect(self.on_TRF)
        self.jog.clicked.connect(self.enable_jog)
        self.speed.valueChanged.connect(self.updateVal)

        #Button connection
        self.btn1.clicked.connect(lambda ignore, label=0, direction='-': self.on_button_delta(label, direction))
        self.btn2.clicked.connect(lambda ignore, label=0, direction='+': self.on_button_delta(label, direction))
        self.btn3.clicked.connect(lambda ignore, label=1, direction='-': self.on_button_delta(label, direction))
        self.btn4.clicked.connect(lambda ignore, label=1, direction='+': self.on_button_delta(label, direction))
        self.btn5.clicked.connect(lambda ignore, label=2, direction='-': self.on_button_delta(label, direction))
        self.btn6.clicked.connect(lambda ignore, label=2, direction='+': self.on_button_delta(label, direction))
        self.btn7.clicked.connect(lambda ignore, label=3, direction='-': self.on_button_delta(label, direction))
        self.btn8.clicked.connect(lambda ignore, label=3, direction='+': self.on_button_delta(label, direction))
        self.btn9.clicked.connect(lambda ignore, label=4, direction='-': self.on_button_delta(label, direction))
        self.btn10.clicked.connect(lambda ignore, label=4, direction='+': self.on_button_delta(label, direction))
        self.btn11.clicked.connect(lambda ignore, label=5, direction='-': self.on_button_delta(label, direction))
        self.btn12.clicked.connect(lambda ignore, label=5, direction='+': self.on_button_delta(label, direction))

        self.joymode.clicked.connect(self.on_joy_mode)
        
    def enable_jog(self):
        if self.jog.isChecked():
                
            self.jointsMode.setEnabled(True)
            self.WRFMode.setEnabled(True)
            self.TRFMode.setEnabled(True)
            self.joymode.setEnabled(True)

            self.btn1.setEnabled(True)
            self.btn2.setEnabled(True)
            self.btn3.setEnabled(True)
            self.btn4.setEnabled(True)
            self.btn5.setEnabled(True)
            self.btn6.setEnabled(True)
            self.btn7.setEnabled(True)
            self.btn8.setEnabled(True)
            self.btn9.setEnabled(True)
            self.btn10.setEnabled(True)
            self.btn11.setEnabled(True)
            self.btn12.setEnabled(True)

        else:
    
            self.jointsMode.setEnabled(False)
            self.WRFMode.setEnabled(False)
            self.TRFMode.setEnabled(False)
            self.joymode.setEnabled(False)

            self.btn1.setEnabled(False)
            self.btn2.setEnabled(False)
            self.btn3.setEnabled(False)
            self.btn4.setEnabled(False)
            self.btn5.setEnabled(False)
            self.btn6.setEnabled(False)
            self.btn7.setEnabled(False)
            self.btn8.setEnabled(False)
            self.btn9.setEnabled(False)
            self.btn10.setEnabled(False)
            self.btn11.setEnabled(False)
            self.btn12.setEnabled(False)

    def on_joy_mode(self):
        if self.joymode.isChecked():
            self.btn1.setEnabled(False)
            self.btn2.setEnabled(False)
            self.btn3.setEnabled(False)
            self.btn4.setEnabled(False)
            self.btn5.setEnabled(False)
            self.btn6.setEnabled(False)
            self.btn7.setEnabled(False)
            self.btn8.setEnabled(False)
            self.btn9.setEnabled(False)
            self.btn10.setEnabled(False)
            self.btn11.setEnabled(False)
            self.btn12.setEnabled(False)
        else:
            self.btn1.setEnabled(True)
            self.btn2.setEnabled(True)
            self.btn3.setEnabled(True)
            self.btn4.setEnabled(True)
            self.btn5.setEnabled(True)
            self.btn6.setEnabled(True)
            self.btn7.setEnabled(True)
            self.btn8.setEnabled(True)
            self.btn9.setEnabled(True)
            self.btn10.setEnabled(True)
            self.btn11.setEnabled(True)
            self.btn12.setEnabled(True)
            
    def on_joints(self):
        self.mode.emit("Joints")
        self.updateLabel("Joints")
    def on_WRF(self):
        self.mode.emit("WRF")
        self.updateLabel("WRF")
    def on_TRF(self):
        self.mode.emit("TRF")
        self.updateLabel("TRF")
        
    def updateLabel(self,value):
        if value == "Joints":
            self.label_1.setText("J1")
            self.label_2.setText("J2")
            self.label_3.setText("J3")
            self.label_4.setText("J4")
            self.label_5.setText("J5")
            self.label_6.setText("J6")
            
            
        elif (value == "WRF") or (value == "TRF"):
            self.label_1.setText("X")
            self.label_2.setText("Y")
            self.label_3.setText("Z")
            self.label_4.setText("Rx")
            self.label_5.setText("Ry")
            self.label_6.setText("Rz")

    def updateVal(self, value):
        self.val.setText(str(value))
        self.vel.emit(value)

    def on_button_delta(self, label, direction):
        data = [0, 0, 0, 0, 0, 0]
        if direction == '+':
            data[label] = 1
        else:
            data[label] = -1
        self.delta.emit(data)


class TeachPanel(QtWidgets.QWidget):
    def __init__(self,parent = None):
        super (TeachPanel,self).__init__(parent)
        #self.setWindowTitle("QThread Application")
        #self.setWindowIcon(QtGui.QIcon("Path/to/image/file.png"))
        #self.setMinimumWidth(resolution.width() / 3)
        #self.setMinimumHeight(resolution.height() / 1.5)
        #self.setStyleSheet("QScrollBar:horizontal {width: 1px; height: 1px;}, QScrollBar:vertical {width: 1px;height: 1px;}")
        self.linef = QtWidgets.QLineEdit(self)
        self.linef.setPlaceholderText("Command to send...")
        self.linef.setStyleSheet("margin: 1px; padding: 7px;border-style: solid;border-radius: 3px;border-width: 0.5px;")
        self.but1 = PushBut(self)
        self.but1.setText("Send")
        #self.but1.setFixedWidth(72)
        #self.but1.setFont(font_but)
                                 
        self.textf = QtWidgets.QPlainTextEdit(self)
        self.textf.setPlaceholderText("Programm...")
        self.textf.setTabStopDistance(QtGui.QFontMetricsF(self.textf.font()).horizontalAdvance(' ') * 4)
        #self.textfsetStyleSheet("margin: 1px; padding: 7px;border-style: solid;border-radius: 3px;border-width: 0.5px;")
                                 
        self.but2 = PushBut(self)
        self.but2.setText("MoveJoints")
        #self.but2.setFixedWidth(72)
        #self.but2.setFont(font_but)
        self.but3 = PushBut(self)
        self.but3.setText("MovePose")
        #self.but3.setFixedWidth(72)
        #self.but3.setFont(font_but)
        self.but4 = PushBut(self)
        self.but4.setText("MoveLin")
        #self.but4.setFixedWidth(72)
        #self.but4.setFont(font_but)

        self.grid2 = QtWidgets.QGridLayout()
        self.grid2.addWidget(self.but2, 0, 0, 1, 1)
        self.grid2.addWidget(self.but3, 0, 2, 1, 1)
        self.grid2.addWidget(self.but4, 0, 3, 1, 1)
        self.grid1 = QtWidgets.QGridLayout()
        self.grid1.addWidget(self.linef, 0, 0, 1, 1)
        self.grid1.addWidget(self.but1, 1, 0, 1, 1)
        self.grid1.addWidget(self.textf, 2, 0, 13, 1)
        self.grid1.addLayout(self.grid2, 16, 0, 1, 1)
        self.grid1.setContentsMargins(7, 7, 7, 7)
        self.setLayout(self.grid1)

class MoxaVisual(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MoxaVisual, self).__init__(parent)
        self.wid = QtWidgets.QHBoxLayout()
        self.Inputs = QtWidgets.QVBoxLayout()
        self.Outputs = QtWidgets.QVBoxLayout()
        self.OutLabels = QtWidgets.QVBoxLayout()

        self.wid.addLayout(self.Inputs)
        self.wid.addLayout(self.OutLabels)
        self.wid.addLayout(self.Outputs)

        self.in_0 = QtWidgets.QLabel()
        self.in_1 = QtWidgets.QLabel()
        self.in_2 = QtWidgets.QLabel()
        self.in_3 = QtWidgets.QLabel()
        self.in_4 = QtWidgets.QLabel()
        self.in_5 = QtWidgets.QLabel()
        self.in_6 = QtWidgets.QLabel()
        self.in_7 = QtWidgets.QLabel()

        self.outL_0 = QtWidgets.QLabel()
        self.outL_1 = QtWidgets.QLabel()
        self.outL_2 = QtWidgets.QLabel()
        self.outL_3 = QtWidgets.QLabel()
        self.outL_4 = QtWidgets.QLabel()
        self.outL_5 = QtWidgets.QLabel()
        self.outL_6 = QtWidgets.QLabel()
        self.outL_7 = QtWidgets.QLabel()

        self.outL_0.setText("Output 0")
        self.outL_1.setText("Output 1")
        self.outL_2.setText("Output 2")
        self.outL_3.setText("Output 3")
        self.outL_4.setText("Output 4")
        self.outL_5.setText("Output 5")
        self.outL_6.setText("Output 6")
        self.outL_7.setText("Output 7")

        self.out_0 = PyQt5Widgets.OutputButton()
        self.out_0.setCheckable(True)
        self.out_1 = PyQt5Widgets.OutputButton()
        self.out_1.setCheckable(True)
        self.out_2 = PyQt5Widgets.OutputButton()
        self.out_2.setCheckable(True)
        self.out_3 = PyQt5Widgets.OutputButton()
        self.out_3.setCheckable(True)
        self.out_4 = PyQt5Widgets.OutputButton()
        self.out_4.setCheckable(True)
        self.out_5 = PyQt5Widgets.OutputButton()
        self.out_5.setCheckable(True)
        self.out_6 = PyQt5Widgets.OutputButton()
        self.out_6.setCheckable(True)
        self.out_7 = PyQt5Widgets.OutputButton()
        self.out_7.setCheckable(True)

        self.in_0.setText("Input 0")
        self.in_0.setStyleSheet("border: 1px solid black;")
        self.in_1.setText("Input 1")
        self.in_1.setStyleSheet("border: 1px solid black;")
        self.in_2.setText("Input 2")
        self.in_2.setStyleSheet("border: 1px solid black;")
        self.in_3.setText("Input 3")
        self.in_3.setStyleSheet("border: 1px solid black;")
        self.in_4.setText("Input 4")
        self.in_4.setStyleSheet("border: 1px solid black;")
        self.in_5.setText("Input 5")
        self.in_5.setStyleSheet("border: 1px solid black;")
        self.in_6.setText("Input 6")
        self.in_6.setStyleSheet("border: 1px solid black;")
        self.in_7.setText("Input 7")
        self.in_7.setStyleSheet("border: 1px solid black;")

        self.Inputs.addWidget(self.in_0)
        self.Inputs.addWidget(self.in_1)
        self.Inputs.addWidget(self.in_2)
        self.Inputs.addWidget(self.in_3)
        self.Inputs.addWidget(self.in_4)
        self.Inputs.addWidget(self.in_5)
        self.Inputs.addWidget(self.in_6)
        self.Inputs.addWidget(self.in_7)

        self.OutLabels.addWidget(self.outL_0)
        self.OutLabels.addWidget(self.outL_1)
        self.OutLabels.addWidget(self.outL_2)
        self.OutLabels.addWidget(self.outL_3)
        self.OutLabels.addWidget(self.outL_4)
        self.OutLabels.addWidget(self.outL_5)
        self.OutLabels.addWidget(self.outL_6)
        self.OutLabels.addWidget(self.outL_7)

        self.Outputs.addWidget(self.out_0)
        self.Outputs.addWidget(self.out_1)
        self.Outputs.addWidget(self.out_2)
        self.Outputs.addWidget(self.out_3)
        self.Outputs.addWidget(self.out_4)
        self.Outputs.addWidget(self.out_5)
        self.Outputs.addWidget(self.out_6)
        self.Outputs.addWidget(self.out_7)

        self.setLayout(self.wid)

    def update_input(self, values):
        color_high = "background-color:rgb(0,255,0)"
        color_low = "background-color:rgb(200,200,200)"
        if values[0]:
            self.in_0.setStyleSheet(color_high)
        else:
            self.in_0.setStyleSheet(color_low)
        if values[1]:
            self.in_1.setStyleSheet(color_high)
        else:
            self.in_1.setStyleSheet(color_low)
        if values[2]:
            self.in_2.setStyleSheet(color_high)
        else:
            self.in_2.setStyleSheet(color_low)
        if values[3]:
            self.in_3.setStyleSheet(color_high)
        else:
            self.in_3.setStyleSheet(color_low)
        if values[4]:
            self.in_4.setStyleSheet(color_high)
        else:
            self.in_4.setStyleSheet(color_low)
        if values[5]:
            self.in_5.setStyleSheet(color_high)
        else:
            self.in_5.setStyleSheet(color_low)
        if values[6]:
            self.in_6.setStyleSheet(color_high)
        else:
            self.in_6.setStyleSheet(color_low)
        if values[7]:
            self.in_7.setStyleSheet(color_high)
        else:
            self.in_7.setStyleSheet(color_low)
