# LabVIEW Examples for Mecademic Meca500

LabVIEW-based sample programs demonstrating robot control and monitoring via TCP/IP communication.

## Examples

### [LabVIEW Connection and Control](./LabVIEW%20Connection%20and%20Control/)
Basic robot control using TCP/IP commands with custom SubVIs for movement and configuration.

### [LabVIEW Monitoring](./LabVIEW%20Monitoring/)
Robot status monitoring and data display using the monitoring port with real-time feedback.

## Prerequisites

- **LabVIEW software**
- **Meca500 robot** connected to network
- **Network access** to robot IP address

## Quick Start

1. Choose an example directory
2. Open the main VI file in LabVIEW
3. Configure robot IP (default: 192.168.0.100)
4. Run the program

## Common Configuration

- **Robot IP**: 192.168.0.100 (default)
- **Control Port**: 10000 (for sending commands)
- **Monitoring Port**: 10001 (for receiving status)

## Safety Warning

⚠️ **These programs physically move the robot.** Ensure workspace is clear and emergency stop is accessible before running.

## Troubleshooting

- **Connection issues**: Verify robot IP and network connectivity
- **Robot not responding**: Check robot activation and homing status
- **TCP errors**: Ensure firewall allows communication on ports 10000/10001