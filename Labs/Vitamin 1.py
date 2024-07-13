lst = [1, [2, 3], ["a", "b"] ]
lst_slice = lst[:]
lst_assign = lst
lst.append("c")
for i in range(1, 3):
    lst_slice[i][0] *= 2

    
print(lst)

print(lst_slice)

print(lst_assign)