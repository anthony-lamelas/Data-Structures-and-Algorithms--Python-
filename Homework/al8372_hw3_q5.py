from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue

def permutations(lst):
    s = ArrayStack()
    q = ArrayQueue()

    if len(lst) == 0:
        return []
    for each in lst:
        s.push(each)

    q.enqueue([])

    while not s.is_empty():
        curr = s.pop()
        
        length = len(q)
        for i in range(length):
            old = q.dequeue()
            
            for j in range(len(old) + 1):
                new = old[:]
                new.insert(j, curr)
                q.enqueue(new)

    answer = []
    for i in range(len(q)):
        answer.append(q.dequeue())

    return answer

