"""
    Find the result of mulitiply operator not using * / just + - and >> <<
    Solution 1:
        3*4 = 1*4 + 2*4 = 4 + 1*4 + 1*4 = 4 + 4 + 4 = 12
"""

def min_product(a, b):
    bigger = a if a > b else b
    smaller = b if b < a else a
    memo = [0 for i in range(smaller + 1)]
    return min_product_helper(smaller, bigger, memo)

def min_product_helper(smaller, bigger, memo):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    elif memo[smaller] > 0:
        return memo[smaller]
    s = smaller >> 1
    side1 = memo[s] if memo[s] > 0 else min_product_helper(s, bigger, memo) 
    side2 = side1 if smaller % 2 == 0 else min_product_helper(smaller - s, bigger, memo)
    memo[smaller] = side1 + side2
    return memo[smaller]

print(min_product(999, 23))