from DoublyLinkedList import *

class FlippableQueue:
    def __init__(self):
        self.data = DoublyLinkedList
        self.flipped = False
    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return (len(self) == 0)
    
    def enqueue(self,item):
        if self.flipped:
            self.data.add_first(item)
        else:
            self.data.add_last(item)

    def dequeue(self):
        if self.flipped:
            return self.data.delete_last
        else:
            return self.data.delete_first

    def first(self):
        if self.flipped:
            return self.data.header.next.data
        else:
            return self.data.trailer.prev.data
        
    def flip(self):
        self.flipped = not self.flipped

    

        
