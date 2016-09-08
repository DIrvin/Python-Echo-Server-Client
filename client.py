import socket

host = 'localhost'
port = 50000
size = 1024
message = ''

# exit loop condition of user input ‘quit’
while message != 'quit':

   # Create a socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  #get user input to send to server side
  message = raw_input("Enter message: ")

  # Connect to the socket made in the server side
  s.connect((host,port))
  # send user input to server and receive in data from the server  
  s.send(message)
  data = s.recv(size)
  # Close socket 
  s.close()
  print 'Received:', data

# confirm client stopping
print 'Quit'
