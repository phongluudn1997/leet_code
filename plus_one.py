class Solution:
    def plus_one(self, digits):
        def transfer_to_number(digits):
            number = 0
            for i in range(len(digits)):
                number = number * 10 + digits[i]
            return number

        def trans_to_digits(number):
            digits = list()
            while number > 0:
                digits.append(number % 10)
                number //= 10
            return digits
        new_number = transfer_to_number(digits) + 1
        return trans_to_digits(new_number)[::-1]


result = Solution().plus_one([1, 2, 3, 4])
print(result)
