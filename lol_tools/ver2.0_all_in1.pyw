import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from ui_all_1 import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        goi_auto_click =  self.uic.Button_auto_click.clicked

    def auto_click(goi_auto_click):
        
        import auto_click
        auto_click()
        
        
               

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
