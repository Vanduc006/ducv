from ast import Load
from PIL import Image
import PIL.Image
import tkinter as tk 
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
import sys


import os

class Ma_Anh:
	def __init__(self, window ):
			window.title('Ascii Converter'); window.resizable()
			global Load
			Load = Button(window, activeforeground = "blue", activebackground = "green", text = 'Convert IMG',  width = 5, font = ('Arial', 10), command = self.openfile_and_convert)
			Play = Button(window, activeforeground = "blue", activebackground = "green", text = 'Read File',  width = 5,font = ('Arial', 10), command = self.open_file_convert)
			Load.grid(row=1, column=0, sticky="nwse", ipadx=30,ipady=30)
			Play.grid(row=1, column=2, sticky="nwse", ipadx=30,ipady=30)
			
	def quit():
		global quit
		sys.exit()
	def openfile_and_convert(self):
		file_path = filedialog.askopenfilename() # askopenfilename  chính là hỏi chọn file dố=))
		# mở file trong ter
		pict = PIL.Image.open(file_path)
		height, width = pict.size
		aspect_ratio = height/width
		# set kích tước mới
		new_width = 240
		new_height = aspect_ratio * new_width*0.5
		pict = pict.resize((new_width, int(new_height)))
		pict = pict.convert('L')
		pixels = pict.getdata()
		# mã hóa ảnh thnahf các kí tự đặc biệt
		chars = ["i", "o", "#", "%", "!", "-", ":", ":", "&", "*", "i"]
		new_pixels = [chars[pixel//25] for pixel in pixels]
		new_pixels = ''.join(new_pixels)
		new_pixels_count = len(new_pixels)
		ascii_picture = [new_pixels[index:index+new_width]
						 for index in range(0, new_pixels_count, new_width)]
		ascii_picture = "\n".join(ascii_picture)
		global add_txt
		name_file = simpledialog.askstring("Input File Name", "Enter file Name...",parent=root)
		add_txt = name_file + '.txt'
		Load = Button(text = 'Xong')
	
		# ghi lại với file txt
		with open(add_txt, 'w') as file:
				file.write(ascii_picture)
				file.close()
				
		
	def open_file_convert(self):		 
		os.startfile(add_txt)
				


#xong
#messagebox.showinfo(title="FINISH",
#			message="ĐÃ MÃ HÓA XONG ẢNH SANG ASCII")    

#sys.exit()            
#open_file = open('ascii_pic.txt', 'r', encoding='utf-8')
#with open('ascii_pic.txt', 'r') as open_file:
#    data = open_file.read()
#    print(data) 

root = Tk()
app= Ma_Anh(root)
root.mainloop()