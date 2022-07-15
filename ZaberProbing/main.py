from mecademicpy.robot import Robot
from zaber_motion import Library
from zaber_motion import DeviceDbSourceType
from zaber_motion.ascii import Connection
from zaber_motion import Units
from moveFunctions import *
from time import sleep

Library.set_device_db_source(DeviceDbSourceType.FILE, url_or_file_path = 'devices-public.sqlite')

r = Robot()
r.Connect()
r.ResetError()
r.ResumeMotion()
r.ActivateAndHome()
r.WaitHomed()

r.MoveJoints(0,15,0,0,-15,0)
cp1 = r.SetCheckpoint(1)
cp1.wait()

with Connection.open_serial_port("COM5") as connection:
    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))
    device = device_list[0]
    axis = device.get_axis(1)

    axis.home()
    axis.wait_until_idle()
    print("Axis Homed")
    axis.move_absolute(150, Units.LENGTH_MILLIMETRES)
    axis.wait_until_idle()
    
    while(True):
        # Start
        r.MoveJoints(0,15,0,0,-15,0)
        axis.move_absolute(150, Units.LENGTH_MILLIMETRES)
        cp10 = r.SetCheckpoint(10)
        cp10.wait()
        r.ResumeMotion()
        r.SetTrf(93,0,15,0,90,0)

        # Bottom Right
        r.SetWrf(315.329986572-4.5,13.987500191-0.5,-14.189999580-2,0,0,0)
        r.SetJointVel(30)
        r.SetCartAcc(100)
        r.SetCartLinVel(270)
        r.SetCartAngVel(300)
        bottomRight(r)
        cp11 = r.SetCheckpoint(11)
        cp11.wait()
        print("Bottom Right Finished")
        r.SetCartAcc(27)
        r.MoveLinRelWRF(0,150,30,-20,0,0)
        axis.move_absolute(300,Units.LENGTH_MILLIMETRES)
        cp11 = r.SetCheckpoint(11)
        cp11.wait()
        
        # Top Right
        r.SetCartAcc(100)
        r.SetWrf(164.994995117-4.5,147.294998169-0.5,-21.415000916-2,0,0,0)
        topRight(r)
        cp12 = r.SetCheckpoint(12)
        cp12.wait()
        r.MoveLinRelWrf(0,0,10,0,0,0)
        r.MoveLinRelWrf(130,-150,20,20,0,0)
        axis.move_absolute(225, Units.LENGTH_MILLIMETRES)
        cp12 = r.SetCheckpoint(12)
        cp12.wait()
        

        #Bottom Left
        r.SetWrf(263.437500000-4.5,-93.870002747-0.5,-26.004999161-2,0,0,0)
        bottomLeft(r)
        cp13 = r.SetCheckpoint(13)
        cp13.wait()
        r.MoveLinRelWrf(0,0,10,0,0,0)
        r.MoveLinRelWrf(-100, -75, 0,0,0,0)
        axis.move_absolute(150, Units.LENGTH_MILLIMETRES)
        cp13 = r.SetCheckpoint(13)
        cp13.wait()

        #Top Left
        r.SetWrf(126.662498474-4.5,-183.240005493-0.5,-21.299999237-2,0,0,0)
        topLeft(r)
        cp14 = r.SetCheckpoint(14)
        cp14.wait()
        r.MoveLinRelWrf(0,0,10,0,0,0)
        #cp14 = r.SetCheckpoint(14)
        #cp14.wait()


        # Funky Moves
        r.SetCartAngVel(30)
        r.MoveJoints(0, 20, 0, 0, -20, 0)
        r.MoveLinRelWrf(0,0,0,-20,0,0)
        r.MoveLinRelWrf(0,0,0,40,0,0)
        r.MoveLinRelWrf(0,0,0,-20,0,0)
        r.MoveLinRelWrf(0,0,0,0,-20,0)
        r.MoveLinRelWrf(0,0,0,0,20,0)
        r.MoveLinRelWrf(0,0,0,0,20,0)
        r.MoveLinRelWrf(0,0,0,0,-20,0)
        cp15 =r.SetCheckpoint(15)
        cp15.wait()

        sleep(1)