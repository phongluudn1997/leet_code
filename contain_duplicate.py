def contain_duplicate(nums):
    hash_table = dict()
    for i in nums:
        if i in hash_table.keys():
            return True
        else:
            hash_table[i] = 1
    return False


def contain_duplicate_1(nums):
    set_nums = set()
    for i in nums:
        if set_nums.__contains__(i):
            return True
        set_nums.add(i)
    return False


def contain_duplicate_2(nums):
    return len(nums) != len(set(nums))


print(contain_duplicate_2([1, 2, 3, 4, 5]))
