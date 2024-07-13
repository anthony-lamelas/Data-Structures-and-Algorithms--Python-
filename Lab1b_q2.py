def move_zeros(nums):
    left = 0
    right = 0

    for val in range(nums):
        left = val
        if val == 0:
            right = val
        nums.append(nums[val])
        nums.pop(val)

    return nums
            

print(move_zeros([0,1,0,3,13,0]))