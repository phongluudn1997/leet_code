from decorators import working_time


class Solution:
    @classmethod
    def approach_1(cls, nums):
        result = [0 for i in nums]
        for i, v in enumerate(nums):
            for j in nums:
                if j < v:
                    result[i] += 1
        return result

    @classmethod
    @working_time
    def approach_2(cls, nums):
        count = [0] * 102
        for num in nums:
            count[num + 1] += 1
        print(count)
        for i in range(1, 102):
            count[i] += count[i - 1]
        print(count)
        return [count[num] for num in nums]

    @classmethod
    @working_time
    def approach_3(cls, nums):
        dct = dict()
        for i, v in enumerate(sorted(nums)):
            if v not in dct:
                dct[v] = i
            return [dct[v] for v in nums]


print(Solution.approach_2([6, 1, 5, 3, 2, 7, 8, 5]))
