def is_anagram(s, t):
    if len(s) != len(t):
        return False
    hash_table = dict()
    for i in s:
        if i in hash_table.keys():
            hash_table[i] += 1
        else:
            hash_table[i] = 1
    print(hash_table)
    for i in t:
        if i not in hash_table.keys():
            return False
        else:
            hash_table[i] -= 1
    for value in hash_table.values():
        if value != 0:
            return False
    return True


def is_anagram_2(s, t):
    return sorted(s) == sorted(t)


print(is_anagram_2('hello', 'lloeh'))
