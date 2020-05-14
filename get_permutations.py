def get_permutations(list_number):
    permutations = list()
    if len(list_number) <= 1:
        permutations.append(list_number)
        return permutations

    for index in range(len(list_number)):
        element = list_number[index]
        remainder = list_number[:index] + list_number[index + 1:]
        for permutation in get_permutations(remainder):
            permutations.append([element] + permutation)
    return permutations


# print(get_permutations([1, 2, 3]))


# Approach #2:
"""
    Remember each permutation always lack the last element
    Ex: P(a1a2) = a2 + P(a1) = a2a1 and a1a2
    which `+ operator` means insert a2 into every index in all permutations of P(a1)
"""


def get_perms(string):
    # Base case:
    list_permutations = list()
    if len(string) == 1:
        list_permutations.append(string)
        return list_permutations
    first_char = string[0]
    remainder = string[1:]
    print(f'fist: {first_char}, remainder: {remainder}')

    def insert_char_at_index(char, index, word):
        return word[:index] + char + word[index:]

    for perm in get_perms(remainder):
        print(f'perm: {perm}')
        for index in range(len(perm) + 1):
            list_permutations.append(insert_char_at_index(char=first_char, index=index, word=perm))
    return list_permutations


print(get_perms('abc'))
