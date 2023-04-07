from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.options import Options
from discord import SyncWebhook
import random
import string

import pyautogui

geckopath = "./geckodriver.exe"
driver = webdriver.Firefox(executable_path=geckopath)
driver.set_window_size(700, 800)

lan = input('>')
lan = int(lan)
for i in range(lan):
    
    
    time.sleep(3)
    driver.get("https://shopxulaohac.vn/client/register")
    letters = string.digits
    so = ( ''.join(random.choice(letters) for i in range(10)) )
    letters2 = string.ascii_uppercase
    chu = ( ''.join(random.choice(letters2) for i in range(10)) )
    fakename = 'spambyvduc'+so+chu 
    fakemail = chu + '@fuckmail.com'
    password = 'diTcuThangNguxxx-666-999-fucku'
    driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(fakename)
    
    driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(fakemail)
    
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)

    driver.find_element(By.XPATH,'//*[@id="repassword"]').send_keys(password)
    
    driver.find_element(By.XPATH,'//*[@id="btnRegister"]').click()
    time.sleep(3)
    with open('troll.txt','a') as f:
        data = f'''
        https://shopxulaohac.vn/client/register
        name:{fakename}
        
        mail:{fakemail}
        pass : diTcuThangNguxxx-666-999-fucku
        -------------------------------------
        '''
        f.write(data)
driver.quit()