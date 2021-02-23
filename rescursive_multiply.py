"""
    Find the result of mulitiply operator not using * / just + - and >> <<
"""

def min_product(a, b):
    bigger = a if a > b else b
    smaller = b if b < a else a
    return min_product_helper(smaller, bigger)

def min_product_helper(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    s = smaller >> 1
    side1 = min_product_helper(s, bigger) 
    side2 = side1 if smaller % 2 == 0 else min_product_helper(smaller - s, bigger)
    return side1 + side2

print(min_product(17, 23))