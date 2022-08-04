import requests
import urllib3

respone = requests.get('https://www.google.com/', verify=False)
print(respone.status_code)

    

# LẤY MÃ NGUỒN TRANG HANOI STUDY
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#url = 'https://study.hanoi.edu.vn/ket-qua-thi/1/273/on-tap-thcs-mon-lich-su-e-so-25-6V_z7AiHjEm47g25qNujVw'
#requests.packages.urllib3.disable_warnings()
#requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
#try:
#    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
#except AttributeError:
#    # no pyopenssl support used / needed / available
#    pass
#
#page = requests.get(url, verify=False)
#print(page.text)