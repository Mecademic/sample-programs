# C Examples for Mecademic Meca500

C-based sample programs demonstrating low-level TCP/IP socket communication with the Meca500 robot.

## Examples

### [Basic TCP Communication](./Basic-TCP-Communication/)
Foundation TCP/IP socket implementation for direct robot control using Windows sockets (Winsock).

## Prerequisites

- **Windows environment**
- **GCC compiler** (MinGW or similar)
- **Meca500 robot** connected to network
- **Network access** to robot IP address

## Quick Start

1. Navigate to the example directory
2. Compile the program:
   ```bash
   gcc -o robot_example main.c robot_interface.c socket_comm.c -lws2_32
   ```
3. Configure robot IP (default: 192.168.0.100)
4. Run the executable:
   ```bash
   robot_example.exe [robot_ip]
   ```

## Common Configuration

```c
// Standard connection settings used across examples
#define ROBOT_IP "192.168.0.100"
#define ROBOT_PORT 10000
```

## Safety Warning

⚠️ **These programs physically move the robot.** Ensure workspace is clear and emergency stop is accessible before running.

## Troubleshooting

- **Connection issues**: Verify robot IP and network connectivity
- **Compilation errors**: Ensure MinGW or GCC is properly installed
- **Winsock errors**: Check Windows firewall settings for port 10000
- **Robot not responding**: Check robot activation status and connection state