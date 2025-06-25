![Mecademic](./docs/logo/mecademic_logo.jpg  "Mecademic")

# Mecademic Sample Programs

This repository contains comprehensive programming examples and demonstrations for Mecademic robots across multiple programming languages and integration scenarios.

## Supported Robots

* **Meca500 R3 and R4** - 6-axis industrial robot arm
* **Meca500 R5** - Latest generation 6-axis robot

## Programming Languages & Examples

### 🐍 [Python Examples](./Python/)
Ready-to-use Python applications demonstrating various robot capabilities:

* **[HandGuiding](./Python/HandGuiding/)** - Force-controlled hand guiding with haptic feedback
* **[PythonUI](./Python/PythonUI/)** - Complete PyQt5 GUI for robot control
* **[ZaberProbing](./Python/ZaberProbing/)** - Integration with Zaber linear stages for automated probing

### ⚙️ [C Examples](./C/)
Low-level C programming examples for Windows systems:

* **[Basic TCP Communication](./C/basic-tcp-communication/)** - Socket-based robot control implementation

### 🏭 [PLC Integration](./PLC/)
Industrial automation examples for various PLC systems:

* **Coming Soon** - Allen-Bradley, Siemens, Schneider Electric, and more


## Prerequisites

### General Requirements
- **Robot Connection**: Ensure your Meca500 robot is connected to your network
- **Network Access**: Computer must be able to communicate with robot IP address
- **Robot Firmware**: Compatible firmware version for your robot model

### Language-Specific Requirements
- **Python**: Python 3.7+ with required packages (see individual example READMEs)
- **C**: Windows development environment with Winsock2 support
- **PLC**: Appropriate programming software for your PLC brand

## Quick Start

1. **Choose your programming language** from the examples above
2. **Navigate to the specific example directory** 
3. **Read the individual README** for setup and usage instructions
4. **Configure robot IP address** in the example code
5. **Run the example** following the provided instructions

## Robot Network Configuration

Most examples use these default settings:
- **Control Port**: 10000 (TCP)
- **Monitoring Port**: 10001 (TCP) 
- **Default IP**: 192.168.0.100

Refer to your robot's documentation for network configuration details.

## Getting Help

For technical support:
- **GitHub Issues**: Report bugs or request features on the Mecademic GitHub page
- **Email Support**: support@mecademic.com
- **Documentation**: Visit [Mecademic Documentation](https://mecademic.com/resources/documentation)

## Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch
3. Add your example with proper documentation
4. Submit a pull request

## License

All packages in this repository are licensed under the MIT license.

## Authors 

* **Mecademic** - *Continuous work*

