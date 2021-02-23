"""
Write a method to return all subsets of a set.
"""

def get_subsets(set):
    if len(set) == 0:
        return [[]]

    result = get_subsets(set[:-1])

    for i in get_subsets(set[:-1]):
        i.append(set[-1])
        result.append(i)

    return result

def subsets(set):
    if not len(set):
        return [[]]
    else:
        # compute P(n-1) and clone result
        n = set[-1]
        cloned_set = subsets(set[:-1])

        # add a(n) to each cloned sets.
        new_set = [i + [n] for i in cloned_set]
        
        # return cloned set + new set
        return cloned_set + new_set

print(subsets([1]))
print(subsets([1, 2]))
print(subsets([1, 2, 3]))

