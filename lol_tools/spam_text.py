from tkinter.filedialog import askopenfilename
import pyautogui as auto
import time
import keyboard
text = input("Enter the text you want to spam: ")

time.sleep(1)
while True:
    if keyboard.is_pressed('space'):
        print('dừng spam')
        break
           
    auto.write(text)
    auto.press('enter')
    time.sleep(0.1)
