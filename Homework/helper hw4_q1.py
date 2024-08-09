from DoublyLinkedList import DoublyLinkedList

class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        if orig_str:
            count = 1
            current_char = orig_str[0]
            for char in orig_str[1:]:
                if char is current_char:
                    count += 1
                else:
                    self.data.add_last((current_char, count))
                    count = 1
                    current_char = char
            self.data.add_last((current_char, count))
    
    def __add__(self, other):
        new = DoublyLinkedList()
        
        self_node = self.data.header.next
        other_node = other.data.header.next
        
        while self_node is not self.data.trailer:
            new.add_last(self_node.data)
            self_node = self_node.next
        
        if new.trailer.prev.data[0] is other_node.data[0]:
            last_data = new.trailer.prev.data
            new.trailer.prev.data = (last_data[0], last_data[1] + other_node.data[1])
            other_node = other_node.next
        
        while other_node is not other.data.trailer:
            new.add_last(other_node.data)
            other_node = other_node.next
        
        result = CompactString("")
        result.data = new
        return result
    
    def __lt__(self, other):
        self_node = self.data.header.next
        other_node = other.data.header.next

        while self_node is not self.data.trailer and other_node is not other.data.trailer:
            if self_node.data[0] < other_node.data[0]:
                return True
            elif self_node.data[0] > other_node.data[0]:
                return False
            else:  # Characters are the same
                if self_node.data[1] < other_node.data[1]:
                    next_self_node = self_node.next
                    next_other_node = other_node.next
                    if next_other_node is not other.data.trailer and \
                    (next_self_node is self.data.trailer or next_self_node.data[0] < next_other_node.data[0]):
                        return True
                    return False
                elif self_node.data[1] > other_node.data[1]:
                    return False
                else:
                    self_node = self_node.next
                    other_node = other_node.next

        if self_node is self.data.trailer and other_node is not other.data.trailer:
            return True
        return False

    def __le__(self, other):
        self_node = self.data.header.next
        other_node = other.data.header.next

        while self_node is not self.data.trailer and other_node is not other.data.trailer:
            if self_node.data[0] < other_node.data[0]:
                return True
            elif self_node.data[0] > other_node.data[0]:
                return False
            else:  # Characters are the same
                if self_node.data[1] < other_node.data[1]:
                    next_self_node = self_node.next
                    next_other_node = other_node.next
                    if next_other_node is not other.data.trailer and \
                    (next_self_node is self.data.trailer or next_self_node.data[0] < next_other_node.data[0]):
                        return True
                    return False
                elif self_node.data[1] > other_node.data[1]:
                    return False
                else:
                    self_node = self_node.next
                    other_node = other_node.next

        if self_node is self.data.trailer and other_node is not other.data.trailer:
            return True
        if self_node is self.data.trailer and other_node is self.data.trailer:
            return True
        return False


        
        
    
    def __gt__(self, other):
        return not self <= other
    
    def __ge__(self, other):
        return not self < other
    
    def __repr__(self):
        result = ''
        node = self.data.header.next
        while node is not self.data.trailer:
            result += node.data[0] * node.data[1]
            node = node.next
        return result
    






s1 = CompactString('aaaaaaacccaaaaa')
s2 = CompactString('aaaaaaacccaaaa') 

print(s1 > s2) #true

c1 = CompactString('aaaaabbbaaac')
c2 = CompactString('aaaaaaacccaaaa')

print( c1 <= c2) #false

d1 = CompactString('aaaaa')
d2 = CompactString('aaaaa')

print(d1 <= d2) #true

