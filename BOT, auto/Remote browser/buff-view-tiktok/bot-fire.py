from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import os, sys
from tkinter import messagebox


# tích hợp proxy
#from selenium.webdriver.common.proxy import Proxy, ProxyType
#proxy_ip_port


os.system("cls")
username = input('Nhập tên tài khoản (NOT ID): ')
#url_img = input('Nhập url thumnail của vid: ')
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
os.system("cls")
# banner with text : BUFF VIEW TIKTOK
driver.set_window_position(-10000,0)
driver.get("https://fireliker.com/")
driver.set_window_size(700, 800)
time.sleep(2)
driver.find_element(By.CLASS_NAME,'form-control').send_keys(username)
print("đang nhập tên vào hệ thống")
time.sleep(2)
driver.find_element(By.CLASS_NAME,'btn').click()

time.sleep(15)
driver.execute_script("window.scrollTo(0, 300)") 
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/a').click()
print("Đang lấy thông tin tài khoản")
time.sleep(2)
driver.set_window_size(1000, 1500)
driver.set_window_position(0,0)
messagebox.showinfo(title="Nhập CAPTCHA ;-;",

			message="Hãy tự nhập captcha nào boss ơi")
input("Nhập CAPTCHA rồi nhấn Enter để tiếp tục")   
time.sleep(5)         
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/fieldset/div/div/a[2]').click()      
time.sleep(15)
driver.find_element(By.CLASS_NAME,'btn-primary').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/form/button').click()
print("Hoàn thành nhiệm vụ")