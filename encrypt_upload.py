import sys
import tqdm
import os
import rsa

from cryptography.fernet import Fernet

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1Z3t-FckIlQUTT-KnYsDVbveZQqduc1of'

with open("generated_key/private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

with open("generated_key/filekey.key", "rb") as f:
    enckey = f.read()

key = rsa.decrypt(enckey,private_key)

# using the generated key
fernet = Fernet(key)


if("--file" in  sys.argv):
    file = sys.argv[sys.argv.index("--file") + 1] 


if("--filename" in  sys.argv):
    filename = sys.argv[sys.argv.index("--filename") + 1] 
    

with open("file/"+file, "rb") as f:
    data = f.read()

file_size = os.path.getsize("file/"+file)

print("Total Data Size:")
print(str(file_size)+"-bytes")
print("\n")
print("Encrypting Data using filekey:")

with tqdm.tqdm(total=file_size) as progress:
    for chunk in data:
        progress.update(chunk)
    encrypted = fernet.encrypt(data)       
      
with open("encrypted/enc.crypt", "wb") as f:
    f.write(encrypted)

file_upload = "encrypted/enc.crypt"
print("\n")
print("Preparing encrypted file to upload...")

file1 = drive.CreateFile(metadata={
    "title": ""+filename+".crypt",
    "parents": [{"id": folder}],
    "mimeType":"txt/crypt"
})
print("uploading...")
file1.SetContentFile(file_upload)
file1.Upload()
print("\n")
print("Finished!")


