from src.LinkedList import LinkedList


class PlayList(LinkedList):
    def __init__(self, name_playlist):
        super().__init__()
        self.name_playlist = name_playlist

    def play_all(self, item): # начать проигрывать все треки, начиная с item;
        pass

    def next_track(self): # перейти к следующему треку;
        pass

    def previous_track(self): # перейти к предыдущему треку;
        pass

    def current(self): # получить текущи трек, реализовать в виде свойства.
        pass