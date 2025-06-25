# Python Examples for Mecademic Meca500

This directory contains Python-based examples demonstrating various capabilities of the Mecademic Meca500 robot.

## Examples Overview

### [HandGuiding](./HandGuiding/)
**Force-controlled hand guiding with haptic feedback**
- Real-time force/torque sensor integration
- Manual robot guidance with force feedback
- Safety monitoring and collision detection
- Interactive robot teaching interface

### [PythonUI](./PythonUI/)
**Complete PyQt5 graphical user interface**
- Full robot control panel
- Joint and Cartesian coordinate control
- Real-time robot status monitoring
- Joystick integration for manual control
- Visual robot position display

### [ZaberProbing](./ZaberProbing/)
**Automated probing with Zaber linear stages**
- Integration with Zaber motion control systems
- Automated coordinate probing sequences
- Database storage of measurement results
- Synchronized robot and linear stage movement

## Prerequisites

### Python Environment
- **Python 3.7 or higher**
- **pip** package manager

### Required Python Packages
Install packages specific to each example (see individual README files):
```bash
pip install mecademicpy  # Main Mecademic Python library
pip install PyQt5        # For PythonUI example
pip install numpy        # For mathematical calculations
pip install matplotlib   # For data visualization
```

### Hardware Requirements
- **Meca500 robot** connected to network
- **Network connection** between computer and robot
- **Additional hardware** as specified in individual examples

## Getting Started

1. **Choose an example** from the list above
2. **Navigate to the example directory**
3. **Read the specific README** for detailed setup instructions
4. **Install required dependencies** for that example
5. **Configure robot IP address** in the code
6. **Run the example**

## Common Configuration

Most Python examples use similar robot connection settings:

```python
# Robot network configuration
ROBOT_IP = "192.168.0.100"  # Change to your robot's IP
CONTROL_PORT = 10000        # Robot command port
MONITOR_PORT = 10001        # Robot monitoring port
```

## Safety Notes

⚠️ **Important Safety Considerations:**
- Always ensure the robot workspace is clear before running any example
- Keep emergency stop readily accessible
- Start with simulation mode when possible
- Verify robot limits and safety settings
- Monitor robot behavior closely during operation

## Common Issues & Solutions

### Connection Problems
- Verify robot IP address and network connectivity
- Check that robot is powered on and initialized
- Ensure no firewall blocking robot ports (10000, 10001)

### Import Errors
- Install required packages: `pip install mecademicpy`
- Check Python version compatibility (3.7+)
- Verify virtual environment if using one

### Robot Not Responding
- Check robot activation status
- Verify robot is not in error state
- Restart robot controller if necessary

## API Reference

All Python examples use the **mecademicpy** library. Key classes and methods:

```python
from mecademicpy.robot import Robot

# Basic robot operations
robot = Robot()
robot.Connect(ip_address='192.168.0.100')
robot.ActivateAndHome()
robot.MoveJoints(0, 0, 0, 0, 0, 0)
robot.Disconnect()
```

For complete API documentation, visit the [mecademicpy documentation](https://pypi.org/project/mecademicpy/).

## Contributing

To add a new Python example:
1. Create a new directory under `Python/`
2. Include all necessary Python files
3. Add a comprehensive README.md
4. List required dependencies
5. Provide usage examples
6. Include safety considerations