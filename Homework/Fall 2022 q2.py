from ArrayQueue import ArrayQueue

def insert_to_sorted_queue(srt_q, elem):
    if srt_q.is_empty():
        srt_q.enqueue(elem)
    
    else:
        count = 0
        curr = srt_q.dequeue()
        size = len(srt_q)
        while curr <= elem and count<size:
            srt_q.enqueue(curr)
            curr = srt_q.dequeue()
            count += 1

        srt_q.enqueue(elem)
        srt_q.enqueue(curr)

        while count < size:
            srt_q.enqueue(srt_q.dequeue())
            count += 1

    return srt_q
    

q = ArrayQueue()

q.enqueue(1)
q.enqueue(5)
q.enqueue(7)
q.enqueue(12)

print(insert_to_sorted_queue(q, 6))
            


