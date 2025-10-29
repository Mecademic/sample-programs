#include "robot_interface.h"

#include "stdio.h"
#include "stdlib.h"
#include "string.h"

/// The control port for the meca500
static const char *CONTROL_PORT = "10000";

/// Utility to exit the function if the robot is not connected
#define EXIT_ON_ROBOT_NOT_CONNECTED(connected_flag) \
    if (connected_flag == 0)                        \
    {                                               \
        printf("Robot not connected.\r\n");         \
        return -1;                                  \
    }

//=============================================================================
//
/// Extract the code ("[3000][..." -> 3000) from a message and return it as int.
/// if not found, return 0;
int extract_code(const char *message)
{
    int code = 0;
    char *first_bracket = NULL;
    char *second_bracket = NULL;
    do
    {
        first_bracket = strchr(message, '[');
        second_bracket = strchr(message, ']');
        if ((int)(second_bracket - first_bracket) == 5)
        {
            code = 1000 * (first_bracket[1]-'0') + 
                   100 * (first_bracket[2]-'0') + 
                   10 * (first_bracket[3]-'0') + 
                   1 * (first_bracket[4]-'0');
            break;
        }
        message = second_bracket + 1;
    } while (first_bracket != NULL && second_bracket != NULL);
    
    return code;
}

//=============================================================================
//
int connect_robot(char* address, Meca500 *robot)
{
    robot->connected_ = 0;
    int result = tcpip_connect(address, CONTROL_PORT, &(robot->robot_connection_));
    if (result == 0)
    {
        robot->connected_ = 1;
    }
    return result;
}

//=============================================================================
//
int disconnect_robot(Meca500 *robot)
{
    EXIT_ON_ROBOT_NOT_CONNECTED(robot->connected_);
    tcpip_disconnect(&(robot->robot_connection_));
    robot->connected_ = 0;
    return 0;
}

//=============================================================================
//
int wait_for_return_code(int code, Meca500 *robot)
{
    EXIT_ON_ROBOT_NOT_CONNECTED(robot->connected_);
    
    char buffer[1024];
    int received_code = 0;

    while (received_code != code)
    {
        memset(buffer, 0, sizeof(buffer));
        int result = tcpip_receive(buffer, sizeof(buffer) - 1, &(robot->robot_connection_));
        
        if (result <= 0)
        {
            return -1; // Network error or connection closed
        }
        
        received_code = extract_code(buffer);

        // Check for error codes (1000-2000 range)
        if (received_code >= 1000 && received_code < 2000)
        {
            printf("Error code received: %d\r\n", received_code);
            return 1; // Error code received
        }
    }
    
    return 0; // Success
}

//=============================================================================
//
int wait_for_EOB(Meca500 *robot)
{
    return wait_for_return_code(3004, robot); // EOB code is 3004
}

//=============================================================================
//
int activate_robot(Meca500 *robot)
{
    EXIT_ON_ROBOT_NOT_CONNECTED(robot->connected_);
    
    const char* command = "ActivateRobot\r\n";
    int result = tcpip_send(command, strlen(command), &(robot->robot_connection_));
    if (result != 0)
    {
        return -1;
    }
    
    return wait_for_return_code(2000, robot); // Wait for robot activated
}

//=============================================================================
//
int deactivate_robot(Meca500 *robot)
{
    EXIT_ON_ROBOT_NOT_CONNECTED(robot->connected_);
    
    const char* command = "DeactivateRobot\r\n";
    int result = tcpip_send(command, strlen(command), &(robot->robot_connection_));
    if (result != 0)
    {
        return -1;
    }
    
    return wait_for_return_code(2004, robot); // Wait for robot deactivated
}

//=============================================================================
//
int activate_sim(Meca500 *robot)
{
    EXIT_ON_ROBOT_NOT_CONNECTED(robot->connected_);
    
    const char* command = "ActivateSim\r\n";
    int result = tcpip_send(command, strlen(command), &(robot->robot_connection_));
    if (result != 0)
    {
        return -1;
    }
    
    return wait_for_return_code(2045, robot); // Wait for sim activated
}

//=============================================================================
//
int deactivate_sim(Meca500 *robot)
{
    EXIT_ON_ROBOT_NOT_CONNECTED(robot->connected_);
    
    const char* command = "DeactivateSim\r\n";
    int result = tcpip_send(command, strlen(command), &(robot->robot_connection_));
    if (result != 0)
    {
        return -1;
    }
    
    return wait_for_return_code(2046, robot); // Wait for sim deactivated
}

//=============================================================================
//
int home(Meca500 *robot)
{
    EXIT_ON_ROBOT_NOT_CONNECTED(robot->connected_);
    
    const char* command = "Home\r\n";
    int result = tcpip_send(command, strlen(command), &(robot->robot_connection_));
    if (result != 0)
    {
        return -1;
    }
    
    return wait_for_return_code(2002, robot); // Wait for homing done
}

//=============================================================================
//
int movejoints(Meca500 *robot, float joints[6])
{
    EXIT_ON_ROBOT_NOT_CONNECTED(robot->connected_);
    
    char command[256];
    snprintf(command, sizeof(command), "MoveJoints(%.3f,%.3f,%.3f,%.3f,%.3f,%.3f)\r\n",
             joints[0], joints[1], joints[2], joints[3], joints[4], joints[5]);
    
    return tcpip_send(command, strlen(command), &(robot->robot_connection_));
}

//=============================================================================
//
int movepose(Meca500 *robot, float euler[6])
{
    EXIT_ON_ROBOT_NOT_CONNECTED(robot->connected_);
    
    char command[256];
    snprintf(command, sizeof(command), "MovePose(%.3f,%.3f,%.3f,%.3f,%.3f,%.3f)\r\n",
             euler[0], euler[1], euler[2], euler[3], euler[4], euler[5]);
    
    return tcpip_send(command, strlen(command), &(robot->robot_connection_));
}

//=============================================================================
//
int movetozero(Meca500 *robot)
{
    float zero_joints[6] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
    return movejoints(robot, zero_joints);
}

//=============================================================================
//
int movetoshipping(Meca500 *robot)
{
    float shipping_joints[6] = {0.0, -60.0, 60.0, 0.0, 0.0, 0.0};
    return movejoints(robot, shipping_joints);
}