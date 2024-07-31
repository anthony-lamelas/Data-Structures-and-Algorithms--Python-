from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.stack1 = ArrayStack()
        self.stack2 = ArrayStack()

    def __len__(self):
        return len(self.stack1) + len(self.stack2)
    
    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()
    
    def enqueue(self, item):
        self.stack1.push(item)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        
        if self.stack2.is_empty():
            for i in range (len(self.stack1)):
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()
    
    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        
        if self.stack2.is_empty():
            for i in range (len(self.stack1)):
                self.stack2.push(self.stack1.pop())

        return self.stack2.top()