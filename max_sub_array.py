from decorators import working_time


@working_time
def approach_1(nums):
    hash_table = dict()
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            hash_table[(i, j)] = sum([nums[k] for k in range(i, j + 1)])
    return max(hash_table.values())


@working_time
def approach_2(nums):
    def find_sum(nums):
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                yield sum([nums[k] for k in range(i, j + 1)])
    max = nums[0]
    for i in find_sum(nums):
        if i > max:
            max = i
    return max


@working_time
def approach_3(nums):
    def find_i():
        for i in range(len(nums)):
            yield i

    def find_j():
        for i in find_i():
            for j in range(i, len(nums)):
                yield i, j

    def find_max():
        maximum = nums[0]
        for i, j in find_j():
            total = 0
            for k in range(i, j + 1):
                total += nums[k]
            maximum = total if total > maximum else maximum
        return maximum
    return find_max()


@working_time
def approach_4(nums):
    max = nums[0]
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            total = sum([nums[k] for k in range(i, j + 1)])
            max = total if total > max else max
    return max


@working_time
def approach_5(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


@working_time
def approach_6(nums):
    dp = [i for i in nums]
    dp[0] = nums[0]
    maximum = dp[0]
    for i in range(1, len(nums)):
        dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)
        print(maximum)
        print(dp)
        maximum = max(maximum, dp[i])
    return maximum


res = approach_6([1, 2, -1, 4])
print(f'result: {res}')
