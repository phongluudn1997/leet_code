def recursive(target_sum, numbers):
    if target_sum == 0: return True
    if target_sum < 0: return False
    return any([recursive(target_sum - number, numbers) for number in numbers])

def memoization(target_sum, numbers, memo={}):
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return True
    if target_sum < 0: return False
    memo[target_sum] = any([memoization(target_sum - number, numbers, memo) for number in numbers])
    return memo[target_sum]

print(memoization(300, [7, 14]))