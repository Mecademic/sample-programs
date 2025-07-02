using System;
using System.Net.Sockets;
using System.Text;
using System.Threading;

namespace Meca500Examples
{
    /// <summary>
    /// Meca500 Quick Start Example
    /// This script demonstrates the absolute basics of connecting to and controlling a Meca500 robot.
    /// 
    /// Prerequisites:
    /// - Meca500 robot connected to network
    /// - Robot IP address known (default: 192.168.0.100)
    /// - Robot in normal mode (not recovery mode)
    /// 
    /// Usage:
    /// 1. Update the ROBOT_IP constant to match your robot's IP address
    /// 2. Compile and run
    /// 3. Follow console prompts
    /// </summary>
    class Meca500QuickStart
    {
        // ========== CONFIGURATION ==========
        // Change this to match your robot's IP address
        const string ROBOT_IP = "192.168.0.100";
        const int ROBOT_PORT = 10000;

        // Basic movement parameters (in mm and degrees)
        const double SAFE_Z_HEIGHT = 200;  // Safe height to avoid collisions
        const double MOVE_SPEED = 25;      // Movement speed percentage (0-100)

        static void Main(string[] args)
        {
            Console.WriteLine("=== Meca500 Quick Start Example ===\n");
            
            TcpClient? client = null;
            NetworkStream? stream = null;

            try
            {
                // ========== STEP 1: CONNECT TO ROBOT ==========
                Console.WriteLine($"[1] Connecting to robot at {ROBOT_IP}:{ROBOT_PORT}...");
                
                client = new TcpClient();
                // Set timeout for connection attempt (5 seconds)
                var result = client.BeginConnect(ROBOT_IP, ROBOT_PORT, null, null);
                var success = result.AsyncWaitHandle.WaitOne(TimeSpan.FromSeconds(5));
                
                if (!success)
                {
                    throw new Exception("Connection timeout - check robot IP and network connection");
                }
                
                client.EndConnect(result);
                stream = client.GetStream();
                Console.WriteLine("    ✓ Connected successfully!\n");

                // Give robot time to process connection
                Thread.Sleep(500);

                // ========== STEP 2: ACTIVATE ROBOT ==========
                Console.WriteLine("[2] Activating robot...");
                SendCommand(stream, "ActivateRobot");
                Console.WriteLine("    - Command sent, waiting for activation...");
                
                // Wait for activation (typically takes 2-3 seconds)
                Thread.Sleep(3000);
                Console.WriteLine("    ✓ Robot activated!\n");

                // ========== STEP 3: HOME ROBOT ==========
                Console.WriteLine("[3] Homing robot...");
                SendCommand(stream, "Home");
                Console.WriteLine("    - Homing in progress...");
                
                // Wait for homing confirmation from robot
                WaitForResponse(stream, "[2002][Homing done.]");
                Console.WriteLine("    ✓ Robot homed!\n");

                // ========== STEP 4: SET MOTION PARAMETERS ==========
                Console.WriteLine("[4] Setting motion parameters...");
                
                // Set joint velocity (percentage of max speed)
                SendCommand(stream, $"SetJointVel({MOVE_SPEED})");
                Thread.Sleep(100);
                
                // Set Cartesian linear velocity (percentage of max speed)  
                SendCommand(stream, $"SetCartLinVel({MOVE_SPEED})");
                Thread.Sleep(100);
                
                // Resume motion (required after activation)
                SendCommand(stream, "ResumeMotion");
                Thread.Sleep(100);
                
                Console.WriteLine("    ✓ Motion parameters set!\n");

                // ========== STEP 5: PERFORM TEST MOVEMENTS ==========
                Console.WriteLine("[5] Performing test movements...");
                Console.WriteLine("    WARNING: Robot will move! Ensure area is clear.");
                Console.WriteLine("    Press any key to continue...");
                Console.ReadKey();

                // Get current position
                Console.WriteLine("\n    - Getting current position...");
                SendCommand(stream, "GetPose");
                Thread.Sleep(500);  // In production, you'd read the response

                // Move to safe position above home
                Console.WriteLine($"    - Moving to safe position (Z={SAFE_Z_HEIGHT}mm)...");
                SendCommand(stream, $"MovePose(190, 0, {SAFE_Z_HEIGHT}, 0, 90, 0)");
                
                // Wait for movement to complete
                Thread.Sleep(5000);
                Console.WriteLine("    ✓ Reached safe position");

                // Move in a square pattern (X-Y plane)
                Console.WriteLine("    - Executing square pattern...");
                
                // Corner 1
                SendCommand(stream, $"MovePose(100, 100, {SAFE_Z_HEIGHT}, 0, 90, 0)");
                Thread.Sleep(3000);
                
                // Corner 2  
                SendCommand(stream, $"MovePose(100, -100, {SAFE_Z_HEIGHT}, 0, 90, 0)");
                Thread.Sleep(5000);
                
                // Corner 3
                SendCommand(stream, $"MovePose(200, -100, {SAFE_Z_HEIGHT}, 0, 90, 0)");
                Thread.Sleep(3000);
                
                // Corner 4
                SendCommand(stream, $"MovePose(200, 100, {SAFE_Z_HEIGHT}, 0, 90, 0)");
                Thread.Sleep(3000);
                
                // Return to center
                SendCommand(stream, $"MovePose(190, 0, {SAFE_Z_HEIGHT}, 0, 90, 0)");
                Thread.Sleep(3000);
                
                Console.WriteLine("    ✓ Test movements complete!\n");

                // ========== STEP 6: DEACTIVATE ROBOT ==========
                Console.WriteLine("[6] Deactivating robot...");
                SendCommand(stream, "DeactivateRobot");
                Thread.Sleep(2000);
                Console.WriteLine("    ✓ Robot deactivated\n");

                Console.WriteLine("=== Quick Start Example Complete! ===");
                Console.WriteLine("\nNext steps:");
                Console.WriteLine("- Try modifying the movement positions");
                Console.WriteLine("- Add error checking with GetStatusRobot");
                Console.WriteLine("- Explore other commands in the Meca500 manual");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"\n!!! ERROR: {ex.Message}");
                Console.WriteLine("\nTroubleshooting:");
                Console.WriteLine("1. Check robot IP address in configuration");
                Console.WriteLine("2. Ensure robot is powered on and connected to network");
                Console.WriteLine("3. Verify no other application is connected to robot");
                Console.WriteLine("4. Check robot is not in error state (red LED)");
            }
            finally
            {
                // ========== CLEANUP ==========
                Console.WriteLine("\n[7] Closing connection...");
                
                // Close network stream
                if (stream != null)
                {
                    stream.Close();
                    stream.Dispose();
                }
                
                // Close TCP client
                if (client != null)
                {
                    client.Close();
                    client.Dispose();
                }
                
                Console.WriteLine("    ✓ Connection closed\n");
                Console.WriteLine("Press any key to exit...");
                Console.ReadKey();
            }
        }

