from ui_tiktok_downloader import Ui_MainWindow
from PyQt5.QtGui import QIcon,QPixmap
import requests
import re
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidgetItem,QProgressDialog,QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QListWidget, QProgressBar,QRadioButton,QMessageBox
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
        self.pushButton.setIcon(QIcon('assets/down.png'))

        self.pushButton_2.setIcon(QIcon('assets/xlsx.png'))
        self.pushButton_3.clicked.connect(self.reload_all)
        self.pushButton_3.setIcon(QIcon('assets/reload.png'))
        self.pushButton_4.setIcon(QIcon('assets/about.png'))
        self.setMaximumSize(850, 580) 
        # radio list  
        self.radioButton.clicked.connect(self.check_radio_selected)
        self.radioButton_2.clicked.connect(self.check_radio_selected)
        self.radioButton_3.clicked.connect(self.check_radio_selected)
        self.radioButton_4.clicked.connect(self.check_radio_selected) 
        # checkbox list
        self.checkBox.stateChanged.connect(self.check_mota)
        self.checkBox_2.stateChanged.connect(self.check_cmt)
        self.checkBox_3.stateChanged.connect(self.check_tim)
        self.checkBox_4.stateChanged.connect(self.check_view)
        self.checkBox_5.stateChanged.connect(self.check_share)
        self.checkBox_6.stateChanged.connect(self.check_save)
        self.checkBox_7.stateChanged.connect(self.check_video_time)
        self.checkBox_8.stateChanged.connect(self.check_is_ban)
        #golbal json
        self.global_json = {}
        # list append/remove check 
        self.check_list = []
        #spin box
        self.spinBox.valueChanged.connect(self.spin)
        self.value = {}
        self.row_count = 0  
        self.progressBar
        #css
        self.css()
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
    def css(self):
        self.pushButton.setStyleSheet(
            "QPushButton {"
            "   border-radius: 10px;"
            "   background-color: #A2FF6B;"
            "   color: #000;"
            "}"
            "QPushButton:hover {"
            "   background-color: #7BFF2E;"
            "}"
            "QPushButton:pressed {"
            "   background-color: #42B100;"
            "}"
        )  
        self.pushButton_2.setStyleSheet(
            "QPushButton {"
            "   border-radius: 10px;"
            "   background-color: #A2FF6B;"
            "   color: #000;"
            "}"
            "QPushButton:hover {"
            "   background-color: #7BFF2E;"
            "}"
            "QPushButton:pressed {"
            "   background-color: #42B100;"
            "}"
        ) 
        self.pushButton_3.setStyleSheet(
            "QPushButton {"
            "   border-radius: 10px;"
            "   background-color: #A2FF6B;"
            "   color: #000;"
            "}"
            "QPushButton:hover {"
            "   background-color: #7BFF2E;"
            "}"
            "QPushButton:pressed {"
            "   background-color: #42B100;"
            "}"
        )  
        self.pushButton_4.setStyleSheet(
            "QPushButton {"
            "   border-radius: 10px;"
            "   background-color: #FFCD7D;"
            "   color: #000;"
            "}"
            "QPushButton:hover {"
            "   background-color: #FFB133;"
            "}"
            "QPushButton:pressed {"
            "   background-color: #DF9C30;"
            "}"
        ) 


    def check_box_disable(self):
        self.checkBox.setEnabled(False)
        self.checkBox_2.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.checkBox_5.setEnabled(False)
        self.checkBox_6.setEnabled(False)
        self.checkBox_7.setEnabled(False)
        self.checkBox_8.setEnabled(False)
    def check_box_enable(self):
        self.checkBox.setEnabled(True)
        self.checkBox_2.setEnabled(True)
        self.checkBox_3.setEnabled(True)
        self.checkBox_4.setEnabled(True)
        self.checkBox_5.setEnabled(True)
        self.checkBox_6.setEnabled(True)
        self.checkBox_7.setEnabled(True)
        self.checkBox_8.setEnabled(True)   
    def radio_selected(self):
        #self.pushButton.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.check_box_disable()
        dang_pt = QMessageBox()
        dang_pt.setText('Chức năng vân đang được vduc phát triển:))')
        if self.selected_button is not None:
            radio_selected_is = self.selected_button.text()
            if radio_selected_is == 'Links':
                self.tai_thuong()
            if radio_selected_is == 'Usernames':
                self.textEdit.setReadOnly(True)
                self.usernames_type()
                self.textEdit.setReadOnly(False)
            if radio_selected_is == 'Hastags' or radio_selected_is == 'Từ khóa':
                dang_pt.exec_()
                self.pushButton.setEnabled(True)
                self.check_box_enable()
                   
        else:
            none_selected = QMessageBox()
            none_selected.setText('Bạn chưa chọn phương thức nào cả')
            none_selected.exec_()
            self.pushButton.setEnabled(True)
            self.check_box_enable()
    def tai_thuong(self):
        def get_links():
            list_links = self.textEdit.toPlainText() 
            links = list_links.split('\n')
            for i in links:
                self.tableWidget.insertRow(self.row_count)
                item = QtWidgets.QTableWidgetItem(i)
                self.tableWidget.setItem(self.row_count, 0, item )
                QApplication.processEvents()
                def check_links():
                    corect_links= QtWidgets.QTableWidgetItem('Link đúng')
                    erro_links = QtWidgets.QTableWidgetItem('Link sai')
                    pattern = r"\/video\/"
                    if re.search(pattern, i):
                        self.tableWidget.setItem(self.row_count, 1, corect_links )
                        QApplication.processEvents()
                        self.download(i)        
                    else:
                        self.tableWidget.setItem(self.row_count, 1, erro_links)    
                        QApplication.processEvents()
                                                
                check_links()
                self.row_count += 1
        get_links() 
        self.textEdit.clear()              
        self.pushButton.setEnabled(True)  
        self.check_box_enable()
    def download(self,i):
        url = f"{i}"
        video_id = re.search(r'/video/(\d+)', url).group(1)
        username = re.search(r'@(\w+)', url).group(1)
        url = f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={video_id}' 
        res = requests.get(url)
        being_rq = QtWidgets.QTableWidgetItem('Kết nối máy chủ')
        self.tableWidget.setItem(self.row_count, 2, being_rq )
        QApplication.processEvents()
        r = res.json()
        self.global_json = r
        link = r['aweme_list'][0]['video']['play_addr']['url_list'][0]
        #username = r['aweme_list'][0]['author']['nickname']
        files_name = str(username) + '-' + str(video_id) + '.mp4'
        files_name = str(files_name)
        response = requests.get(link)
        with open(f'download/{files_name}', 'wb') as f:
            f.write(response.content)
        show_name_file = QtWidgets.QTableWidgetItem(f'{files_name}')
        self.tableWidget.setItem(self.row_count, 3, show_name_file )
        QApplication.processEvents()
        #thêm nút xem video 
        button = QPushButton("Xem Video")
        self.tableWidget.setCellWidget(self.row_count, 4,button)
        QApplication.processEvents()
        button.clicked.connect(self.xem_video)  
        def is_checked():
            if 'Mô tả' in self.check_list:
                mota = self.global_json['aweme_list'][0]['desc']
                mota = QtWidgets.QTableWidgetItem(f'{mota}')
                mota.setBackground(QColor('#6EFF78'))
                self.tableWidget.setItem(self.row_count, 5, mota)
                QApplication.processEvents()
            if not 'Mô tả' in self.check_list:
                mota = QTableWidgetItem()
                mota.setBackground(QColor('#A8A5A5'))
                self.tableWidget.setItem(self.row_count, 5, mota)

            if 'Bình luận' in self.check_list:
                cmt = self.global_json['aweme_list'][0]['statistics']['comment_count']
                cmt = QtWidgets.QTableWidgetItem(f'{cmt}')
                cmt.setBackground(QColor('#6EFF78'))
                self.tableWidget.setItem(self.row_count, 6, cmt)
                QApplication.processEvents()
            if not 'Bình luận' in self.check_list:
                cmt = QTableWidgetItem()
                cmt.setBackground(QColor('#A8A5A5'))
                self.tableWidget.setItem(self.row_count, 6, cmt)

            if 'Tim' in self.check_list:
                tim = self.global_json['aweme_list'][0]['statistics']['digg_count']
                tim = QtWidgets.QTableWidgetItem(f'{tim}')
                tim.setBackground(QColor('#6EFF78'))
                self.tableWidget.setItem(self.row_count, 7, tim)
                QApplication.processEvents()
            if not 'Tim' in self.check_list:
                tim = QTableWidgetItem()
                tim.setBackground(QColor('#A8A5A5'))
                self.tableWidget.setItem(self.row_count, 7, tim)

            if 'View' in self.check_list:
                view = self.global_json['aweme_list'][0]['statistics']['play_count']
                view = QtWidgets.QTableWidgetItem(f'{view}')
                view.setBackground(QColor('#6EFF78'))
                self.tableWidget.setItem(self.row_count, 8, view)
                QApplication.processEvents()
            if not 'View' in self.check_list:
                view = QTableWidgetItem()
                view.setBackground(QColor('#A8A5A5'))
                self.tableWidget.setItem(self.row_count, 8, view)

            if 'Share' in self.check_list:
                share = self.global_json['aweme_list'][0]['statistics']['share_count']
                share = QtWidgets.QTableWidgetItem(f'{share}')
                share.setBackground(QColor('#6EFF78'))
                self.tableWidget.setItem(self.row_count, 9, share)
                QApplication.processEvents()
            if not 'Share' in self.check_list:
                share = QTableWidgetItem()
                share.setBackground(QColor('#A8A5A5'))
                self.tableWidget.setItem(self.row_count, 9, share)

            if 'Lưu' in self.check_list:
                save = self.global_json['aweme_list'][0]['statistics']['collect_count']
                save = QtWidgets.QTableWidgetItem(f'{save}')
                save.setBackground(QColor('#6EFF78'))
                self.tableWidget.setItem(self.row_count, 10, save)
                QApplication.processEvents()
            if not 'Lưu' in self.check_list:
                save = QTableWidgetItem()
                save.setBackground(QColor('#A8A5A5'))
                self.tableWidget.setItem(self.row_count, 10, save)

            if 'Video time' in self.check_list:
                video_time = self.global_json['aweme_list'][0]['music_end_time_in_ms']
                video_time = QtWidgets.QTableWidgetItem(f'{video_time}')
                self.tableWidget.setItem(self.row_count, 11, video_time)
                QApplication.processEvents()
            if not 'Video time' in self.check_list:
                video_time = QTableWidgetItem()
                video_time.setBackground(QColor('#A8A5A5'))
                self.tableWidget.setItem(self.row_count, 11, video_time)

            if 'Is BAN?' in self.check_list:
                is_ban = self.global_json['aweme_list'][0]['status']['is_prohibited']
                is_ban = QtWidgets.QTableWidgetItem(f'{is_ban}')
                self.tableWidget.setItem(self.row_count, 12, is_ban)
                QApplication.processEvents()
            if not 'Is BAN?' in self.check_list:
                is_ban = QTableWidgetItem()
                is_ban.setBackground(QColor('#A8A5A5'))
                self.tableWidget.setItem(self.row_count, 12, is_ban)

        is_checked()



    def xem_video(self):
        
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        row = index.row()
        name_file = self.tableWidget.item(row, 3)
        if name_file is not None:
            name_file = name_file.text()
            file_path = f'download\{name_file}'
            os.startfile(file_path)
    def usernames_type(self): 
        real_value_loop = self.value
        list_links = self.textEdit.toPlainText() 
        links = list_links.split('\n') 
        if self.value == {}:
            none_value = QMessageBox()
            none_value.setText('Vui lòng điền số video muốn tải, cho phương thức usernames,hastags,từ khóa nhé bạn')
            none_value.exec_()
            sys.exit()
            
        options = ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        driver = Chrome(options=options)

        for i in links:
            def remote_browers():
                driver.get(f"{i}")
                # Lưu trữ các liên kết đã truy cập
                visited_links = set()
                while True:

                    previous_height = driver.execute_script("return document.body.scrollHeight")
                    time.sleep(3.5)
                    #print('Scrolling...')
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                    # Quét và in ra các đường liên kết duy nhất
                    elements = driver.find_elements(By.CSS_SELECTOR, ".tiktok-yz6ijl-DivWrapper > a")
                    if len(elements) == 0:
                        #print("No more elements found")
                        driver.quit()
                        tiktok_ban = QMessageBox()
                        tiktok_ban.setText('Lỗi bất định')
                        tiktok_ban.exec_()
                        QApplication.processEvents()
                        break
                    
                    for element in elements:
                        total_elements = len(visited_links)
                        if real_value_loop == total_elements:
                            break
                        href = element.get_attribute("href")
                        if href not in visited_links:
                            self.tableWidget.insertRow(self.row_count)
                            href = str(href)
                            item = QtWidgets.QTableWidgetItem(href)
                            self.tableWidget.setItem(self.row_count, 0, item )
                            QApplication.processEvents()
                            self.download(href)
                            self.row_count += 1
                            visited_links.add(href)
                    current_height = driver.execute_script("return document.body.scrollHeight")
                    
                    if current_height == previous_height:
                        QApplication.processEvents()
                        break
                    previous_height = current_height
            try:        
                remote_browers()
                self.textEdit.clear()
                self.pushButton.setEnabled(True)
                self.check_box_enable()
            except:            
                browser_erro = QMessageBox()
                browser_erro.setText('Đã cố lỗi xảy ra, xin hãy làm lại thao tác')
                browser_erro.exec_()
                self.pushButton.setEnabled(True)
                self.check_box_enable()
                break
    
    def check_mota(self,state):
        mota = 'Mô tả'
        if state != 0:
            self.check_list.append(mota)
        else:
            self.check_list.remove(mota)    
    def check_cmt(self,state):
        cmt = 'Bình luận'
        if state != 0:
            self.check_list.append(cmt)
        else:
            self.check_list.remove(cmt)       
    def check_tim(self,state):
        tim = 'Tim'
        if state != 0:
            self.check_list.append(tim)
        else:
            self.check_list.remove(tim)     
    def check_view(self,state):
        view = 'View'
        if state != 0:
            self.check_list.append(view)
        else:
            self.check_list.remove(view)      
    def check_share(self,state):
        share = 'Share'
        if state != 0:
            self.check_list.append(share)
        else:
            self.check_list.remove(share)       
    def check_save(self,state):
        save = 'Lưu'
        if state != 0:
            self.check_list.append(save)
        else:
            self.check_list.remove(save)    
    def check_video_time(self,state):
        video_time = 'Video time'
        if state != 0:
            self.check_list.append(video_time)
        else:
            self.check_list.remove(video_time)                             
    def check_is_ban(self,state):
        is_ban = 'Is BAN?'
        if state != 0:
            self.check_list.append(is_ban)
        else:
            self.check_list.remove(is_ban)   
    def spin(self):
        value = self.spinBox.value()    
        self.value = value
    def reload_all(self):
        self.textEdit.clear()
        #self.tableWidget.clear()
        self.spinBox.clear()
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.checkBox_8.setChecked(False)
        # radio phức tạp vcd
        
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setChecked(False)
        self.radioButton.setAutoExclusive(True)
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setAutoExclusive(True)
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setAutoExclusive(True)
        self.radioButton_4.setAutoExclusive(False)
        self.radioButton_4.setChecked(False)
        self.radioButton_4.setAutoExclusive(True)
        # clear row
        row_count = self.tableWidget.rowCount()
        if row_count > 1:
            self.tableWidget.setRowCount(0)
        '''
    def closeEvent(self, event):
        # Hiển thị hộp thoại xác nhận trước khi đóng ứng dụng
        reply = QMessageBox.question( 
            self,
            'Thông báo',
            'Bạn có chắc muốn thoát phần mềm ?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()                
        else:
            event.ignore()'''

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Tiktok (Mutil) Downloader - By Vduc006')
    url_ico = "https://live.staticflickr.com/65535/52933830724_ff4ffa852e_o.png"
    response = requests.get(url_ico)
    image = QPixmap()
    image.loadFromData(response.content)
    window.setWindowIcon(QIcon(image))
    window.show()
    sys.exit(app.exec_())
