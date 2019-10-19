import socket

s = socket.socket()

port = 12345

s.connect(('127.0.0.1', port))

filename = input("Enter filename: ")

to_send = open(filename, 'rb')
l = to_send.read(32768)
s.send(l)

received = open('return_file', 'wb')
l = s.recv(32768)
received.write(l)
received.close()

generated_hash = s.recv(32768).decode("utf-8")
print("Hash: " + generated_hash) 
print("The file sent by the server has been stored as \"return_file\"")

s.close()