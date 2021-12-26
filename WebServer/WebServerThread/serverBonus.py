import sys
from socket import *
import threading


#Thread function
def threadFunct(connectionSocket, address):
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

    # # Close client socket  
    # connectionSocket.shutdown(socket.SHUT_RDWR)
    connectionSocket.close()

# Main function
def main():
    threads = []
    serverSocket = None

    PORT = 6787 
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', PORT))
    serverSocket.listen(10)

    # Main loop
    while True:
        # Accept a connection
        print("Server is ready!")
        clientSocket, address = serverSocket.accept()
        clientSocket.settimeout(5)
        t = threading.Thread(target=threadFunct, args=(clientSocket,address))
        threads.append(t)
        t.start()

if __name__ == "__main__":
    main()