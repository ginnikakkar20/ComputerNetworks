# Computer Networks Trivial Twitter (Socket Programming Assignment)

## Name: Ginni Kakkar                      GTID: 903540294

## Server Implementation
1. The server takes a port as an argument and creates a socket
2. Server listens for any client requests using listen() function
3. As soon as server gets a client connection request, it creates a new thread for the client and sends the client details to a function "threaded". Server creates a separate thread to handle each client
4. The threaded function receives data/command from client using recv() function
5. The server checks whether the username sent by the client is already present in dicitonary or not. If it already exists, it notifies the client of unavailability of username. Else it establishes connection with client and waits for further commands from client
6. When server gets a command from the client, it checks what type of a command it is.
  - If it is a "tweet" command, the string in double quotes entered by the client is stored in other users' dictionary along       with client's username. Server first checks that the tweet is 150 characters long. If it is longer, it notifies user and       doesn't store it. If it is less than 150 characters, it stores the tweet in dicitionary
  - If it is a "timeline" command, the server displays all unread tweets from the inbox and deletes them from the dicitonary so     that they are no longer present in inbox. If there are no unread messages in inbox, it notifies the user of the same.
  - If it is an "exit" command, server deletes user from dictionary and deletes all user data and ends client connection after     displaying the message "Bye Bye"
  - If it receives any command other than the above three, it ignores it


## Client Implementation

1. Client takes hostname (127.0.0.1 for localhost), port and username as agruments
2. Client checks if the username is valid i.e. it has only alphabets and digits and is less than 64 characters in length.
  - If username is valid, it creates a socket, connects to the server and send the username to the server
  - If username isn't valid, it notifies the user
3. Then it waits for server to respond - whether username is already taken or if connection is established with given username
4. Once connection is established, client asks for user to input commands
5. It checks user input for the following:
  - If user enters "tweet" command, it sends this command to the server
  - If user enters "timeline" command, it sends this command to server and waits for server response to display unread messages from inbox
  - If user enters "exit" command, send this command to the server and display "Bye Bye" message for the user
  - If user enters any other command, notify user that command not found
 6. Client closes the connection with server with exit command. Till then it keeps waiting for user input
