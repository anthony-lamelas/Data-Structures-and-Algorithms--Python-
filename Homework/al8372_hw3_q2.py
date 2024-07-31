from ArrayStack import ArrayStack

class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.maxval = None

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return len(self.data)

    def push(self, item):
        self.data.push((item , self.maxval))
        if self.maxval is None or item > self.maxval:
            self.maxval = item

    def top(self):
        if self.is_empty():
            raise Exception("Empty stack")
        return self.data.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception("Empty stack")
        result = self.data.pop()
        if result[1] is None or result[0] > result[1]:
            self.maxval = result[1]
        return result[0]

    def max(self):
        if self.is_empty():
            raise Exception("Empty stack")
        return self.maxval
    
    



