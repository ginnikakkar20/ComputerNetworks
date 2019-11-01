# Import socket module 
import socket 
import sys
import re
  
def Main(): 
    # local host IP '127.0.0.1' 
    host = sys.argv[1]

    # Define the port on which you want to connect 
    port = int(sys.argv[2])

    # UserName provided by client
    userName = sys.argv[3]

    #regular expression to check if username contains any special characters
    reg = re.compile('^[a-z0-9]+$')

    if( reg.match(userName) != None and len(userName) <= 64):
        # create a socket
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        # connect to server on local computer 
        s.connect((host,port)) 
    
        # username sent to server 
        s.send(userName.encode('ascii')) 

        # message received from server  on whether username existing or not
        data = s.recv(1024) 

        # display whether username available or not to the user
        print(str(data.decode('ascii'))) 
    
        while True:
            #  client will enter command tweet or timeline or exit 
            command = input(">")
            tokens = command.split(" ")

            # if "tweet" command, just send command to server
            if(tokens[0] == "tweet"):
                s.send(command.encode('ascii'))
            
            # if "timeline" command, send command and wait for server to respond with unread messages in inbox
            elif(tokens[0] == "timeline"):
                s.send(command.encode('ascii'))
                timeLineData = s.recv(1024)
                print(str(timeLineData.decode('ascii')))
            
            # if "exit" command, send command to server and display message for user
            elif(tokens[0] == "exit"):
                s.send(command.encode('ascii'))
                print("-Bye Bye")
                break
            
            # if any other command, notify user that command not found
            else:
                print('-Command not found')
                


        # close the connection 
        s.close() 
    else:
        print("Username is not valid. Please ensure that username can only have upper case alphabet, lower case alphabet or numbers and should be less than 64 characters")

if __name__ == '__main__': 
    Main() 
