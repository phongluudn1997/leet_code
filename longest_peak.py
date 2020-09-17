"""
Tìm longest peak vd:
1,2,3,3,4,0,10,6,5,-1,-3,2,3
=> Longest peak 0, 10, 6, 5,-1,-3
Chiến thuật:
Step1: Tìm tất cả các peaks
Step2: So sánh xem thử thằng nào dài nhất.
"""


def find_longest_peak(array):
    def find_all_peaks():
        if array[0] > array[1]:
            yield 0
        for i in range(1, len(array) - 2):
            if array[i] > array[i - 1] and array[i] > array[i + 1]:
                yield(i)
        if array[-1] > array[-2]:
            yield(len(array) - 1)

    def find_length_of_peak(peak):
        left = peak - 1
        right = peak + 1
        length = 1

        while left >= 0 and array[left] < array[left + 1]:
            left -= 1
            length += 1

        while right <= len(array) - 1 and array[right] < array[right - 1]:
            right += 1
            length += 1

        return length

    return max([find_length_of_peak(peak) for peak in find_all_peaks()])


if __name__ == '__main__':
    print(find_longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
