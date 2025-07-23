#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "robot_interface.h"

int main(int argc, char* argv[])
{
    Meca500 robot;
    char robot_ip[256] = "192.168.0.100"; // Default IP
    
    // Parse command line arguments for robot IP
    if (argc > 1)
    {
        strcpy(robot_ip, argv[1]);
    }
    else
    {
        printf("Usage: %s <robot_ip>\n", argv[0]);
        printf("Using default IP: %s\n", robot_ip);
    }
    
    printf("Connecting to Meca500 robot at %s...\n", robot_ip);
    
    // Connect to robot
    if (connect_robot(robot_ip, &robot) != 0)
    {
        printf("Failed to connect to robot at %s\n", robot_ip);
        return -1;
    }
    
    printf("Connected successfully!\n");
    
    // Example sequence: Activate -> Home -> Move -> Deactivate
    printf("Activating robot...\n");
    if (activate_robot(&robot) != 0)
    {
        printf("Failed to activate robot\n");
        disconnect_robot(&robot);
        return -1;
    }
    
    printf("Homing robot...\n");
    if (home(&robot) != 0)
    {
        printf("Failed to home robot\n");
        deactivate_robot(&robot);
        disconnect_robot(&robot);
        return -1;
    }
    
    printf("Moving to zero position...\n");
    if (movetozero(&robot) != 0)
    {
        printf("Failed to move to zero\n");
    }
    
    // Wait for movement to complete
    printf("Waiting for movement to complete...\n");
    wait_for_EOB(&robot);
    
    printf("Moving to shipping position...\n");
    if (movetoshipping(&robot) != 0)
    {
        printf("Failed to move to shipping position\n");
    }
    
    // Wait for movement to complete
    printf("Waiting for movement to complete...\n");
    wait_for_EOB(&robot);
    
    printf("Deactivating robot...\n");
    if (deactivate_robot(&robot) != 0)
    {
        printf("Failed to deactivate robot\n");
    }
    
    printf("Disconnecting...\n");
    disconnect_robot(&robot);
    
    printf("Example completed successfully!\n");
    return 0;
}