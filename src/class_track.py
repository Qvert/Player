"""Module with work at track"""

class Composition:
    """Class work at track"""
    def __init__(self, title, path):
        self.title = title
        self.path = path

    @property
    def get_title(self):
        """Get title"""
        return self.title

    def __str__(self):
        return f"{self.title}"
