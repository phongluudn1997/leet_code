"""
Đề bài: Cho một array, một number, sắp xếp array để đẩy number ve phia cuoi array.
input: [2,1,2,2,2,3,4,2] vs 2 
output: [1,3,4,2,2,2,2,2]
"""


def useTwoPointer(list, num):
    left = 0
    right = len(list) - 1
    while left < right:
        if list[right] == num:
            right -= 1
        if list[left] == num:
            list[left], list[right] = list[right], list[left]
            left += 1
            right -= 1
        else:
            left += 1
    return list


result = useTwoPointer([2, 1, 2, 2, 2, 3, 4, 2], 2)
print(result)
