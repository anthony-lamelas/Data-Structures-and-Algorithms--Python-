def majority_number(lissy):
    
    count = 0
    for num in lissy:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    
    return candidate
    


print(majority_number([0,1,5,-1,1,1,-99,1,2,1,1]))
print(majority_number([0,1,5,-1,1,99,99,99,99,99,99]))
