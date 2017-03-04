from linkedlist import LinkedList


class Stack:

    def __init__(self):
        self.items = LinkedList()

    def push(self, item):
        self.items.add(item)
        pass

    def pop(self):
        if self.size() == 0:
            return None
        returned_item = self.items.remove(self.items.tail.value)
        return returned_item.value
        pass

    def peek(self):
        if self.size() == 0:
            return None
        returned_item = self.items.tail
        return returned_item.value
        pass

    def size(self):
        return self.items.size()
        pass
