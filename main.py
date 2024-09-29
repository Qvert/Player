from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QPushButton, QTextEdit, QLineEdit
from PyQt6 import uic

import sys

from src.PlayList import PlayList


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.play_lists = list()
        self.setWindowTitle("PLayer")
        uic.loadUi("ui/MainWindow.ui", self)
        self.create_playlist.clicked.connect(self.create_playlist_func)
        self.show()

    def create_playlist_func(self):
        self.name = NamePlaylist(self)
        self.name.show()

    def update_playlist(self):
        self.playlist.clear()
        for el in self.play_lists:
            self.playlist.addItem(el.name_playlist)

class NamePlaylist(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.resize(200, 80)
        self.setWindowTitle("Название плейлиста:")
        self.label = QLabel("Введите название плейлиста", self)
        self.text_name = QLineEdit(self)
        self.text_name.move(0, 20)
        self.button_save = QPushButton("Сохранить", self)
        self.button_save.resize(200, 30)
        self.button_save.move(0, 45)
        self.button_save.clicked.connect(self.post_picture)

    def post_picture(self):
        playlist_name = self.text_name.text()
        if playlist_name:
            self.main_window.play_lists.append(PlayList(playlist_name))
        self.close()
        self.main_window.update_playlist()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()