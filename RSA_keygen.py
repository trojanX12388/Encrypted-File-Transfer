import rsa

public_key, private_key = rsa.newkeys(1024)

with open("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))
    
message = "HELLO WORDL!"

encrypted_message = rsa.encrypt(message.encode(), public_key)

clear_message = rsa.decrypt(encrypted_message, private_key)

print(clear_message.decode())


