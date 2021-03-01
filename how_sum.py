def recursive(target_sum, numbers):
    if target_sum == 0: return []
    if target_sum < 0: return None

    for number in numbers:
        remainder = target_sum - number
        result = recursive(remainder, numbers)
        if result is not None:
            return result + [number]
    
    return None

def memoization(target_sum, numbers, memo={}):
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None

    for number in numbers:
        remainder = target_sum - number
        result = memoization(remainder, numbers, memo)
        if result is not None:
            memo[target_sum] = result + [number]
            return memo[target_sum]
    
    memo[target_sum] = None
    return None

print(memoization(7, [2, 3]))
print(memoization(7, [5, 3, 4, 7]))
print(memoization(7, [2, 4]))
print(memoization(8, [2, 3, 5]))
print(memoization(300, [7, 14]))

