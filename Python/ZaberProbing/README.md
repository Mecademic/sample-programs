# Zaber Probing Automation for Mecademic Robots

Python scripts for coordinated probing automation between Mecademic robots and Zaber linear stages.

## Description

Automates probing sequences across multiple quadrants, coordinating robot movements with Zaber linear stage positioning for inspection applications.

## Prerequisites

- **Python 3.x** (no specific version specified)
- **Mecademic robot** (M500, M1000, or SCARA series) accessible at default IP **192.168.0.100**
- **Zaber linear stage** with ASCII protocol support and **axis 1 configured**
- **Serial/USB connection** to Zaber device (scripts use COM5)
- **Windows OS** required for COM port functionality

## Dependencies

Install required Python packages:

```bash
pip install mecademicpy zaber-motion
```

**Standard library modules used**: `time` (sleep function)

## Hardware Setup

1. Connect Mecademic robot to network at **192.168.0.100**
2. Connect Zaber linear stage to **COM5** serial port
3. Ensure Zaber device **axis 1** is configured for ASCII protocol
4. Set up probing target in robot workspace

## Configuration

1. **Database Setup**: Run `storeDb.py` first OR download `devices-public.sqlite` from Zaber
2. **COM Port**: Update COM port in scripts if not using COM5
3. **Coordinates**: Update TRF and WRF coordinates in `main.py` for your workspace

## Running the Application

```bash
python test.py        # Test Zaber connection
python test2.py       # Test robot-Zaber coordination  
python main.py        # Full automation (infinite loop)
```

## File Structure

- `main.py` - Main automation sequence with full probing cycle
- `moveFunctions.py` - Probing patterns for each quadrant
- `test.py` - Basic Zaber connection test
- `test2.py` - Combined robot and Zaber coordination test
- `storeDb.py` - Zaber device database utility

## Safety Notes

- Keep emergency stop accessible
- Verify coordinates are within safe workspace
- Start with reduced velocities for testing

## Troubleshooting

- **Robot Connection**: Check IP 192.168.0.100 and network connectivity
- **Zaber Not Found**: Verify COM port and cable connections
- **Database Error**: Run `storeDb.py` or download `devices-public.sqlite`