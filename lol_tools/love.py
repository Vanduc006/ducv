"""""import tkinter as tk

text = '''Chúng ta luôn đắng cay vào cuối ngày
Chúng ta luôn đớn đau từng giây phút
Nếu em không giữ lấy niềm vui này
Thì trái tim em có bao giờ day dứt
(Giống như anh)
Anh không quan tâm ta đã có bao nhiêu niềm đau
Anh không quan tâm trên đời có phép nhiệm màu
Anh chỉ muốn biết ta đang có làm phiền nhau
Khi chìm sâu lâu thật lâu ở tận đâu trong mắt em
Ta chỉ nhìn nhau khi câu hát cuối dài hơn
Vì cơn đau của ta nhiều như cát dưới đại dương
Em không cần nghe những thứ triết học đại cương
Vì vài chương câu chuyện cũ ta đều không muốn nhắc thêm
Strongbow rep vẫn có trong tay'''

lines  = text.split('\n')
for i in lines:
        window = tk.Tk()
        button = tk.Button(window, text=f"{i}", font=("Arial", 24))
        window.geometry("+100+100")
        window.after(1000, window.destroy)
        button.pack()
        window.mainloop()"""
import pyglet,time,os
import tkinter as tk
import webbrowser

text = '''Chúng ta luôn đắng cay vào cuối ngày
Chúng ta luôn đớn đau từng giây phút
Nếu em không giữ lấy niềm vui này
Thì trái tim em có bao giờ day dứt
(Giống như anh)'''
# Tải tệp nhạc và lời
lines  = text.split('\n')

#os.system('py love_play.py')
for i in lines:
    window = tk.Tk()
    window.title('<3')
    button = tk.Button(window, text=f"{i}", font=("Arial", 18))
    window.geometry("+100+100")
    
    button.pack()
    window.mainloop()
webbrowser.open('https://ducvan.tk/cmsn.html')    
    



# Phát nhạc và hiển thị lời


