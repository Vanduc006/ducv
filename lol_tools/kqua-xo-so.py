import requests
from bs4 import BeautifulSoup

def KQXS(so, con,day):
    cons = con.replace(" ","-")
    rq = requests.get('https://ketqua1.net/xo-so-"+cons+"/'+".php?"+day)
    soup = BeautifulSoup(rq.content, 'html.parser')
    table = soup.find('table', class_='table table-condensed table-bordered table-kq-hover kqcenter kqbackground table-kq-bold-border region-table')
    kq = []
    for value in table.splitlines():
        if value != '':
            kq.append(value)
    kqxs = kq[2].split('G')
    bingo = []
    print()
    print()
    print()
    print("-------Kết quả xổ--------")
    print()
    g0 = kqxs[0][8:14]
    print("Giải đặc biệt: "+g0)
    if so == g0:
        bingo.append("Đặc Biệt")
    g1 = kqxs[1][8:13]
    print("Giải nhất: "+g1)
    if so == g1:
        bingo.append("Nhất")  
    g2 = kqxs[7][7:12]  
    print("Giải nhì: "+g2)
    if so == g2:
        bingo.append("Nhì")
    g3replace = kqxs[3].replace("giải ba",'')
    g3 = [g3replace[0:5],g3replace[5:10]]
    print("Giải ba: "+g3[0]+" "+g3[1])       
    for valueG3 in g3:
        if so[1:7] == valueG3:
            bingo.append("Ba")   
    g4replace = kqxs[4].replace("giải tư","")
    g4 = [g4replace[0:5],g4replace[5:10],g4replace[10:15],g4replace[15:20],g4replace[20:25],g4replace[25:30]] 
    print("Giải tư: "+g4[0]+" "+g4[1]+" "+g4[2]+" "+g4[3]+" "+g4[4]+" "+g4[5]+" "+g4[6])
    for valueG4 in g4:
        if so[1:7] == valueG4:
            bingo.append("Tư")     
    g5 = kqxs[5][7:11]
    print("Giải năm: "+g5)     
    if so[2:7] == g5:
        bingo.append("Năm")    
    g6replace = kqxs[6].replace("giải sáu","")
    g6 = [g6replace[0:4], g6replace[4:8], g6replace[8:12], g6replace[12:16]]
    print("Giải sáu: "+g6[0]+" "+g6[1]+" "+g6[2]+" "+g6[3])
    for valueG6 in g6:
        if so[2:7] == valueG6:
            bingo.append("Sáu")
    g7 = kqxs[7][7:10]
    print("Giải bảy: "+g7)      
    if so[3:7] == g7:
        bingo.append("Bảy")  
    g8 = kqxs[8][7:9]
    print("Giải tám: "+g8)
    if so[4:7] == g8:
        bingo.append("Tám")
    print()
    print()
    print("--------------------------------------------------------------------------------------------------------------------")
    print()
    if len(bingo) == 0:
        print("Không có số nào trùng với số bạn đã chọn")
    elif len(bingo) == 1:
        if bingo[0] == "Đặc Biệt":
            print("Bạn đã trúng giải đặc biệt")
        else:
            print("Bạn đã trúng giải "+bingo[0])
    else :
        print("Bạn đã trúng giải "+len(bingo)+" giải :")     
        for i in bingo:
            print("Giải :" + i)     
    print()
    print()
    print("--------------------------------------------------------------------------------------------------------------------")          
    print()
so = str(input("Nhập số của bạn : "))
con = str(input("Nhập tên tỉnh của bạn(VD: tien giang): "))    
day = str(input("Nhập ngày của bạn(VD: ngày 01/01/2020): "))
KQXS(so,con,day)
#--------------------------------------------------------------------------------------------------------------------
print("Cảm ơn bạn đã tham gia chương trình")
print("Lấy dữ liệu từ https://ketqua1.net")

