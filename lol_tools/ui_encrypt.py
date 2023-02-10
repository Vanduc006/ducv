from PyQt5 import QtWidgets
from ma_hoa import Ui_MainWindow
from cryptography.fernet import Fernet
import base64
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import *
import os
from cryptography.fernet import Fernet
import hashlib
import datetime
from PyQt5.QtWidgets import QMessageBox,QLabel
import webbrowser as wb
from PyQt5.QtGui import QIcon,QPixmap
import requests




current_date = datetime.datetime.now()
ngay = current_date.strftime("%Y-%m-%d")
directory = "ma hoa - " + ngay
directory = str(directory)

if not os.path.exists(directory):
    os.makedirs(directory)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ma_hoa_file_thuong)
        self.pushButton_2.clicked.connect(self.giai_ma_thuong)
        self.pushButton_3.clicked.connect(self.ma_hoa_pass)
        self.pushButton_4.clicked.connect(self.giai_ma_pass)
        self.pushButton_5.clicked.connect(self.dang_phat_trien)
        self.pushButton_6.clicked.connect(self.dang_phat_trien)
        self.pushButton_7.clicked.connect(self.dang_phat_trien)
        self.pushButton_8.clicked.connect(self.dang_phat_trien)
        self.pushButton_9.clicked.connect(self.dang_phat_trien)
        self.pushButton_10.clicked.connect(self.dang_phat_trien)
        self.pushButton_11.clicked.connect(self.web)
        self.pushButton_12.clicked.connect(self.face)
        self.pushButton_13.clicked.connect(self.github)
        self.pushButton_14.clicked.connect(self.donate)


    def face(self):
        url = f'https://www.facebook.com/profile.php?id=100065525475828'
        wb.get().open(url)    
    def web(self):
        url = f'https://ducvan.tk/'  
        wb.get().open(url)   
    def github(self):
        url = f'https://github.com/Vanduc006/' 
        wb.get().open(url)      
    def donate(self):
        message_box1 = QMessageBox()
        message_box1.setWindowTitle("Oh my godddd")
        message_box1.setText("Tôi sẽ rất vui hihi [Mb bank: 0373871213]. Thank You!!")
        message_box1.exec_()    
    def dang_phat_trien(self):
        message_box1 = QMessageBox()
        message_box1.setWindowTitle("Lỗi bất định")
        message_box1.setText("Chức năng vẫn đang trong quá trình phát triển!")
        message_box1.exec_()
    def ma_hoa_file_thuong(self):
        file_path_thuong_en = filedialog.askopenfilename()
        try:
            file_name_thuong_en = os.path.basename(file_path_thuong_en)
        
            with open(file_path_thuong_en,"rb") as f:
                original_data = f.read()

            encoded_data = base64.b64encode(original_data)

            with open(os.path.join(directory,file_name_thuong_en), "wb") as f:
                f.write(encoded_data)
            message_box = QMessageBox()
            message_box.setWindowTitle("Thành công!")
            message_box.setText("Đã mã hóa xong file")
            message_box.exec_()      
        except:
            message_box = QMessageBox()
            message_box.setWindowTitle("Lỗi! Vui lòng thử lại")
            message_box.setText("Vui lòng chọn file!! bạn vừa không chọn file nào cả")
            message_box.exec_()      
    def giai_ma_thuong(self):

        file_path_thuong_de = filedialog.askopenfilename()    
        try:   
            with open(file_path_thuong_de, "rb") as f:
                encoded_data = f.read()

            decoded_data = base64.b64decode(encoded_data)

            with open(file_path_thuong_de, "wb") as f:
                f.write(decoded_data) 
            message_box = QMessageBox()
            message_box.setWindowTitle("Thành công!")
            message_box.setText("Đã giải mã hóa file xong")
            message_box.exec_()      
        except:
            message_box = QMessageBox()
            message_box.setWindowTitle("Lỗi! Vui lòng thử lại")
            message_box.setText("Vui lòng chọn file!! bạn vừa không chọn file nào cả")
            message_box.exec_()          
    def ma_hoa_pass(self):
        file_path_pass_en = filedialog.askopenfilename() 
        try:
            file_name_pass_en = os.path.basename(file_path_pass_en)
            pass_1 = simpledialog.askstring("Pass", "Nhập mật khẩu bạn muốn đặt :")
            password = f"{pass_1}".encode('utf-8')
            key = hashlib.sha256(password).digest()
            cipher = Fernet(base64.urlsafe_b64encode(key))
            
            with open(file_path_pass_en, "rb") as f:
                original_data = f.read()
            encrypted_data = cipher.encrypt(original_data)

            with open(os.path.join(directory,file_name_pass_en), "wb") as f:
                f.write(encrypted_data)
            message_box = QMessageBox()
            message_box.setWindowTitle("Thành công!")
            message_box.setText("Đã mã hóa file (có pass) xong ")
            message_box.exec_()     
        except:
            message_box = QMessageBox()
            message_box.setWindowTitle("Lỗi! Vui lòng thử lại")
            message_box.setText("Vui lòng chọn file!! bạn vừa không chọn file nào cả")
            message_box.exec_()      


    def giai_ma_pass(self):
        file_path_pass_de = filedialog.askopenfilename()  
        try:
            pass_2 = simpledialog.askstring("Pass", "Nhập mật khẩu mà bạn đã đặt:")
            password = f"{pass_2}".encode('utf-8')
            key = hashlib.sha256(password).digest()
            cipher = Fernet(base64.urlsafe_b64encode(key))
            
            with open(file_path_pass_de, "rb") as f:
                encrypted_data = f.read()

            decrypted_data = cipher.decrypt(encrypted_data)  
            with open(file_path_pass_de, "wb") as f:
                
                f.write(decrypted_data)

            message_box = QMessageBox()
            message_box.setWindowTitle("Thành công!")
            message_box.setText("Đã giải mã file (có pass) xong")
            message_box.exec_()     
        except:
            message_box = QMessageBox()
            message_box.setWindowTitle("Lỗi! Vui lòng thử lại")
            message_box.setText("Vui lòng chọn file!! bạn vừa không chọn file nào cả")
            message_box.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    window.setWindowTitle('Encrypt & Decrypt By duc krikman')
    url_ico = "https://live.staticflickr.com/65535/52680404476_644f049aaa_o.png"
    response = requests.get(url_ico)
    image = QPixmap()
    image.loadFromData(response.content)
    window.setWindowIcon(QIcon(image))

    window.show()
    sys.exit(app.exec_())
