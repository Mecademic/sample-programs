#include <stdio.h>
#include <stdlib.h>
#include "socket_comm.h"

#define DEBUG 0

// Keep count of the user to init/close the library.
static int socket_system_user_count = 0;
// the WSData required by windows sockets.
static WSADATA wsaData;

/// Utility to exit the function if the socket system is not initialized.
#define EXIT_ON_SYSTEM_NOT_INITED() if(socket_system_user_count == 0) {return -1;}

/// Initialise the socket library if needed.
int init_socket_system()
{
    if (socket_system_user_count == 0)
    {
        printf("Init WSA\r\n");
        int result = WSAStartup(MAKEWORD(2, 2), &wsaData);
        if (result != 0)
        {
            printf("WSAStartup failed with error: %d\r\n", result);
            cleanup_socket_system();
            return -1;
        }
    }
    socket_system_user_count++;
    return 0;
}

/// Close the socket library if no more user on it.
void cleanup_socket_system()
{
    socket_system_user_count--;
    if (socket_system_user_count == 0)
    {
        printf("Closing WSA\r\n");
        WSACleanup();
    }
}

//=============================================================================
//
int tcpip_connect(const char *address, const char *port, tcpip_connection *connection)
{
    int result = 0;
    result = init_socket_system();
    if (result != 0)
    {
        return -1;
    }

    struct addrinfo hints, *addr_result;
    ZeroMemory(&hints, sizeof(hints));
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_protocol = IPPROTO_TCP;
    // Get the address information for the connection
    result = getaddrinfo(address, port, &hints, &addr_result);

    if (result != 0)
    {
        printf("getaddrinfo failed with error: %d\r\n", result);
        cleanup_socket_system();
        return -1;
    }

    // Create a SOCKET for connecting to server
    connection->socket_ = socket(addr_result->ai_family,
                                 addr_result->ai_socktype,
                                 addr_result->ai_protocol);
    if (connection->socket_ == INVALID_SOCKET)
    {
        printf("socket failed with error: %ld\r\n", WSAGetLastError());
        cleanup_socket_system();
        return -1;
    }

    // Connect to server.
    result = connect(connection->socket_,
                     addr_result->ai_addr,
                     (int)addr_result->ai_addrlen);
    if (result == SOCKET_ERROR)
    {
        closesocket(connection->socket_);
        cleanup_socket_system();
        connection->socket_ = INVALID_SOCKET;
        return -1;
    }

    // Done with socket creation.
    freeaddrinfo(addr_result);

    return 0;
}

//=============================================================================
//
void tcpip_disconnect(tcpip_connection *connection)
{
    if (socket_system_user_count == 0)
    {
        return;
    }
    closesocket(connection->socket_);
    cleanup_socket_system();
}

//=============================================================================
//
int tcpip_send(const char *buffer, int len, tcpip_connection *connection)
{
    EXIT_ON_SYSTEM_NOT_INITED();
// Send an initial buffer
#ifdef DEBUG
    printf("Sending: %s\r\n", buffer);
#endif

    int send_result = send(connection->socket_, buffer, len, 0);
    if (send_result == SOCKET_ERROR)
    {
        printf("send failed with error: %d\r\n", WSAGetLastError());
        closesocket(connection->socket_);
        cleanup_socket_system();
        return -1;
    }

    // Did not send everything, return the amount of data that was sent.
    if (send_result != len)
    {
        return send_result;
    }

    // everything was sent and
    return 0;
}

//=============================================================================
//
int tcpip_receive(char *buffer, int len, tcpip_connection *connection)
{
    EXIT_ON_SYSTEM_NOT_INITED();

    int recv_result = recv(connection->socket_, buffer, len, 0);
    if (recv_result == 0) // Closing connection case
    {
        printf("Connection closed\r\n");
        closesocket(connection->socket_);
        cleanup_socket_system();
        return 0;
    }
    else if (recv_result < 0) // Error case
    {
        printf("recv failed with error: %d\r\n", WSAGetLastError());
        return -1;
    }
#ifdef DEBUG
    printf("Receiving: %s\r\n", buffer);
#endif

    // contains the amount of data received.
    return recv_result;
}