"""
Give array, find if it is monotonic array (non-increase or non-decrease)
Ex: [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
"""


def isMonotonicArray(array):
    if len(array) <= 2:
        return True
    for i in range(2, len(array) - 1):
        if (array[i] - array[i - 1]) * (array[i - 1] - array[i - 2]) < 0:
            return False
    return True


potential_monotonic = [1, 5, 10, 1100, 900, 1101, 1102, 9001]
result = isMonotonicArray(potential_monotonic)
print(result)
