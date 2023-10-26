import os
import socket

from Crypto.Cipher import AES

key = b"67890451298123451232123212321Key"
nonce = b"67890451298123451232123212321Nce"

cipher = AES.new(key, AES.MODE_EAX, nonce)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))

file_size = os.path.getsize("sample.mp4")

with open("sample.mp4", "rb") as f:
    data = f.read()
    
encrypted = cipher.encrypt(data)

client.send("file.mp4".encode('UTF-8'))
client.send(str(file_size).encode('UTF-8'))
client.sendall(encrypted)
client.send(b"<END>")

client.close()
