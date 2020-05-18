class Solution:
    def de_compress_RLE_list(self, nums):
        result = []
        for i in range(0, len(nums), 2):
            result += [nums[i + 1] for j in range(nums[i])]
        return result


print(Solution().de_compress_RLE_list([1, 2, 3, 4]))
