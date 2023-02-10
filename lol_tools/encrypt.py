from cryptography.fernet import Fernet
import base64
import tkinter as tk 
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
import os
from cryptography.fernet import Fernet
import hashlib
import datetime


current_date = datetime.datetime.now()
ngay = current_date.strftime("%Y-%m-%d")
directory = "ma hoa - " + ngay
directory = str(directory)

if not os.path.exists(directory):
    os.makedirs(directory)
methods = input('simple or base64 ')

#def ma_hoa_thuong():
if methods == '1':
    file_path_thuong_en = filedialog.askopenfilename()
    file_name_thuong_en = os.path.basename(file_path_thuong_en)
    with open(file_path_thuong_en,"rb") as f:
        original_data = f.read()

    encoded_data = base64.b64encode(original_data)

    with open(os.path.join(directory,file_name_thuong_en), "wb") as f:
        f.write(encoded_data)
#def giai_ma_thuong():
if methods == '2':
    file_path_thuong_de = filedialog.askopenfilename()       
    with open(file_path_thuong_de, "rb") as f:
        encoded_data = f.read()

    decoded_data = base64.b64decode(encoded_data)

    with open(file_path_thuong_de, "wb") as f:
        f.write(decoded_data)      
if methods == '3':
    file_path_pass_en = filedialog.askopenfilename()   
    file_name_pass_en = os.path.basename(file_path_pass_en)

    pass_1 = input('Đặt mật khẩu :')
    password = f"{pass_1}".encode('utf-8')
    key = hashlib.sha256(password).digest()
    cipher = Fernet(base64.urlsafe_b64encode(key))
    print(key)
    with open(file_path_pass_en, "rb") as f:
        original_data = f.read()
    encrypted_data = cipher.encrypt(original_data)

    with open(os.path.join(directory,file_name_pass_en), "wb") as f:
        f.write(encrypted_data)


if methods == '4':
    file_path_pass_de = filedialog.askopenfilename()  
    pass_2 = input('Nhập mật khẩu :')
    password = f"{pass_2}".encode('utf-8')
    key = hashlib.sha256(password).digest()
    cipher = Fernet(base64.urlsafe_b64encode(key))
    print(key) 
    with open(file_path_pass_de, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = cipher.decrypt(encrypted_data)  
    with open(file_path_pass_de, "wb") as f:
        
        f.write(decrypted_data)
    


'''
note :

làmthêm phần giao diện

chỉ để có pass hoặc ko pass xóa cái mp3 cố định đi

hard work!!!
'''