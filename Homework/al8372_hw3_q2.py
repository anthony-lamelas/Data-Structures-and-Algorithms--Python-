from ArrayStack import ArrayStack

class MaxStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.maxval = None

    def is_empty(self):
        return self.stack.is_empty()

    def __len__(self):
        return len(self.stack)

    def push(self, item):
        self.stack.push((item , self.maxval))
        if self.maxval is None or item > self.maxval:
            self.maxval = item

    def top(self):
        if self.is_empty():
            raise Exception("Empty stack")
        return self.stack.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception("Empty stack")
        result = self.stack.pop()
        if result[1] is None or result[0] > result[1]:
            self.maxval = result[1]
        return result[0]

    def max(self):
        if self.is_empty():
            raise Exception("Empty stack")
        return self.maxval
    
    



