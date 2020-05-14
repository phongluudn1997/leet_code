class Solution:
    def addDigits(self, num: int) -> int:
        def sum_of_num(n):
            result = 0
            while n > 0:
                result += n % 10
                n = (n - n % 10) / 10
            return int(result)
        res = sum_of_num(num)
        if res < 10:
            return res
        else:
            print('res = {}'.format(res))
            return self.addDigits(res)


def sum_of_num(n):
    result = 0
    while n > 0:
        result += n % 10
        n = (n - n % 10) / 10
    return int(result)


res = Solution().addDigits(199)
print(res)
