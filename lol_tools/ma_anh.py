from PIL import Image
import tkinter as tk 
from tkinter import filedialog
from tkinter import messagebox
import sys
from asyncore import read, write,close_all
import os


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename() # askopenfilename  chính là hỏi chọn file dố=))
def quit():
	global quit
	sys.exit()

# mở file trong ter
pict = Image.open(file_path)
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

# ghi lại với file txt
with open('ascii_pic.txt', 'w') as file:
    file.write(ascii_picture)
anh_ascii =r"ascii_pic.txt"
os.startfile(anh_ascii)
#xong
messagebox.showinfo(title="FINISH",
			message="ĐÃ MÃ HÓA XONG ẢNH SANG ASCII")    

sys.exit()            
#open_file = open('ascii_pic.txt', 'r', encoding='utf-8')
#with open('ascii_pic.txt', 'r') as open_file:
#    data = open_file.read()
#    print(data) 

