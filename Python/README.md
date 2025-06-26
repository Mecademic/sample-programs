# Python Examples for Mecademic Meca500

Python-based sample programs demonstrating robot control, GUI interfaces, and automation integration.

## Examples

### [HandGuiding](./HandGuiding/)
Force-controlled hand guiding with real-time haptic feedback using force/torque sensors.

### [PythonUI](./PythonUI/)
Complete PyQt5 graphical interface for robot control with joystick integration and real-time monitoring.

### [ZaberProbing](./ZaberProbing/)
Automated probing system integrating Meca500 with Zaber linear motion stages.

## Prerequisites

- **Python 3.7+**
- **Meca500 robot** connected to network
- **Required packages** (install per example needs):
  ```bash
  pip install mecademicpy    # Core robot library
  pip install PyQt5          # For PythonUI example
  pip install zaber-motion   # For ZaberProbing example
  ```

## Quick Start

1. Choose an example directory
2. Install example-specific dependencies  
3. Configure robot IP (default: 192.168.0.100)
4. Run the main script

## Common Configuration

```python
# Most examples use these connection settings
ROBOT_IP = "192.168.0.100"
CONTROL_PORT = 10000
MONITOR_PORT = 10001
```

## Safety Warning

⚠️ **These programs physically move the robot.** Ensure workspace is clear and emergency stop is accessible before running.

## Troubleshooting

- **Connection issues**: Verify robot IP and network connectivity
- **Import errors**: Install mecademicpy with `pip install mecademicpy`  
- **Robot not responding**: Check robot activation status and error state