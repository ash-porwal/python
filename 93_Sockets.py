'''
As we know for different connection we have different security ports - 22, 21, 80, 443 etc

so using socket library in python we can talk to those ports.
Python has built-in support for TCP sockets
'''
import socket

#in socket library we are calling the socket function
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('data.pr4e.org', 80)) #here we passing ("host", Port)

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.clsoe()

'''     http://www.abc.com/pagel.html  
        here http:// is protocol 
        and www.abc.com is host
        pagel.html is document

'''