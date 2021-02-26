from decorators import working_time

def climb_stairs(n):
    """recursion"""
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return climb_stairs(n - 1) + climb_stairs(n - 2)

@working_time
def approach_1(n):
    if n == 1:
        return 1
    result = [0 for i in range(n)]
    result[0], result[1] = 1, 2
    for i in range(2, n):
        result[i] = result[i - 1] + result[i - 2]
    return result[n - 1]

@working_time
def approach_2(n):
    hash_table = {
        1: 1,
        2: 2
    }
    for i in range(3, n + 1):
        hash_table[i] = hash_table[i - 1] + hash_table[i - 2]
    return hash_table[n]


#* memoization
# TODO: not optimized, should be implemented bottom up
@working_time
def approach_3(n):
    memo = [0 for i in range(n + 1)]
    return climb_stairs_with_memo(n, memo)
def climb_stairs_with_memo(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > 0:
        return memo[n]
    else:
        memo[n] = climb_stairs_with_memo(n - 1, memo) + climb_stairs_with_memo(n - 2, memo)
        return memo[n]

# *memoization with bottom-up
@working_time
def approach_5(n):
    climb_nth_2 = 1
    climb_nth_1 = 1
    for i in range(2, n + 1):
        climb_nth_2, climb_nth_1 = climb_nth_1, climb_nth_1 + climb_nth_2
    return climb_nth_1

print(approach_5(110))