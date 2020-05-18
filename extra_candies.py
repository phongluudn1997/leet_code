class Solution:
    def kids_with_candies(self, candies, extra_candies):
        max_candy = max(candies)
        return [candy + extra_candies >= max_candy for candy in candies]


print(Solution().kids_with_candies([4, 2, 1, 1, 2], 1))
