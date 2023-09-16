import requests, json

while True:
    json_api = requests.get('https://640c374f94ce1239b0a7ebd5.mockapi.io/api/v1/troll').json()
    get_json = json_api[0]['jobs']
    print(get_json)
# import ctypes  # An included library with Python install.
# def Mbox(title, text, style):
#     return ctypes.windll.user32.MessageBoxW(0, text, title, style)
# Mbox('Your title', 'Your text', 1)