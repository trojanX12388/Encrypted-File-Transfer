import os
import socket
import sys

from Crypto.Cipher import AES

charData = 0
saltData = 0

key = None
nonce = None

if("--key" in  sys.argv):
    key = sys.argv[sys.argv.index("--key") + 1]  
    for i in key:
        charData += ord(i)  
            
password = int(charData)
password = '{:032b}'.format(password)

if("--salt" in  sys.argv):
    nonce = sys.argv[sys.argv.index("--salt") + 1]  
    for j in nonce:
        saltData += ord(j)  
            
noncekey = int(saltData)
noncekey = '{:032b}'.format(noncekey)


key = b"".join([password.encode('utf-8')])
nonce = b"".join([noncekey.encode('utf-8')])


cipher = AES.new(key, AES.MODE_EAX, nonce)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))

file = None

if("--file" in  sys.argv):
    file = sys.argv[sys.argv.index("--file") + 1]  


file_size = os.path.getsize("file/"+file)


with open("file/"+file, "rb") as f:
    data = f.read()

if("--filename" in  sys.argv):
    filename = sys.argv[sys.argv.index("--filename") + 1]  

encrypted = cipher.encrypt(data)

client.send((""+filename).encode())
client.send(bytes(str(file_size),"UTF-32LE"))
client.sendall(encrypted)
client.send(b"<END>")

client.close()

print("File is successfully sent!")

