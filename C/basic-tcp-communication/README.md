# C TCP/IP Communication Example for Meca500

This example demonstrates basic TCP/IP socket communication with the Meca500 robot using C on Windows systems.

## Overview

The example consists of:
- **socket_comm.h/.c**: Low-level TCP/IP socket communication functions
- **robot_interface.h/.c**: High-level robot command interface
- **main.c**: Example usage demonstrating a complete robot operation sequence

## Features

- Connect to Meca500 robot via TCP/IP
- Send robot commands (activate, home, move, deactivate)
- Wait for command completion and error handling
- Cross-platform socket implementation (Windows focus)

## Prerequisites

- Windows development environment
- Visual Studio or MinGW compiler
- Meca500 robot connected to network
- Winsock2 library (ws2_32.lib)

## Building

### Visual Studio
```bash
cl main.c robot_interface.c socket_comm.c -lws2_32 -o robot_example.exe
```

### MinGW
```bash
gcc main.c robot_interface.c socket_comm.c -lws2_32 -o robot_example.exe
```

## Usage

```bash
robot_example.exe [robot_ip_address]
```

If no IP address is provided, the default `192.168.0.100` will be used.

### Example:
```bash
robot_example.exe 192.168.0.100
```

## Program Flow

1. **Connect** to robot control port (10000)
2. **Activate** the robot
3. **Home** the robot
4. **Move** to zero position
5. **Move** to shipping position
6. **Deactivate** the robot
7. **Disconnect** from robot

## Error Handling

The program includes comprehensive error handling:
- Network connection errors
- Robot error codes (1000-2000 range)
- Command timeout handling
- Automatic disconnection on errors

## Robot Commands Used

- `ActivateRobot`: Enable robot motors
- `Home`: Home all robot axes
- `MoveJoints`: Move to specified joint positions
- `DeactivateRobot`: Disable robot motors

## Return Codes

- **3001**: Robot activated
- **3002**: Robot deactivated  
- **3003**: Homing completed
- **3004**: End of Block (EOB) - movement completed
- **1000-2000**: Error codes range

## Customization

To add new robot commands:

1. Add function declaration to `robot_interface.h`
2. Implement function in `robot_interface.c`
3. Use `tcpip_send()` to send command
4. Use `wait_for_return_code()` to wait for completion

## Safety Notes

- Always activate the robot before sending motion commands
- Always deactivate the robot when finished
- Ensure robot workspace is clear before running movements
- Monitor robot status and error codes during operation