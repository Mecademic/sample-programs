# C# Examples for Mecademic Meca500

C# and .NET-based sample programs demonstrating robot control, real-time communication, and automation integration.

## Examples

### [Meca500 Quick Start](./Meca500-Quickstart/)
Essential TCP/IP robot control example with smart homing, movement patterns, and comprehensive error handling.

## Prerequisites

- **.NET 9.0+** (or compatible .NET version)
- **Meca500 robot** connected to network
- **Robot IP address** known (default: 192.168.0.100)
- **Robot in normal mode** (not recovery mode)

## Quick Start

1. Clone or download the C# example
2. Configure robot IP in the source code
3. Build and run:
   ```bash
   dotnet build
   dotnet run
   ```

## Common Configuration

```csharp
// Standard connection settings used across examples
const string ROBOT_IP = "192.168.0.100";
const int ROBOT_PORT = 10000;
```

## Safety Warning

⚠️ **These programs physically move the robot.** Ensure workspace is clear and emergency stop is accessible before running.

## Troubleshooting

- **Connection issues**: Verify robot IP and network connectivity
- **Build errors**: Ensure .NET SDK is installed with `dotnet --version`
- **Runtime errors**: Check robot activation status and connection state
- **Nullable warnings**: Update to nullable reference types or disable in project file