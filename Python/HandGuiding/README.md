# Hand Guiding Example

This example demonstrates force-controlled hand guiding of the Meca500 robot using real-time force/torque sensor feedback.

## Overview

The Hand Guiding application allows users to manually guide the robot by applying forces to the end-effector. The robot responds to these forces by moving in the corresponding direction, providing an intuitive way to teach robot positions and paths.

## Features

- **Real-time force sensing** using NetFT force/torque sensor
- **Responsive robot movement** based on applied forces
- **Safety monitoring** with force limits and emergency stops
- **Visual feedback** showing force vectors and robot status
- **Teaching mode** for recording robot positions
- **Haptic feedback** through controlled robot resistance

## Prerequisites

### Hardware
- Meca500 robot with force/torque sensor capability
- NetFT force/torque sensor (ATI or compatible)
- Network connection to both robot and force sensor

### Software
- Python 3.7+
- Required Python packages:
  ```bash
  pip install mecademicpy numpy matplotlib
  ```

## Files Description

- **`ForceControl.py`** - Main force control logic and robot movement
- **`NetFT.py`** - Force/torque sensor communication interface
- **`robot.py`** - Robot communication and control wrapper
- **`robot_common.py`** - Shared robot utilities and constants
- **`robot_logger.py`** - Logging functionality for debugging
- **`mx_robot_def.py`** - Robot-specific definitions and parameters

## Configuration

### Robot Settings
Update the robot IP address in the main script:
```python
ROBOT_IP = "192.168.0.100"  # Change to your robot's IP address
```

### Force Sensor Settings
Configure the NetFT sensor parameters:
```python
SENSOR_IP = "192.168.0.200"  # Force sensor IP address
FORCE_THRESHOLD = 5.0        # Force threshold in Newtons
TORQUE_THRESHOLD = 0.5       # Torque threshold in Nm
```

### Safety Parameters
Adjust safety limits as needed:
```python
MAX_VELOCITY = 50.0          # Maximum robot velocity (mm/s)
MAX_FORCE = 20.0             # Maximum allowed force (N)
WORKSPACE_LIMITS = [...]     # Define safe workspace boundaries
```

## Usage

1. **Connect hardware**:
   - Ensure robot is connected and initialized
   - Connect force/torque sensor to network
   - Verify sensor calibration

2. **Run the application**:
   ```bash
   python ForceControl.py
   ```

3. **Initialize the system**:
   - The robot will activate and home automatically
   - Force sensor will be zeroed
   - System will enter hand guiding mode

4. **Hand guiding operation**:
   - Apply gentle forces to the robot end-effector
   - Robot will move in the direction of applied force
   - Release force to stop movement
   - Use teaching interface to record positions

## Operation Modes

### Teaching Mode
- Record robot positions for later playback
- Save/load position sequences
- Define custom motion paths

### Force Following Mode
- Robot follows applied forces in real-time
- Adjustable sensitivity and response speed
- Safety limits prevent excessive forces

### Compliance Mode
- Robot provides controlled resistance
- Useful for assembly operations
- Configurable stiffness parameters

## Safety Features

- **Force monitoring**: Continuous monitoring of applied forces
- **Emergency stop**: Immediate robot stop on excessive force
- **Workspace limits**: Robot movement restricted to safe area
- **Velocity limits**: Maximum robot speed constraints
- **Sensor validation**: Force sensor health monitoring

## Troubleshooting

### Common Issues

**Robot not responding to forces:**
- Check force sensor connection and calibration
- Verify force thresholds are appropriate
- Ensure robot is in correct mode

**Excessive robot movement:**
- Reduce force sensitivity settings
- Check for sensor noise or drift
- Verify workspace limits are configured

**Connection errors:**
- Verify IP addresses for robot and sensor
- Check network connectivity
- Restart robot controller if necessary

### Debug Mode
Enable debug output for detailed information:
```python
DEBUG_MODE = True  # Enable detailed logging
FORCE_DISPLAY = True  # Show real-time force values
```

## Advanced Configuration

### Custom Force Mappings
Modify force-to-velocity mappings in `ForceControl.py`:
```python
def force_to_velocity(force_vector):
    # Custom mapping function
    velocity = scale_factor * force_vector
    return apply_limits(velocity)
```

### Sensor Calibration
Perform sensor calibration before use:
```python
sensor.calibrate()  # Zero force/torque readings
sensor.set_bias()   # Set bias compensation
```

## API Reference

### Key Functions
- `start_hand_guiding()` - Initialize hand guiding mode
- `process_forces()` - Process force sensor data
- `move_robot()` - Execute robot movement
- `record_position()` - Save current robot position
- `emergency_stop()` - Immediate robot stop

For detailed API documentation, see the individual Python file headers.

## Safety Warnings

⚠️ **IMPORTANT SAFETY INFORMATION:**
- Always maintain clear workspace around robot
- Keep emergency stop readily accessible
- Do not exceed maximum force limits
- Monitor robot behavior continuously
- Ensure proper sensor calibration before use