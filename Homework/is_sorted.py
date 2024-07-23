def is_sorted(lst,low,high):
   
    if low >= high:
        return True
    if lst[low] > lst[low+1]:
        return False
    return is_sorted(lst,low+1,high)
        
   



lst = [1, 3, 6, 8, 12, 15, 31]
print(is_sorted(lst, 0, 6))
