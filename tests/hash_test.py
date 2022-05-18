import hashlib

# encode string hello to bytes
plaintext = 'hello'.encode()

# call the sha256() function to return a hash object
d = hashlib.sha256(plaintext)

# generate binary hash of 'hello' string
hash_txt = d.digest()
print(hash_txt)