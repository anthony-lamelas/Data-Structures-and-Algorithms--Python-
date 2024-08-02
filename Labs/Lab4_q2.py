class DoublyLinkedList:
    class Node:
        def __init__(self, elem = None, next = None, prev = None):
            self.data = elem
            self.next = next
            self.prev = prev

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.header = self.Node()
        self.trailer = self.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def add_after(self, node, elem):
        new_node = self.Node(elem)

        predecessor = node
        successor = node.next
        new_node.prev = predecessor
        new_node.next = successor
        predecessor.next = new_node
        successor.prev = new_node
        self.size += 1
        return new_node

    def add_first(self, elem):
        return self.add_after(self.header, elem)

    def add_last(self, elem):
        return self.add_after(self.trailer.prev, elem)

    def add_before(self, node, elem):
        return self.add_after(node.prev, elem)

    def delete_node(self, node):
        if (self.is_empty()):
            raise Exception("DoublyLinkedList is Empty")
        return_val = node.data
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        node.disconnect()
        self.size -= 1
        return return_val

    def delete_first(self):
        return self.delete_node(self.header.next)

    def delete_last(self):
        return self.delete_node(self.trailer.prev)

    def __iter__(self):
        cursor = self.header.next
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        # [100 <---> 200 <---> 500]
        return "["+ " <---> ".join([str(each) for each in self])+"]"
    
    def __getitem__(self,i):
        if i < 0:
            i = len(self) + 1
        if i < 0 or i >= len(self):
            raise IndexError('Out of Range')
        mid = len(self) // 2 
        if i == 0:
            return self.header.next

        if i == len(self) - 1:
            return self.trailer.prev
        
        if i <= mid:
            node = self.header.next
            for i in range(i):
                node = node.next
            
        else:
            node = self.trailer.prev
            for i in range(len(self) - i-1):
                node = node.prev
        return node.data

