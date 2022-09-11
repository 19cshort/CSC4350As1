#Connor Short
#server to listen on port 8000 and handle various requests sent by a client
#python version 3.9.4, used the socket library, the datetime library, and the optparse library
#Open an IDLE Shell and run the server


from datetime import datetime
from socket import *
import socket
from optparse import OptionParser

#options for command line parameters, use -h to get the help statements to show up
parser = OptionParser()
parser.add_option("-p",
                  action = "store", type="int", dest="serverPort", default = 8000,
                  help = "choose port for connection, must be same as on client")
parser.add_option("-t",
                  action = "store", type="str", dest="protocolChoice", default = "TCP",
                  help = "choose transmission protocol to use, TCP is default can also choose UDP")

(options, args) = parser.parse_args()

if options.protocolChoice == "UDP":

    serverSocket = socket.socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('',options.serverPort))
    print ("The server is ready to recieve")

    while True: #while loop to keep the server open and redy to recieve
        message, clientAddress = serverSocket.recvfrom(2048) #recieving the message and the address from the client
        print(message)
        print(clientAddress)
        modifiedMessage = message.decode() #decoding the recieved message

        if modifiedMessage == '1':
            hostname=socket.gethostname() 
            IPAddr=socket.gethostbyname(hostname) #these two^ functions get the ip address
            serverSocket.sendto (IPAddr.encode(), clientAddress) #sending the ip address back to the client
        elif modifiedMessage == '2':
            message = str(clientAddress[1]) #turning the port number into a string for encoding
            print (message)
            serverSocket.sendto (message.encode(), clientAddress) #sending the port number back to the client
        else:
            message = datetime.now() #getting the servers date and time
            modifiedMessage = datetime.strptime(modifiedMessage, "%Y/%m/%d, %H:%M:%S:%f") #taking the client date and time and formatting it
            print (message)
            print(modifiedMessage)
            newMessage = message - modifiedMessage #calculating the delay between the client and the server
            newMessage = str(newMessage)
            wholeMessage = newMessage + ' ' + str(message) #combining the delay and the servers date time into one string for transmission
            serverSocket.sendto(wholeMessage.encode(),clientAddress) #sending the whole message back to the client

elif options.protocolChoice == "TCP":
    
    serverSocket = socket.socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('',options.serverPort))
    serverSocket.listen(1)
    print ("The server is ready to recieve")

    while True: #while loop to keep the server open and redy to recieve
        connectionSocket, clientAddress = serverSocket.accept()
        message = connectionSocket.recv(2048) #recieving the message and the address from the client
        #print(message)
        #print(clientAddress)
        modifiedMessage = message.decode() #decoding the recieved message

        if modifiedMessage == '1':       
            hostname=socket.gethostname() 
            IPAddr=socket.gethostbyname(hostname) #these two^ functions get the ip address
            connectionSocket.send (IPAddr.encode()) #sending the ip address back to the client
        elif modifiedMessage == '2':
            message = str(clientAddress[1]) #turning the port number into a string for encoding
            print (message)
            connectionSocket.send(message.encode()) #sending the port number back to the client
        else:
            message = datetime.now() #getting the servers date and time
            modifiedMessage = datetime.strptime(modifiedMessage, "%Y/%m/%d, %H:%M:%S:%f") #taking the client date and time and formatting it
            print (message)
            print(modifiedMessage)
            newMessage = message - modifiedMessage #calculating the delay between the client and the server
            newMessage = str(newMessage)
            wholeMessage = newMessage + ' ' + str(message) #combining the delay and the servers date time into one string for transmission
            connectionSocket.send(wholeMessage.encode()) #sending the whole message back to the client

else:
    print ("Unsupported protocol sent, use TCP or UDP")
