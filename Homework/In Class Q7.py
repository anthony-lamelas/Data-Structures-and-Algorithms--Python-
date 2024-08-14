def print_missing(arr, low, high):
    fmap = {}
    for elem in arr:
        fmap[elem] = elem
    for i in range (low, high + 1):
        if i not in fmap:
            print(i)
      

print(print_missing([1,14,11,51,15],50,55))