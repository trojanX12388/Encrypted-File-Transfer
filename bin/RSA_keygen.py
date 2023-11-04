import rsa
from cryptography.fernet import Fernet


print("Generating Keys. Please wait...")

public_key, private_key = rsa.newkeys(1024)

with open("generated_key/public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("generated_key/private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))

with open("generated_key/public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

key = Fernet.generate_key() 
 
with open('generated_key/filekey.key', 'wb') as filekey:
   filekey.write(rsa.encrypt(key,public_key))
