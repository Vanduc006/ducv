import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_address = s.getsockname()[0]
with open('item/youripaddress.txt', 'w') as file:
    file.write(ip_address)
s.close()