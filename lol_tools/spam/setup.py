import os
print("""[0] pip\n[1] pip3\nchọn 0 hoặc 1 để setup?""")
c = input("chọn số ngay đây: ")
if c == "0":
    os.system("pip install requests")
    os.system("pip install colorama")

else:
    os.system("pip3 install requests")
    os.system("pip3 install colorama")
print('xong')
exit()