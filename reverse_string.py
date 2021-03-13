class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])


solution = Solution()
result = solution.reverseString(["h", "e", "l", "l", "o"])
print(result)
