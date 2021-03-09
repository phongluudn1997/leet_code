def best_sum(target_sum, numbers):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_path = None

    for number in numbers:
        remainder = target_sum - number
        remainderCombination = best_sum(remainder, numbers)
        if remainderCombination is not None:
            combination = remainderCombination + [number]
            shortest_path = combination if shortest_path is None or len(
                combination) < len(shortest_path) else shortest_path

    return shortest_path


def memoization(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_path = None

    for number in numbers:
        remainder = target_sum - number
        remainderCombination = memoization(remainder, numbers, memo)
        if remainderCombination is not None:
            combination = remainderCombination + [number]
            shortest_path = combination if shortest_path is None or len(
                combination) < len(shortest_path) else shortest_path

    memo[target_sum] = shortest_path
    return shortest_path


# print(memoization(7, [5, 3, 4, 7]))
print(memoization(8, [5, 4]))
# print(memoization(8, [1, 4, 5]))
# print(memoization(100, [1, 2, 5, 25]))
# print(memoization(300, [7, 14]))
