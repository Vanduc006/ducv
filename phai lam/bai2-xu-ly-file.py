import os

#print(os.getcwd()) # lấy đường dẫn hiện tại

os.chdir(r'test_cho_bai2') # chuyển đến thư mục test

f =open("tao_ra_text_cho_bai2.docx", "w") #tạo ra 1 file tên "tao_ra_text_cho_bai2.docx" và mở để ghi
                                          # vì ở trên đã chuyển đến thư mục test lên sẽ tạo ra ở thư mục test

f.write("Hello World" + "\n") # ghi vào file "tao_ra_text_cho_bai2.docx" với chữ "Hello World"
f.close() # đóng file

os.rename("tao_ra_text_cho_bai2.docx", "xu_li_file.txt")    # đổi tên file "tao_ra_text_cho_bai2.txt" 
                                                            #  thành "xu_li_file.txt"" 


from shutil import copyfile# thư viện để copyfile
copyfile("xu_li_file.txt", "xu_li_file2_copy.txt") 

os.remove("xu_li_file.txt") # xóa file 

with open('xu_li_file2_copy.txt', 'r') as f:
    print(f.read()) # đọc file "xu_li_file2_copy.txt" và in ra ra màn hình

os.chdir(r'..') # chuyển đến thư mục gốc
print('kết nối đến file nè...bùm')
with open('bai1_text.txt', 'r') as f:
    for line in f:
        print(line) # in ra file "bai1_text.txt"
