class Solution:
    @classmethod
    def recursive(cls, nums):
        """
        :type nusm: List(int)
        :rtype: int
        """
        def max_at_i(nums, index):
            if index == 0:
                return nums[index]
            if index < 2:
                return max(nums[0], nums[1])
            return max(nums[index] + max_at_i(nums, index - 2), max_at_i(nums, index - 1))
        return 0 if len(nums) == 0 else max_at_i(nums, len(nums) - 1)

    @classmethod
    def top_down(cls, nums):
        hash_table = dict()

        def max_at_i(index):
            if index == 0:
                return nums[index]
            if index < 2:
                return max(nums[0], nums[1])
            if index in hash_table:
                return hash_table[index]
            return max(nums[index] + max_at_i(index - 2), max_at_i(index - 1))
        return 0 if len(nums) == 0 else max_at_i(len(nums) - 1)


result = Solution.top_down([183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66,
                            90, 238, 168, 128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211])
print(result)
