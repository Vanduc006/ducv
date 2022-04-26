
from tkinter import messagebox
  
name_duc = (f"Nguyễn Văn Đức")
name_duc_2 = (f"nguyễn văn đức")
name_dung = (f"Nguyễn Tuấn Dũng")
name_dung_2 = (f"nguyễn tuấn dũng")
name_minh =(f"Dương Nguyễn Bình Minh")
name_minh_2 =(f"dương nguyễn bình minh")
name_co = (f"dương tiến anh")
nme_co_1 = (f"Dương Tiến Anh")
names = {name_duc, name_dung_2, name_duc_2, name_dung,  name_minh, name_minh_2 }

def name():
    name = input("Nhập tên của bạn : ").strip()
    birth_year = int(input("Bạn sinh năm bao nhiêu: "))
    age = 2022 - birth_year
    
      
        


    
    print(f"Xin chào {name}")
    messagebox.showinfo(title="Thông báo",
			message="Hệ thống đang lấy thông tin của bạn vui lòng chờ trong giây lát")
    

    
    if name == name_duc or name == name_duc_2 :
        print(f"INFO : Bạn {age} tuổi/ Học Trường THPT Trần Hưng Đạo")
    if name == name_dung or name == name_dung_2 or name == name_minh or name == name_minh_2 :
        print(f"INFO : Bạn {age} tuổi/ Học Trường THCS Phú Lương  ")    
    if name ==  name_co :
        print(f"INFO : Bạn {age} tuổi / Học trường tiểu học Phú lương I")    
    else :
         print (f"Xin lỗi tên của bạn không có trong hệ thống. Vui lòng thử lại sau!!!")    
         

name()   


 