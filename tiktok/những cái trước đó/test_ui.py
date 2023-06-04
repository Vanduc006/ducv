from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Thiết lập màu nền cho giao diện
        painter.setBrush(QColor("#f2f2f2"))
        painter.drawRect(self.rect())
if __name__ == '__main__':
	app = QApplication([])
	window = CustomWidget()
	window.setStyleSheet("background-image: url('back.png')")
	window.show()
	app.exec_()
