import MainUI
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time import sleep
import joystick
import parsdict
from functools import partial

import robot
import MOXAE1212 as mx


class Application(QtWidgets.QMainWindow, MainUI.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(1114, 730)

        # Display UI setup
        self.setWindowTitle("Mecademic Robot")
        self.setWindowIcon(QtGui.QIcon("robot_icon.png"))
        self.tcpPose.set_label(['x', 'y', 'z', 'alpha', 'beta', 'gamma'])
        self.jointPose.set_label(['J1', 'J2', 'J3', 'J4', 'J5', 'J6'])
        self.disableUI()
        self.errorLabel.setStyleSheet("background-color:rgb(200,200,200)")

        # Build backend
        self.robot = robot.Robot()
        self.moxa = mx.MoxaE1212()
        self.monitorThread = QThread()
        self.monitorWorker = RobotMonitoring(self.robot)
        self.moxaThread = QThread()
        self.moxaWorker = Moxa_monitoring(self.moxa)
        self.jogMode = None
        self.jogVelocity = None
        self.jointp = None
        self.tcpp = None
        self.moxa_state = None

        # Connect Buttons
        self.pushButtonConnect.clicked.connect(self.on_connect)
        self.pushButtonDisconnect.clicked.connect(self.on_disconnect)
        self.pushButtonUnpause.clicked.connect(self.on_unpause)
        self.pushButtonActivate.clicked.connect(self.on_activate)
        self.pushButtonHome.clicked.connect(self.on_home)
        self.pushButtonReset.clicked.connect(self.on_reset_error)
        self.pushButtonTest.clicked.connect(self.on_get_robot_state)
        # self.pushButtonTest.clicked.connect(self.on_test_move)
        self.pushButtonStart.clicked.connect(self.on_play)
        self.pushButtonGenerate.clicked.connect(self.on_generate_script)

        self.jogWindow.delta.connect(self.on_jog_button)
        self.jogWindow.mode.connect(self.on_get_jog_mode)
        self.jogWindow.vel.connect(self.on_get_jog_velocity)
        self.jogWindow.joymode.clicked.connect(self.on_joy_mode)

        self.teachWindow.but1.clicked.connect(self.on_send_command)
        self.teachWindow.but2.clicked.connect(self.on_insert_movejoints)
        self.teachWindow.but3.clicked.connect(self.on_insert_movepose)
        self.teachWindow.but4.clicked.connect(self.on_insert_movelin)

        self.moxaWidget.out_0.clicked.connect(lambda ignore, out=0: self.on_click_output(out))
        self.moxaWidget.out_1.clicked.connect(lambda ignore, out=1: self.on_click_output(out))
        self.moxaWidget.out_2.clicked.connect(lambda ignore, out=2: self.on_click_output(out))
        self.moxaWidget.out_3.clicked.connect(lambda ignore, out=3: self.on_click_output(out))
        self.moxaWidget.out_4.clicked.connect(lambda ignore, out=4: self.on_click_output(out))
        self.moxaWidget.out_5.clicked.connect(lambda ignore, out=5: self.on_click_output(out))
        self.moxaWidget.out_6.clicked.connect(lambda ignore, out=6: self.on_click_output(out))
        self.moxaWidget.out_7.clicked.connect(lambda ignore, out=7: self.on_click_output(out))

        # Connect Monitoring
        self.monitorWorker.joints.connect(self.updateJointPose)
        self.monitorWorker.pose.connect(self.updateTCPPose)
        self.monitorWorker.error_state.connect(self.updateErrorState)

    def closeEvent(self, event):
        self.monitorWorker.dcFlag()
        self.moxaWorker.dcFlag()
        event.accept()

    def on_connect(self):
        try:
            self.robot.Connect()
        except:
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle("Connection Error")
            error_dialog.showMessage("Could not connect to the robot")
            return
        if self.useMoxa.isChecked():
            r = self.moxa.connect(self.moxaIP.text())
            if not r:
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.setWindowTitle("Connection Error")
                error_dialog.showMessage("Could not connect to the moxa")
                self.robot.Disconnect()
                return
        self.pushButtonConnect.setStyleSheet("background-color:rgb(0,255,0)")
        sleep(0.25)
        self.enableUI()

        # Start Monitoring
        if not self.monitorThread.isRunning():
            self.monitorWorker.moveToThread(self.monitorThread)
            self.monitorThread.started.connect(self.monitorWorker.run)
            self.monitorWorker.finished.connect(self.monitorThread.quit)
            self.monitorWorker.finished.connect(self.monitorWorker.deleteLater)
            self.monitorThread.finished.connect(self.monitorThread.deleteLater)
            self.monitorThread.start()
        else:
            print("Thread already running")
            self.monitorWorker.dcPause()
        if self.useMoxa.isChecked():
            if not self.moxaThread.isRunning():
                self.moxaWorker.moveToThread(self.moxaThread)
                self.moxaThread.started.connect(self.moxaWorker.run)
                self.moxaWorker.finished.connect(self.moxaThread.quit)
                self.moxaWorker.finished.connect(self.moxaWorker.deleteLater)
                self.moxaThread.finished.connect(self.moxaThread.deleteLater)
                self.moxaWorker.moxa_state.connect(self.updateMoxa)
                self.moxaThread.start()
            else:
                self.moxaWorker.pFlag()

    def on_disconnect(self):
        try:
            self.robot.Disconnect()
        except:
            print("Error")
        self.pushButtonConnect.setStyleSheet("background-color:rgb(127,127,127)")
        self.monitorWorker.dcPause()
        if self.useMoxa.isChecked():
            self.moxaWorker.pFlag()
        self.disableUI()

    def on_activate(self):
        self.robot.ActivateRobot()

    def on_home(self):
        self.robot.Home()

    def on_unpause(self):
        self.robot.ResumeMotion()

    def on_reset_error(self):
        self.robot.ResetError()

    def on_get_robot_state(self):
        print(self.robot.GetRobotState().error_status)

    def updateJointPose(self, joints):
        self.jointPose.update(joints)
        self.jointp = joints

    def updateTCPPose(self, pose):
        self.tcpPose.update(pose)
        self.tcpp = pose

    def updateErrorState(self, state):
        if state:
            self.errorLabel.setStyleSheet("background-color:rgb(255,0,0)")
            self.errorLabel.setText("Error")
        else:
            self.errorLabel.setStyleSheet("background-color:rgb(0,255,0)")
            self.errorLabel.setText("No Error")

    def updateMoxa(self, state):
        self.moxa_state = state
        self.moxaWidget.update_input(state)

    def on_click_output(self, out):
        self.moxaWorker.pFlag()
        if out == 0:
            if self.moxaWidget.out_0.isChecked():
                self.moxa.setsingleoutput(0, True)
            else:
                self.moxa.setsingleoutput(0, False)
        if out == 1:
            if self.moxaWidget.out_1.isChecked():
                self.moxa.setsingleoutput(1, True)
            else:
                self.moxa.setsingleoutput(1, False)
        if out == 2:
            if self.moxaWidget.out_2.isChecked():
                self.moxa.setsingleoutput(2, True)
            else:
                self.moxa.setsingleoutput(2, False)
        if out == 3:
            if self.moxaWidget.out_3.isChecked():
                self.moxa.setsingleoutput(3, True)
            else:
                self.moxa.setsingleoutput(3, False)
        if out == 4:
            if self.moxaWidget.out_4.isChecked():
                self.moxa.setsingleoutput(4, True)
            else:
                self.moxa.setsingleoutput(4, False)
        if out == 5:
            if self.moxaWidget.out_5.isChecked():
                self.moxa.setsingleoutput(5, True)
            else:
                self.moxa.setsingleoutput(5, False)
        if out == 6:
            if self.moxaWidget.out_6.isChecked():
                self.moxa.setsingleoutput(6, True)
            else:
                self.moxa.setsingleoutput(6, False)
        if out == 7:
            if self.moxaWidget.out_7.isChecked():
                self.moxa.setsingleoutput(7, True)
            else:
                self.moxa.setsingleoutput(7, False)
        self.moxaWorker.pFlag()

    def on_play(self):
        self.disableUI()
        if self.jogWindow.joymode.isChecked():
            self.joyWorker.stoptrig()
            self.jogWindow.joymode.setChecked(False)
        self.jogWindow.jog.setChecked(False)
        self.interpreterThread = QThread()
        text = self.teachWindow.textf.toPlainText()
        self.liveInterpreter = Interpreter(self.robot, self.moxa, text)
        self.liveInterpreter.moveToThread(self.interpreterThread)
        self.interpreterThread.started.connect(self.liveInterpreter.run)
        self.interpreterThread.finished.connect(self.enableUI)
        self.liveInterpreter.finished.connect(self.interpreterThread.quit)
        self.liveInterpreter.finished.connect(self.liveInterpreter.deleteLater)
        self.interpreterThread.finished.connect(self.interpreterThread.deleteLater)
        self.interpreterThread.start()

    def on_test_move(self):
        self.robot.MovePose(200, 0, 300, 0, 90, 0)
        self.robot.MovePose(200, 100, 300, 0, 90, 0)
        self.robot.MovePose(200, 100, 100, 0, 90, 0)
        self.robot.MovePose(200, -100, 100, 0, 90, 0)
        self.robot.MovePose(200, -100, 300, 0, 90, 0)
        self.robot.MovePose(200, 0, 300, 0, 90, 0)

    def on_jog_button(self, data):
        if self.jogMode is None:
            print('Select jog mode')
        elif self.jogVelocity is None:
            print('Select a velocity')
        else:
            vel_scale = self.jogVelocity / 100.0
            if self.jogMode == 'Joints':
                joint_vel = [150, 150, 180, 300, 300, 500]
                data_vel = [d * vel_scale for d in data]
                data_temp = [joint_vel[i] * data_vel[i] for i in range(6)]
                self.robot.MoveJointsVel(data_temp[0], data_temp[1], data_temp[2], data_temp[3], data_temp[4],
                                         data_temp[5])
            if self.jogMode == 'WRF':
                joint_vel = [500, 500, 500, 150, 150, 150]
                data_vel = [d * vel_scale for d in data]
                data_temp = [joint_vel[i] * data_vel[i] for i in range(6)]
                self.robot.MoveLinVelWRF(data_temp[0], data_temp[1], data_temp[2], data_temp[3], data_temp[4],
                                         data_temp[5])
            if self.jogMode == 'TRF':
                joint_vel = [500, 500, 500, 150, 150, 150]
                data_vel = [d * vel_scale for d in data]
                data_temp = [joint_vel[i] * data_vel[i] for i in range(6)]
                self.robot.MoveLinVelTRF(data_temp[0], data_temp[1], data_temp[2], data_temp[3], data_temp[4],
                                         data_temp[5])

    def on_get_jog_velocity(self, value):
        self.jogVelocity = value

    def on_get_jog_mode(self, mode):
        self.jogMode = mode

    def on_joy_mode(self):
        if self.jogWindow.joymode.isChecked():
            self.joystick = joystick.MecaJoy()
            if not self.joystick.checkdriver():
                return
            if not self.joystick.checkplugged():
                return
            self.joystick.getcaps()
            self.joyThread = QThread()
            self.joyWorker = Joystick_monitoring(self.joystick)
            self.joyWorker.moveToThread(self.joyThread)
            self.joyThread.started.connect(self.joyWorker.run)
            self.joyWorker.joy_data.connect(self.on_get_joy)
            self.joyWorker.finished.connect(self.joyThread.quit)
            self.joyWorker.finished.connect(self.joyWorker.deleteLater)
            self.joyThread.finished.connect(self.joyThread.deleteLater)
            self.joyThread.start()

        else:
            self.joyWorker.stoptrig()

    def on_get_joy(self, data):
        if self.jogMode is None:
            print('Select jog mode')
        elif self.jogVelocity is None:
            print('Select a velocity')
        else:
            vel_scale = self.jogVelocity/100
            if self.jogMode == 'Joints':
                if not data[3] and not data[4]:
                    joint_vel = [150, 150, 180, 300, 300, 500]
                    data_vel = [data[0] * vel_scale, data[1] * vel_scale, data[2] * vel_scale]
                    data_temp = [joint_vel[i] * data_vel[i] for i in range(3)]
                    self.robot.MoveJointsVel(data_temp[0], data_temp[1], data_temp[2], 0, 0, 0)
                else:
                    joint_vel = [150, 150, 180, 300, 300, 500]
                    data_vel = [data[0] * vel_scale, data[1] * vel_scale, data[2] * vel_scale]
                    data_temp = [joint_vel[i+3] * data_vel[i] for i in range(3)]
                    self.robot.MoveJointsVel(0, 0, 0, data_temp[0], data_temp[1], data_temp[2])
            if self.jogMode == 'WRF':
                if not data[3] and not data[4]:
                    joint_vel = [500, 500, 500, 150, 150, 150]
                    data_vel = [data[0] * vel_scale, data[1] * vel_scale, data[2] * vel_scale]
                    data_temp = [joint_vel[i] * data_vel[i] for i in range(3)]
                    self.robot.MoveLinVelWRF(data_temp[0], data_temp[1], data_temp[2], 0, 0, 0)
                else:
                    joint_vel = [500, 500, 500, 150, 150, 150]
                    data_vel = [data[0] * vel_scale, data[1] * vel_scale, data[2] * vel_scale]
                    data_temp = [joint_vel[i + 3] * data_vel[i] for i in range(3)]
                    self.robot.MoveLinVelWRF(0, 0, 0, data_temp[0], data_temp[1], data_temp[2])
            if self.jogMode == 'TRF':
                if not data[3] and not data[4]:
                    joint_vel = [500, 500, 500, 150, 150, 150]
                    data_vel = [data[0] * vel_scale, data[1] * vel_scale, data[2] * vel_scale]
                    data_temp = [joint_vel[i] * data_vel[i] for i in range(3)]
                    self.robot.MoveLinVelTRF(data_temp[0], data_temp[1], data_temp[2], 0, 0, 0)
                else:
                    joint_vel = [500, 500, 500, 150, 150, 150]
                    data_vel = [data[0] * vel_scale, data[1] * vel_scale, data[2] * vel_scale]
                    data_temp = [joint_vel[i+3] * data_vel[i] for i in range(3)]
                    self.robot.MoveLinVelTRF(0, 0, 0, data_temp[0], data_temp[1], data_temp[2])


    def on_send_command(self):
        command = self.teachWindow.linef.text()
        self.robot.SendCustomCommand(command)

    def on_insert_movejoints(self):
        command = "MoveJoints(" + str(self.jointp[0]) + ', ' + str(self.jointp[1]) + ', ' + str(
            self.jointp[2]) + ', ' + str(self.jointp[3]) + ', ' + str(self.jointp[4]) + ', ' + str(self.jointp[5]) + ')'
        self.teachWindow.textf.insertPlainText(command + '\n')

    def on_insert_movelin(self):
        command = "MoveLin(" + str(self.tcpp[0]) + ', ' + str(self.tcpp[1]) + ', ' + str(self.tcpp[2]) + ', ' + str(
            self.tcpp[3]) + ', ' + str(self.tcpp[4]) + ', ' + str(self.tcpp[5]) + ')'
        self.teachWindow.textf.insertPlainText(command + '\n')

    def on_insert_movepose(self):
        command = "MovePose(" + str(self.tcpp[0]) + ', ' + str(self.tcpp[1]) + ', ' + str(self.tcpp[2]) + ', ' + str(
            self.tcpp[3]) + ', ' + str(self.tcpp[4]) + ', ' + str(self.tcpp[5]) + ')'
        self.teachWindow.textf.insertPlainText(command + '\n')

    def disableUI(self):
        self.jointPose.setEnabled(False)
        self.tcpPose.setEnabled(False)
        self.jogWindow.setEnabled(False)
        self.teachWindow.setEnabled(False)
        self.pushButtonDisconnect.setEnabled(False)
        self.pushButtonActivate.setEnabled(False)
        self.pushButtonHome.setEnabled(False)
        self.moxaWidget.setEnabled(False)
        self.errorLabel.setStyleSheet("background-color:rgb(200,200,200)")

    def enableUI(self):
        self.jointPose.setEnabled(True)
        self.tcpPose.setEnabled(True)
        self.jogWindow.setEnabled(True)
        self.teachWindow.setEnabled(True)
        self.pushButtonDisconnect.setEnabled(True)
        self.pushButtonActivate.setEnabled(True)
        self.pushButtonHome.setEnabled(True)
        if self.useMoxa.isChecked():
            self.moxaWidget.setEnabled(True)
        if self.robot.GetRobotState().error_status:
            self.errorLabel.setStyleSheet("background-color:rgb(255,0,0)")
            self.errorLabel.setText("Error")
        else:
            self.errorLabel.setStyleSheet("background-color:rgb(0,255,0)")
            self.errorLabel.setText("No Error")

    def on_generate_script(self):
        file = open('generated_script.py', 'w+')
        file.write('import robot\n\n')
        file.write('r = robot.Robot()\n')
        file.write('r.Connect()\n')
        file.write('r.ActivateRobot()\n')
        file.write('r.Home()\n')
        file.write('print(r.WaitHomed())\n')

        mod_text = self.teachWindow.textf.toPlainText()
        rep = parsdict.gen_script
        for i, j in rep.items():
            mod_text = mod_text.replace(i, j)
        file.write(mod_text+'\n')


        file.write('r.Disconnect()')
        file.close()



# Worker classes
class RobotMonitoring(QObject):
    finished = pyqtSignal()
    joints = pyqtSignal(list)
    pose = pyqtSignal(list)
    error_state = pyqtSignal(bool)

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.jointpos = [0, 0, 0, 0, 0, 0]
        self.connectedFlag = True
        self.pauseDC = False

    def run(self):
        prev_error_state = self.robot.GetRobotState().error_status
        while self.connectedFlag:
            while self.pauseDC:
                pass
            jpose = self.robot.GetJoints()
            tcppose = self.robot.GetPose()
            self.joints.emit(jpose)
            self.pose.emit(tcppose)
            new_error_state = self.robot.GetRobotState().error_status
            if new_error_state is not prev_error_state:
                self.error_state.emit(new_error_state)
                prev_error_state = new_error_state
            sleep(0.1)
        self.finished.emit()

    def dcFlag(self):
        self.connectedFlag = False
        self.pauseDC = False

    def dcPause(self):
        if self.pauseDC:
            self.pauseDC = False
        else:
            self.pauseDC = True


class Interpreter(QObject):
    finished = pyqtSignal()

    def __init__(self, robot, moxa, text):
        super().__init__()
        self.robot = robot
        self.moxa = moxa
        self.text = text

    def run(self):
        mod_text = self.text
        rep = parsdict.live_rep
        mox = parsdict.moxadict
        for i, j in rep.items():
            mod_text = mod_text.replace(i, j)
        for i, j in mox.items():
            mod_text = mod_text.replace(i, j)
        try:
            exec(mod_text)
        except:
            print("Error")
        self.finished.emit()


class Moxa_monitoring(QObject):
    finished = pyqtSignal()
    moxa_state = pyqtSignal(list)

    def __init__(self, moxa):
        super().__init__()
        self.moxa = moxa
        self.connectFlag = True
        self.pauseFlag = False

    def run(self):
        while self.connectFlag:
            state = self.moxa.readallinputs()
            self.moxa_state.emit(state)
            while self.pauseFlag:
                pass
            sleep(0.2)
        self.finished.emit()

    def dcFlag(self):
        self.connectFlag = False
        self.pauseFlag = False

    def pFlag(self):
        if self.pauseFlag:
            self.pauseFlag = False
        else:
            self.pauseFlag = True

class Joystick_monitoring(QObject):
    finished = pyqtSignal()
    joy_data = pyqtSignal(list)
    def __init__(self, joy):
        super().__init__()
        self.joy = joy
        self.stopFlag = True

    def run(self):
        while self.stopFlag:
            data = self.joy.getinfo()
            self.joy_data.emit(data)
            sleep(0.05)
        self.finished.emit()

    def stoptrig(self):
        self.stopFlag = False

