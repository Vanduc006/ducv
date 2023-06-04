import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QCheckBox, QTableWidget, QTableWidgetItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Thêm/Xóa cột khi checkbox được chọn")

        # Create a QLabel to display the checkbox status
        self.label = QLabel("Checkbox status: ")

        # Create the checkboxes
        self.checkbox1 = QCheckBox("Box 1")
        self.checkbox2 = QCheckBox("Box 2")

        # Connect the checkbox state changed signals to slots
        self.checkbox1.stateChanged.connect(self.checkbox_state_changed)
        self.checkbox2.stateChanged.connect(self.checkbox_state_changed)

        # Create a QTableWidget
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Cột 1", "Cột 2"])

        # Create a QVBoxLayout to arrange the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.checkbox1)
        layout.addWidget(self.checkbox2)
        layout.addWidget(self.table)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Set the central widget of the main window
        self.setCentralWidget(central_widget)

        # Variable to store the display state of each column for each checkbox
        self.column_display_state = {
            self.checkbox1: [True, False],
            self.checkbox2: [False, True]
        }

    def checkbox_state_changed(self):
        # Update the label text based on the checkbox state
        states = {
            self.checkbox1: self.checkbox1.isChecked(),
            self.checkbox2: self.checkbox2.isChecked()
        }

        column_count = self.table.columnCount()

        # Remove all columns except the first two
        while self.table.columnCount() > 2:
            self.table.removeColumn(self.table.columnCount() - 1)

        # Add columns based on checkbox states
        for checkbox, state in states.items():
            if state:
                display_state = self.column_display_state[checkbox]
                for i, display in enumerate(display_state):
                    if display:
                        column_index = self.table.columnCount()
                        column_label = f"Cột {column_index + 1}"
                        self.table.setColumnCount(column_count + 1)
                        self.table.setHorizontalHeaderItem(column_index, QTableWidgetItem(column_label))

                        for row in range(self.table.rowCount()):
                            item = QTableWidgetItem(f"Dữ liệu {row + 1}, {column_label}")
                            self.table.setItem(row, column_index, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
