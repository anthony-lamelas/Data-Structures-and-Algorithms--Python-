def split_by_parity(lst):
    def recursive_split(lst, left, right):
        if left >= right:
            return lst

        # Create a copy of the current list segment to work with
        new_lst = lst[:]
        
        if new_lst[left] % 2 == 0:
            return recursive_split(new_lst, left + 1, right)
        elif new_lst[right] % 2 != 0:
            return recursive_split(new_lst, left, right - 1)
        else:
            # Swap elements
            new_lst[left], new_lst[right] = new_lst[right], new_lst[left]
            return recursive_split(new_lst, left + 1, right - 1)

    return recursive_split(lst, 0, len(lst) - 1)

#print(split_by_parity([3, 6, 2, 1, 8]))




def in_somewhere(lissy, value):
    for each in lissy:
        if isinstance(each, list):
            if in_somewhere(each, value):  
                return True
        elif each == value:
            return True
    return False





def binary_search(lst, val):
    def helper(left, right):
        mid = (left + right) // 2
        if val == lst[mid]:
            return mid
        elif val < lst[mid]:
            return helper(left,mid-1)
        else:
            return helper(mid+1, right)
        
    return helper(0,len(lst)-1)

lst = [1,2,3,4,5,6,7,8,9,20]

print(binary_search(lst, 9))


