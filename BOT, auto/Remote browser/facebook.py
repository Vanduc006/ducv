from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.options import Options


import pyautogui as auto
geckopath = "./geckodriver.exe"
driver = webdriver.Firefox(executable_path=geckopath)
driver.get("https://facebook.com/")

print(driver.title)
time.sleep(2)
# Tìm đến điền thông username/sđt/email
username = driver.find_element_by_name("email")
username.send_keys("100030029031374")
username.send_keys(Keys.RETURN)
time.sleep(2)
# tìm đến điền  password
password = driver.find_element_by_name("pass")
password.send_keys("Chaudo12345")
password.send_keys(Keys.RETURN)
time.sleep(2)
# ấn nút đăng nhập