def bubbleSort(array):
    i = len(array) - 1
    while i > 0:
        for j in range(i):
            if array[j] > array[j + 1]:
                swap(j, j + 1, array)
        i -= 1
    return array


def swap(idx1, idx2, array):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp


sorted_list = bubbleSort([4, -2, 1, 9, 5])
print(sorted_list)
