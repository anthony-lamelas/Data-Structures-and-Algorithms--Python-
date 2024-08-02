
import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()


class ArrayQueue:
    
    initial_capacity = 10
    
    def __init__(self):
        self.data_arr = make_array(ArrayQueue.initial_capacity)
        self.num_of_items = 0
        self.front = None
    
    def __len__(self): # theta(1)
        return self.num_of_items
                
    def is_empty(self): #theta(1)
        return self.num_of_items == 0
    
    def resize(self, new_size):
        new_array = make_array(new_size)
        old_array = self.data_arr
        old_index = self.front
        
        for new_index in range(self.num_of_items):
            new_array[new_index] = old_array[old_index]
            old_index = (old_index+1)%len(old_array)
        
        self.data_arr = new_array
        self.front = 0
    
    def enqueue(self, item): # amortized theta(1)
        if (self.num_of_items == len(self.data_arr)):
            self.resize(2*len(self.data_arr))
        
        if(self.is_empty()):
            self.data_arr[0] = item
            self.front = 0
            self.num_of_items += 1
        else:
            end_ind = (self.front+self.num_of_items)%len(self.data_arr)
            self.data_arr[end_ind] = item
            self.num_of_items += 1
                                    
    
    def dequeue(self): # amortized theta(1)
        if (self.is_empty()):
            raise Exception("Queue is Empty!!!")
        
        returned_item = self.data_arr[self.front]
        self.data_arr[self.front] = None
        self.front = (self.front+1)%len(self.data_arr)
        self.num_of_items -= 1
        
        if (self.is_empty()):
            self.front = None

        if (self.num_of_items < len(self.data_arr)//4 and len(self.data_arr) > ArrayQueue.initial_capacity):
            self.resize(len(self.data_arr)//2)
        
        return returned_item
            
    def first(self): #theta(1)
        if (self.is_empty()):
            raise Exception("Queue is Empty!!!")
        return self.data_arr[self.front]
 

  

