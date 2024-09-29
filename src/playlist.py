"""Music track playback module"""
import pygame
from src.linked_list import LinkedList


class PlayList(LinkedList):
    """Class for working with tracks"""
    def __init__(self, name_playlist):
        super().__init__()
        self.name_playlist = name_playlist
        self.current_track = None

    def play_all(self, item=None):
        """Play all tracks starting from item"""
        self.current_track = item
        self.play_track()

    def next_track(self):
        """Skip to next track"""
        self.current_track = self.current_track.next_item\
            if self.current_track.next_item else self.first_item
        self.play_track()

    def previous_track(self):
        """Skip to previous track"""
        self.current_track = self.current_track.previous_item \
            if self.current_track.previous_item else self.first_item
        self.play_track()

    @property
    def current(self):
        """Getting the current item"""
        return self.current_track.data if self.current_track else None

    def play_track(self):
        """Playing a track."""
        pygame.mixer.init()
        pygame.mixer.music.load(self.current_track.data.path)
        pygame.mixer.music.play()

    def move_item_up(self, index):
        """Move track up"""
        if index > 0:
            self.swap(index, index - 1)

    def move_item_down(self, index):
        """Move the track down"""
        if index < self.length - 1:
            self.swap(index, index + 1)

    def swap(self, index1, index2):
        """Swap two tracks"""
        if self.first_item is None:
            raise IndexError("Playlist is empty")

        if not 0 <= index1 < self.length or not 0 <= index2 < self.length:
            raise IndexError("Index beyond")

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
            raise IndexError("Failed to find nodes at the given indices.")
