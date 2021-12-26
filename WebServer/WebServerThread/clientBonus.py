#import socket module
from socket import *
import sys

# If any argument passed
if len(sys.argv) == 4:
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]
else:
    print "Please provide arguments <server_host> <server_port> <filename>"
    sys.exit(1)
    
# Prepare socket
try:
    connection=socket(AF_INET,SOCK_STREAM)
    connection.connect((server_host,server_port))
except Exception as error:
    print("ERROR!", error)
    sys.exit(1)

#Send get request
connection.send('GET /'+filename.encode())

#returned data from server
response = ""
while True:
    data = connection.recv(1024).decode()
    if not data:
        break
    response += data 

# Print data
print(response)

# Close socket
connection.close()
