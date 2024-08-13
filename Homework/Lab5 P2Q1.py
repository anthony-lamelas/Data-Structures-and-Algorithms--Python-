def most_frequent(lst):
    fmap = {}
    max = 0
    max_key = None
    for each in lst:
        if each not in fmap:
            fmap[each] = 1
        else:
            fmap[each] += 1

            if fmap[each] > max:
                max = fmap[each]
                max_key = each
                
    return max_key


def first_unique(lst):
    fmap = {}

    for each in lst:
        if each not in fmap:
            fmap[each] = 1
        else:
            fmap[each] += 1

    for each in lst:
        if fmap[each] > 1:
            return each
        

def two_sum(lst, target):
    seen = {}

    for i in range(len(lst)):
        if target - lst[i] in seen:
            return(seen[target-lst[i]],i)
        seen[lst[i]] = i



lst = [-2, 11, 15, 21, 20, 7]
print(two_sum(lst, 22))