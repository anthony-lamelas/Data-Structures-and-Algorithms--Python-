def shift(lst, k, direction="left"):
    length = len(lst)

    if direction != 'left' and direction != 'right':
        raise ValueError('Direction must be left or right.')

    elif direction == "left":
        temp = lst[:k]
        for i in range(length - k):
            lst[i] = lst[i + k]
        for i in range(k):
            lst[length - k + i] = temp[i]

    elif direction == "right":
        temp = lst[-k:]
        for i in range(length - 1, k - 1, -1):
            lst[i] = lst[i - k]
        for i in range(k):
            lst[i] = temp[i]
    

    return lst


