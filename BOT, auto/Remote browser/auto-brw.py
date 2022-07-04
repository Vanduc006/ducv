import sys
from colorama import Fore, Back, Style
from colorama import init, AnsiToWin32
import hashlib
import platform
import random
import string
import time
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream


print("BOt made by DUC :D, pls don't copy oke")
key_pass = input("Nhập key :")
if 'boductuyetvoi' in key_pass:
    print(Fore.RED + 'NHẬP KEY THÀNH CÔNG NHA', file=stream)
    print(Style.RESET_ALL, file=stream) #reset color
else :
    print(Fore.RED + 'NHẬP KEY THẤT BẠI!!!', file=stream)
    print(Fore.GREEN + 'ĐI HỎI BỐ ĐỨC ĐỂ CÓ KEY NGHE CHƯA -.-', file=stream)
    sys.exit()

type_url = input("""Nhập url của bạn
                    Ví Dụ: https://w3theband.ga/

                    URL:""")
ques = input("chạy ko?(y/n):")
print(Fore.YELLOW + """Chọn Trình Duyệt 
                            |1.Chrome               | 
                            |2.FireFox              |
                            |3.Edge(developing)     | 
                            |4.IE(developing)       |
                            |5.Opera(developing)    |    """, file=stream)
chosse_brw = input(" Bạn Muốn Chạy Trên Trình Duyệt Nào *số thứ tự* :")
                                  # chọn trình duyệt

if '1' in chosse_brw:
    print(Fore.GREEN + 'Chạy Chrome', file=stream)
    print(Style.RESET_ALL, file=stream) #reset color
    print("Đang chạy Chrome")
    #Dành cho trình duyệt FireFox

    while True:
            if 'y' in ques:
                print("1")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("3")
                time.sleep(1)
                print("Đã Tạo BOT.")
                time.sleep(1)
                print("Chạy BOT...")

                chromepath = "./chromedriver.exe"
                driver = webdriver.Chrome(executable_path=chromepath)
                driver.get(type_url)
                time.sleep(5)
                sys.exit()
            elif 'n' in ques:
                print("Hủy nhiêm vụ hoàn tất!!")
                sys.exit()

if '2' in chosse_brw:
    print(Fore.GREEN + 'Chạy FireFox', file=stream)
    print(Style.RESET_ALL, file=stream) #reset color
    print("Đang chạy FireFox")
    #Dành cho trình duyệt FireFox
   
    while True:
            if 'y' in ques:
                print("1")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("3")
                time.sleep(1)
                print("Đã Tạo BOT.")
                time.sleep(1)
                print("Chạy BOT...")

                geckopath = "./geckodriver.exe"
                driver = webdriver.Firefox(executable_path=geckopath)
                driver.get(type_url)
                time.sleep(5)
                kill_task = r"kill.bat"
                os.startfile(kill_task)
                sys.exit()
            elif 'n' in ques:
                print("Hủy nhiêm vụ hoàn tất!!")
                sys.exit()

else:
    print(Fore.RED + 'Trình Duyệt Bạn Chọn Đang Được Phát Triển', file=stream)
    print(Style.RESET_ALL, file=stream)

    











        

            
        


