from src.LinkedList import LinkedList
import pygame


class PlayList(LinkedList):
    def __init__(self, name_playlist):
        super().__init__()
        pygame.init()
        self.name_playlist = name_playlist

    def play_all(self, item):
        # начать проигрывать все треки, начиная с item;
        pygame.mixer.music.load(item)
        pygame.mixer.music.play()
        self.next_track()

    def next_track(self): # перейти к следующему треку;
        pass

    def previous_track(self): # перейти к предыдущему треку;
        pass

    @property
    def current(self): # получить текущи трек, реализовать в виде свойства.
        pass