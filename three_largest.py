def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateThreeLargest(threeLargest, num)
    return threeLargest


def updateThreeLargest(array, num):
    if array[2] is None or num > array[2]:
        shiftAndUpdate(array, num, 2)  # TODO;
    elif array[1] is None or num > array[1]:
        shiftAndUpdate(array, num, 1)  # @TODO
    elif array[0] is None or num > array[0]:
        shiftAndUpdate(array, num, 0)


def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]


threeLargest = findThreeLargestNumbers([1, -14, 34, 251, 67, 92, -22])
print(threeLargest)
