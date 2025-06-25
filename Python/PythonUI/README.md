# Python GUI Application for Meca500

This example provides a complete PyQt5-based graphical user interface for controlling and monitoring the Meca500 robot.

## Overview

The Python UI application offers comprehensive robot control through an intuitive graphical interface. It includes joint control, Cartesian positioning, real-time monitoring, and joystick integration for manual operation.

## Features

- **Comprehensive Robot Control**: Joint and Cartesian coordinate control
- **Real-time Monitoring**: Live robot status, position, and sensor data
- **Joystick Integration**: Manual robot control using game controllers
- **Visual Interface**: Interactive 3D robot representation
- **Program Management**: Load, edit, and execute robot programs
- **I/O Control**: Digital input/output monitoring and control
- **Safety Features**: Emergency stops, workspace limits, and error handling

## Prerequisites

### Software Requirements
- Python 3.7+
- PyQt5 development framework
- Required Python packages:
  ```bash
  pip install mecademicpy PyQt5 pygame numpy matplotlib
  ```

### Hardware Requirements
- Meca500 robot connected to network
- Optional: Game controller/joystick for manual control
- Optional: Additional I/O devices (MOXAE1212 modules)

## Files Description

- **`MainUI.py`** - Main application window and control logic
- **`MainUI.ui`** - Qt Designer UI layout file
- **`UIApp.py`** - Application initialization and main window setup
- **`PyQt5Widgets.py`** - Custom PyQt5 widgets and components
- **`RobotToolWidgets.py`** - Robot-specific control widgets
- **`joystick.py`** - Joystick/gamepad integration
- **`joystick_test.py`** - Joystick testing and calibration
- **`MOXAE1212.py`** - I/O expansion module interface
- **`main.py`** - Application entry point
- **`main.spec`** - PyInstaller specification for executable creation
- **`parsdict.py`** - Configuration file parsing utilities

## Installation & Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure robot connection**:
   Edit the robot IP address in `MainUI.py`:
   ```python
   ROBOT_IP = "192.168.0.100"  # Change to your robot's IP
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## User Interface Components

### Main Control Panel
- **Connection Status**: Robot connection and communication status
- **Robot State**: Current robot mode (activated, homed, moving, etc.)
- **Emergency Stop**: Immediate robot stop button
- **Mode Selection**: Manual, automatic, and programming modes

### Joint Control
- **Individual Joint Control**: Sliders and input fields for each joint
- **Joint Limits**: Visual indicators for joint limit ranges
- **Joint Velocities**: Real-time joint velocity display
- **Preset Positions**: Quick access to common robot positions

### Cartesian Control
- **Position Control**: X, Y, Z coordinate input and control
- **Orientation Control**: Roll, pitch, yaw angle adjustment
- **Tool Frame**: Tool coordinate system settings
- **Work Frame**: Work coordinate system configuration

### Program Management
- **Program Editor**: Built-in editor for robot programs
- **Program Execution**: Run, pause, stop program functions
- **Variable Monitor**: Real-time program variable display
- **Checkpoint Management**: Set and monitor robot checkpoints

### I/O Panel
- **Digital Inputs**: Status display for digital input signals
- **Digital Outputs**: Control switches for digital outputs
- **Analog I/O**: Analog signal monitoring and control
- **External Devices**: Interface for additional I/O modules

## Joystick Control

### Supported Controllers
- Xbox controllers (wired/wireless)
- PlayStation controllers
- Generic USB game controllers
- Logitech joysticks

### Control Mapping
- **Left Stick**: X/Y positioning
- **Right Stick**: Z positioning and rotation
- **Triggers**: Fine movement speed control
- **Buttons**: Emergency stop, mode switching, preset positions

### Setup Instructions
1. Connect joystick to computer
2. Run joystick calibration: `python joystick_test.py`
3. Configure button mapping in application settings
4. Enable joystick mode in main interface

## Configuration

### Robot Parameters
Configure robot-specific settings in the configuration file:
```python
ROBOT_CONFIG = {
    'ip_address': '192.168.0.100',
    'control_port': 10000,
    'monitor_port': 10001,
    'joint_limits': [...],
    'workspace_limits': [...],
    'safety_parameters': {...}
}
```

### UI Customization
Modify UI appearance and behavior:
- **Theme Settings**: Dark/light mode, color schemes
- **Layout Options**: Panel arrangement, window sizes
- **Display Units**: Metric/imperial unit selection
- **Update Rates**: Real-time data refresh intervals

## Advanced Features

### Programming Interface
- **Drag-and-Drop Programming**: Visual program creation
- **Syntax Highlighting**: Code editor with syntax support
- **Auto-completion**: Intelligent code completion
- **Error Checking**: Real-time syntax and logic validation

### Data Logging
- **Position Logging**: Record robot positions over time
- **Performance Metrics**: Track robot performance data
- **Error Logging**: Comprehensive error and event logging
- **Export Options**: CSV, JSON, and XML data export

### Customization
- **Plugin System**: Add custom functionality
- **Widget Extensions**: Create custom control widgets
- **Theme Development**: Design custom UI themes
- **Language Support**: Multi-language interface options

## Building Executable

Create a standalone executable using PyInstaller:

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller main.spec

# Find executable in dist/ folder
```

## Troubleshooting

### Common Issues

**Application won't start:**
- Check Python version (3.7+ required)
- Verify all dependencies are installed
- Check for missing Qt libraries

**Robot connection problems:**
- Verify robot IP address and network connectivity
- Check firewall settings
- Ensure robot is powered and initialized

**Joystick not detected:**
- Install appropriate joystick drivers
- Run joystick test utility
- Check USB connection and permissions

**UI display issues:**
- Update PyQt5 to latest version
- Check display scaling settings
- Verify graphics driver compatibility

### Debug Mode
Enable debug output for troubleshooting:
```python
DEBUG_MODE = True
VERBOSE_LOGGING = True
```

## API Integration

The UI can be extended with custom robot functions:

```python
# Custom robot command
def custom_robot_operation():
    robot.CustomCommand()
    update_ui_status()

# Add to UI button
custom_button.clicked.connect(custom_robot_operation)
```

## Safety Considerations

⚠️ **Safety Guidelines:**
- Always have emergency stop accessible
- Verify robot workspace is clear
- Test programs in simulation first
- Monitor robot behavior continuously
- Maintain proper safety distances

## Contributing

To extend the UI application:
1. Follow PyQt5 best practices
2. Maintain consistent UI design
3. Add comprehensive error handling
4. Include user documentation
5. Test thoroughly before submission