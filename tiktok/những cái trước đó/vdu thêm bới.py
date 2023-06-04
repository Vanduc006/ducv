from ui_tiktok_downloader import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox,QLabel
from PyQt5.QtGui import QIcon,QPixmap
import requests
import re
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QListWidget, QProgressBar,QRadioButton
import os
import time
from openpyxl import Workbook
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service as ChromeService
import requests                
from selenium.webdriver.common.by import By    
from selenium import webdriver
import time
from undetected_chromedriver.v2 import Chrome, ChromeOptions

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.selected_button = None
        self.pushButton.clicked.connect(self.radio_selected)
        self.setMaximumSize(850, 580)   
        self.radioButton.clicked.connect(self.check_radio_selected)
        self.radioButton_2.clicked.connect(self.check_radio_selected)
        self.radioButton_3.clicked.connect(self.check_radio_selected)
        self.radioButton_4.clicked.connect(self.check_radio_selected)   
    directory = 'download'
    if not os.path.exists(directory):
        os.makedirs(directory)
    def create_button(self):
        button = QPushButton("Kiểm tra", self)
        button.move(50, 100)
        button.clicked.connect(self.radio_selected_is)
    def check_radio_selected(self):
        sender = self.sender()
        if sender.isChecked():
            self.selected_button = sender
    def radio_selected(self):
        #self.pushButton.setEnabled(False)
        if self.selected_button is not None:
            radio_selected_is = self.selected_button.text()
            if radio_selected_is == 'Links':
                self.tai_thuong()
            if radio_selected_is == 'Usernames':
                self.textEdit.setReadOnly(True)
                self.remote_browsers()
                self.textEdit.setReadOnly(False)

    def tai_thuong(self):
        row = self.tableWidget.rowCount() 
        def get_links():
            list_links = self.textEdit.toPlainText() 
            links = list_links.split('\n')
            for i in links:
                self.tableWidget.insertRow(row)
                item = QtWidgets.QTableWidgetItem(i)
                self.tableWidget.setItem(row, 0, item )
                QApplication.processEvents()
                def check_links():
                    corect_links= QtWidgets.QTableWidgetItem('Link đúng')
                    erro_links = QtWidgets.QTableWidgetItem('Link sai')
                    pattern = r"\/video\/"
                    if re.search(pattern, i):
                        self.tableWidget.setItem(row, 1, corect_links )
                        QApplication.processEvents()
                        def download():
                            url = f"{i}"
                            video_id = re.search(r'/video/(\d+)', url).group(1)
                            username = re.search(r'@(\w+)', url).group(1)
                            url = f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={video_id}' 
                            res = requests.get(url)
                            being_rq = QtWidgets.QTableWidgetItem('Kết nối máy chủ')
                            self.tableWidget.setItem(row, 2, being_rq )
                            QApplication.processEvents()
                            r = res.json()
                            link = r['aweme_list'][0]['video']['play_addr']['url_list'][0]
                            #username = r['aweme_list'][0]['author']['nickname']
                            files_name = str(username) + '-' + str(video_id) + '.mp4'
                            files_name = str(files_name)
                            response = requests.get(link)
                            with open(f'download/{files_name}', 'wb') as f:
                                f.write(response.content)
                            show_name_file = QtWidgets.QTableWidgetItem(f'{files_name}')
                            self.tableWidget.setItem(row, 3, show_name_file )
                            QApplication.processEvents()
                            #thêm nút xem video 
                            button = QPushButton("Xem Video")
                            self.tableWidget.setCellWidget(row, 4,button)
                            QApplication.processEvents()
                            button.clicked.connect(self.xem_video)
                        download()        
                    else:
                        self.tableWidget.setItem(row, 1, erro_links)    
                        QApplication.processEvents()
                                                
                check_links()

        get_links() 
        self.textEdit.clear()              
        self.pushButton.setEnabled(True)  
    def xem_video(self):
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        row = index.row()
        name_file = self.tableWidget.item(row, 3)
        if name_file is not None:
            name_file = name_file.text()
            file_path = f'download\{name_file}'
            os.startfile(file_path)
    def remote_browsers(self):
        row = self.tableWidget.rowCount() 
        list_links = self.textEdit.toPlainText() 
        links = list_links.split('\n')
        options = ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        driver = Chrome(options=options)
        for i in links:
            driver.get(f"{i}")
            # Lưu trữ các liên kết đã truy cập
            visited_links = set()
            while True:
                previous_height = driver.execute_script("return document.body.scrollHeight")
                time.sleep(3)
                print('Scrolling...')
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                # Quét và in ra các đường liên kết duy nhất
                elements = driver.find_elements(By.CSS_SELECTOR, ".tiktok-yz6ijl-DivWrapper > a")
                if len(elements) == 0:
                    print("No more elements found")
                    QApplication.processEvents()
                    #break
                for element in elements:
                    href = element.get_attribute("href")
                    if href not in visited_links:
                        visited_links.add(href)
                        
                # In tổng số các phần tử duy nhất
                total_elements = len(visited_links)
                current_height = driver.execute_script("return document.body.scrollHeight")
                
                if current_height == previous_height:
                    print("Reached end of page")
                    QApplication.processEvents()
                    #break
                previous_height = current_height

    '''      
    def closeEvent(self, event):
        # Hiển thị hộp thoại xác nhận trước khi đóng ứng dụng
        reply = QMessageBox.question(
            self,
            'Thông báo',
            'BBạn có chắc muốn thoát ứng dụng?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()                
        else:
            event.ignore()
'''  

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
