def split_parity(lst):
    length = len(lst)
    left = 0
    right = length - 1
    
    while right > left:
        
        if lst[left] % 2 == 0:  
            while right > left and lst[right] % 2 == 0:
                right -= 1
            
            if right > left:
                lst[left], lst[right] = lst[right], lst[left]
                right -= 1
                
        left += 1  
    return lst
    

