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

	l = c.recv(32768)
	received.write(l)
	received.close()
	print("File received.")

	# Hashing file with SHA256
	with open('received', "rb") as f:
		bytes = f.read()

	readable_hash = hashlib.sha256(bytes).hexdigest();
	print("Hash Generated: " + readable_hash)

	to_send = open('received', 'rb')
	l = to_send.read(32768)
	c.send(l)

	c.send(str.encode(readable_hash))
	c.close()

s.close()