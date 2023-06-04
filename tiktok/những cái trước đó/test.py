from ui_tiktok_downloader import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QLabel
from PyQt5.QtGui import QIcon,QPixmap
import requests
import re
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QListWidget, QProgressBar
import os
import time
from openpyxl import Workbook

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.tai_thuong)
        self.setMinimumSize(400, 300)
        self.setMaximumSize(800, 600)      
    directory = 'download'
    if not os.path.exists(directory):
        os.makedirs(directory)

    
    def tai_thuong(self):
        self.pushButton.setEnabled(False)
        row = self.tableWidget.rowCount() 
        row = int(row) 
        for i in range(0, row+1):
            type_links = self.tableWidget.item(i, 1)
            if type_links is not None:
                text_type = type_links.text()
                if f'{text_type}' == 'Link đúng':
                    self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem('Check Xong')) 
                    links = self.tableWidget.item(i, 0)
                    if type_links is not None:
                        value = links.text() 
                        value = str(value)# Giá trị ở hàng i , cột 1e
                        url = f"{value}"
                        video_id = re.search(r'/video/(\d+)', url).group(1)
                        username = re.search(r'@(\w+)', url).group(1)
                        url = f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={video_id}' 
                        res = requests.get(url)
                        being_rq = QtWidgets.QTableWidgetItem('Kết nối máy chủ')
                        self.tableWidget.setItem(i, 2, being_rq )
                        r = res.json()
                        link = r['aweme_list'][0]['video']['play_addr']['url_list'][0]
                        #username = r['aweme_list'][0]['author']['nickname']
                        files_name = str(username) + '-' + str(video_id) + '.mp4'
                        files_name = str(files_name)
                        response = requests.get(link)
                        with open(f'download/{files_name}', 'wb') as f:
                            f.write(response.content)
                        show_name_file = QtWidgets.QTableWidgetItem(f'{files_name}')
                        self.tableWidget.setItem(i, 3, show_name_file )
                        #thêm nút xem video 
                        button = QPushButton("Xem Video")
                        self.tableWidget.setCellWidget(i, 4,button)
                        button.clicked.connect(self.xem_video)
                else:    
                    self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem('Lỗi'))   
        self.textEdit.clear()              
        self.pushButton.setEnabled(True)