from socket import *
from base64 import *
import ssl
userEmail = input("Enter Your Email Address: ")
userPassword = input("Enter Your Password: ")
userDestinationEmail = input("Enter Email Destination: ")
userSubject = input("Enter Subject: ")
userBody = input("Enter Message: ")


msg = '{}.\r\n I love operating systems!'.format(userBody)
endmsg = "\r\n.\r\n"
# Choosing a mail server 
mailserver = 'smtp.gmail.com'
mailPort = 587 #port no for smtp
# Creating a socket called clientSocket and establishing a TCP connection

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailPort))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
strtlscmd = "STARTTLS\r\n".encode()
clientSocket.send(strtlscmd)
revc2 = clientSocket.recv(1024)


sslClientSocket = ssl.wrap_socket(clientSocket)


emailA = b64encode(userEmail.encode("utf-8"))
emailP = b64encode(userPassword.encode("utf-8"))


authorizationCMD = "AUTH LOGIN\r\n"


sslClientSocket.send(authorizationCMD.encode())
recv2 = sslClientSocket.recv(1024)
print(recv2)


sslClientSocket.send(emailA + "\r\n".encode())
recv3 = sslClientSocket.recv(1024)
print(recv3)


sslClientSocket.send(emailP + "\r\n".encode())
recv4 = sslClientSocket.recv(1024)
print(recv4)


# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "Mail from: <{}>\r\n".format(userDestinationEmail)
sslClientSocket.send(mailFrom.encode())
recv5 = sslClientSocket.recv(1024)
print(recv5)
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
rcptto = "RCPT TO: <{}>\r\n".format(userDestinationEmail)
sslClientSocket.send(rcptto.encode())
recv6 = sslClientSocket.recv(1024)
print(recv6)
# Fill in end
# Send DATA command and print server response.
# Fill in start
data = 'DATA\r\n'
sslClientSocket.send(data.encode())
recv7 = sslClientSocket.recv(1024)
print(recv7)
# Fill in end
# Send message data.
# Fill in start
sslClientSocket.send("Subject: {}\n\n{}".format(userSubject, msg).encode())
# Fill in end
# Message ends with a single period.
# Fill in start
sslClientSocket.send(endmsg.encode())
recv8 = sslClientSocket.recv(1024)
print(recv8)
# Fill in end
# Send QUIT command and get server response.
# Fill in start
quitCMD = 'QUIT\r\n'
sslClientSocket.send(quitCMD.encode())
recv9 = sslClientSocket.recv(1024)
print(recv9)
sslClientSocket.close()
print('Success')