# Socket_Programming_Python
Simple Python SMTP Email Client

This Python program is a simple implementation of an SMTP (Simple Mail Transfer Protocol) email client that allows you to send emails through a Gmail account using sockets and SSL/TLS encryption. It prompts the user for their email credentials, recipient information, subject, and message body.
How it Works

User Input: The program begins by requesting the user's Gmail email address and password. It also prompts for the recipient's email address, subject, and message body.

Socket Initialization: It establishes a TCP connection with Gmail's SMTP server (smtp.gmail.com) on port 587.

TLS Encryption: After connecting, it issues a STARTTLS command to enable SSL/TLS encryption for secure communication.

Authentication: The program uses Base64 encoding to securely transmit the email address and password to authenticate with the SMTP server.

Email Composition: The user's input is used to compose the email, including the sender, recipient, subject, and message body.

SMTP Commands: The program sends SMTP commands to the server, such as MAIL FROM, RCPT TO, DATA, and QUIT, to follow the SMTP protocol and send the email.

Email Sending: The message is sent to the recipient's email address through the Gmail SMTP server.

Completion: After successfully sending the email, the program closes the connection and displays a "Success" message.


Important Notes:

Gmail may require you to enable "Less secure apps" in your Google Account settings to use this script. Please use caution and consider using an app password for better security.
This script is for educational purposes and may require adjustments for production use.

