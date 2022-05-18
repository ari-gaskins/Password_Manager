# import required module from cryptography library
import os
from cryptography.fernet import Fernet

# key generation 
key = Fernet.generate_key()

# string the key in a file
with open('filekey.key', 'x') as filekey:
    filekey.write(key)
                

