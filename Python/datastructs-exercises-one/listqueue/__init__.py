from linkedlist import LinkedList


class Queue:

    def __init__(self):
        self.items = LinkedList()

    def enqueue(self, item):
        self.items.add(item)
        pass

    def dequeue(self):
        if self.size() == 0:
            return None
        returned_item = self.items.remove(self.front())
        return returned_item.value
        pass

    def front(self):
        if self.size() == 0:
            return None
        returned_item = self.items.head
        return returned_item.value
        pass

    def rear(self):
        if self.size() == 0:
            return None
        returned_item = self.items.tail
        return returned_item.value
        pass

    def size(self):
        return self.items.size()
        pass
