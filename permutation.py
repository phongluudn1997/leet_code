<<<<<<< HEAD
def permuatation(nums):
    res = []

    def dfs(nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)
    dfs(nums, [], res)
    return res


print(permuatation([1, 2, 3]))
=======
def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


for i in all_perms([1, 2, 3, 4, 5, 6]):
    print(i)
>>>>>>> 7eac51a27f00e9ebb4979826c76995a503258203
