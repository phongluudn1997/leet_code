def find_substring(parent, child):
    for i in range(len(parent)):
        for j in range(len(child)):
            print(f'i: {i}, j: {j}')
            print(parent[i + j], child[j])
            if parent[i + j] != child[j]:
                break
            else:
                return i
    return -1


def find_sub(parent, child):
    for i in range(len(child)):
        for j in range(len(parent)):
            print(child[i], parent[j])
            if child[i] != parent[i + j]:
                break
            print(child[i])


res = find_substring('geeksfo', 'for')
print(res)
