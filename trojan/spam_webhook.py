'''from discord import SyncWebhook
import requests
def spam():
    URL = "https://picsum.photos/500/500/?random"
    response = requests.get(URL)
    open("img.jpeg", "wb").write(response.content)
    # URL của Webhook Discord
    url = "https://discord.com/api/webhooks/1091569895906476043/k5xe52BTH07v1PgPizsAggkQx_9y0BSGUQLZD4l8EKXmnTIjTGHi-hPyKwMahyQLh515"

    # Đường dẫn đến tệp đính kèm
    file_path = "img.jpeg"

    # Mở tệp đính kèm và đọc dữ liệu
    with open(file_path, "rb") as f:
        file_data = f.read()

    # Tạo payload gửi cho Webhook Discord
    payload = {
        
        "file": ("img.jpeg", file_data, "image/jpeg")
    }

    # Gửi yêu cầu POST với payload
    response = requests.post(url, files=payload)

n = 0
while True:
    spam()   
    n = n + 1
    print(n,'súc sét' ) '''
'''
import requests
from PIL import Image
import io
import pyperclip
import pyautogui
import time

URL = "https://picsum.photos/500/500/?random"
response = requests.get(URL)
open("img.png", "wb").write(response.content)
# URL của Webhook Discord
url = "https://discord.com/api/webhooks/1091569895906476043/k5xe52BTH07v1PgPizsAggkQx_9y0BSGUQLZD4l8EKXmnTIjTGHi-hPyKwMahyQLh515"
# Đường dẫn đến tệp đính kèm
file_path = "img.png"
# Mở tệp ảnh và đọc dữ liệu
with open(file_path, "rb") as f:
    image_data = f.read()

# Tạo đối tượng Image từ dữ liệu ảnh
image = Image.open(io.BytesIO(image_data))

# Sao chép ảnh vào clipboard
pyperclip.copy(image)

time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')'''

import base64
en = ''
de = 'hello'
decoded_str = base64.b64decode(en).decode('utf-8')


print(decoded_str)
print(encode)  # Output: "laster is a base64 string"