"""
https://leetcode.com/problems/move-zeroes/discuss/172432/THE-EASIEST-but-UNUSUAL-snowball-JAVA-solution-BEATS-100-(O(n))-%2B-clear-explanation
"""


class Solution:
    def move_zeroes(self, nums):
        size = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                size += 1
            else:
                # swap with the most left 0
                nums[i-size], nums[i] = nums[i], nums[i-size]
        return nums


solution = Solution()
result = solution.move_zeroes([1, 2, 3, 4, 0, 2, 3, 0, 1, 2])
print(result)
