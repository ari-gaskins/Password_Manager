from cryptography.fernet import Fernet

# encode string to bytes
plaintext = 'password'.encode()

# key generation 
key = Fernet.generate_key()

# create fernet object
f = Fernet(key)

# encrypt plaintext using key
encrypted = f.encrypt(plaintext)
print(encrypted)

# decrypt encrypted text
decrypted = f.decrypt(encrypted)
print(decrypted)





# string the key in a file
#with open('filekey.key', 'x') as filekey:
#    filekey.write(key)
                

