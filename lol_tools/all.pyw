from  tkinter import*

lenh1 = "(1) : Open Auto Click "
lenh2 = "(2) : Open QR Code Genator "
lenh3 = "(3) : Open Spam text message "
lenh4 = "(4) : Open Text Programming "


def lenh1():
    import auto_click
    auto_click()
def lenh2():
    import QR
    QR()
def lenh3():
    import spam_text
    spam_text()
def lenh4():
    import text_programing
    text_programing()            
def lenh5():
    import ma_anh
    ma_anh()


top = Tk()
top.geometry("100x250")


b1 = Button( text = "Auto Click", activeforeground = "gold", command = lenh1, activebackground = "pink", pady = 10)
b2 = Button( text = "Qr Code Genator", activeforeground = "gold", command = lenh2, activebackground = "pink", pady = 10)
b3 = Button( text = "Spam Text", activeforeground = "gold", command = lenh3, activebackground = "pink", pady = 10)
b4 = Button( text = "Text Programming", activeforeground = "gold", command = lenh4, activebackground = "pink", pady = 10)
b5 = Button( text = "ASCII CONVERT", activeforeground = "gold", command = lenh5, activebackground = "pink", pady = 10)
b1.pack(side = TOP )
b2.pack()
b3.pack()
b4.pack()      
b5.pack()
top.mainloop()

