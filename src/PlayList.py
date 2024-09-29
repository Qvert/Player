from src.LinkedList import LinkedList
import pygame


class PlayList(LinkedList):
    def __init__(self, name_playlist):
        super().__init__()
        self.name_playlist = name_playlist
        self.current_track = None

    def play_all(self, item=None):
        self.current_track = item
        while self.current_track:
            self.play_track(self.current_track.data)
            self.current_track = self.current_track.next_item
            if self.current_track == self.first_item:
                break

    def next_track(self):
        """Перейти к следующему треку"""
        self.current_track = self.current_track.next_item\
            if self.current_track.next_item else self.first_item
        self.play_track(self.current_track.data)

    def previous_track(self):
        self.current_track = self.current_track.previous_item \
            if self.current_track.previous_item else self.first_item
        self.play_track(self.current_track.data)

    @property
    def current(self):
        return self.current_track.data if self.current_track else None

    def play_track(self, track):
        """Воспроизводит трек."""
        pygame.mixer.init()
        pygame.mixer.music.load(track.path)
        pygame.mixer.music.play()
