class Solution:

    def merge_two_sorted_list_2(self, a, b):
        i = j = 0
        result = list()

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        while i < len(a):
            result.append(a[i])
            i += 1
        while j < len(b):
            result.append(b[j])
            j += 1

        return result


print(Solution().merge_two_sorted_list([1, 3, 6], [2, 4, 5]))
