# Python TCP/IP Socket Client for Meca500

Simple TCP/IP socket client demonstration for direct robot communication using Python's built-in socket library.

## Prerequisites

- **Python 3.7+**
- **Meca500 robot** connected to network
- **Network Access**: Computer must be able to communicate with robot IP address
- **Robot Firmware**: Compatible firmware version

## Overview

This example demonstrates how to set up a simple TCP/IP socket client to exchange data with the robot. The example is intended as a reference for how a TCP/IP client works with the robot to send and receive ASCII strings. The concepts discussed here can be easily applied across multiple programming languages and PLCs.

## Key Features

- **Direct socket communication** with robot control port
- **Error handling** for socket operations
- **Step-by-step robot control** sequence
- **ASCII NULL terminator** handling
- **Response monitoring** for each command

## Usage

1. **Configure robot IP** (default: 192.168.0.100)
2. **Run the script**:
   ```bash
   python main.py
   ```

## Program Flow

The script performs the following sequence:

1. **Create socket** - IPv4 TCP socket creation
2. **Connect to robot** - Establish connection to control port
3. **Verify connection** - Read robot welcome message
4. **Activate robot** - Send activation command
5. **Home robot** - Initialize robot to home position
6. **Move to zero** - Move all joints to zero position
7. **Move to sample position** - Move to demonstration position
8. **Deactivate robot** - Safe shutdown
9. **Close connection** - Clean socket closure

## Code Structure

### Socket Creation
```python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### Connection Establishment
```python
client.connect((ROBOT_IP, ROBOT_PORT))
```

### Command Sending
```python
client.send(bytes(cmd + '\0', 'ascii'))  # ASCII NULL terminator required
```

### Response Reading
```python
msg = client.recv(1024).decode('ascii')
```

## Robot Commands Used

| Command | Description | Wait Time |
|---------|-------------|-----------|
| `ActivateRobot` | Activate robot motors | 15 seconds |
| `Home` | Initialize robot to home position | 5 seconds |
| `MoveJoints(0,0,0,0,0,0)` | Move to zero position | Immediate |
| `MoveJoints(0,-60,60,0,0,0)` | Move to demonstration position | Immediate |
| `DeactivateRobot` | Deactivate robot motors | Immediate |

## Expected Output

```
Socket Created
Socket Connected to 192.168.0.100
[3000][Connected to Meca500 R3 v8.x.x.]
[2000][Motors activated.]
[2000][Homing sequence completed.]
[2000][MoveJoints completed.]
[2000][MoveJoints completed.]
[2000][Motors deactivated, robot deactivated.]
```

## Error Handling

The script includes error handling for:
- **Socket creation failures**
- **Connection failures**
- **Data transmission failures**

## Network Configuration

- **Robot IP**: 192.168.0.100 (configurable)
- **Control Port**: 10000
- **Protocol**: TCP/IP (IPv4)
- **Connection Type**: Single client connection

## Safety Warnings

⚠️ **Robot Movement**: This program causes physical robot movement. Ensure:
- Clear workspace around robot
- Emergency stop accessible
- Robot properly secured
- Personnel at safe distance

⚠️ **Connection Management**: Always close socket connections properly to avoid resource leaks.

## Related Examples

- **[TCP/IP Communication Guide](../../TCP-Communication/)** - Foundational TCP/IP concepts
- **[PythonUI](../PythonUI/)** - Advanced GUI-based robot control
- **[HandGuiding](../HandGuiding/)** - Force-controlled robot interaction

## Support

For additional support and documentation:
- [Mecademic Support Portal](https://www.mecademic.com/support/)
- [Programming Manual](https://www.mecademic.com/support/)