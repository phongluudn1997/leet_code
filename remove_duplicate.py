class Solution:
    def remove_duplicates(self, nums):
        set_nums = set()
        i = 0
        while i < len(nums):
            if set_nums.__contains__(nums[i]):
                nums.pop(i)
                i -= 1
            else:
                set_nums.add(nums[i])
            i += 1
        return len(nums)

    def approach_2(self, nums):
        """
        :type nums: List(int) -> sourted
        :rtype: int
        """
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        print(nums)
        return i + 1


solution = Solution()
print(solution.approach_2(
    [0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4]))
