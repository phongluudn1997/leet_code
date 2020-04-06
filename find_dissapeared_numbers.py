class Solution:

    @classmethod
    def approach_1(cls, nums):
        hash_table = dict()
        result = list()
        for i in range(1, len(nums) + 1):
            hash_table[i] = 0
        print(hash_table)
        for i in nums:
            hash_table[i] += 1
        print(hash_table)
        for i in range(1, len(nums) + 1):
            if hash_table[i] == 0:
                result.append(i)
        return result

    @classmethod
    def approach_2(cls, nums):
        result = [i for i in range(1, len(nums) + 1)]
        for i in nums:
            try:
                result.remove(i)
            except Exception:
                pass
        return result

    @classmethod
    def approach_3(cls, nums):
        nums = [0] + nums
        print(nums)
        for i in range(len(nums)):
            index = abs(nums[i])
            nums[index] = -abs(nums[index])
            print(nums)
        return [i for i in range(len(nums)) if nums[i] > 0]

    @classmethod
    def approach_4(cls, nums):
        nums = [0] + nums
        for i in range(len(nums)):
            print(nums[nums[i]])
            nums[nums[i]] = -1
        print(nums)
        return [i for i in range(len(nums)) if nums[i] > 0]


print(Solution.approach_4([4, 3, 2, 7, 8, 2, 3, 1]))
