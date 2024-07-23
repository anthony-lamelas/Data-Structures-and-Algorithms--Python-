def remove_all_evens(lst):
    left = 0
    right = len(lst)-1

    while left < right:

        if lst[right] % 2 == 0:
            lst.pop()
            right -= 1
        
        if lst[left] %2 != 0:
            left += 1

        elif lst[left] % 2 == 0 and lst[right] % 2 != 0:
            lst[left], lst[right] = lst[right],lst[left]
            lst.pop()
            left += 1
            right -= 1

    return lst

        








lst = [2, 3, 5, 2, 16, 13]
print(remove_all_evens(lst))