import socket
import os

s = socket.socket()

port = 12345

filename = input("Enter filename: ")

if os.path.exists(filename):

        s.connect(('127.0.0.1', port))

        length = os.path.getsize(filename)
        s.send(length.to_bytes(4,byteorder='little'))

        to_send = open(filename, 'rb')
        l = to_send.read(length)
        s.send(l)

        received = open('return_file', 'wb')
        l = s.recv(length)
        received.write(l)
        received.close()

        generated_hash = s.recv(32768).decode("utf-8")
        print("Hash: " + generated_hash) 
        print("The file sent by the server has been stored as \"return_file\"")

else:
        print("File Does Not Exist")

s.close()
