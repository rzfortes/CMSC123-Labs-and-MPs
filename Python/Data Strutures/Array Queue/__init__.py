class Queue:

    def __init__(self):
        self.items = []
        self.ctr = 0

    # add items to the end of the items list
    def enqueue(self, item):
        self.items += [item]
        self.ctr = self.ctr + 1
        pass

    # return the first item of the items list
    def dequeue(self): 
        if self.ctr == 0:
            return None
        else:
            removed_item = self.items[0]
            # remove the first item before returning
            for i in range(0, self.ctr - 1):
                self.items[i] = self.items[i + 1]
            self.ctr = self.ctr - 1

            return removed_item
        pass

    # return the first item of the items list
    def front(self):
        if self.ctr == 0:
            return None
        return self.items[0]
        pass

    # return the last item of the items list
    def rear(self):
        if self.ctr == 0:
            return None
        return self.items[self.ctr - 1]
        pass

    # return the length of the items list
    def size(self):
        return self.ctr
        pass
