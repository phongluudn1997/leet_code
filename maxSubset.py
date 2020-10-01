"""
    Đề bài: Tìm các element trong array sao cho tổng của chúng là lớn nhất
    và các element không được gần nhau.

    Giải:
    Theo phương dinamic programming, chia bài toán thành nhiều bài toán nhỏ hơn.
    Công thức tìm maxSum ở phần tử thứ i:
        maxSum[i] = {
                        maxSum[i - 1]
                        or
                        maxSum[i - 2] + arr[i]
                    }

"""


# O(n) time | O(n) space
def findMaxSubset_1(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]

    maxSums = array[:]
    maxSums[0] = array[0]
    maxSums[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])

    return maxSums[-1]


# O(n) time | O(1) space
def findMaxSubset_2(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]

    first = array[1]
    second = array[0]
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first


if __name__ == '__main__':
    maxSum = findMaxSubset_2([7, 10, 12, 7])
    print(maxSum)
