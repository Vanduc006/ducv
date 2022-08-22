from tkinter.filedialog import askopenfilename
import pyautogui as auto
import time
import keyboard
import random



time.sleep(1)
while True:
    if keyboard.is_pressed('space'):
        print('dừng spam')
        break
           
    auto.write("y")
    auto.press('enter')

    
    auto.press('enter')
    time.sleep(1)
