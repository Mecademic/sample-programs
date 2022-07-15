from zaber_motion import Library
from zaber_motion.ascii import Connection
from zaber_motion import Units

Library.enable_device_db_store()

with Connection.open_serial_port("COM5") as connection:
    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))
    device = device_list[0]
    axis = device.get_axis(1)
    