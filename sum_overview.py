"""
Give a number and array of numbers. Find that if
E.g. Input: 11 and [1,2,5]
1. Can 11 sum up by [1,2,5]
2. Find one path to sum up 11 => [5,2,2,2]
3. Find the length of shortest path => 3 because [5,5,1] is the shortest path
4. Find shortest path
5. Find all path
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


def find_one_path(total, numbers):
    if total == 0:
        return []
    if total < 0:
        return None
    for number in numbers:
        remainder = total - number
        result = find_one_path(remainder, numbers)
        if result is not None:
            return result + [number]


def find_one_path_with_memo(total, numbers, memo={}):
    if total == 0:
        return []
    if total < 0:
        return None
    if total in memo:
        return memo[total]
    for number in numbers:
        remainder = total - number
        result = find_one_path(remainder, numbers)
        if result is not None:
            memo[total] = result + [number]
            return memo[total]


def find_shortest_path(total, numbers):
    if total == 0:
        return []
    if total < 0:
        return None
    shorstest_path = None
    for number in numbers:
        remainder = total - number
        path_of_child = find_shortest_path(remainder, numbers)
        if path_of_child is not None:
            current_path = path_of_child + [number]
            shorstest_path = current_path if shorstest_path is None or len(
                current_path) < len(shorstest_path) else shorstest_path
    return shorstest_path


def find_shortest_path_with_memo(total, numbers, memo={}):
    if total == 0:
        return []
    if total < 0:
        return None
    if total in memo:
        return memo[total]
    shorstest_path = None
    for number in numbers:
        remainder = total - number
        path_of_child = find_shortest_path_with_memo(remainder, numbers, memo)
        if path_of_child is not None:
            current_path = path_of_child + [number]
            shorstest_path = current_path if shorstest_path is None or len(
                current_path) < len(shorstest_path) else shorstest_path
    memo[total] = shorstest_path
    return shorstest_path


def find_all_path(total, numbers, memo={}):
    if total == 0:
        return [[]]
    if total < 0:
        return None
    if total in memo:
        return memo[total]
    paths = []
    for number in numbers:
        remainder = total - number
        # [[], [], []] or None
        path_at_number = find_all_path(remainder, numbers)
        if path_at_number is not None:
            paths = paths + [[number] + p for p in path_at_number]
    memo[total] = paths
    return paths


print(find_all_path(50, [1, 2, 5]))
