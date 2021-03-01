def recursive(m, n):
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    return recursive(m-1, n) + recursive(m, n-1)

def memoization(m, n, memo={}):
    key = str(m) + ', ' + str(n)
    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    memo[key] = memoization(m-1, n, memo) + memoization(m, n-1, memo)
    return memo[key]

print(memoization(1, 1))
print(memoization(1, 3))
print(memoization(18, 18))
