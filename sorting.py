

class Sorting(object):

    @classmethod
    def bubble_sort(cls, nums):
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    @classmethod
    def selection_sort(cls, nums):
        for i in range(len(nums)):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[min_index] > nums[j]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

    @classmethod
    def insertion_sort(cls, nums):
        for i in range(1, len(nums)):
            pos = i
            while pos > 0 and nums[pos - 1] > nums[pos]:
                nums[pos], nums[pos - 1] = nums[pos - 1], nums[pos]
                pos -= 1
        return nums

    @classmethod
    def merged_sort(cls, nums):
        # divide
        def divide(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) // 2
            left, right = arr[:mid], arr[mid:]
            return left, right
        return divide(nums)


print(Sorting.insertion_sort([4, 3, 2, 1]))
