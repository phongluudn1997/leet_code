def approach_1(amount, denoms):
    return recursive(amount, denoms, 0)
def recursive(amount, denoms, index):
    if index >= len(denoms):
        return 1
    else:
        denom_amount = denoms[index]
        ways = 0
        i = 0
        while i * denom_amount <= amount:
            remain = amount - i * denom_amount
            i = i + 1
            ways += recursive(remain, denoms, index + 1)
        return ways

print(approach_1(11, [1, 2, 5]))