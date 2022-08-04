from asyncio import new_event_loop
import  openpyxl
import os
#filename = 'excel bai3.xlsx'#tên file excel
#cellname = 'A1'#dòng trong file excel
#cellname2 = 'A2'
def get_value_ecxel(filename, cellname):
    wb = openpyxl.load_workbook(filename)#lấy toàn bộ dữ liệu của file
    sheet = wb['Sheet1']#chỉ lấy trong sheet 1
    wb.close()
    return sheet[cellname].value 

def update_value_excel(filename, cellname, value):
    wb = openpyxl.load_workbook(filename)
    sheet = wb['Sheet1']
    sheet[cellname].value = value
    
    wb.close() 
    wb.save(filename)   

#data = get_value_ecxel(filename, cellname)# lấy dữ liệu từ file excel, dòng 1, cột A
#new_value = 'đuceptraivcl'# tăng giá trị lên 1
#change_data = update_value_excel(filename, cellname2, new_value)# thay đổi dữ liệu từ file excel, dòng 1, cột A
#data2 = get_value_ecxel(filename, cellname2)# lấy dữ liệu từ file excel, dòng 1, cột A
#print(data)
#print(data2)    



# Lấy username và password từ file excel
for i in range(1,10000):
    username = get_value_ecxel('excel bai3.xlsx', 'A'+str(i))
    password = get_value_ecxel('excel bai3.xlsx', 'B'+str(i))
    if username == None:
        break
    if password == None:
        break
    use_and_pass = f"{username}|{password}"
    print(use_and_pass)

#kết nối với phần đã học ở bài 2
#with open('ket_noi_voi_bai2.txt','w',encoding="utf-8") as f:
#    f.write(use_and_pass)
#    f.close()

