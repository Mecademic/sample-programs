#!/usr/bin/python3.7.3
import robot as rb
import robot_common
from NetFT import Sensor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt, QThread, QObject
import time


class ForceGuideWidget(QtWidgets.QWidget):
    ForceJogStop = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        # UI Stuff
        self.setWindowTitle("Meca500")
        self.setWindowIcon(QtGui.QIcon("favicon.ico"))
        
        #self.setMinimumWidth(350)
        #self.setMinimumHeight(350)
        self.showMaximized()

        self.logo = QtWidgets.QLabel()
        self.logo.setPixmap(QtGui.QPixmap('logo.png'))

        self.robot_on = QtWidgets.QPushButton(self)
        self.robot_on.setIcon(QtGui.QIcon('robot.png'))
        self.robot_on.setMaximumWidth(100)
        self.robot_on.setMaximumHeight(100)
        self.robot_on.setIconSize(QtCore.QSize(75, 75))
        self.robot_on.setStyleSheet("margin: 1px; padding: 7px; background-color:rgba(125,125,125,0); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
        self.robot_on.setCheckable(True)
        
        self.enable = QtWidgets.QPushButton(self)
        self.enable.setIcon(QtGui.QIcon('data-wave.png'))
        self.enable.setMaximumWidth(100)
        self.enable.setMaximumHeight(100)
        self.enable.setIconSize(QtCore.QSize(90, 90))
        self.enable.setStyleSheet("margin: 1px; padding: 7px; background-color:rgba(125,125,125,0); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
        self.enable.setCheckable(True)
        self.enable.setEnabled(False)

        self.play = QtWidgets.QPushButton()
        self.play.setIcon(QtGui.QIcon('gripper.png'))
        self.play.setMaximumWidth(100)
        self.play.setMaximumHeight(100)
        self.play.setIconSize(QtCore.QSize(75, 75))
        self.play.setStyleSheet("margin: 1px; padding: 7px; background-color:rgba(125,125,125,0); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
        self.play.setCheckable(True)
        self.play.setEnabled(False)

        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.robot_on)
        self.hbox.addWidget(self.enable)
        self.hbox.addWidget(self.play)

        self.vbox = QtWidgets.QVBoxLayout()
        #self.vbox.addWidget(self.logo)
        self.vbox.addLayout(self.hbox)
        self.vbox.addSpacing(100)
        self.setLayout(self.vbox)

        self.slave_mode = False
        self.slave_address = "192.168.0.102"

        # Backend setup
        self.master_robot = rb.Robot()
        self.monitor_robot = rb.Robot()
        self.slave_robot = rb.Robot()
        self.sensor = Sensor("192.168.0.101")

        self.SensorFeedbackThread = None
        self.SensorFeedbackWorker = None
        self.sensorvalues = []
        self.MasterControlThread = None
        self.MasterControlWorker = None
        self.MasterMonitoringThread = None
        self.MasterMonitoringWorker = None
        self.jointvalues = []
        self.SlaveControlThread = None
        self.SlaveControlWorker = None

        # Connect Buttons
        self.robot_on.clicked.connect(self.on_robot)
        self.enable.clicked.connect(self.on_enable)
        self.play.clicked.connect(self.on_gripper)

    def closeEvent(self, event):
        if self.slave_mode:
            self.slave_robot.Disconnect()
        self.master_robot.Disconnect()
        event.accept()

    def on_robot(self):
        if self.robot_on.isChecked():
            self.enable.setEnabled(True)
            self.robot_on.setStyleSheet("margin: 1px; padding: 7px; background-color:rgba(125,125,125,125); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
            try:
                self.master_robot.Connect()
                self.master_robot.SetTRF(0, 0, 0, 0, 0, -22)
                self.master_robot.SetVelTimeout(0.10)
            except robot_common.CommunicationError:
                self.robot_on.setChecked(False)
                self.enable.setEnabled(False)
                print("Connection Error Master")
                self.robot_on.setStyleSheet("margin: 1px; padding: 7px; background-color:rgba(125,125,125,0); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
                return
            print("Master Connected")
            self.master_robot.ActivateAndHome()
            if self.slave_mode:
                try:
                    self.slave_robot.Connect(self.slave_address)
                except robot_common.CommunicationError:
                    self.robot_on.setChecked(False)
                    self.enable.setEnabled(False)
                    self.robot_on.setStyleSheet("margin: 1px; padding: 7px; background-color:rgba(125,125,125,0); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
                    self.master_robot.Disconnect()
                    print("Connection Error Slave")
                    return
                print("Slave Connected")
                self.play.setEnabled(True)
                self.slave_robot.ActivateAndHome()
        else:
            if self.slave_mode:
                self.slave_robot.Disconnect()
                self.monitor_robot.Disconnect()
                self.play.setEnabled(False)
            self.enable.setEnabled(False)
            self.robot_on.setStyleSheet("margin: 1px; padding: 7px; background-color:rgba(125,125,125,0); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
            self.master_robot.Disconnect()

    def on_enable(self):
        if self.enable.isChecked():
            self.robot_on.setEnabled(False)
            self.enable.setStyleSheet(
                "margin: 1px; padding: 7px; background-color:rgba(125,125,125,125); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
            # Move robot to a safe position
            if self.slave_mode:
                self.slave_robot.ClearMotion()
                self.slave_robot.ResetError()
                self.slave_robot.ResumeMotion()
            self.master_robot.ClearMotion()
            self.master_robot.ResetError()
            self.master_robot.ResumeMotion()
            self.master_robot.MoveJoints(0, 10, 15, 0, 65, 0)
            time.sleep(2)
            # Start Acquisition Thread
            self.sensor.setBias()
            self.sensor.startStreaming()
            self.SensorFeedbackThread = QThread()
            self.SensorFeedbackWorker = SensorFeedbackWorker(self.sensor)
            self.SensorFeedbackWorker.moveToThread(self.SensorFeedbackThread)
            self.SensorFeedbackThread.started.connect(self.SensorFeedbackWorker.run)
            self.SensorFeedbackWorker.finished.connect(self.SensorFeedbackThread.quit)
            self.SensorFeedbackWorker.finished.connect(self.SensorFeedbackWorker.deleteLater)
            self.SensorFeedbackThread.finished.connect(self.SensorFeedbackThread.deleteLater)
            self.SensorFeedbackWorker.sensorvalue.connect(self.update_sensor_values)
            self.SensorFeedbackThread.start()

            if self.slave_mode:
                self.start_monitoring_thread()
                self.start_jog_thread()
                self.start_slave_thread()
            else:
                self.start_jog_thread()
        else:
            self.robot_on.setEnabled(True)
            self.enable.setStyleSheet(
                "margin: 1px; padding: 7px; background-color:rgba(125,125,125,0); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
            if self.slave_mode:
                self.SlaveControlWorker.stopSignal()
                self.MasterMonitoringWorker.stopSignal()
            self.MasterControlWorker.stopSignal()
            self.SensorFeedbackWorker.stopSignal()
            self.sensor.stopStreaming()

    def on_gripper(self):
        if self.play.isChecked():
            self.slave_robot.GripperClose()
            self.play.setStyleSheet(
                "margin: 1px; padding: 7px; background-color:rgba(125,125,125,125); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")
        else:
            self.slave_robot.GripperOpen()
            self.play.setStyleSheet(
                "margin: 1px; padding: 7px; background-color:rgba(125,125,125,0); color: black; border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: black;")

    def start_jog_thread(self):
        self.MasterControlThread = QThread()
        self.MasterControlWorker = MasterControlWorker(self.master_robot)
        self.MasterControlWorker.moveToThread(self.MasterControlThread)
        self.MasterControlThread.started.connect(self.MasterControlWorker.run)
        self.MasterControlWorker.finished.connect(self.MasterControlThread.quit)
        self.MasterControlWorker.finished.connect(self.MasterControlWorker.deleteLater)
        self.MasterControlThread.finished.connect(self.MasterControlThread.deleteLater)
        self.MasterControlThread.start()

    def start_monitoring_thread(self):
        self.MasterMonitoringThread = QThread()
        self.MasterMonitoringWorker = RobotFeedbackWorker(self.master_robot)
        self.MasterMonitoringWorker.moveToThread(self.MasterMonitoringThread)
        self.MasterMonitoringThread.started.connect(self.MasterMonitoringWorker.run)
        self.MasterMonitoringWorker.finished.connect(self.MasterMonitoringThread.quit)
        self.MasterMonitoringWorker.finished.connect(self.MasterMonitoringWorker.deleteLater)
        self.MasterMonitoringThread.finished.connect(self.MasterMonitoringThread.deleteLater)
        self.MasterMonitoringWorker.jointpos.connect(self.update_joint_pos)
        self.MasterMonitoringThread.start()

    def start_slave_thread(self):
        self.jointvalues = self.master_robot.GetJoints()
        self.slave_robot.SetJointVel(20)
        self.slave_robot.MoveJoints(self.jointvalues[0],
                                    self.jointvalues[1],
                                    self.jointvalues[2],
                                    self.jointvalues[3],
                                    self.jointvalues[4],
                                    self.jointvalues[5])
        time.sleep(2)
        print("Create Slave Thread")
        self.SlaveControlThread = QThread()
        self.SlaveControlWorker = SlaveControlWorker(self.slave_robot)
        self.SlaveControlWorker.updatetargetpos(self.jointvalues)
        self.SlaveControlWorker.moveToThread(self.SlaveControlThread)
        self.SlaveControlThread.started.connect(self.SlaveControlWorker.run)
        self.SlaveControlWorker.finished.connect(self.SlaveControlThread.quit)
        self.SlaveControlWorker.finished.connect(self.SlaveControlWorker.deleteLater)
        self.SlaveControlThread.finished.connect(self.SlaveControlThread.deleteLater)
        self.SlaveControlThread.start()

    def on_replay(self):
        pass

    def update_sensor_values(self, values):
        self.sensorvalues = values
        self.MasterControlWorker.updatesensorval(values)

    def update_joint_pos(self, values):
        self.jointvalues = values
        self.SlaveControlWorker.updatetargetpos(values)

class RobotFeedbackWorker(QObject):
    finished = pyqtSignal()
    jointpos = pyqtSignal(list)

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.runFlag = True

    def run(self):
        print("Starting Master Monitoring")
        while self.runFlag:
            vals = self.robot.GetJoints()
            self.jointpos.emit(vals)
            time.sleep(0.01)
        self.finished.emit()

    def stopSignal(self):
        self.runFlag = False


class SensorFeedbackWorker(QObject):
    finished = pyqtSignal()
    sensorvalue = pyqtSignal(list)

    def __init__(self, sensor):
        super().__init__()
        print("Creating Sensor")
        self.sensor = sensor
        self.runFlag = True
        self.prev_2_vals = [0]*6
        self.prev_1_vals = [0]*6

    def run(self):
        print("Running Sensor")
        while self.runFlag:
            vals = self.sensor.measurement()
            l = 0.045
            Fay = -vals[3]/l
            Fax = vals[4]/l
            May = -(vals[0]-Fax)*l
            Max = (vals[1]-Fay)*l
            vals[0] = Fax
            vals[1] = Fay
            vals[3] = Max
            vals[4] = May
            vals = self.norm_force_data(vals)
            self.sensorvalue.emit(vals)
        print("Sensor Finished")
        self.finished.emit()

    def norm_force_data(self, val):
        norm_val = [val[0] / 40, val[1] / 40, val[2] / 120, val[3], val[4], val[5]]
        for i in range(0, 6):
            if abs(norm_val[i]) < 0.01:
                norm_val[i] = 0
        return norm_val

    def stopSignal(self):
        print("Stopping Sensor")
        self.runFlag = False


class MasterControlWorker(QObject):
    finished = pyqtSignal()

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.sensorvals = [0] * 6
        self.sensorval_prev = [0] * 6
        self.runFlag = True
        self.d = 100

    def run(self):
        print("Starting Master Control")
        max_vel = 500
        max_rot = 250
        self.robot.ResumeMotion()
        while self.runFlag:
            cmd = [max_vel*self.sensorvals[0] - self.d*self.sensorvals[0]-self.sensorval_prev[0],
                   max_vel*self.sensorvals[1] - self.d*self.sensorvals[1]-self.sensorval_prev[1],
                   max_vel*self.sensorvals[2] - self.d*self.sensorvals[2]-self.sensorval_prev[2],
                   max_rot*self.sensorvals[3] - self.d*self.sensorvals[3]-self.sensorval_prev[3],
                   max_rot*self.sensorvals[4] - self.d*self.sensorvals[4]-self.sensorval_prev[4],
                   max_rot*self.sensorvals[5] - self.d*self.sensorvals[5]-self.sensorval_prev[5]]
            self.sensorval_prev = self.sensorvals
            self.robot.MoveLinVelTRF(cmd[0], cmd[1], cmd[2], cmd[3], cmd[4], cmd[5])
            time.sleep(0.004)
        print("Finishing Master Control")
        self.finished.emit()

    def updatesensorval(self, val):
        self.sensorvals = val

    def stopSignal(self):
        self.runFlag = False


class SlaveControlWorker(QObject):
    finished = pyqtSignal()

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.targetpos = []
        self.runFlag = True

    def run(self):
        print("Starting Slave Control")
        self.robot.ResumeMotion()
        self.robot.SetJointAcc(30)
        self.robot.SetJointVel(35)
        while self.runFlag:
            self.robot.MoveJoints(self.targetpos[0],
                                  self.targetpos[1],
                                  self.targetpos[2],
                                  self.targetpos[3],
                                  self.targetpos[4],
                                  self.targetpos[5])
            time.sleep(0.03)
        self.finished.emit()

    def updatetargetpos(self, values):
        self.targetpos = values

    def stopSignal(self):
        self.runFlag = False


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = ForceGuideWidget()
    gui.show()
    sys.exit(app.exec_())


