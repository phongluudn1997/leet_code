def coin_change(amount, coins, memo={}):
    if amount in memo: return memo[amount]
    if amount == 0: return 0
    if amount < 0: return None

    shortest_path = None

    for coin in coins:
        remainder = amount - coin
        remainder_combination = coin_change(remainder, coins, memo)
        if remainder_combination is not None:
            path = 1 + remainder_combination
            shortest_path = path if shortest_path is None or path < shortest_path else shortest_path

    memo[amount] = shortest_path
    return memo[amount]




# print(coin_change(3, [1,2]))
# print(coin_change(0, [1,2]))
print(coin_change(5, [4,3]))
