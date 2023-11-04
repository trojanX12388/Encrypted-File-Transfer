import os
import socket
import sys
import tqdm
import os.path

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


file_size = os.path.getsize(os.path.dirname(__file__) + '/../file/'+file)


with open(os.path.dirname(__file__) + '/../file/'+file, "rb") as f:
    data = f.read()

if("--filename" in  sys.argv):
    filename = sys.argv[sys.argv.index("--filename") + 1]  

encrypted = cipher.encrypt(data)

client.send((""+filename).encode())
client.send(bytes(str(file_size),"UTF-32LE"))

print("filename:"+filename)
print("filesize (in bytes):"+str(file_size))

progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1024, total=int(file_size))

for i in range(file_size):
    progress.update(1)
progress.close()

client.sendall(encrypted)

client.send(b"<END>")
client.close()

print("\n")
print("File is successfully sent!")

