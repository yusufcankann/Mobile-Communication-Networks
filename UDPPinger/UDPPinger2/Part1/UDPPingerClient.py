import time
import socket

#Creates the UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Sets timeout to 1
clientSocket.settimeout(1.0)

rttList=[]
lossCount=0
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
        rttList.append(passingTime)

    except socket.timeout:
        print "Request "+str(i)+" Timed Out"
        lossCount+=1
#if all of the packages loss, no calculation
if len(rttList)!=0:
    sum = sum(rttList)
    min = min(rttList)
    max = max(rttList)
    avg = sum / len(rttList)

    print "-----Statistic-----\n"
    print "Sum RTT:     "+str(sum)
    print "Min RTT:     "+str(min)
    print "Max RTT:     "+str(max)
    print "Average RTT: "+str(avg)

lossRate = (lossCount*100)/10
print "Package Loss Rate: %"+str(lossRate)