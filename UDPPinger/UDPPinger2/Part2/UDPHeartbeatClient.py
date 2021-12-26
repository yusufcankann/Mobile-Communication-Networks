import time
import socket


# sends package to server every heathbeatInterval second
heathbeatInterval=1

#Creates the UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Sets timeout to 1
clientSocket.settimeout(1.0)

#client sends udp packages until it is closed
i=0
while True:
    #start time
    t1 = time.time()

    #sets sequence number and timestamp
    m="Ping "+str(i)+" "+str(t1)
    
    #Send the UDP messages with time and sequence number
    clientSocket.sendto(m.encode(),("127.0.0.1", 12000))
    print "Sent Message:",m
    i+=1
    time.sleep(heathbeatInterval)
