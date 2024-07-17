def count_lowercase(s, low, high):

    if len(s) == 0 or low > high:
        return 0
    
    if s[low].islower():
        return 1 + count_lowercase(s, low+1, high)
    else:
        return count_lowercase(s,low+1,high)




def is_number_of_lowercase_even(s,low,high):

    if count_lowercase(s, low, high) % 2 == 0:
        return True
    else:
        return False
    
