import collections


def first_uniq_char(s):
    hash_table = collections.Counter(s)
    for k, v in enumerate(s):
        if hash_table[v] == 1:
            return k
    return -1

print(first_uniq_char('leetocde'))