# Meca500 C# Quick Start Example

This example demonstrates the absolute basics of connecting to and controlling a Meca500 robot using C#.

## Prerequisites

- Meca500 robot connected to network
- Robot IP address known (default: 192.168.0.100)
- Robot in normal mode (not recovery mode)
- .NET 9.0 or later installed

## Setup and Usage

1. **Update Robot IP**: Edit `Meca500-Quickstart.cs` and change the `ROBOT_IP` constant to match your robot's IP address
2. **Build the project**:
   ```bash
   dotnet build
   ```
3. **Run the example**:
   ```bash
   dotnet run
   ```

## What This Example Does

1. **Connects** to the robot via TCP
2. **Activates** the robot
3. **Homes** the robot (waits for completion confirmation)
4. **Sets motion parameters** (speed, velocity)
5. **Performs test movements** in a square pattern
6. **Deactivates** the robot safely

## Troubleshooting

If you encounter connection issues:
1. Check robot IP address in configuration
2. Ensure robot is powered on and connected to network
3. Verify no other application is connected to robot
4. Check robot is not in error state (red LED)