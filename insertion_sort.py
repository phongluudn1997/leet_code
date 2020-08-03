def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1
    return array


def swap(idx1, idx2, array):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp


insertion_sort_array = insertion_sort([4, 3, 1, 6, -2, 9, 15])
print(insertion_sort_array)
