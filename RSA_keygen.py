import rsa

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

public_key, private_key = rsa.newkeys(1024)

with open("generated_key/public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("generated_key/private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))


gauth = GoogleAuth()
drive = GoogleDrive(gauth)


folder = '1Z3t-FckIlQUTT-KnYsDVbveZQqduc1of'


file = "encrypted.crypt"

message = "HELLO SAMPLE"

data = rsa.encrypt(message.encode(), public_key)

clear_message = rsa.decrypt(data, private_key)

print(clear_message.decode())


file_list = drive.ListFile({'q': "'%s' in parents and trashed=false"%(folder)}).GetList()

took = False
for file1 in file_list:
  print('Filename: %s , id: %s , Date Created: %s , Size(Bytes): %s ' % (file1['title'] , file1['id'], file1['createdDate'], file1['quotaBytesUsed']))
  file_id = file1['id']


file6 = drive.CreateFile({'id': '1EoBbj6qrvwRj1v4t9PqPc3nFIerNfd7Z'})
file6.GetContentFile('enc.crypt')

