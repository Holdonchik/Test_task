def find_mediana(nums):
    nums.sort()
    if (len(nums) % 2) == 0:
        index2 = len(nums)//2
        index1 = index2-1
        result = (nums[index1]+nums[index2])/2
    else:
        index = len(nums)//2
        result = nums[index]
    return print(result)


find_mediana([100, 1, 5])
find_mediana([1, 2, 4, 4, 5, 6, 10, 11])
find_mediana([1, 1, 1, 1, 2, 3, 8, 10, 587])
find_mediana([1, 1, 1, 1, 2, 3, 8, 10])