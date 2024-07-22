def m_times_n(m,n):
    if n == 0:
        return 0
    elif n ==1 :
        return m
    else:
        return m + (m_times_n(m,n-1))
    
print(m_times_n(9,7))


#Number 4

#The runtime is 0(n) because it will run n times (the lenght of the list)
#Each call is indexing the last element of the list, which has a local cost of 1.
# (1+1+1...) n times = 0(n)


#Number 4b

'''
It is 0(n^2) because three for loops to the n run time. j in range 100 is 0(1) because it is set.

'''