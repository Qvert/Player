from src.LinkedListItem import LinkedListItem


class LinkedList:
    def __init__(self, first_item=None):
        self.first_item = first_item
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

    def append_left(self, item): # добавление элемента в начало списка;
        new_item = LinkedListItem(item)
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

    def append_right(self, item): # добавление элемента в конец списка;
        pass

    def append(self, item):
        self.append_right(item)

    def remove(self, item):
        if self.first_item is None:
            raise ValueError()
        current_item = self.first_item
        for i in range(len(self)):
            if current_item.data == item:
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

    def insert(self, previous, item): # вставка элемента item после элемента previous.
        if self.first_item is None:
            raise ValueError("Список пуст.")
        current = self.first_item
        for i in range(self.length):
            if current.data == previous:
                item.next = current.next
                item.previous = current
                current.next.previous = item
                current.next = item
                self.length += 1
                return None
            current = current.next
        raise ValueError("Элемент с такими данными не найден в списке.")

    @property
    def last(self):
        """Получение последнего элемента списка"""
        if self.first_item is None:
            return None
        last = self.first_item.previous
        return last

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
        index_sign = index // abs(index)

        for i in range(index_sign * len(self)):
            if i == index:
                return current_item.data
            current_item = current_item.next
        else:
            raise IndexError()

    def __contains__(self, item):
        current_item = self.first_item
        for i in range(len(self)):
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