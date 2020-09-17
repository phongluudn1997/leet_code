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


def longestPeak(array):
    # Solution of Algo but it's not worked!
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue
        leftIndex = i - 2
        while leftIndex >= 0 and array[leftIndex] < array[leftIndex + 1]:
            leftIndex -= 1

        rightIndex = i + 2
        while rightIndex < len(array) and array[rightIndex] < array[rightIndex - 1]:
            rightIndex += 1

        currentPeakLength = rightIndex - leftIndex + 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIndex
    return longestPeakLength


if __name__ == '__main__':
    print(longestPeak([5, 4, 3, 2, 1]))
