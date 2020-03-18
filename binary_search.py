def find_x(nums, x):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if x == nums[mid]:
            return mid
        elif x < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return - 1


print(find_x([1, 2, 3, 4, 5, 6], 4))
