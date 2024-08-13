from ArrayQueue import *

class ExtendedPartiesQueue:
    def __init__(self):
        self.parties = {}
        self.q = ArrayQueue()

    def __len__(self):
        return len(self.q)
    
    def enq_party(self, party_name, party_size):
        self.q.enqueue((party_name,party_size))
        self.parties[party_name] = party_size

    def add_to_party(self, party_name, size_to_add):
        if party_name not in self.parties:
            raise Exception('Party Name not Found')
        else:
            self.parties[party_name] += size_to_add

    def first_party(self):
        if(len(self) == 0):
            raise Exception("ExtendedPartiesQueue is empty")

        return self.parties[self.q.first()[0]]

    def deq_first_party(self):
        if(len(self) == 0):
            raise Exception("ExtendedPartiesQueue is empty")   
        
        return self.parties[self.q.dequeue()[0]]
            

