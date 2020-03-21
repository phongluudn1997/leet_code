def max_profit(prices):
    max_profit = 0
    for ind, val in enumerate(prices):
        if val > prices[ind - 1]:
            max_profit += val - prices[ind - 1]
    return max_profit


profit = max_profit([7, 1, 5, 3, 6, 4])
print(profit)
