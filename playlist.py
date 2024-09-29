from pygame import mixer
from linked_list import LinkedList


class PlayList(LinkedList):
    """Класс, реализующий логику работы плейлиста
       Унаследован от базового класса LinkedList"""

    def __init__(self) -> None:
        super().__init__()
        self.current_track = None

    def play_all(self, start_track=None) -> None:
        """Воспроизводит все песни начиная с выбранного."""
        if start_track is None:
            start_track = self.first_item
        self.current_track = start_track

        while self.current_track:
            self.play_track(self.current_track.data)
            self.current_track = self.current_track.next_item
            if self.current_track == self.first_item:
                break

    def next_track(self):
        """Перейти к следующему треку"""
        if self.current_track is None:
            self.current_track = self.first_item
        else:
            self.current_track = self.current_track.next_item \
                if self.current_track.next_item else self.first_item
            self.play_track(self.current_track.data)

    def previous_track(self):
        """Перейти к предыдущему треку"""
        if self.current_track is None:
            self.current_track = self.first_item
        else:
            self.current_track = self.current_track.previous_item \
                if self.current_track.previous_item else self.first_item
            self.play_track(self.current_track.data)

    @property
    def current(self):
        """Получить текущий трек, реализовать в виде свойства"""
        return self.current_track.data if self.current_track else None

    def play_track(self, track):
        """Воспроизводит трек."""
        mixer.init()
        mixer.music.load(track.path)
        mixer.music.play()

    def move_item_up(self, index):
        """Передвинуть трек вверх"""
        if index > 0:
            self.swap(index, index - 1)

    def move_item_down(self, index):
        """Передвинуть трек вниз"""
        if index < self.length - 1:
            self.swap(index, index + 1)

    def swap(self, index1, index2):
        """Поменять два трека местами"""
        if self.first_item is None:
            raise IndexError("Плейлист пуст")

        if not (0 <= index1 < self.length) or not (0 <= index2 < self.length):
            raise IndexError("Индекс за пределами")

        node1, node2 = None, None
        current_item = self.first_item

        for i in range(self.length):
            if i == index1:
                node1 = current_item
            if i == index2:
                node2 = current_item
            current_item = current_item.next_item

        if node1 and node2:
            node1.data, node2.data = node2.data, node1.data

            if self.current_track == node1:
                self.current_track = node2
            elif self.current_track == node2:
                self.current_track = node1
        else:
            raise IndexError("Не удалось найти узлы по заданным индексам.")