import sys,os,time

try :
  import random
  from pystyle import Write, Colors
except :
  os.system('pip install pystyle')
  os.system('pip install random')
    
color1 = Colors.red_to_yellow
color2 = Colors.green_to_blue
color3 = Colors.blue_to_red
color4 = Colors.red_to_purple
color5 = Colors.purple_to_blue
color6 = Colors.blue_to_cyan
list_color = [color1,color2,color3,color4,color5,color6]
random_color = random.choice(list_color)
#name = Write.Input("Enter your name -> ", Colors.red_to_purple, interval=0.0025)
#Write.Print(f"Nice to meet you, {name}!", Colors.blue_to_green, interval=0.05)
Write.Print(''' 

 _____         _    ______                                        _             
|_   _|       | |   | ___ \                                      (_)            
  | | _____  _| |_  | |_/ / __ __ _ _ __ __ _ _ __ ___  _ __ ___  _ _ __   __ _ 
  | |/ _ \ \/ / __| |  __/ '__/ _` | '__/ _` | '_ ` _ \| '_ ` _ \| | '_ \ / _` |
  | |  __/>  <| |_  | |  | | | (_| | | | (_| | | | | | | | | | | | | | | | (_| |
  \_/\___/_/\_\|__| \_|  |_|  \__, |_|  \__,_|_| |_| |_|_| |_| |_|_|_| |_|\__, |
                               __/ |                                       __/ |
                              |___/                                       |___/ 
  BẠN CÓ THỂ TÌM THẤY NHIỀU THỨ THÚ VỊ Ở ĐÂY
	https://github.com/Vanduc006 \n''',random_color,interval=0.0015)    
    
text = Write.Input("Bạn MuốN Viết Gì? :",random_color, interval=0.0025)
try :
  so_lan_lap = int(Write.Input("Nhập số lần lặp lại *lên để nhỏ hơn 10* :",random_color,interval=0.0025))
except :
  print('Phải nhập số bạn nhek')
  sys.exit()
if so_lan_lap > 10 :
  print("Số lần lặp phải nhỏ hơn 10")
  sys.exit()

trim = text


for so_lan in range(so_lan_lap):
  time.sleep(2)
  for i in range(10):
    print(text)

  for l in range(30):
      for i in range(10):
          print("" * i, text)    
          print("" *(3-i), text)

  for k in range(3):
    for i in range(6):
      print(" " * i, text)
    for i in range(6):
      print(" " * (5-i), text)

  for k in range(3):
    for i in range(len(text)):
      print(text[i:], text[:i])

  for k in range(3):
    for i in range(6):
      print(text[:6], i * " ",
          text[6:])
    for i in range(6):
      print(text[:6], (5 - i) * " ",
          text[6:])


  for n in range(5):
    for i in range(5):
      print(trim[:5]+ i*" "+
      trim[5]+ (5-i)*" " + trim[6:])
    for i in range(5):
      print(trim[:5]+ (5-i)*" "+
          trim[5]+ i*" " + trim[6:])


  for i in range(len(trim)):
    for j in range(5):
      print(trim[:i], (4-j)*" ",
          trim[i],j*" ", trim[i+1:])

  for i in range(20):
    print(trim)

  for i in range(30):
    print(text)

  for k in range(3):
    for i in range(6):
      print(" " * i, text)
    for i in range(6):
      print(" " * (5-i), text)

  for k in range(3):
    for i in range(len(text)):
      print(text[i:], text[:i])

  for k in range(3):
    for i in range(6):
      print(text[:6], i * " ",
          text[6:])
    for i in range(6):
      print(text[:6], (5 - i) * " ",
          text[6:])


  for n in range(5):
    for i in range(5):
      print(trim[:5]+ i*" "+
      trim[5]+ (5-i)*" " + trim[6:])
    for i in range(5):
      print(trim[:5]+ (5-i)*" "+
          trim[5]+ i*" " + trim[6:])


  for i in range(len(trim)):
    for j in range(5):
      print(trim[:i], (4-j)*" ",
          trim[i],j*" ", trim[i+1:])

  for i in range(20):
    print(trim)
  for i in range(30):
    print(text)

  for k in range(3):
    for i in range(6):
      print(" " * i, text)
    for i in range(6):
      print(" " * (5-i), text)

  for k in range(3):
    for i in range(len(text)):
      print(text[i:], text[:i])

  for k in range(3):
    for i in range(6):
      print(text[:6], i * " ",
          text[6:])
    for i in range(6):
      print(text[:6], (5 - i) * " ",
          text[6:])


  for n in range(5):
    for i in range(5):
      print(trim[:5]+ i*" "+
      trim[5]+ (5-i)*" " + trim[6:])
    for i in range(5):
      print(trim[:5]+ (5-i)*" "+
          trim[5]+ i*" " + trim[6:])


  for i in range(len(trim)):
    for j in range(5):
      print(trim[:i], (4-j)*" ",
          trim[i],j*" ", trim[i+1:])

  for i in range(20):
    print(trim)
  for i in range(30):
    print(text)

  for k in range(3):
    for i in range(6):
      print(" " * i, text)
    for i in range(6):
      print(" " * (5-i), text)

  for k in range(3):
    for i in range(len(text)):
      print(text[i:], text[:i])

  for k in range(3):
    for i in range(6):
      print(text[:6], i * " ",
          text[6:])
    for i in range(6):
      print(text[:6], (5 - i) * " ",
          text[6:])


  for n in range(5):
    for i in range(5):
      print(trim[:5]+ i*" "+
      trim[5]+ (5-i)*" " + trim[6:])
    for i in range(5):
      print(trim[:5]+ (5-i)*" "+
          trim[5]+ i*" " + trim[6:])


  for i in range(len(trim)):
    for j in range(5):
      print(trim[:i], (4-j)*" ",
          trim[i],j*" ", trim[i+1:])

  for i in range(20):
    print(trim)


