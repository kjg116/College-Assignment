# UDP-Client-Server

Class project using UDP sockets to transmit data from one host to another host. Host A reads a file and sends a 4-bit packet to Host B. Host B capitalizes the recieved information and sends a packet containing the capitalized letters to Host A. This transaction continues until the end of the file. 


To run the program you will need two terminals. One terminal will run client.java and the other will run server.java. 

Terminal command arguments for client.java: [hostname, portnumber, filename]

Terminal command arguments for server.java: [portnumber]
