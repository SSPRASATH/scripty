from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding

with open("private.key", 'rb') as pkey:
  private_key = serialization.load_pem_private_key(pkey.read(), password=None, backend=default_backend())

with open('flag.enc', 'rb') as encrypted_file:
  ciphertext = encrypted_file.read()

plaintext = private_key.decrypt(ciphertext, padding.PKCS1v15())
print plaintext