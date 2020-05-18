class Solution:
    def find_numbers(self, nums):
        def is_even_number_of_digit(number):
            print(number)
            number_of_digit = 0
            while number > 0:
                number_of_digit += 1
                number //= 10
            print(f'-> {number_of_digit % 2}')
            return number_of_digit % 2 == 0

        result = 0
        for num in nums:
            result += 1 if is_even_number_of_digit(num) else 0
        return result

    def approach_2(self, nums):
        result = 0
        for num in nums:
            result += 1 if num in range(10, 100) or num in range(1000, 10000) else 0
        return result


result = Solution().approach_2([12, 345, 2, 6, 7896])
print(result)
