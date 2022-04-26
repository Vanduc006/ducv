

while True:
    num1 = int(input("[+] Nhập giá trị 1 :")) 
    num2 = int(input("[+] Nhập giá trị 2 :"))
    phep_tinh_hd = """Hãy nhập như sau :[nếu là cộng gõ '+'] 
                        [nếu là trừ gõ '-' ]
                        [nếu là nhân gõ '*']
                        [nếu là chia gõ '/']
                                        """
    print(phep_tinh_hd)   
    phep_tinh = input("[-] Nhập giá trị phép tính :")
    def go_ngu():   
        if phep_tinh != '+' and phep_tinh != '-' and phep_tinh != '*' and phep_tinh != '/':
            print("Bạn đã nhập sai, xin vul lòng nhập lại")   
            phep_tinh = input("[-] Nhập giá trị phép tính :")  
        return phep_tinh
            
                
    if '+' in phep_tinh:
        kq = int(num1) + int(num2)
        print(f"{num1} + {num2} = {kq}")

    if '-' in phep_tinh:
        kq = int(num1) - int(num2)
        print(f"{num1} - {num2} = {kq}")
    if '*' in phep_tinh:
        kq = int(num1) * int(num2)
        print(f"{num1} * {num2} = {kq}")       
    if '/' in phep_tinh:
        kq = int(num1) / int(num2)
        print(f"{num1} / {num2} = {kq}")
