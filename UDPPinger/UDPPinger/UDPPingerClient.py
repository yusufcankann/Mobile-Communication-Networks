import time
import socket

#Creates the UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Sets timeout to 1
clientSocket.settimeout(1.0)

for i in range(1,11):
    #start time
    t1 = time.time()

    m="Ping "+ str(i)+" "+str(t1)
    #Send the UDP messages with time and sequence number
    clientSocket.sendto(m,("127.0.0.1", 12000))
    print "Sent Message:",m

    try:
        #Get message
        data, server = clientSocket.recvfrom(1024)
        #response time
        t2 = time.time()
        #Time differences
        passingTime = t2 - t1
        #Prints the received message data and rtt with sequence number
        print "Received Message:",data,"Sequence Number:",i,"Round Trip Time(RTT):",passingTime

    except socket.timeout:
        print "Request "+str(i)+" Timed Out"