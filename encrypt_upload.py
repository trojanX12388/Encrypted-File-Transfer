import socket
import tqdm
import rsa 

with open("key/private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9999))
server.listen()

client, addr = server.accept()


file_name = client.recv(1024).decode()
print(file_name)
file_size = client.recv(1024).decode(errors='ignore')
print(file_size)

file = open(file_name, "wb")

done = False 

file_bytes = b""

progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))

while not done:
    data = client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes += data
    progress.update(1024)

print(file_bytes)

file.write(rsa.decrypt(file_bytes[:-5], private_key))

file.close()
client.close()
server.close() 

