from mecademicpy.robot import Robot
from zaber_motion import Library
from zaber_motion.ascii import Connection
from zaber_motion import Units
from moveFunctions import *

r = Robot()
r.Connect()
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

    axis.move_absolute(300, Units.LENGTH_MILLIMETRES)
    axis.wait_until_idle()
    print("Finished Moving")
    axis.move_absolute(150, Units.LENGTH_MILLIMETRES)
    axis.wait_until_idle()
    # Speed 270mm/s

    r.SetCartLinVel(270)
    r.SetCartAcc(28)
    r.MoveLinRelWRF(0,100,0,0,0,0)
    axis.move_absolute(250, Units.LENGTH_MILLIMETRES)
    cp2 = r.SetCheckpoint(2)
    cp2.wait()


