# CSC4350As1
Server and client socket connection

Description:
The client will reach out to the server and ask for specific information determined by the user
The client can get the I.P. Address from the request 
The client can get the Port used to make the connection to the server
The client can get the timedelay from both client to server and server back to client

Instruction for execution and command line flags:
I ran both of these on python version 3.9.4
I opened an IDLE for each of the files and opened them from the IDLE

Command line parameters:
On the server side -t can be used to set the transmission protocol (TCP or UDP), -p can be used to set the port the server listens on, 
and -h will provide help messages
On the client side -t can be used to set the transmission protocol (TCP or UDP) (must be same as server), 
-p can be used to set destination port (must be same as server), -i can be used to set the address (i could only get 127.x.x.x to work),
and -h can be used to get help messages

Notes:
The UDP side works perfectly fine but the TCP side will only allow one request from the client and if another is sent the client hangs
All of the methods still work in TCP but it will only allow one to be asked for
other than that I believe that everything is working as intended
