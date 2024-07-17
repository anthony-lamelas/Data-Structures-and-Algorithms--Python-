def fibs(n):
    previous = 1
    previous2 = 1
    
    if n >= 1:
        yield 1

    if n >= 2:
        yield 1
        
    for i in range(2,n):
        temp = previous + previous2
        yield temp
        
        previous2 = previous
        previous = temp




