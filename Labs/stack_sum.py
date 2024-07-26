def stack_sum(s):
    sum = 0
    if len(s) == 1:
        sum += s.top()
        return sum
    else:
        val = s.pop()
        sum += val + stack_sum(s)

    return sum