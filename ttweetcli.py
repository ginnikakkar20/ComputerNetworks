# Import socket module 
import socket 
import sys
import re
  
def Main(): 

    # local host IP '127.0.0.1' 
    host = sys.argv[1]

    # Define the port on which you want to connect 
    port = int(sys.argv[2])

    #UserName 
    userName = sys.argv[3]
    #regular expression to check if username contains any special characters
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 

    if( regex.search(userName) == None and len(userName) <= 64):

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

        # connect to server on given host and port
        s.connect((host,port)) 
    
        # username sent to server
        s.send(userName.encode('ascii')) 

        # message received from server 
        data = s.recv(1024) 

        # print the received message
        print(str(data.decode('ascii'))) 
    
        while True:
            #  client will do tweet or time line or exit
            command = input(">")
            tokens = command.split(" ")
            print(tokens)

            if(tokens[0] == "exit"):
                print("inside exit block client")
                clientData = s.recv(1024)
                print(clientData)
                print(str(clientData.decode('ascii')))
                #break
            
            elif(tokens[0] == "tweet"):
                #print("in Tweet: " + command)
                s.send(command.encode('ascii'))
            
            elif(tokens[0] == "timeline"):
                s.send(command.encode('ascii'))
                #print("Waiting for timeLine Data")
                timeLineData = s.recv(1024)
                print(str(timeLineData.decode('ascii')))
            else:
                print("-Command not found")



        # close the connection 
        s.close() 
    else:
        print("Username is not valid. Please ensure that username can only have upper case alphabet, lower case alphabet or numbers and should be less than 64 characters")

if __name__ == '__main__': 
    Main() 