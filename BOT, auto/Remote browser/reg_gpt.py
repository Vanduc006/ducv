import threading
from selenium import webdriver
import time
import numpy as np
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import requests                
from selenium.webdriver.common.by import By       
import sys    
from datetime import datetime
from datetime import date  
import tkinter as tk 
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *           
def chong_scam():
    url = "https://640c374f94ce1239b0a7ebd5.mockapi.io/api/v1/clm"
    response = requests.get(url)
    res_json = response.json()
    for h in res_json:
        content = h["content"]
    content = str(content)
    if content == '1':
        print('Hola!!!')
    else:
        print('lỗi vui lòng liên hệ tôi !!!')
        sys.exit()


chong_scam()

def lay_mail():
    currentDateAndTime = datetime.now()
    gio1 = currentDateAndTime.hour
    phut1 = currentDateAndTime.minute
    giay1 = currentDateAndTime.second
                                
    #print('domain live:',h.json())                             
    #print('data:',i.json())                                    
    #print('data body',t.json())
    times = int(input('số lượng mail bạn muốn lấy từ 1secmail :'))
    type_domain = input('bạn muốn lấy mail đuổi gì? [Vdu: @dcctb.com] :')
    ten_file_mail = input('Hãy đặt tên cho data trả về :')
    add_txt = ten_file_mail + '.txt'
    tao_files = open(f'{add_txt}','w')
    tao_files.write(f'Start run at {gio1}:{phut1}:{giay1}')
    tao_files.close()

    n = 0
    while True:  
        if n == times:
            print('xong!')
            sys.exit()   
        get_random_mail = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')   
        
        m = get_random_mail.json()
        m = m[0]
        m = str(m)
        if f'{type_domain}' in m:
            n = n + 1
            print('random mail :',m)
            m = str(m)
            tach =  m.split('@')     
            print(tach)     
            name_mail = tach[0]
            domain_mail = tach[1]    
            print('name mail :',name_mail , '|','domain name :',domain_mail)
            
            currentDateAndTime = datetime.now()
            gio = currentDateAndTime.hour
            phut = currentDateAndTime.minute
            giay = currentDateAndTime.second
            ngay = date.today()
            
            
            with open(f'{add_txt}','a') as f:
                data = f'''
[{gio}:{phut}:{giay}]|{m}|{name_mail}|{domain_mail}|
                '''
                f.write(data)    


def haha():
    import requests                                            
    g = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=10')                                
    h = requests.get('https://www.1secmail.com/api/v1/?action=getDomainList')                                             
    i = requests.get('https://www.1secmail.com/api/v1/?action=getMessages&login=e35ac08p7e&domain=qiott.com')             
    t = requests.get('https://www.1secmail.com/api/v1/?action=readMessage&login=e35ac08p7e&domain=qiott.com&id=199081190')
    print('radom maul:',g.json())                              
    print('domain live:',h.json())                             
    print('data:',i.json())                                    
    print('data body',t.json())

        #h = requests.get('https://www.1secmail.com/api/v1/?action=getDomainList')  
    
 
#print(get_data.json())  
#get_content = requests.get('https://www.1secmail.com/api/v1/?action=readMessage&login=e35ac08p7e&domain=qiott.com&id=199081190')

def data_mail():
    mail_path = filedialog.askopenfilename()
    # Mở file văn bản
    with open(mail_path, 'r') as file:
    # Đọc từng dòng
        next(file)
        for line in file:
            # Xử lý từng dòng ở đây
            try:
                tach_in_line = line.split('|')
                username_in_line = tach_in_line[2]
                domain_in_line = tach_in_line[3]
                print(tach_in_line)
                print(username_in_line,'|',domain_in_line)
                login_mail = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={username_in_line}&domain={domain_in_line}')
                print(login_mail.json())
                log_json = login_mail.json()
                for message in log_json:
                    message_id = message["id"]
                    if message_id == '[]':
                        print('mail này chưa có bất kì tin nhắn nào gửi đến!!')
                    else:    
                        get_data = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={username_in_line}&domain={domain_in_line}&id={message_id}')   
                        print(get_data.json()) 
                        def rm():
                            Options =  webdriver.ChromeOptions()
                            Options.add_argument('--app=https://chat.openai.com/')
                            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=Options) 
                            driver.implicitly_wait(5)
                            driver.get(f'https://www.1secmail.com/mailbox/?action=readMessageFull&id={message_id}&login={username_in_line}&domain={domain_in_line}')
                        try:
                            rm()    
                        except:
                            print('huhu lũi rùi:< đây có thể lỗi tui chưa phát hiện ra, ib tui luôn nha<3')    
            except:
                print('xong')
    

def test2():
    get_data = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login=nguyenduc&domain=dcctb.com&id=205594485')   
    print(get_data.json())

def browser():
    
    #driver.get('https://ducvan.tk/app/down.html')
    #driver.get('https://www.1secmail.com/mailbox/?action=readMessageFull&id=205594485&login=nguyenduc&domain=dcctb.com')
    #driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/div[4]/div/center/table/tbody/tr/td/div[2]/p[2]/a').click()
    input('f')

nhiem_vu = input('''
Hi chào bạn <3 Chúc bạn ngày mới vui vẻ
Hãy chọn 1 trong những chức năng sau nhé

Nhập 1 để lấy random mail từ 1secmail :D
Nhập 2 để verify mail nếu bạn đã thực hiện reg :3

3 là để tui test nha kk

Bạn chọn chức năng gì nhỉ > ''')

if nhiem_vu == '1':
    lay_mail()
if nhiem_vu == '2':
    data_mail()
if nhiem_vu == '3':
    print('haha tui xóa chức năng này ùi:>')    

   




'''
time.sleep(2)
#keyword = chunks[l][0] : nhập tốc độ tùy theo luồng 
Options =  webdriver.ChromeOptions()
Options.add_argument('--app=https://chat.openai.com/')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=Options) 
driver.implicitly_wait(5)
driver = uc.Chrome()
driver.get('https://chat.openai.com/')
driver.set_window_rect(400,10,400,600)
#driver.get(f'https://www.youtube.com/results?search_query={keyword}')
driver.get('https://chat.openai.com/')
print('point 1')
time.sleep(10)


time.sleep(10)
driver.find_element(By.XPATH,"//div[@id='__next']/div/div/div[4]/button[2]/div").click() 
print('point 2')

driver.refresh()   
time.sleep(2)
print('point 3')

time.sleep(10)
driver.find_element(By.XPATH,"//button[@name='action']").send_keys(f'{m}')
input('')
print('Kết thúc hết số luồng')
'''