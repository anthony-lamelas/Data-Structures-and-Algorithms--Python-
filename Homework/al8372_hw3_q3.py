from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack():
    def __init__(self):
        self.stack = ArrayStack()
        self.queue = ArrayDeque()
    
    def is_empty(self):
        return self.stack.is_empty() and self.queue.is_empty()
    
    def __len__(self):
        return len(self.stack) + len(self.queue)
    
    def push(self, item):
        self.queue.enqueue_last(item)
        if len(self.queue) > len(self.stack):
            self.stack.push(self.queue.dequeue_first())

    def top(self):
        if self.is_empty():
            raise Exception("Empty stack")
        if self.queue.is_empty():
            return self.stack.top()
        else:
            return self.queue.last()
    
    def pop(self):
        if self.is_empty():
            raise Exception("Empty stack")
        if len(self.stack) > len(self.queue):
            self.queue.enqueue_first(self.stack.pop())
        return self.queue.dequeue_last()
            
        
    def mid_push(self, item):
        if len(self.stack) > len(self.queue):
            self.queue.enqueue_first(item)
        else:
            self.stack.push(item)


'''
4
4 5
45 6
45 67
456 78
456 789
4567 891
'''





