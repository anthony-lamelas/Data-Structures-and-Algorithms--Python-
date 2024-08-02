from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue

def permutations(lst):
    s = ArrayStack()
    q = ArrayQueue()

    for each in lst:
        s.push(each)

    q.enqueue([])

    while not s.is_empty():
        curr = s.pop()
        
        for i in range(len(q)):
            old = q.dequeue()
            
            for j in range(len(old) + 1):
                new = old[:]
                new.insert(j, curr)
                q.enqueue(new)

    return [q.dequeue() for i in range(len(q))]

