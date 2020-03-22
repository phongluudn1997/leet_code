def climb_stairs(n):
    """recursion"""
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return climb_stairs(n - 1) + climb_stairs(n - 2)


def approach_1(n):
    if n == 1:
        return 1
    result = [0 for i in range(n)]
    result[0], result[1] = 1, 2
    for i in range(2, n):
        result[i] = result[i - 1] + result[i - 2]
    return result[n - 1]


def approach_2(n):
    hash_table = {
        1: 1,
        2: 2
    }
    for i in range(3, n + 1):
        hash_table[i] = hash_table[i - 1] + hash_table[i - 2]
    return hash_table[n]


res = approach_2(1000)
print(res)
