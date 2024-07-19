def split_by_sign(lst, low, high):
    left = low
    right = high

    while right > left:
        if lst[right] > 0:
            right -= 1
            split_by_sign(lst, left, right)
        else:
            if lst[left] > 0:
                lst[right], lst[left] = lst[left], lst[right]
            else:
                left += 1
                split_by_sign(lst, left, right)

    return lst
    
