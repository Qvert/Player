"""Module for working with double-linked list"""

class LinkedListItem:
    """Class bilinked list"""
    def __init__(self, value):
        self.data = value
        self.next = None
        self.previous = None

    @property
    def next_item(self):
        """Get next item"""
        return self.next

    @next_item.setter
    def next_item(self, value):
        self.next = value
        if value is not None:
            value.previous = self

    @property
    def previous_item(self):
        """Get previous item"""
        return self.previous

    @previous_item.setter
    def previous_item(self, value):
        self.previous = value
        if value is not None:
            value.next = self

    def __repr__(self) -> str:
        return f"LinkedListItem({self.data})"
