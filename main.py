"""Main module"""

import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QDialog,
                             QLabel, QPushButton, QLineEdit, QFileDialog)
from PyQt6 import uic
import pygame

from src.playlist import PlayList
from src.class_track import Composition


class MainWindow(QMainWindow):
    """Main class"""
    def __init__(self):
        super().__init__()
        self.name = None
        pygame.init()
        self.play_lists = []
        self.setWindowTitle("PLayer")
        uic.loadUi("ui/MainWindow.ui", self)
        self.create_playlist.clicked.connect(self.create_playlist_func)
        self.add_composition.clicked.connect(self.add_com)
        self.delete_composition.clicked.connect(self.delete_com)
        self.compositions.itemDoubleClicked.connect(self.play_music)
        self.playlist.itemDoubleClicked.connect(self.open_playlist)
        self.delete_playlist.clicked.connect(self.del_playlist)
        self.next_track.clicked.connect(self.next_comp)
        self.prev_track.clicked.connect(self.prev_comp)
        self.insert_composition_up.clicked.connect(self.up_track)
        self.insert_composition_down.clicked.connect(self.down_track)
        self.show()

    def up_track(self):
        """Move the track to a higher position"""
        try:
            selected_playlist = self.playlist.currentItem().text()
            selected_composition = self.compositions.currentItem().text()
            for playlist in self.play_lists:
                if playlist.name_playlist == selected_playlist:
                    for composition in playlist:
                        if composition.data.title == selected_composition:
                            playlist.move_item_up(self.play_lists.index(playlist) + 1)
                            self.update_compositions(playlist)
        except AttributeError as _err:
            print("Вы не выбрали песню")

    def down_track(self):
        """Move the track to the position below"""
        try:
            selected_playlist = self.playlist.currentItem().text()
            selected_composition = self.compositions.currentItem().text()
            for playlist in self.play_lists:
                if playlist.name_playlist == selected_playlist:
                    for composition in playlist:
                        if composition.data.title == selected_composition:
                            playlist.move_item_down(self.play_lists.index(playlist) + 1)
                            self.update_compositions(playlist)
        except AttributeError as _err:
            print("Вы не выбрали песню")

    def prev_comp(self):
        """Previous composition"""
        try:
            pygame.mixer.music.stop()
            selected_playlist = self.playlist.currentItem().text()
            for playlist in self.play_lists:
                if playlist.name_playlist == selected_playlist:
                    playlist.previous_track()
        except AttributeError as _err:
            print("Нет доступных треков в плейлисте")

    def next_comp(self):
        """Next composition"""
        try:
            pygame.mixer.music.stop()
            selected_playlist = self.playlist.currentItem().text()
            for playlist in self.play_lists:
                if playlist.name_playlist == selected_playlist:
                    playlist.next_track()
        except AttributeError as _err:
            print("Нет доступных треков в плейлисте")

    def open_playlist(self):
        """Opening playlist"""
        selected_playlist = self.playlist.currentItem().text()
        for playlist in self.play_lists:
            if playlist.name_playlist == selected_playlist:
                self.update_compositions(playlist)

    def del_playlist(self):
        """Delete playlist"""
        try:
            selected_playlist = self.playlist.currentItem().text()
            for playlist in self.play_lists:
                if playlist.name_playlist == selected_playlist:
                    del self.play_lists[self.play_lists.index(playlist)]
                    self.update_playlist()
                    self.compositions.clear()
        except AttributeError as _err:
            print("Нет доступных плейлистов")

    def play_music(self):
        """Playing music"""
        selected_playlist = self.playlist.currentItem().text()
        selected_composition = self.compositions.currentItem().text()
        for playlist in self.play_lists:
            if playlist.name_playlist == selected_playlist:
                for composition in playlist:
                    if composition.data.title == selected_composition:
                        playlist.play_all(composition)

    def delete_com(self):
        """Delete composition"""
        try:
            selected_playlist = self.playlist.currentItem().text()
            selected_composition = self.compositions.currentItem().text()
            for playlist in self.play_lists:
                if playlist.name_playlist == selected_playlist:
                    for composition in playlist:
                        if composition.data.title == selected_composition:
                            playlist.remove(composition.data)
                            pygame.mixer.music.stop()
                            self.update_compositions(playlist)
        except AttributeError as _err:
            print("Доступных композиций не имеется")

    def add_com(self):
        """Adding composition"""
        selected_item = self.playlist.currentItem()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open file", "c:\\",
                                                   "Image file (*mp3 *wav)")
        if selected_item:
            for elem in self.play_lists:
                if elem.name_playlist == selected_item.text():
                    elem.append_right(Composition(file_path.split("/")[-1], file_path))
                    self.update_compositions(elem)

    def create_playlist_func(self):
        """Creating a playlist"""
        self.name = NamePlaylist(self)
        self.name.show()

    def update_playlist(self):
        """Updating the widget with playlist names"""
        self.playlist.clear()
        for el in self.play_lists:
            self.playlist.addItem(el.name_playlist)

    def update_compositions(self, playlist):
        """Function to update QListWidget"""
        self.compositions.clear()
        if playlist:
            for composition in playlist:
                self.compositions.addItem(composition.data.title)


class NamePlaylist(QDialog):
    """Class for playlist name"""
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
        """Function for creating a playlist"""
        playlist_name = self.text_name.text()
        new_playlist = PlayList(playlist_name)
        if playlist_name:
            self.main_window.play_lists.append(new_playlist)
        self.close()
        self.main_window.update_playlist()
        self.main_window.update_compositions(new_playlist)

    def plug(self):
        """Plug function"""
        return "Plug"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
