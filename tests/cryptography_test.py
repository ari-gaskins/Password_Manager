from cryptography.fernet import Fernet

# encode string to bytes
plaintext = 'password'.encode()

# key generation 
key = Fernet.generate_key()
print(f'This is the key: {key}')

# create fernet object
f = Fernet(key)

# encrypt plaintext using key
encrypted = f.encrypt(plaintext)
print(f'This is the encrypted plaintext: {encrypted}')

# decrypt encrypted text
decrypted = f.decrypt(encrypted)
# decode method changes from bytes to string
print(f'This is the decrypted encrypted text: {decrypted.decode()}')





# string the key in a file
#with open('filekey.key', 'x') as filekey:
#    filekey.write(key)
                

