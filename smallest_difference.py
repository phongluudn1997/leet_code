"""
Bài toán:
Cho 2 mảng với số lượng phần tử lần lượt là n và m. Tìm trong mỗi mảng một phần tử sao cho difference là nhỏ nhất.
<- Input:
first_list = [-1, 5, 10, 20, 28, 3]
second_list = [26, 134, 136, 15, 17]
-> Output: [28, 26]
Thuật toán: Sử dụng 2 pointer
B1: Sắp xếp 2 mảng theo chiều tăng dần
B2: Cho 2 con trỏ ở index đầu tiên của mỗi mảng gọi là left và right
B3: Tính difference, tăng index của pointer bên nào nhỏ hơn.
"""


def smallest_difference(l1, l2):
    l1 = sorted(l1)
    l2 = sorted(l2)
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idxOne < len(l1) and idxTwo < len(l2):
        firstNum = l1[idxOne]
        secondNum = l2[idxTwo]
        if firstNum > secondNum:
            current = firstNum - secondNum
            idxTwo += 1
        elif firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        else:
            return [firstNum, secondNum]
        if current < smallest:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair


if __name__ == "__main__":
    l1 = [-1, 5, 10, 20, 28, 3]
    l2 = [26, 134, 136, 15, 17]
    smallestPair = smallest_difference(l1, l2)
    print(smallestPair)
