# CSC4350As2
Server and client socket connection

Description:
The client will reach out to the server and ask for specific information determined by the user
The client can get the I.P. Address from the request 
The client can get the Port used to make the connection to the server
The client can get the timedelay from both client to server and server back to client

The server now sends response codes back with the requested data
It also now logs each request, whether valid or invalid, in a txt file
The logs are formatted as follows: datetime method responseCode (ex. 2022-09-19 15:23:19.792500	PORT	OK)

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

*TCP now handles multiple requests, changed the connection from per client run to per client request
