# import socket programming library 
import socket 
  
# import thread module 
from _thread import *
import threading 
import sys
  
print_lock = threading.Lock() 

#UserClass that stores the username and timeline for user
class User(object):
    name = ""
    address = ""
    port = 0
    timeLine = []
    # The class "constructor" - It's actually an initializer 
    def __init__(self, name,address, port):
        self.name = name
        self.address = address
        self.port = port
  
# Global userName Dictionary #
userData = {}
users =[]

def addTweetToUsersTimeLine(userName, tweet):
    for u in users:
        print("Users " + u.name)
        if(u.name != userName):
            u.timeLine.append("-"+ u.name + " from " + userName + ": \""  + tweet + "\"\n")


# thread fuction that handles all the client calls
def threaded(c,addr): 

   #receive data from client
   data = c.recv(1024) 
   userName = data.decode('ascii')

   #if username provided by user already exists in dictionary, notify user
   if(userName in userData):
      c.send("-Username already exists".encode('ascii'))
      return
   else:
      userData[userName] = str(addr[0]) + ":" + str(addr[1])
      user = User(userName, str(addr[0]), addr[1])
      users.append(user)
      c.send("-username legal, connection established".encode('ascii')) 

   while True:
      # Wait for further request from Client
      data = c.recv(1024)
      #if there is no more calls from client break out of the loop
      if not data:
         break  
      
      command = data.decode('ascii')
      #split the data to get what command the client has sent
      tokens = command.split(" ")

      #if user sends exit command, remove user data from dictionary and exit the client
      if(tokens[0] == "exit"):
         bye = "-Bye Bye"
         c.send(bye.encode('ascii'))
         break

      #if user sends tweet command, add the tweet to dictionary after removing double quotes from text
      #and check that tweet is less than 150 characters
      if(tokens[0] == "tweet"):
         tweet = ''.join([str(elem) for elem in tokens[1:]])
         tweet = tweet[1:-1]
         if(len(tweet) <= 150):
            addTweetToUsersTimeLine(userName, tweet)
            #print(userName + " " + tweet)
         else:
            c.send("-tweet is too long. Please keep the tweet below 150 characters".encode('ascii'))


      #if user sends timeline command, display unread messages from the inbox
      if(tokens[0] == "timeline"):
         if not user.timeLine:
            timeLineData = "-No new message"
         else:
            timeLineData = ''.join([str(elem) for elem in user.timeLine])
         print("Sending TimeLine Data to " + userName)
         c.send(timeLineData.encode('ascii'))
         user.timeLine.clear()

   c.close() 
  
  
def Main(): 
    host = "" 
  
    # port number for server
    port = int(sys.argv[1])

    #create socket and bind it with host and port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 

    # put the socket into listening mode 
    s.listen(5)
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
   
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread for each client and pass client details as agrument to threaded function
        start_new_thread(threaded, (c,addr)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 