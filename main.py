from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6 import uic

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PLayer")
        uic.loadUi("MainWindow.ui", self)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    app.exec()