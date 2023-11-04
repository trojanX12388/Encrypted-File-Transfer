import socket
import tqdm
import sys
import os.path

from Crypto.Cipher import AES

charData = 0
saltData = 0

key = None
nonce = None

if ("--key" in sys.argv):
    key = sys.argv[sys.argv.index("--key") + 1]
    for i in key:
        charData += ord(i)

password = int(charData)
password = '{:032b}'.format(password)

if ("--salt" in sys.argv):
    nonce = sys.argv[sys.argv.index("--salt") + 1]
    for j in nonce:
        saltData += ord(j)

noncekey = int(saltData)
noncekey = '{:032b}'.format(noncekey)

key = b"".join([password.encode('utf-8')])
nonce = b"".join([noncekey.encode('utf-8')])

cipher = AES.new(key, AES.MODE_EAX, nonce)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9999))
server.listen()

client, addr = server.accept()
print("")
print("")
print("Receiving file from server. Please wait while loading...")
print("")
file_name = client.recv(1024).decode()
print(file_name)
file_size = client.recv(1024)

file = open(os.path.dirname(__file__) + '/../received/' + file_name, "wb")

done = False

file_bytes = b""

progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1024, total=int(file_size.decode("UTF-32LE")))

while not done:
    data = client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes += data
    progress.update(1024)

file.write(cipher.decrypt(file_bytes[:-5]))

file.close()
client.close()
server.close() 

print("")
print("")
print("File is successfully Received! Check the file in receive folder...")