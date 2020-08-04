def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
            array[min_index], array[i] = array[i], array[min_index]
    return array


array = [1, -4, 8, 13, -23]
sorted_array = selectionSort(array)
print(sorted_array)
