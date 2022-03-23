nums = [2,11,15,7]
target = 9
for i in range(len(nums)):
    #start the range at index 1 because we adding 1 to i index
    for j in range(1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)
