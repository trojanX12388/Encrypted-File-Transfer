import os
import socket
import rsa 
from time import sleep

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
drive = GoogleDrive(gauth)


with open("key/public.pem", "rb") as f:
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


folder = '1Z3t-FckIlQUTT-KnYsDVbveZQqduc1of'


with open("sample.txt", "rb") as f:
    data = f.read()

file = "encrypted.crypt"

file1 = drive.CreateFile(metadata={
    "title": file,
    "parents": [{"id": folder}],
    "mimeType":"txt/crypt"
})


file1.SetContentFile(file)
file1.Upload()

sleep(5)   

os.remove(file)
