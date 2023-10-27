import os
import socket
import rsa 

with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))

file_size = os.path.getsize("sample.txt")

with open("sample.txt", "rb") as f:
    data = f.read()

encrypted = rsa.encrypt(data, public_key)

client.send("file.txt".encode('UTF-8'))
client.send(str(file_size).encode('UTF-8'))
client.sendall(encrypted)
client.send(b"<END>")

client.close()
