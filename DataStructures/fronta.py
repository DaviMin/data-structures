
class CharQueue:
    def __init__(self, size): # size urcuje maximalni velikosti fronty
        self.size = size
        self.queue = []

    def  is_empty(self):
        return len(self.queue) ==0

    def is_full(self): # s podrtzitkama by bylo PRIVATE
        return len(self.queue) == self.size

    def enqueue(self, item):
        if not self.is_full():
            self.queue.append(item)
            return True # zpetna vazba jakoze se povedlo
        return False # nepovedlo se
    def  dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0) # ta 0 je jakoze poradi, index
            return item
        return None

    def show(self):
        if not self.is_empty():
            for i in self.queue:
                print(i, end=" ")
            print()
        else:
            print("Queue is empty.")