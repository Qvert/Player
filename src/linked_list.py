"""Module for working with double-linked list data"""

from src.linked_list_items import LinkedListItem


class LinkedList:
    """Class linked list"""
    def __init__(self, first_item=None):
        self.first_item = first_item
        self.last_item = None
        self.iter_current = None
        self.iter_start = None
        self.length = 0
        if first_item:
            current = first_item
            while True:
                self.length += 1
                if current.next_item == first_item:
                    break
                current = current.next_item
            current.next_item = first_item
            first_item.previous_item = current

    def append_left(self, data):
        """Adding an item to the beginning of the list"""
        new_item = LinkedListItem(data)
        if len(self) == 0:
            self.first_item = new_item
            new_item.next = self.first_item
            new_item.previous = self.first_item
        else:
            last = self.first_item.previous
            last.next = new_item
            new_item.previous = last
            new_item.next = self.first_item
            self.first_item.previous = new_item
            self.first_item = new_item
        self.length += 1

    def append_right(self, data):
        """Adding an item to the end of the list"""
        new_item = LinkedListItem(data)
        if len(self) == 0:
            self.first_item = new_item
            new_item.next = self.first_item
            new_item.previous = self.first_item
        else:
            last = self.first_item.previous
            last.next = new_item
            new_item.previous = last
            new_item.next = self.first_item
            self.first_item.previous = new_item
        self.length += 1

    def append(self, item):
        """Allias for append_right"""
        self.append_right(item)

    @property
    def last(self):
        """Last item retrieval"""
        if self.first_item is None:
            return None
        last = self.first_item.previous
        return last

    def remove(self, data):
        """Deleting an item from the list"""
        if self.first_item is None:
            raise ValueError()
        current_item = self.first_item
        for _ in range(len(self)):
            if current_item.data == data:
                if len(self) == 1:
                    self.first_item = None
                else:
                    previous_item = current_item.previous_item
                    next_item = current_item.next_item
                    previous_item.next_item = next_item
                    next_item.previous_item = previous_item
                    if current_item == self.first_item:
                        self.first_item = next_item
                self.length -= 1
                return None
            current_item = current_item.next_item
        raise ValueError()

    def insert(self, previous_item_data, new_item_data):
        """Insert an item in place of another"""
        if self.first_item is None:
            raise ValueError("Список пуст.")

        current = self.first_item
        while current is not None:
            if current.data == previous_item_data:
                new_item = LinkedListItem(new_item_data)
                new_item.next = current.next
                new_item.previous = current

                # Устанавливаем обратные ссылки
                if current.next is not None:
                    current.next.previous = new_item

                current.next = new_item

                # Обновляем last_item, если вставка происходит в конец списка
                if current == self.last_item:
                    self.last_item = new_item

                self.length += 1
                return

            current = current.next

        raise ValueError("Элемент с такими данными не найден в списке.")

    def __len__(self):
        return self.length

    def __iter__(self):
        self.iter_current = self.first_item
        if self.iter_current is not None:
            self.iter_start = self.iter_current
        return self

    def __next__(self):
        if self.iter_current is None:
            raise StopIteration
        current_data = self.iter_current
        self.iter_current = self.iter_current.next_item
        if self.iter_current == self.iter_start:
            self.iter_current = None
        return current_data

    def __getitem__(self, index):
        if self.first_item is None:
            raise IndexError()
        current_item = self.first_item

        if index >= 0:
            for i in range(len(self)):
                if i == index:
                    return current_item.data
                current_item = current_item.next
        else:
            for i in range(-len(self), 0):
                if i == index:
                    return current_item.data
                current_item = current_item.next
        return current_item

    def __contains__(self, item):
        current_item = self.first_item
        for _ in range(len(self)):
            if current_item.data == item:
                return True
            current_item = current_item.next
        return False

    def __reversed__(self):
        if not self.first_item:
            return None
        current = self.first_item.previous_item
        while True:
            yield current.data
            current = current.previous_item
            if current == self.first_item.previous_item:
                break
        return current

    def print_linked_list(self):
        """Print the contents of a doubly linked list"""
        if self.first_item is None:
            print("Список пуст.")
            return

        current_item = self.first_item
        while True:
            print(f"Узел: {current_item}, Данные: {current_item.data}")
            current_item = current_item.next
            if current_item == self.first_item:
                break
