import qrcode
from tkinter import messagebox
messagebox.showinfo(title="ON",
			message="CODE BY DUC")
img = qrcode.make(input("NHẬP ĐƯỜNG LINK CỦA BẠN :"))
img.save('myQRcode.png')
img. show()