"""
Write a method to return all subsets of a set.
"""

def print_decorator(fn):
    def wrapper(*args):
        print(fn(*args))
    return wrapper

def get_subsets(set):
    if len(set) == 0:
        return [[]]

    result = get_subsets(set[:-1])

    for i in get_subsets(set[:-1]):
        i.append(set[-1])
        result.append(i)

    return result
