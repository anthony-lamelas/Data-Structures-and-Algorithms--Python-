from DoublyLinkedList import DoublyLinkedList

'''
dll = DoublyLinkedList()
dll.add_first(1)
dll.add_last(3)

dll.add_last(5)
dll.add_after(dll.header.next,2)
dll.add_before(dll.trailer.prev,4)

dll.delete_node(dll.trailer.prev)
dll.add_first(0)
print(dll)

'''

class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
        
    def push(self, e):
        self.data.add_first(e)

    def top(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        return self.data.header.next
    
    def pop(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        return self.data.delete_first()
    
    

