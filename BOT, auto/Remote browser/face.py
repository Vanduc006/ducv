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
driver.get("https://facebook.com/login")
driver.set_window_size(700, 800)
driver.find_element("name", "email").send_keys("nguyenvantuan@gmail.com")
driver.find_element("name", "pass").send_keys("khongconchoai1883")
driver.find_element("name", "login").click()
print(driver.title)
time.sleep(2)