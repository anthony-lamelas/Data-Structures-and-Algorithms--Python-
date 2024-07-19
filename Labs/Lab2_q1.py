def sum_subarray(lst, k):
    length = len(lst)
    current = sum(lst[:k])
    max = current

    for i in range(length-k):
        current = current - lst[i] + lst[i + k]
        if current > max:
            max = current

    return max
    



lst = [1,12,-5,-6,50,3]
print(sum_subarray(lst, 3))