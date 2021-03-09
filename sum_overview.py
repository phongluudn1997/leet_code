"""
Give a number and array of numbers. Find that if
E.g. Input: 11 and [1,2,5]
1. Can 11 sum up by [1,2,5]
2. Find one path to sum up 11 => [5,2,2,2]
3. Find the length of shortest path => 3 because [5,5,1] is the shortest path
4. Find all path
"""


def can_sum_up(total, numbers):
    result = False
    if total == 0:
        return True
    for number in numbers:
        remainder = total - number
        result = result or can_sum_up(remainder, numbers)
    return result


def can_sum_up_2(total, numbers):
    if total < 0:
        return False
    if total == 0:
        return True
    return any([can_sum_up_2(total-number, numbers) for number in numbers])


def can_sum_up_with_memozation(total, numbers, memo={}):
    if total < 0:
        return False
    if total == 0:
        return True
    if total in memo:
        return memo[total]
    memo[total] = any([can_sum_up_2(total-number, numbers)
                       for number in numbers])
    return memo[total]


print(can_sum_up_with_memozation(111, [1]))
