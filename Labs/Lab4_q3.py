from DoublyLinkedList import DoublyLinkedList

class Midstack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, e):
        self.data.add_first(e)

    def top(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        return self.data.header.next.element
    
    def pop(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        return self.data.delete_first()
    
    def mid_push(self, e):
        if self.is_empty():
            raise Exception('Empty Stack')
        
        mid = (len(self) + 1) // 2
        node = self.data.header.next
        for i in range(mid):
            node = node.next
        self.data.add_after(node, e)
