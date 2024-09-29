class Composition:
    def __init__(self, title, artist, duration, path):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.path = path

    def __str__(self):
        return f"{self.title} by {self.artist} - {self.duration}"