class Stack:

    def __init__(self):
        self.items = []
        self.ctr = 0
        
    # add item to the end of items list
    def push(self, item):
        self.items += [item]
        self.ctr = self.ctr + 1
        pass

    # return the last item of items list
    def pop(self):
        if self.ctr == 0:
            return None
        else:
            popped_item = self.items[self.ctr - 1]
            self.ctr = self.ctr - 1
            return popped_item
        pass

    def peek(self):
        if self.ctr == 0:
            return None
        return self.items[self.ctr - 1]
        pass

    def size(self):
        return self.ctr
        pass
