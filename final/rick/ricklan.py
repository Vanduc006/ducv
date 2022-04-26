from  tkinter import*
import os
import sys

top = Tk("hello")

def open():
	global open

	meme =r"oho.mp4"
	os.startfile(meme)
	
def quit():
	global quit
	sys.exit()

b1 = Button( text = "START", activeforeground = "gold", command = open, activebackground = "pink", pady = 10)
b2 = Button( text = "QUIT", activeforeground = "gold", command = quit, activebackground = "pink", pady = 10)
b1.grid(row=1, column=0, sticky="nwse", ipadx=100,ipady=100)
b2.grid(row=1, column=1, sticky="nwse", ipadx=100,ipady=100)
top.mainloop()