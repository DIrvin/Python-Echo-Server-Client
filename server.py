import socket

#host port name set to ‘’ to make it simpler to run with whatever host we use
host = ''
# port number
port = 50000
size = 1024
x = 1

#create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the current host name and port number designated
s.bind((host,port))
#keep a backlog of five connection
s.listen(1)

while x == 1:
   client, address = s.accept()
   data = client.recv(size)

   # if the client sends quit we end the loop 
   if data == 'quit':
       x = 0

   # else we return the user input uppercase
   elif data:
       client.send(data.upper())
   client.close()

# Confirm Server Closing
print 'Quit'
