# Zaber Probing Integration Example

This example demonstrates automated coordinate probing using a Meca500 robot integrated with Zaber linear motion stages for precise positioning and measurement.

## Overview

The Zaber Probing application combines the precision of the Meca500 robot with Zaber linear stages to create an automated probing system. This is ideal for quality control, dimensional measurement, and automated inspection tasks.

## Features

- **Synchronized Motion**: Coordinated movement between robot and linear stages
- **Automated Probing Sequences**: Programmable probing patterns and paths
- **Data Collection**: Real-time measurement data capture and storage
- **Database Integration**: SQLite database for measurement result storage
- **Precision Positioning**: High-accuracy positioning using Zaber stages
- **Flexible Patterns**: Customizable probing grids and sequences

## Prerequisites

### Hardware Requirements
- **Meca500 robot** with appropriate end-effector/probe
- **Zaber linear stages** (compatible models)
- **Probe sensor** or measurement tool
- **Serial/USB connection** to Zaber stages
- **Network connection** to robot

### Software Requirements
- Python 3.7+
- Required packages:
  ```bash
  pip install mecademicpy zaber-motion sqlite3 numpy
  ```

## Files Description

- **`main.py`** - Main application and probing sequence control
- **`moveFunctions.py`** - Robot movement and positioning functions
- **`storeDb.py`** - Database operations for measurement storage
- **`test.py`** - Basic functionality testing
- **`test2.py`** - Advanced testing and calibration

## Hardware Setup

### Zaber Stage Configuration
1. **Connect Zaber stages** to computer via USB/serial
2. **Install Zaber drivers** and verify communication
3. **Calibrate stages** using Zaber software
4. **Set coordinate systems** for proper alignment

### Robot Integration
1. **Mount probe tool** on robot end-effector
2. **Establish coordinate relationship** between robot and stages
3. **Define workspace boundaries** for safe operation
4. **Calibrate probe offset** relative to robot TCP

## Configuration

### Device Settings
Update device configurations in `main.py`:

```python
# Zaber stage configuration
ZABER_PORT = "COM5"              # Serial port for Zaber stages
STAGE_DEVICE_ID = 1              # Zaber device ID

# Robot configuration
ROBOT_IP = "192.168.0.100"       # Robot IP address
PROBE_OFFSET = [0, 0, 10]        # Probe tip offset from TCP (mm)

# Measurement parameters
PROBING_SPEED = 50               # Probing approach speed (mm/s)
MEASUREMENT_FORCE = 2.0          # Contact force threshold (N)
GRID_SPACING = 10.0              # Grid point spacing (mm)
```

### Coordinate Systems
Define coordinate transformations:

```python
# Stage-to-robot coordinate transformation
STAGE_TO_ROBOT_TRANSFORM = {
    'translation': [100, 50, 0],   # mm
    'rotation': [0, 0, 90]         # degrees
}
```

## Usage

### Basic Operation

1. **Initialize system**:
   ```bash
   python main.py
   ```

2. **System startup sequence**:
   - Robot connects and activates
   - Zaber stages home automatically
   - Coordinate systems are established
   - Probing sequence begins

3. **Automated probing**:
   - Robot moves to starting position
   - Stages position workpiece
   - Probe approaches and measures
   - Data is recorded to database
   - Sequence continues for all points

### Custom Probing Patterns

Define custom probing sequences in `moveFunctions.py`:

```python
def custom_probing_pattern(robot, stages):
    """Define custom probing sequence"""
    probe_points = [
        {'robot_pos': [300, 0, 100], 'stage_pos': [50]},
        {'robot_pos': [300, 50, 100], 'stage_pos': [75]},
        # Add more points as needed
    ]
    
    for point in probe_points:
        move_to_probe_point(robot, stages, point)
        measurement = perform_probe()
        store_measurement(measurement)
```

## Database Operations

### Measurement Storage
The system automatically stores measurements in SQLite database:

