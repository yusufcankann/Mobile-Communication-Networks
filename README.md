# Mobile-Communication-Networks
##Web Server
###Web Server
This project includes a web server that handles HTTP requests, recieves thre request messages and sends a response. Project does not use httplib or any similar library.  
It uses only TCP sockets for the implementations. The server accepts only GET requests and return only HelloWorld.html page. 
###Web Server Thread
This project has additional improvements of WebServer. It has a simple thread pool on the server side so it can handle multiple request and it has a client code.


##UDP Pinger
###UDP Pinger
This project includes a simple pinger that can send and some ping packages and measuere time between that passed. It uses UDP on the underlying structure instead of ICMP. 
To simulate packet loss, the server randomly drop some packets.
###UDP Pinger2
This project includes some additional RTT measurements in the implementation.
###UDP heartbeat
This project is similar with the UDP Pinger but it has a monitoring system. Client send signals perodically to the server and server calculates the time differences between recieved packages and reports the loss packages using
this calculation. If there is no signal for a while, server assumes client is stopped working.

##SMTP
This project includes a simple mail client that can connect to google server and send emails to provided mail adress. It does not use smtplib or another library. 
It uses a TCP underlying structure. Then communicate with SMTP commands. 
