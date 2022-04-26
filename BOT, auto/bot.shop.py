from re import search
from statistics import quantiles
import pyttsx3 
import datetime 
from datetime import date
import speech_recognition as sr
import webbrowser as wb
from tkinter import messagebox
import os
import sys
from colorama import Fore, Back, Style
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
#BẮT ĐẦU
messagebox.showinfo(title="Start",
			message="Bot made by DUC :D")
# set tiếng cho bot
bot = pyttsx3.init()
voice = bot.getProperty('voices')
# id : 0 là trai, 1 là gái
bot.setProperty('voice',voice[1].id)
# nhập tên người dùng
def ten():
    global Ten
    Ten = input("Nhập tên của ban :")
    
ten()
# Hàm này phát tiếng cho bot(kiến cho bot nói dc)
def speak(audio):
    global speak
    print("DUC.BOT :" + audio)
    bot.say(audio)
    bot.runAndWait()
# hàm lấy thời gian    
def time():
    global Time
    Time = datetime.datetime.now().strftime("%I: %M: %p:")
time()  
#hàm lấy thời gian để chào theo h hiện tại
def welcom() :
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12 :
        speak(f"Good morning {Ten}")
    elif hour >= 12 and hour < 18 :
        speak(f"Good afternoon {Ten}")     
    elif hour >= 18 and hour < 21 :
        speak(f"Good evening {Ten}")     
    elif hour >= 21 and hour < 24 :
        speak(f"Good night {Ten}")
    # hỏi lệnh người dùng    
    speak(f"How I can help you {Ten}")  
    print(f"Tôi có thể giúp gì cho bạn nào {Ten}")


#  Hàm lệnh    
def lenh():
    global query
    
    try :
        # Chỗ nhập lệnh
        query = input("Lệnh của bạn là :").strip() 
        
        
    except sr.UnknownValueError :
        # nếu nhập lệnh sai, hoặc ko đúng các thứ
        print (f"{Ten} please repeat or typing the command (Hãy nói lại hoặc ghi lệnh * tiếng anh* )  ")  
        
    return query
     


welcom()     
# Vòng lặp hỏi
while True :
    query = lenh().lower()
    if 'google' in query :
        speak (f"What should I search {Ten} ?")
        print (f"Tôi lên tìmm kiếm gì {Ten} ?")
        search = lenh().lower()
        url = f'https://www.google.com/search?q={search}'
        wb.get().open(url)
        speak(f"Here is your  {search} on web")
    elif "youtube" in query:
            speak(f"What should I search {Ten}")
            print(f"Bạn muốn xem gì {Ten} ?")
            search = lenh().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')    
    elif 'đóng' in query :
        speak(f"Goodbye {Ten}")
        print(f"Tạm biệt nhé {Ten} ")
        raise SystemExit(0)    
         
    elif 'mấy giờ' in query :
        speak(Time)    
    elif 'hôm nay là sinh nhật tôi'   in query:
        speak(f"Happy birthday {Ten}!!")
        print(f"Bài hát này dành cho bạn <3")
        search = lenh().lower()
        url = f"https://www.youtube.com/watch?v=Wu8NeFXaoOc&ab_channel=Phan%C4%90inhT%C3%B9ng?q{search}"
        wb.get().open(url)

    elif 'app' in query:
        app = input("APP bạn muốn mở là :").strip() 
        if 'google' in app:
            speak('starting google')        #dòng này có cũng được không có cũng không sao :v
            os.startfile('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
               
    # các th còn lại    
    else :
        speak(f"Please try again with new command")
        print(Back.GREEN +  'Hãy nhập lại với một lênh mới MR.THU', file=stream )   
        print(Style.RESET_ALL, file=stream)
        
         