```python
# Measurement data structure
measurement_data = {
    'timestamp': datetime.now(),
    'robot_position': [x, y, z, rx, ry, rz],
    'stage_position': stage_pos,
    'measurement_value': probe_value,
    'probe_force': contact_force,
    'measurement_id': unique_id
}
```

### Data Retrieval
Query stored measurements:

```python
from storeDb import get_measurements

# Retrieve all measurements
all_data = get_measurements()

# Filter by date range
recent_data = get_measurements(start_date='2024-01-01')

# Export to CSV
export_measurements_csv('probing_results.csv')
```

## Probing Functions

### Standard Probing Operations

**Bottom Right Probing** (`bottomRight()`):
- Positions robot for corner measurement
- Accounts for workpiece orientation
- Records coordinate data

**Grid Probing** (custom function):
- Systematic grid pattern measurement
- Configurable spacing and coverage
- Statistical analysis of results

**Profile Probing**:
- Continuous profile measurement
- Smooth motion coordination
- High-resolution data capture

## Movement Coordination

### Synchronized Motion
The system coordinates robot and stage movements:

```python
def synchronized_move(robot, stage, robot_target, stage_target):
    """Move robot and stage simultaneously"""
    # Start movements
    robot.MoveJoints(*robot_target)
    stage.move_absolute(stage_target)
    
    # Wait for completion
    robot.WaitIdle()
    stage.wait_until_idle()
```

### Safety Interlocks
- **Collision avoidance**: Check clearances before movement
- **Workspace limits**: Enforce safe operating boundaries
- **Emergency stops**: Immediate halt of all motion
- **Force monitoring**: Prevent excessive probe forces

## Calibration Procedures

### System Calibration
1. **Stage calibration**: Home and calibrate Zaber stages
2. **Robot calibration**: Verify robot accuracy and repeatability
3. **Coordinate calibration**: Establish stage-robot relationship
4. **Probe calibration**: Determine probe tip offset and force characteristics

### Calibration Scripts
Run calibration utilities:

```bash
python test.py      # Basic functionality test
python test2.py     # Advanced calibration routines
```

## Data Analysis

### Measurement Processing
Process collected data for analysis:

```python
import numpy as np
from storeDb import get_measurements

# Load measurement data
data = get_measurements()

# Statistical analysis
mean_values = np.mean(data['measurements'])
std_deviation = np.std(data['measurements'])
measurement_range = np.ptp(data['measurements'])

# Generate reports
generate_measurement_report(data)
```

### Visualization
Create measurement visualizations:
- 3D point clouds of measured coordinates
- Heat maps of measurement variations
- Trend analysis over time
- Statistical distribution plots

## Troubleshooting

### Common Issues

**Stage communication errors**:
- Verify COM port settings and connections
- Check Zaber device drivers
- Test with Zaber Console software

**Robot positioning errors**:
- Verify robot calibration
- Check coordinate system definitions
- Ensure workspace limits are appropriate

**Measurement inconsistencies**:
- Calibrate probe force settings
- Check for mechanical vibrations
- Verify stage positioning accuracy

### Debug Mode
Enable detailed logging:

```python
DEBUG_MODE = True
VERBOSE_LOGGING = True
LOG_MEASUREMENTS = True
```

## Advanced Features

### Multi-Stage Systems
Support for multiple Zaber stages:
- XY stage combinations
- Rotary stage integration
- Complex multi-axis positioning

### Adaptive Probing
- Surface-following probing
- Adaptive sampling density
- Intelligent measurement strategies

### Integration APIs
- CAD system integration
- Quality management system interfaces
- Real-time process monitoring

## Safety Guidelines

⚠️ **Important Safety Information:**
- Ensure all motion paths are collision-free
- Verify probe force limits to prevent damage
- Maintain clear workspace during operation
- Test new sequences in simulation first
- Keep emergency stops readily accessible

## Performance Optimization

### Speed Optimization
- Optimize motion paths for efficiency
- Reduce unnecessary movements
- Parallel processing where possible
- Smart measurement sequencing

### Accuracy Optimization
- Minimize thermal effects
- Account for mechanical deflections
- Use appropriate measurement forces
- Regular calibration maintenance