"""
    Write a method to compute all permutations of a string of unique characters.
"""

def permuatation(nums):
    res = []

    def dfs(nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)
    dfs(nums, [], res)
    return res


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


def get_perms(str):
    if len(str) == 0:
        return []
    elif len(str) == 1:
        return [str]
    result = []
    last_character = str[-1]
    prev_perms = get_perms(str[:-1])
    for prev_perm in prev_perms:
        for i in range(len(prev_perm) + 1):
            result.append(prev_perm[:i] + last_character + prev_perm[i:])
    return result

# * Cracking the coding interview
def get_perms_cracking_code(str):
    if not str:
        return None
    permutations = []
    if not len(str):
        permutations.append('')
        return permutations
    if len(str) == 1:
        permutations.append(str)
        return permutations
    first_character = str[0]
    remain_characters = str[1:]
    words = get_perms_cracking_code(remain_characters)
    for word in words:
        for i in range(len(word) + 1):
            s = word[:i] + first_character + word[i:]
            permutations.append(s)
    return permutations


print(get_perms_cracking_code('123'))