
# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *

#max timeout period that will be assumed client is stopped
maxTimeoutPeriod=5

#recieves package every hearthbeatinterval second. This variable also setted in client file
heathbeatInterval=1


# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
serverSocket.settimeout(maxTimeoutPeriod)

t1=0
while True:
    try:
        # Receive the client packet along with the address it is coming from 
        message,address=serverSocket.recvfrom(1024)
        t2=float(message.decode().split(" ")[2])
        t3=t2 - t1 

        if t1!=0 and t3>heathbeatInterval+ 0.05: #0.1 added for any delay during sending operations
            print str(int(t3/heathbeatInterval)) + " packages are lost!"
        else:
            print "Heartbeat..."
        t1=t2
    except timeout:
        if t1!=0:
            print("No heartbeat from client... Client stopped! ")
        

