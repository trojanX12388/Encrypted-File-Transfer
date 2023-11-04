import os
import socket
import sys
import tqdm


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

encrypted = data

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



