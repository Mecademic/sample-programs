import socket
import time
import sys

# Create an INET, STREAMing socket (IPv4, TCP/IP)
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('Socket Created')

ROBOT_IP = "192.168.0.100"
ROBOT_PORT = 10000
# Connect the socket object to the robot using IP address (string) and port (int)
client.connect((ROBOT_IP, ROBOT_PORT))

print('Socket Connected to ' + ROBOT_IP)
# Read the response sent by robot upon connecting
msg = client.recv(1024).decode('ascii')
print(msg)

# Send cmd to Activate the robot
cmd = 'ActivateRobot'
# Add ASCII NULL character at the end of the cmd string
try:
    client.send(bytes(cmd + '\0', 'ascii'))
    time.sleep(15)
    msg = client.recv(1024).decode('ascii')
    print(msg)
    
except socket.error:
    print('Failed to send data')

cmd = 'Home'
# Add ASCII NULL character at the end of the cmd string
try:
    client.send(bytes(cmd + '\0', 'ascii'))
    time.sleep(5)
    msg = client.recv(1024).decode('ascii')
    print(msg)
    
except socket.error:
    print('Failed to send data')

cmd = 'MoveJoints(0,0,0,0,0,0)'
# Add ASCII NULL character at the end of the cmd string
try:
    client.send(bytes(cmd + '\0', 'ascii'))
    msg = client.recv(1024).decode('ascii')
    print(msg)
    
except socket.error:
    print('Failed to send data')

cmd = 'MoveJoints(0,-60,60,0,0,0)'
# Add ASCII NULL character at the end of the cmd string
try:
    client.send(bytes(cmd + '\0', 'ascii'))
    msg = client.recv(1024).decode('ascii')
    print(msg)
    
except socket.error:
    print('Failed to send data')

cmd = 'DeactivateRobot'
# Add ASCII NULL character at the end of the cmd string
try:
    client.send(bytes(cmd + '\0', 'ascii'))
    msg = client.recv(1024).decode('ascii')
    print(msg)
    
except socket.error:
    print('Failed to send data')

# Disconnect from the robot and close the socket object
client.close()
sys.exit()