import os
from cryptography.fernet import Fernet
import os
from cryptography.fernet import Fernet
import hashlib
import base64

files = []
for file in os.listdir():
    if file == "ma_hoa_is_dangerous.py" or file =="thekey.key" or file == "giai_virut.py" or file =='clone_gai.py':
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)
pass_2 = input('nhập pass bạn êi:')
password = f"{pass_2}".encode('utf-8')
key = hashlib.sha256(password).digest() 
cipher = Fernet(base64.urlsafe_b64encode(key))
            
for file in files:
    with open(file, "rb") as f:
        encrypted_data = f.read()

        decrypted_data = cipher.decrypt(encrypted_data)  
    with open(file, "wb") as f:
                
        f.write(decrypted_data)
