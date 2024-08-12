class SinglyLinkedList:

    class Node:
        def __init__(self, elem = None, next = None):
            self.data = elem
            self.next = next


    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, elem):
        new_node = self.Node(elem)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self):
        if (self.is_empty()):
            raise Exception("Linkedlist is Empty!!!")

        return_value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return return_value
    
    def delete_all_occurrences(self, val):
        # Delete all the nodes whose node.data = val
        # Write your code here
        node = self.header.next
        for i in range (len(self)):
            if node.data == val:
                node.prev.next = node.next
            node = node.next
            


        

       

