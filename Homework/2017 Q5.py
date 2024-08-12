from ArrayStack import *

class DuplicateStackADT:

    def __init__(self):
        self.data = ArrayStack()

    def __len__(self):
        return len(self.data)
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self, e):
        if not self.is_empty() and self.data.top() == e:
            self.data.push((e, self.top()[1] + 1))
        else:
            self.data.push((e,0))

    def top(self):
        if self.data.is_empty():
            raise Exception('empty')
        
        return self.data.top()[0]
        
    def top_dups_count(self):
        if self.is_empty():
            raise Exception('empty')
        
        return self.data.top()[1]
    

    def pop(self):
        if self.is_empty():
            raise Exception('empty')
        val = self.data.pop()

        if self.data.top()[0] == val and not self.is_empty():
            count = self.data.top()[1] -1
            element = self.data.pop()

            self.data.push(element[0], count)

        return val
    
    def pop_dups(self):
        if self.is_empty():
            raise Exception('empty')
        
        while self.data.top()[1] != 0:
            self.data.pop()

        return self.data.pop()