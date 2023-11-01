import tqdm
import sys
import os
import rsa

from time import sleep
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


file_list = drive.ListFile({'q': "'%s' in parents and trashed=false"%(folder)}).GetList()

if("--id" in  sys.argv):
    id = sys.argv[sys.argv.index("--id") + 1] 
    
print("\n")
with tqdm.tqdm(total=100, desc="Progress") as process:
        process.update(0)
        print("\n")
        
        print("Retrieving data from cloud...")
        process.update(+5)
        
        file6 = drive.CreateFile({'id': ''+id})
        file_size = int(file6['quotaBytesUsed'])

        with tqdm.tqdm(total=file_size) as progress:
            for i in range(file_size):
                progress.update(1024)
        print("\n")         
        process.update(+30)
        
        file6.GetContentFile('download/dec.crypt')

        with open("download/dec.crypt", "rb") as f:
            enc = f.read()
          
        print("\n")
        print("Decrypting data using file key...")

        with tqdm.tqdm(total=file_size) as progress:
            for chunk in enc:
                progress.update(chunk)
                
            decrypted = fernet.decrypt(enc)
        print("\n") 
        process.update(+42)
        
        with open('download/'+file6['title'][:-6], 'wb') as dec_file:
            dec_file.write(decrypted)
            
        print("\n")  
        print("Deleting cache files...") 
        sleep(0.5) 
       
        print("\nFile is successfully downloaded and decrypted!")
        print("Check your file: download/"+file6['title'][:-6]+" ...")
        print("\n") 
        file = 'dec.crypt'  
        location = "download"
        path = os.path.join(location, file)  
        os.remove(path)
        
        process.update(+23)  
    
        