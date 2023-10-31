import rsa

print("Generating Keys. Please wait...")

public_key, private_key = rsa.newkeys(1024)

with open("generated_key/public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("generated_key/private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))

with open("generated_key/public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("generated_key/private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
    

message = "Key has been successfully generated!"

data = rsa.encrypt(message.encode(), public_key)

clear_message = rsa.decrypt(data, private_key)


print("\n")
print(public_key)
print("\n")
print(private_key)
print("\n")

print("Public key.pem created successfully!")
print("Private key.pem created successfully!")
print("\n")
print(clear_message.decode())
print("Key is located at generated key folder.")
