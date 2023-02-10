"""from pystyle import Write, Colors,Colorate
import random,os
tree = '''
                                                 
        &#BBGGGGBB#&          &#BBGGGGBB#&        
      #GPPPPPPPPPPPPGB&    &BGPPPPPPPPPPPPG#      
    #GPPPPPPPPPPPPPPPPPB  BPPPPPPPPPPPPPPPPPG#    
   #PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP#   
   PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP   
  &PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP&  
  &PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP&  
  &PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP&  
   BPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB   
   &GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG&   
    &GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG&    
      BPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB      
       &BPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB&       
         &BPPPPPPPPPPPPPPPPPPPPPPPPPPPPB&         
            #GPPPPPPPPPPPPPPPPPPPPPPG#            
              &BPPPPPPPPPPPPPPPPPPB&              
                &BGPPPPPPPPPPPPGB&                
                   #GPPPPPPPPG#                   
                     &BPPPPB&                     
                       &BB&                       
                                                  
'''
color1 = Colors.red_to_yellow
cl_m_1 = Colors.yellow_to_green
color2 = Colors.green_to_blue
color3 = Colors.blue_to_red
color4 = Colors.red_to_purple
color5 = Colors.purple_to_blue
color6 = Colors.blue_to_cyan

color7 = Colors.cyan_to_green
color8 = Colors.green_to_red
color9 = Colors.red_to_blue
color10 = Colors.blue_to_white
color11 = Colors.green_to_white
cl_m_2 = Colors.white_to_red



while True:

    Write.Print(f'{tree}',color1,interval=0.000000000000)
    Write.Print(f'{tree}',cl_m_1,interval=0.000000000000)
    Write.Print(f'{tree}',color2,interval=0.000000000000)
    Write.Print(f'{tree}',color3,interval=0.000000000000)
    Write.Print(f'{tree}',color4,interval=0.000000000000)
    Write.Print(f'{tree}',color5,interval=0.000000000000)
    Write.Print(f'{tree}',color6,interval=0.000000000000)
    Write.Print(f'{tree}',color7,interval=0.000000000000)
    Write.Print(f'{tree}',color8,interval=0.000000000000)
    Write.Print(f'{tree}',color9,interval=0.000000000000)
    Write.Print(f'{tree}',color10,interval=0.000000000000)
    Write.Print(f'{tree}',color11,interval=0.000000000000)
    Write.Print(f'{tree}',cl_m_2,interval=0.000000000000)
    os.system('clear')
"""
import time,os

tree = '''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@&#BBGGGGBB#&@@@@@@@@@@&#BBGGGGBB#&@@@@@@@@
@@@@@@#GPPPPPPPPPPPPGB&@@@@&BGPPPPPPPPPPPPG#@@@@@@
@@@@#GPPPPPPPPPPPPPPPPPB@@BPPPPPPPPPPPPPPPPPG#@@@@
@@@#PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP#@@@
@@@PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP@@@
@@&PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP&@@
@@&PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP&@@
@@&PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP&@@
@@@BPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB@@@
@@@&GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG&@@@
@@@@&GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG&@@@@
@@@@@@BPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB@@@@@@
@@@@@@@&BPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPB&@@@@@@@
@@@@@@@@@&BPPPPPPPPPPPPPPPPPPPPPPPPPPPPB&@@@@@@@@@
@@@@@@@@@@@@#GPPPPPPPPPPPPPPPPPPPPPPG#@@@@@@@@@@@@
@@@@@@@@@@@@@@&BPPPPPPPPPPPPPPPPPPB&@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@&BGPPPPPPPPPPPPGB&@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#GPPPPPPPPG#@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@&BPPPPB&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@&BB&@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''                       

while True:
    
    print(f"\033[31m{tree}\033[31m")
    os.system('clear')
    print(f"\033[31m{tree}\033[31m")



