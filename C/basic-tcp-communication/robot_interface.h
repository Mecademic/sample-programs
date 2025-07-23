#ifndef ROBOT_INTERFACE_H
#define ROBOT_INTERFACE_H

#include "socket_comm.h"

// Contain the information about a robots connection.
// Members should not be access individually
typedef struct 
{
    tcpip_connection robot_connection_;
    int connected_;
}Meca500;

/// Connect to a meca500 to the control port
int connect_robot(char* address, Meca500 *robot);

/// Disconnect a meca500
int disconnect_robot(Meca500 *robot);

/// Wait for a specified return code.
/// Return 0 if code was received.
/// Return 1 if an error code ( between 1000 and 2000) was received
/// Return -1 if there was a network error.
int wait_for_return_code(int code, Meca500 *robot);

/// Wait for End of Block flag.
/// Return 0 if code was received.
/// Return 1 if an error code ( between 1000 and 2000) was received
/// Return -1 if there was a network error.
int wait_for_EOB(Meca500 *robot);

/// Send an ActivateRobot command and wait for it to be completed.
/// return 0 for success
/// return -1 for failure
int activate_robot(Meca500 *robot);

/// Send an DeactivateRobot command and wait for it to be completed.
/// return 0 for success
/// return -1 for failure
int deactivate_robot(Meca500 *robot);

/// Send an activatesim command and wait for it to be completed.
/// return 0 for success
/// return -1 for failure
int activate_sim(Meca500 *robot);

/// Send an deactivatesim command and wait for it to be completed.
/// return 0 for success
/// return -1 for failure
int deactivate_sim(Meca500 *robot);

/// Send an home command and wait for it to be completed.
/// return 0 for success
/// return -1 for failure
int home(Meca500 *robot);

/// Sends a MoveJoint command. Do not wait for completion.
/// return 0 for success
/// return -1 for failure
int movejoints(Meca500 *robot, float joints[6]);

/// Sends a MovePose command. Do not wait for completion.
/// return 0 for success
/// return -1 for failure
int movepose(Meca500 *robot, float euler[6]);

/// Sends a MoveJoint command to go to zero. Do not wait for completion.
/// return 0 for success
/// return -1 for failure
int movetozero(Meca500 *robot);

/// Sends a MoveJoint command for the shipping position. Do not wait for completion.
/// return 0 for success
/// return -1 for failure
int movetoshipping(Meca500 *robot);

#endif // ROBOT_INTERFACE_H