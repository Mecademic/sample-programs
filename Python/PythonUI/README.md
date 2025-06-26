# Mecademic Robot Control GUI

PyQt5-based GUI application for Mecademic robot control with joystick support and MOXA I/O integration.

## Description

Graphical interface for robot control featuring joint/Cartesian jogging, teaching pendant functionality, and optional joystick control.

## Prerequisites

- **Windows OS** (required for joystick functionality)
- **Python 3.7+**
- **Mecademic robot** with network connectivity
- **Optional**: Windows-compatible joystick/gamepad
- **Optional**: MOXA ioLogik E1212 I/O module

## Dependencies

```bash
pip install PyQt5 mecademicpy pygame
```

**Note**: All other dependencies are Python standard library modules

## Hardware Setup

1. Connect Mecademic robot to network
2. Connect joystick/gamepad to computer (optional)
3. Connect MOXA I/O module to network (optional)
4. Note IP addresses of all devices

## Configuration

Update IP addresses in the code:
1. Open `main.py` or `UIApp.py`
2. Update robot IP address in connection settings
3. Update MOXA IP address if using I/O module

## Running the Application

```bash
python main.py
```

## File Structure

- `main.py` - Main application entry point
- `UIApp.py` - Main GUI application class
- `MainUI.py` - UI layout and widgets
- `MainUI.ui` - Qt Designer UI file
- `RobotToolWidgets.py` - Robot control widgets
- `PyQt5Widgets.py` - Custom PyQt5 widgets
- `joystick.py` - Joystick interface
- `MOXAE1212.py` - MOXA I/O module interface
- `robot.py` - Mecademic robot communication
- `parsdict.py` - Configuration parser

## Usage

1. **Connect**: Click connect button to establish robot connection
2. **Control**: Use GUI buttons or joystick for robot movement
3. **Monitor**: View real-time joint positions and robot status
4. **I/O**: Control digital I/O through MOXA module (if connected)

## Safety Notes

- Always have emergency stop accessible
- Test movements at low speeds initially
- Verify workspace limits before operation

## Troubleshooting

- **Connection Issues**: Check robot IP and network connectivity
- **Joystick Not Detected**: Verify joystick drivers and connections
- **MOXA I/O Error**: Check MOXA IP address and network settings
- **GUI Not Starting**: Verify PyQt5 installation