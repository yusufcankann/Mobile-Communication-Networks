from socket import *
import ssl
import base64
import sys

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

fromMail=""
toMail="" #Write your own e-mail here!
password=""


# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 587)

# Establish TCP connection
try:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)
except Exception as error:
    print 'Error!' + str(error)
    sys.exit(1)

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print "220 couldn't recieved from server."

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print "250 couldn't recieved from server."
    
# Send MAIL FROM command and print server response.
#ttls command
TLSCommand = "STARTTLS\r\n"
clientSocket.send(TLSCommand.encode())
recv2 = clientSocket.recv(1024)
print recv2
if (recv2[:3] != '220'):
    print "220 couldn't recieved from server. (TTLS)"

clientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)


clientSocket.send(('AUTH LOGIN\r\n').encode())
print(clientSocket.recv(1024).decode())

clientSocket.send((base64.b64encode(fromMail.encode()))+('\r\n').encode())
print(clientSocket.recv(1024).decode())

clientSocket.send((base64.b64encode(password.encode()))+('\r\n').encode())
print(clientSocket.recv(1024).decode())

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <"+fromMail+"> \r\n"
clientSocket.send(mailFrom.encode())
recv3 = clientSocket.recv(1024)
print recv3 
if recv3[:3] != '250':
    print "250 couldn't recieved from server."

# Send RCPT TO command and print server response. 
rcptTo = "RCPT TO: <"+toMail+"> \r\n"
clientSocket.send(rcptTo.encode())
recv4 = clientSocket.recv(1024)
print recv4
if recv4[:3] != '250':
    print "250 couldn't recieved from server."

# Send DATA command and print server response. 
data="DATA\r\n"
clientSocket.send(data.encode())
recv7 = clientSocket.recv(1024)
print recv7
if (recv7[:3] != '354'):
	print "354 couldn't recieved from server."



#Send message data.
#message subject
clientSocket.send(("Subject: Mobile Commumication Network Part3 SMTP Client Test"+" \r\n\r\n").encode())
#message
clientSocket.send(msg.encode())
#message end
clientSocket.send(endmsg.encode())
recv8 = clientSocket.recv(1024)
print(recv8)
if (recv8[:3] != '250'):
	print "250 couldn't recieved from server."



# Send QUIT command and get server response.
quit="QUIT\r\n"
clientSocket.send(quit.encode())
message=clientSocket.recv(1024)
print message
if message[:3] != '221':
    print '221 reply not received from server.'

print "Mail succesfully sent..."

#close socket
clientSocket.close()
