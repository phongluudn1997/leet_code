class Solution:
    @classmethod
    def approach_1(cls, n):
        """
        :type n = int
        :rtype = bool
        """
        if n > 3 and n % 3 == 0:
            return Solution.approach_1(n / 3)
        if n == 3 or n == 1:
            return True
        return False

    @classmethod
    def approach_2(cls, n):
        return n > 0 and 3**19 % n == 0

    @classmethod
    def approach_3(cls, n):
        while(n % 3 == 0):
            n /= 3
        return n == 1


result = Solution.approach_2(9)
print(result)
