class Solution:
    def move_zeroes(self, nums):
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
                print(nums)


solution = Solution()
solution.move_zeroes([1, 2, 3, 4, 0, 2, 3, 0, 1, 2])
