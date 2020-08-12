def usingTwoPointer(array, target):
    sorted_array = sorted(array)
    result = list()
    for index in range(0, len(sorted_array) - 2):
        current_number = sorted_array[index]
        left = index + 1
        right = len(sorted_array) - 1
        while left < right:
            current_sum = current_number + sorted_array[left] + sorted_array[right]
            if current_sum == target:
                result.append([current_number, sorted_array[left], sorted_array[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return result


if __name__ == '__main__':
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    result = usingTwoPointer(array, 0)
    print(result)
