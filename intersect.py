from collections import Counter


def intersect(nums1, nums2):
    hash_table = Counter(nums1)
    result = list()
    for i in nums2:
        if i in hash_table and hash_table[i] > 0:
            result.append(i)
            hash_table[i] -= 1
    return result


def intersect1(nums1, nums2):
    a, b = map(Counter, (nums1, nums2))
    c = (a & b).elements()
    print(list(c))


intersect1([1, 2, 1, 3, 4], [1, 2, 1, 1, 2, 3])

res = intersect([1, 2, 4, 3, 3], [1, 3, 2, 3])
print(res)
