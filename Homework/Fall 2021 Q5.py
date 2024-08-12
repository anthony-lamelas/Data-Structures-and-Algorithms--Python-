from ArrayQueue import *
from ArrayStack import *

def alternating_parity(lst):
    q = ArrayQueue()
    s = ArrayStack()
    even_first = lst[0] % 2 == 0

    for each in lst:
        if each % 2 != 0:
            q.enqueue(each)

    for each in lst[::-1]:
        if each % 2 == 0:
            s.push(each)

    i = 0
    length = len(lst)
    if even_first:
        while i < length:
            if i % 2 == 0 and not s.is_empty():
                lst[i] = s.pop()
            elif not q.is_empty():
                lst[i] = q.dequeue()
            i += 1
    else:
        while i < length:
            if i % 2 == 0 and not q.is_empty():
                lst[i] = q.dequeue()
            elif not s.is_empty():
                lst[i] = s.pop()
            i += 1 
            
    return lst

print(alternating_parity([2, 8, 1, 7, 3, 4]))
