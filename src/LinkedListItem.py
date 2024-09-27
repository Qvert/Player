

class LinkedListItem:
    def __init__(self, track=None):
        self.track = track
        self._next = None
        self._prev = None

    @property
    def next_item(self):
        return self._next

    @next_item.setter
    def next_item(self, item):
        self._next = item

    @property
    def previous_item(self):
        return self._prev

    @previous_item.setter
    def previous_item(self, item):
        self._prev = item
        if item is not None:
            item.next = self

    def __repr__(self) -> str:
        return f"LinkedListItem({self.track})"
