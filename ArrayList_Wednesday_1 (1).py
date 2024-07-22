import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0 # length
        self.capacity = 1 #

    def __len__(self):
        return self.n
        # to do
        #pass

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2*self.capacity)
            #self.resize(self.capacity+100)
        self.data_arr[self.n]= val
        self.n += 1

    def resize(self, new_size):
        temp_arr = make_array(new_size)
        for i in range(self.n):
            temp_arr[i] = self.data_arr[i]
        self.data_arr = temp_arr
        self.capacity = new_size

        # to do
        #pass
    def __getitem__(self, ind):
        if ind<0:
            ind = self.n+ind
        if(ind >=0 and ind <=(self.n-1)):
            return self.data_arr[ind]
        else:
            raise IndexError("Index out of range!")

        # to do
        #pass

    def __setitem__(self, ind, val):

        if ind<0:
            ind = self.n+ind

        if(ind >=0 and ind <=(self.n-1)):
            self.data_arr[ind] = val
        else:
            raise IndexError("Index out of range!")
         #pass

    def __iter__(self): # you are making your arraylist a iterable object
        # to do
        for i in range(self.n):
            yield self.data_arr[i]
        pass

    def extend(self, iter_collection):

        # to do
        for each in iter_collection:
            self.append(each)
        #pass

    def __repr__(self):
        data_as_strings = [str(self.data_arr[i]) for i in range(self.n)]
        return '[' + ', '.join(data_as_strings) + ']'

    def index(self, val):
        # we will do in class
        # Return the index of first occurrence of element val,
        # if not found in the ArrayList return None.
        # Your code
        for i in range(self.n):
            if (self.data_arr[i] == val):
                return i
        return None
        #pass

    def count(self, val):
        # we will do in class
        # return how many times element val is present in the ArrayList
        # to do
        pass

    def is_empty(self):
        # return True if ArrayList is empty, other wise return False
        # to  do
        return self.n == 0
        #pass

mlst1 = ArrayList()
for i in range(5):
    mlst1.append(i)


mlst1[2] = 2000 #__setitem__
x = mlst1[4] #__getitem__
print(x)
mlst1.extend("abc")

print(mlst1) #__repr__

for each in mlst1:
    print(each)
