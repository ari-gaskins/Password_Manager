# I learned that password hashing is used primarily for password verification, 
# it is not for storing and taking out the same password because it is a one-way function
import hashlib

# encode string hello to bytes
plaintext = 'hello'.encode()

# call the sha256() function to return a hash object
d = hashlib.sha256(plaintext)

# generate binary hash of 'hello' string
hash_txt = d.digest()
print(hash_txt)

# generate human readable hash of hello string
hash_txt = d.hexdigest()
print(hash_txt)