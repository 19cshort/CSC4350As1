#Connor Short
#client to send various requests to a server
#python version 3.9.4, used the socket library, datetime library, and optparse library
#Open an IDLE Shell and run the client after starting the server up
#(instructions for running the server is in its source code)


from socket import *
from datetime import datetime
from optparse import OptionParser

choice = 0

#options for command line parameters, do a -h to get the help statements to appear
parser = OptionParser()
parser.add_option("-p",
                  action = "store", type="int", dest="serverPort", default = 8000,
                  help = "choose port for connection, must be same as on server")
parser.add_option("-i",
                  action = "store", type="str", dest="serverName", default = '127.0.0.1',
                  help = "choose address for connection, (i could only get 127.x.x.x to work)")
parser.add_option("-t",
                  action = "store", type="str", dest="protocolChoice", default = "TCP",
                  help = "choose transmission protocol to use, TCP is default can also choose UDP")

(options, args) = parser.parse_args()

if options.protocolChoice == "UDP":

    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #while loop to print out menu as long as connection is left open
    while choice < 4:
        print ("Client Menu")
        print ("Enter a 1 to return the ip address from the client request")
        print ("Enter a 2 to return the port from the client request")
        print ("Enter a 3 to return the date/time from the client")
        print ("Enter a 4 to close the connection")
        choice = int(input ("Please choose an option: ")) #getting user choice

        if choice == 1: #This option will return the ip address used to make the connection
            message = '1'
            clientSocket.sendto(message.encode(),(options.serverName,options.serverPort)) #sending message to the server

            modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #recieving message from the server
            modifiedMessage.decode() #decoding message which is the ip address
            print ("The client ip is: ", modifiedMessage)

        elif choice == 2: #This option will return the port used to make the connection
            message = '2'
            clientSocket.sendto(message.encode(),(options.serverName,options.serverPort)) #sending message to the server

            modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #recieving message from the server
            modifiedMessage.decode() #decoding message which is the port used by client to connect to the server
            print ("The client port is: ", modifiedMessage)

        elif choice == 3: #This option will calculate and return the time delay between the client and server and the time delay from server to client
            message = datetime.now() #getting client date and time
            message = message.strftime("%Y/%m/%d, %H:%M:%S:%f") #formatting the date and time into a string
            clientSocket.sendto(message.encode(),(options.serverName,options.serverPort)) #sending message to the server

            modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #recieving message from the server
            modifiedMessage = modifiedMessage.decode() #decoding the message
            csTimeDelay, serverDate, serverTime = modifiedMessage.split() #splitting the message into 3 parts and storing those parts in their own variable
            print ("The time delay from client to server is: ", csTimeDelay) #printing the time delay from client to server

            serverDateTime = serverDate + ', ' + serverTime #combining the server date and server time into one string
            serverDateTime = datetime.strptime(serverDateTime, "%Y-%m-%d, %H:%M:%S.%f") #taking that string and turning it into a datetime
            clientTime = datetime.now() #calculating the client date and time
            #serverDateTime = datetime.strftime("%Y/%m/%d, %H:%M:%S:%f")
            scTimeDelay = clientTime - serverDateTime #calculating the time delay from server to client
            print ("The time delay from server to client is: ", scTimeDelay) #printing the time delay from server to client

        elif choice == 4: #this option will close the connection
            clientSocket.close

        else: #this is an error handler to avoid incorrect choice inputs
            print ("Selection not valid")

elif options.protocolChoice == "TCP":
    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((options.serverName,options.serverPort))

    #while loop to print out menu as long as connection is left open
    while choice < 4:
        print ("Client Menu")
        print ("Enter a 1 to return the ip address from the client request")
        print ("Enter a 2 to return the port from the client request")
        print ("Enter a 3 to return the date/time from the client")
        print ("Enter a 4 to close the connection")
        choice = int(input ("Please choose an option: ")) #getting user choice

        if choice == 1: #This option will return the ip address used to make the connection
            message = '1'
            clientSocket.send(message.encode()) #sending message to the server

            modifiedMessage = clientSocket.recv(2048) #recieving message from the server
            modifiedMessage.decode() #decoding message which is the ip address
            print ("The client ip is: ", modifiedMessage)

        elif choice == 2: #This option will return the port used to make the connection
            message = '2'
            clientSocket.send(message.encode()) #sending message to the server

            modifiedMessage = clientSocket.recv(2048) #recieving message from the server
            modifiedMessage.decode() #decoding message which is the port used by client to connect to the server
            print ("The client port is: ", modifiedMessage)

        elif choice == 3: #This option will calculate and return the time delay between the client and server and the time delay from server to client
            message = datetime.now() #getting client date and time
            message = message.strftime("%Y/%m/%d, %H:%M:%S:%f") #formatting the date and time into a string
            clientSocket.send(message.encode()) #sending message to the server

            modifiedMessage = clientSocket.recv(2048) #recieving message from the server
            modifiedMessage = modifiedMessage.decode() #decoding the message
            csTimeDelay, serverDate, serverTime = modifiedMessage.split() #splitting the message into 3 parts and storing those parts in their own variable
            print ("The time delay from client to server is: ", csTimeDelay) #printing the time delay from client to server

            serverDateTime = serverDate + ', ' + serverTime #combining the server date and server time into one string
            serverDateTime = datetime.strptime(serverDateTime, "%Y-%m-%d, %H:%M:%S.%f") #taking that string and turning it into a datetime
            clientTime = datetime.now() #calculating the client date and time
            #serverDateTime = datetime.strftime("%Y/%m/%d, %H:%M:%S:%f")
            scTimeDelay = clientTime - serverDateTime #calculating the time delay from server to client
            print ("The time delay from server to client is: ", scTimeDelay) #printing the time delay from server to client

        elif choice == 4: #this option will close the connection
            clientSocket.close

        else: #this is an error handler to avoid incorrect choice inputs
            print ("Selection not valid")

else:
    print ("Unsupported protocol selected, please choose TCP or UDP")
    
