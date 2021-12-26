#import socket module
from socket import *

PORT = 6787
#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
#bind
serverSocket.bind(('', PORT))
serverSocket.listen(1)

while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket,addr=serverSocket.accept()       
    try:
        message=connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()        

        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n')
            
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        print "404 Not Found"
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\n".encode()))
        connectionSocket.send(bytes("<html><head><title> 404 </title></head><body><h1>404 Not Found!</h1></body></html>\r\n".encode()))
        
        connectionSocket.close()     

serverSocket.close()                                    
