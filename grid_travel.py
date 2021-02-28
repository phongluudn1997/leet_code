def recursive(m, n):
    ways = 0
    if m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    else:
        ways += recursive(m-1, n) + recursive(m, n-1)
    return ways

print(recursive(3, 2))