        /// <summary>
        /// Sends a command to the robot
        /// All Meca500 commands must be null-terminated
        /// </summary>
        static void SendCommand(NetworkStream stream, string command)
        {
            // Add null terminator to command
            byte[] data = Encoding.ASCII.GetBytes(command + "\0");
            
            // Send to robot
            stream.Write(data, 0, data.Length);
            stream.Flush();
            
            // Log what we sent
            Console.WriteLine($"    → Sent: {command}");
        }

        /// <summary>
        /// Waits for a specific response from the robot
        /// </summary>
        static void WaitForResponse(NetworkStream stream, string expectedResponse)
        {
            byte[] buffer = new byte[1024];
            var responseBuilder = new StringBuilder();
            
            while (true)
            {
                if (stream.DataAvailable)
                {
                    int bytesRead = stream.Read(buffer, 0, buffer.Length);
                    string response = Encoding.ASCII.GetString(buffer, 0, bytesRead);
                    responseBuilder.Append(response);
                    
                    string fullResponse = responseBuilder.ToString();
                    Console.WriteLine($"    ← Received: {response.Trim()}");
                    
                    if (fullResponse.Contains(expectedResponse))
                    {
                        break;
                    }
                }
                
                Thread.Sleep(100); // Small delay to avoid busy waiting
            }
        }
    }
}