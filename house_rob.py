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

    @classmethod
    def top_down_memoization(cls, nums):
        hash_table = dict()

        if len(nums) < 1:
            return 0

        def max_at(index):
            if index in hash_table:
                return hash_table[index]
            elif index < 1:
                return nums[index]
            elif index == 1:
                return max(nums[0], nums[1])
            else:
                result = max(nums[index] + max_at(index - 2), max_at(index - 1))
                hash_table[index] = result
                print(hash_table)
                return result
        return max_at(len(nums) - 1)

    @classmethod
    def bottom_up_memoization(cls, nums):
        if len(nums) < 1:
            return 0
        hash_table = dict()

        def max_at(i):
            if i == 0:
                return nums[i]
            elif i == 1:
                return max(nums[0], nums[1])
            for index in range(2, i + 1):
                result = max(nums[index] + max_at(index - 2), max_at(index - 1))
                hash_table[index] = result
            return hash_table[i]
        return max_at(len(nums) - 1)

    @classmethod
    def bottom_up_two_variables(cls, nums):
        if len(nums) < 1:
            return 0

        max_at_i_1 = nums[0]
        max_at_i_2 = nums[1]

        for i in range(2, len(nums)):
            current = max(nums[i] + max_at_i_2, max_at_i_1)
            max_at_i_2, max_at_i_1 = max_at_i_1, current

        return current


result = Solution.bottom_up_two_variables([1, 3, 4, 5, 6])
print(result)
