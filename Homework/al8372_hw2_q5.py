def findChange(lst01):
    left = 0
    right = len(lst01) -1
    index = None
    

    while (left <= right):
           mid = left + (right - left) // 2

           if lst01[mid] == 0:
                 left = mid + 1 

           elif lst01[mid]==1:
                 index = mid
                 right = mid - 1
                 
    return index


                 
                 