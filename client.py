import socket               
s = socket.socket()           
port = 8080                 
s.connect(('localhost', port)) 
print ((s.recv(1024)).decode("utf-8")) 
s.close()        

