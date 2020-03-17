class Solution:
    def reverse_string(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def reverse_string_1(self, s):
        for index, value in enumerate(s):
            if index < len(s) / 2:
                s[index], s[len(s) - 1 - index] = s[len(s) -
                                                    1 - index], s[index]
        return s


solution = Solution()
result = solution.reverse_string_1(['a', 'b', 'c', 'd', 'e'])
print(result)
