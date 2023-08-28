def find_values(nums):
    end_range = len(nums)-2
    flag = 'False'
    for i in range(0, end_range):
        if (nums[i] == nums[i+1] and nums[i+1] == nums[i+2]) or\
           (nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]):
            flag = 'True'
        else:
            pass
    if flag == 'True':
        return True
    else:
        return False


print(find_values([1, 2, 2, 4, 66, 6, 7, 1, 2]))
print(find_values([1, 2, 2, 3, 4, 66, 6, 7, 1]))
print(find_values([1, 2, 3, 3, 4, 66, 6, 7, 1]))
print(find_values([1, 2, 2, 3, 4, 66, 6, 7, 8]))
print(find_values([1, 2, 2, 3, 4, 5, 6, 7, 1]))
print(find_values([1, 2, 2, 3, 9, 66, 6, 7, 1]))
