import socket

s = socket.socket()

port = 12345

s.connect(('127.0.0.1', port))

to_send = open('Test.txt', 'rb')
l = to_send.read(1024)
while l:
	s.send(l)
	l = to_send.read(1024)

s.close()