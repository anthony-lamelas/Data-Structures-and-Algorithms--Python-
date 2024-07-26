import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1

    def __len__(self):
        return self.n
    
    def is_empty(self):
        return len(self) == 0

    def resize(self, new_size):
        temp_arr = make_array(new_size)
        for i in range(self.n):
            temp_arr[i] = self.data_arr[i]
        self.data_arr = temp_arr
        self.capacity = new_size

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def pop(self, ind=-1):
        if ind < 0:
            ind += len(self)
        if (ind >= 0 and ind <= (self.n - 1)):
            for i in range(ind, len(self) - 1):
                self[i] = self[i + 1]
            val = self[len(self) - 1]
            self[len(self) - 1] = None
            self.n -= 1
            return val
        else:
            raise IndexError("Index out of range!")
        
    def __getitem__(self, ind):
        if ind < 0:
            ind += len(self)
        if (ind >= 0 and ind <= (self.n - 1)):
            return self.data_arr[ind]
        else:
            raise IndexError("Index out of range!")

    def __setitem__(self, ind, val):
        if ind < 0:
            ind += len(self)
        if (ind >= 0 and ind <= (self.n - 1)):
            self.data_arr[ind] = val
        else:
            raise IndexError("Index out of range!")


class ArrayStack:
    def __init__(self):
        self.data = ArrayList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.pop()