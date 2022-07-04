from tkinter.filedialog import askopenfilename
import pyautogui as auto
import time
import keyboard
import random

chs_text = ["spamer", "bot day", "huhu"]

time.sleep(1)
while True:
    if keyboard.is_pressed('space'):
        print('dừng spam')
        break
           
    auto.write(chs_text[random.randint(0, 2)])
    auto.press('enter')
    auto.press('enter')
    time.sleep(1)
