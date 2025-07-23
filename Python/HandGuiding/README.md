# Hand Guiding Control for Mecademic Robots

Python GUI application for hand guiding control of Mecademic robots using force/torque feedback from an ATI Net F/T sensor.

## Description

This application enables intuitive hand guiding of Mecademic robots by reading force and torque values from an ATI force/torque sensor and translating them into robot movements. The system supports both master-slave robot configurations and single robot force-guided motion.

## Prerequisites

- **Python 3.7.3** (specifically tested version)
- **Mecademic robot** (M500, M1000, or SCARA series)
- **ATI Net F/T force/torque sensor** with network interface
- **Network access** to both robot and sensor with open ports:
  - Robot: TCP ports 10000 (control) and 10001 (monitoring)
  - ATI sensor: UDP port 49152

## Dependencies

Install required Python packages:

```bash
pip install PyQt5
```

**Note**: All other dependencies are Python standard library modules (socket, threading, time, etc.)

## Hardware Setup

1. Connect your Mecademic robot to the network (default IP: 192.168.0.100)
2. Connect the ATI Net F/T sensor to the network
3. Ensure both devices are accessible from your computer
4. Verify the force/torque sensor is properly calibrated
5. Configure firewall to allow:
   - TCP connections to robot on ports 10000-10001
   - UDP communication with sensor on port 49152

## Configuration

Before running, update the IP addresses in the code:

1. Open `ForceControl.py`
2. Locate the robot connection section and update IP addresses
3. Update the ATI sensor IP address in the sensor initialization
4. Ensure network connectivity by testing ping to both devices

## Running the Application

```bash
python ForceControl.py
```

## Usage

1. **Robot Connection**: Click the robot icon to connect to the robot(s)
2. **Enable Sensor**: Click the data wave icon to start force/torque monitoring
3. **Start Guiding**: Click the gripper icon to enable hand guiding mode
4. Apply gentle forces to the robot end-effector to guide it through desired motions

## File Structure

- `ForceControl.py` - Main GUI application with hand guiding logic
- `robot.py` - Mecademic robot communication interface
- `NetFT.py` - ATI Net F/T sensor communication interface
- `robot_common.py` - Common robot utilities and constants
- `robot_logger.py` - Logging functionality
- `mx_robot_def.py` - Mecademic robot definitions

## Safety Notes

- Always have the emergency stop accessible
- Start with low force gains and test carefully
- Ensure proper workspace limits are configured
- Monitor robot movements at all times during operation

## Troubleshooting

- **Connection Issues**: Verify IP addresses and network connectivity
- **Sensor Not Reading**: Check ATI sensor network configuration
- **Robot Not Moving**: Ensure robot is activated and motion is resumed
- **GUI Not Starting**: Verify PyQt5 installation

For technical support, refer to Mecademic and ATI documentation.