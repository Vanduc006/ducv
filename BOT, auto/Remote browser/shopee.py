from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.options import Options


import pyautogui as auto
# test lấy tên dn, pass, từ khóa

with open('usr_and_pass.txt') as file:
    i = 1
    for line in file:
        get_username = line.split('|')[0]
        get_password = line.split('|')[1]
        print(get_username)
        print(get_password)

            
    driver = webdriver.Firefox()
    driver.get("https://shopee.vn/")
    driver.set_window_size(700, 800)
    driver.get("https://shopee.vn/buyer/login?next=https%3A%2F%2Fshopee.vn%2F")
    print(driver.title)
    time.sleep(2) 
    # Tìm đến điền thông username/sđt/email
    username = driver.find_element("name", "loginKey")
    username.send_keys(get_username)
    username.send_keys(Keys.RETURN)
    time.sleep(2)
    # tìm đến điền  password
    password = driver.find_element("name", "password")
    password.send_keys(get_password)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    # ấn nút đăng nhập
    print('ấn ô dn')  
    # ấn ô tìm kiếm
    driver.get("https://shopee.vn/")
    # từ chối thông báo
    time.sleep(5)
    thong_bao = Options()
    thong_bao.add_argument("--disable-notifications") 
    search_product = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input")
    search_product.send_keys("sản phẩm")
    search_product.send_keys(Keys.RETURN)    
    Views = 0
    Hearts = 0
    Followers = 0





