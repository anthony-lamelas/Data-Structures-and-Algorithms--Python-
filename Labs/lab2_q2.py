#worst case is theat n^

def find_missing(lst):
    left, right = 0, len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if lst[mid] != mid + 1:
            right = mid - 1
        else:
            left = mid + 1
    
    return left + 1


print(find_missing([1,2,3,4,5,6,8]))


def find_missing_ns(lst):
    n = len(lst)

    sum = (n*(n+1)) / 2
    actual_sum = 0

    for num in lst:
        actual_sum += num
    
    return sum-actual_sum


lst = [8, 6, 0, 4, 3, 5, 1, 2]
print(find_missing_ns(lst))