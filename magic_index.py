def magic_index(array):
    if not len(array):
        return "No magic index found."
    middle_index = len(array) // 2
    if array[middle_index] == middle_index:
        return middle_index
    if array[middle_index] > middle_index:
        return magic_index(array[:middle_index])
    else:
        return magic_index(array[middle_index:])


print(magic_index([-1, 1, 2, 4]))