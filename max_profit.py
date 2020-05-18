class Solution:
    def max_profit(self, list_price):
        max_current = max_so_far = 0

        for i in range(1, len(list_price)):
            max_current = max(0, max_current + list_price[i] - list_price[i - 1])
            max_so_far = max(max_current, max_so_far)
        return max_so_far


print(Solution().max_profit([7, 1, 5, 3, 6, 4]))
