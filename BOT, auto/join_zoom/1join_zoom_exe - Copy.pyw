from  tkinter import*


from join_zoom import lenh1,lenh2,lenh3,lenh4,lenh5,lenh6,lenh7,lenh8,lenh9,lenh10,lenh11,lenh12,lenh13,lenh14,lenh15,lenh16,lenh17,lenh18,lenh19,lenh20,lenh21,lenh22,lenh23,lenh24,lenh25
top = Tk("join.zom- by vduc")
top.title("JOIN ZOOM -- BY VDUC")


# nút học chính
b1 = Button( text = "ID_TOÁN", activeforeground = "gold", command = lenh1, activebackground = "pink", pady = 10)
b2 = Button( text = "ID_VĂN", activeforeground = "gold", command = lenh2, activebackground = "pink", pady = 10)
b3 = Button( text = "ID_ANH", activeforeground = "gold", command = lenh3, activebackground = "pink", pady = 10)
b4 = Button( text = "ID_SỬ", activeforeground = "gold", command = lenh4, activebackground = "pink", pady = 10)
b5 = Button( text = "ID_ĐỊA", activeforeground = "gold", command = lenh5, activebackground = "pink", pady = 10)
b6 = Button( text = "ID_TIN", activeforeground = "gold", command = lenh6, activebackground = "pink", pady = 10)
b7 = Button( text = "ID_SINH", activeforeground = "gold", command = lenh7, activebackground = "pink", pady = 10)
b8 = Button( text = "ID_CÔNG NGHỆ", activeforeground = "gold", command = lenh8, activebackground = "pink", pady = 10)
b9 = Button( text = "ID_HÓA", activeforeground = "gold", command = lenh9, activebackground = "pink", pady = 10)
b10 = Button( text = "ID_VẬT LÝ", activeforeground = "gold", command = lenh10, activebackground = "pink", pady = 10)
b11 = Button( text = "ID_GDCD", activeforeground = "gold", command = lenh11, activebackground = "pink", pady = 10)
b12 = Button( text = "ID_GDQP", activeforeground = "gold", command = lenh12, activebackground = "pink", pady = 10)
b13 = Button( text = "?", activeforeground = "gold", command = lenh13, activebackground = "pink", pady = 10)


#nút học thêm
b14 = Button( text = "HT_ANH", activeforeground = "gold", command = lenh14, activebackground = "pink", pady = 10)
b15 = Button( text = "HÓA", activeforeground = "gold", command = lenh15, activebackground = "pink", pady = 10)
b16 = Button( text = "HT_ANH_NÓI", activeforeground = "gold", command = lenh16, activebackground = "pink", pady = 10)
b17 = Button( text = "TIME", activeforeground = "gold", command = lenh17, activebackground = "pink", pady = 10)

while True:
    b1.grid(row=1, column=0, sticky="nwse", ipadx=10,ipady=10)
    b2.grid(row=1, column=1, sticky="nwse", ipadx=10,ipady=10)
    b3.grid(row=1, column=2, sticky="nwse", ipadx=10,ipady=10)
    b4.grid(row=1, column=3, sticky="nwse", ipadx=10,ipady=10)
    b5.grid(row=1, column=4, sticky="nwse", ipadx=10,ipady=10)
    b6.grid(row=1, column=5, sticky="nwse", ipadx=10,ipady=10)
    b7.grid(row=2, column=0, sticky="nwse", ipadx=10,ipady=10)
    b8.grid(row=2, column=1, sticky="nwse", ipadx=10,ipady=10)
    b9.grid(row=2, column=2, sticky="nwse", ipadx=10,ipady=10)
    b10.grid(row=2, column=3, sticky="nwse", ipadx=10,ipady=10)
    b11.grid(row=2, column=4, sticky="nwse", ipadx=10,ipady=10)
    b12.grid(row=2, column=5, sticky="nwse", ipadx=10,ipady=10)
    b13.grid(row=3, column=1, sticky="nwse", ipadx=10,ipady=10)
    b14.grid(row=3, column=2, sticky="nwse", ipadx=10,ipady=10)
    b15.grid(row=3, column=3, sticky="nwse", ipadx=10,ipady=10)
    b16.grid(row=3, column=4, sticky="nwse", ipadx=10,ipady=10)
    b17.grid(row=3, column=5, sticky="nwse", ipadx=10,ipady=10)

    top.mainloop()

