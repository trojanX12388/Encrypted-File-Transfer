import socket
import tqdm
import os.path


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

file.write(file_bytes[:-5])

file.close()
client.close()
server.close() 

print("")
print("")
print("File is successfully Received! Check the file in receive folder...")