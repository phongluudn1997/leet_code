from collections import defaultdict


class Solution(object):
    def single_number(self, nums):
        hash_table = dict()
        for i in nums:
            hash_table[i] = 1 if i not in hash_table.keys(
            ) else hash_table[i] + 1
        for k, v in hash_table.items():
            if v == 1:
                return k

    def single_number_1(self, nums):
        return 2 * sum(set(nums)) - sum(nums)


solution = Solution()
result = solution.single_number_1([2, 2, 5, 3, 3, 4, 4])
print(result)
