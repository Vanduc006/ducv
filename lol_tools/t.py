import hashlib

pass_2 = input('Nhập mật khẩu :')
password = f"{pass_2}".encode('utf-8')
key = hashlib.sha256(password).digest()

print(key)
