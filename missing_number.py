def cal_sum(length: int):
    if length == 1:
        return 0
    return length - 1 + cal_sum(length - 1)


def missing_number(nums):
    expected_sum = cal_sum(len(nums) + 1)
    actual_sum = sum(nums)
    print(expected_sum, actual_sum)
    return expected_sum - actual_sum


print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
