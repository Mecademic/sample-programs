#ifndef SOCKET_COMM_H
#define SOCKET_COMM_H

#include <winsock2.h>
#include <windows.h>
#include <ws2tcpip.h>

// For now keep only socket inside, but could add more stuff
// when the program will require more functionality.
typedef struct{
    SOCKET socket_;
}tcpip_connection;

/// Connect a TCP socket. Handles the windows init socket
/// Return 0 for success, -1 for failure.
int tcpip_connect(const char *address, const char *port, tcpip_connection * connection);

/// Disconnect a connection
void tcpip_disconnect(tcpip_connection *connection);

/// Send data to the buffer
/// Return 0 for success, -1 for failure, or the size that was actually sent
/// if the entire data did not fit in the TCP buffer. In that case, you should 
/// send the remaining. 
int tcpip_send(const char* buffer, int len, tcpip_connection *connection);

/// Try to receive len byte of data.
/// Return 0 for CLOSED CONNECTION, -1 for failure, or the nb of data received. 
int tcpip_receive(char* buffer, int len, tcpip_connection *connection);

#endif // SOCKET_COMM_H