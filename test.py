import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 400, 400)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.result_display = QLineEdit()
        self.layout.addWidget(self.result_display)
        button_grid_layout = self.create_button_grid()
        self.layout.addLayout(button_grid_layout)
        self.central_widget.setLayout(self.layout)

    def create_button_grid(self):
        button_grid_layout = QGridLayout()
        button_grid = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', 'C', '=', '+']
        ]
        for i, row in enumerate(button_grid):
            for j, button_text in enumerate(row):
                button = QPushButton(button_text)
                button.clicked.connect(self.on_button_click)
                button_grid_layout.addWidget(button, i, j)

        return button_grid_layout

    def on_button_click(self):
        button = self.sender()
        clicked_text = button.text()
        if clicked_text == "=":
            try:
                result = eval(self.result_display.text())
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")
        elif clicked_text == "C":
            self.result_display.clear()
        else:
            current_text = self.result_display.text()
            self.result_display.setText(current_text + clicked_text)

def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
