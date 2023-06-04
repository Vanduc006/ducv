from ui_tiktok_downloader import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QLabel
import webbrowser as wb
from PyQt5.QtGui import QIcon,QPixmap
import requests
import re
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QListWidget, QProgressBar
import os
import time

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.add_link_work)
        self.pushButton_3.clicked.connect(self.xoa_link_work)
        self.pushButton.clicked.connect(self.tai_thuong)

    # Tạo 1 thư muc thên local nếu không có sẵn    
    directory = 'local'
    if not os.path.exists(directory):
        os.makedirs(directory)
    # logic check file
    # khi mở sẽ xóa file list.txt
    # nếu lỗi sẽ tiếp tục , thực hiện với việc bấm thêm links

    def add_link_work(self):
        text = self.textEdit.toPlainText()
        text = str(text)
        if text == '':
            rong_msg = QMessageBox()
            rong_msg.setText('Rỗng,vui lòng nhập lại')
            rong_msg.exec_()
        else:
            links = self.textEdit_3.setPlainText()
            if links != '':   
                print('exists')
                exit_file = QMessageBox()
                exit_file.setText("Đã tồn tại 1 list links được trước đó bạn muốn:")
                exit_file.setWindowTitle("Xin hãy lưu ý")
                xoa_list = exit_file.addButton("Xóa đi", QMessageBox.YesRole)
                giu_list = exit_file.addButton("Thêm tiếp vào", QMessageBox.NoRole)
                exit_file.exec_()
                if exit_file.clickedButton() == xoa_list: 
                    self.textEdit_3.clear()
                    self.textEdit_3.setPlainText(text) 
                if exit_file.clickedButton() == giu_list:
                    self.textEdit_3.setPlainText(text) 


            else:
                msg_box = QMessageBox()
                msg_box.setText("Bạn có muốn nhập các link này vào danh sách tải ?")
                msg_box.setWindowTitle("Xin hãy lưu ý")
                yes_button = msg_box.addButton("Đúng vậy", QMessageBox.YesRole)
                no_button = msg_box.addButton("Không!", QMessageBox.NoRole)
                msg_box.exec_()
                if msg_box.clickedButton() == yes_button: 
                    self.textEdit_3.setPlainText(text)   
    def xoa_link_work(self):
        xoa_msg =  QMessageBox()
        try:
            self.textEdit.clear()
            with open('local/list.txt','w',encoding='utf-8') as f1:
                    f1.write('\n')
            xoa_msg.setText('Xóa thành công')  
            xoa_msg.exec_()  
        except:
            xoa_msg.setText('Không tồn tại list links trước đó')    
            xoa_msg.exec_()  

                 
    def tai_thuong(self):
        def check_links():
            self.textEdit_2.setReadOnly(True)
            try:
                with open('local/list.txt','r') as f2:
                    for i in f2:
                        pattern = r"\/video\/"
                        # Kiểm tra xem đường link có chứa chuỗi "video" hay không
                        if re.search(pattern, i):
                            tbao = f"Đường link {i} : Bắt đầu tìm kiếm máy chủ"
                            tbao = tbao.replace('\n', '')
                            self.textEdit_2.setPlainText(tbao.strip())
                            time.sleep(3)
                            #tải video
                            '''
                            url = "https://www.tiktok.com/@nhaconaofficial/video/7227673882012945670?is_from_webapp=1&sender_device=pc&web_id=7155705309725296130"
                            video_id = re.search(r'/video/(\d+)\?', url).group(1)
                            username = re.search(r'@(\w+)', url).group(1)
                            url = f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={video_id}' 
                            res = requests.get(url)
                            r = res.json()
                            link = r['aweme_list'][0]['video']['play_addr']['url_list'][0]
                            #username = r['aweme_list'][0]['author']['nickname']
                            print(link)
                            files_name = str(username) + '-' + str(video_id) + '.mp4'
                            files_name = str(files_name)
                            response = requests.get(link)

                            with open(files_name, 'wb') as f:
                                f.write(response.content)
                            '''

                            tbao = f"Đường link {i} : Đã tìm thấy video, bắt đầu tải"
                            tbao = tbao.replace('\n', '')
                            self.textEdit_2.setPlainText(tbao.strip())
                            time.sleep(3)
                            url = f"{i}"
                            video_id = re.search(r'/video/(\d+)', url).group(1)
                            username = re.search(r'@(\w+)', url).group(1)
                            url = f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={video_id}' 
                            res = requests.get(url)
                            r = res.json()
                            link = r['aweme_list'][0]['video']['play_addr']['url_list'][0]
                            #username = r['aweme_list'][0]['author']['nickname']
                            files_name = str(username) + '-' + str(video_id) + '.mp4'
                            files_name = str(files_name)
                            response = requests.get(link)
                            
                            with open(files_name, 'wb') as f:
                                f.write(response.content)
                            time.sleep(3)
                            tbao = f"Đường link {i} : Tải thành công, tên file là {files_name}"
                            tbao = tbao.replace('\n', '')
                            self.textEdit_2.setPlainText(tbao.strip())    

                            
                        else:
                            tbao = f"Đường link {i} : Không hợp lệ."
                            tbao = tbao.replace('\n', '')
                            self.textEdit_2.setPlainText(tbao.strip())

            except:      
                erro_msg =  QMessageBox()  
                erro_msg.setText('Không tìm thấy list link, vui lòng nhập links vào trước!!')    
                erro_msg.exec_() 
        check_links()
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
