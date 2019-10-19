import socket
import sys
import hashlib

s = socket.socket()
print("Socket successfully created.")

port = 12345
s.bind(('', port))
print("Socket binded to " + str(port))

s.listen(5)
print("Socket is listening.")

while True:
	c, addr = s.accept()
	print("Got connection from " + str(addr))
	
	received = open('received', 'wb')

	l = c.recv(1024)
	while l:
		received.write(l)
		l = c.recv(1024)
		print("Receiving file from " + str(addr))

	received.close()
	print("File received.")

	# Hashing file with SHA256
	with open('received', "rb") as f:
		bytes = f.read()

	readable_hash = hashlib.sha256(bytes).hexdigest();
	print("Hash Generated: " + readable_hash)

	c.send(readable_hash)
	c.close()

s.close()