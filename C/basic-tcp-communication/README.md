# Meca500 TCP/IP Communication (C)

Basic TCP/IP socket communication example for the Meca500 robot on Windows.

## Prerequisites
- Windows environment
- GCC compiler (MinGW or similar)
- Meca500 robot powered on and network accessible

## Robot Setup
1. Ensure robot is connected to network
2. Find robot IP address (default: 192.168.0.100)
3. Verify robot is in ready state (not in error)

## Files
- `socket_comm.h/.c` - Socket/TCP-IP communication implementation
- `robot_interface.h/.c` - Robot command interface and message parsing
- `main.c` - Main program demonstrating robot control sequence

## Usage
```bash
gcc -o robot_example main.c robot_interface.c socket_comm.c -lws2_32
robot_example.exe [robot_ip]
```

**⚠️ Safety Warning**: This program physically moves the robot. Ensure safe workspace before running.

## Example Sequence
1. Connect to robot control port
2. Activate robot
3. Home robot
4. Move to zero position
5. Move to shipping position
6. Deactivate and disconnect