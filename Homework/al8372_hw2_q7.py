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
    
print(split_by_sign([1, -2, 3, -4, 5, -6], 0, 5))  # Output could be [-6, -2, -4, 3, 5, 1]
print(split_by_sign([-1, -2, -3, 4, 5, 6], 0, 5)) # Output: [-1, -2, -3, 4, 5, 6]
print(split_by_sign([1, 2, 3, -4, -5, -6], 0, 5)) # Output could be [-6, -5, -4, 3, 2, 1]
print(split_by_sign([1, 2, 3, 4, 5, 6], 0, 5))   # Output: [1, 2, 3, 4, 5, 6]
print(split_by_sign([-1, -2, -3, -4, -5, -6], 0, 5)) # Output: [-1, -2, -3, -4, -5, -6]
print(split_by_sign([], 0, -1)) # Output: []
print(split_by_sign([0, -1, 1], 0, 2)) # Output could be [-1, 0, 1] or [-1, 1, 0]