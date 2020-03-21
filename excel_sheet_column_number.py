from string import ascii_uppercase

'''
    @Question:
    Given a column title as appear in an Excel sheet,
    return its corresponding column number.

    For example:
        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28
        ...
    Example 1:

    Input: "A"
    Output: 1
    Example 2:

    Input: "AB"
    Output: 28
    Example 3:

    Input: "ZY"
    Output: 701
'''


def generate_hash_table() -> dict:
    hash_table = dict()
    for idx, val in enumerate(ascii_uppercase):
        hash_table[val] = idx + 1
    return hash_table


def title_to_number(title: str) -> int:
    hash_table = generate_hash_table()
    result = 0
    for idx, val in enumerate(title[::-1]):
        result += hash_table[val] * len(hash_table) ** idx
    return result


result = title_to_number('A')
print(result)
