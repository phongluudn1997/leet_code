class Solution:
    def subtract_product_and_sum(self, n):
        def get_numbers(number):
            while number > 0:
                num = number % 10
                number = int((number - number % 10) / 10)
                yield num

        def get_products_of_digits():
            product = 1
            for i in get_numbers(n):
                product *= i
            return product

        def get_sum_of_digits():
            sum = 0
            for i in get_numbers(n):
                sum += i
            return sum

        return get_products_of_digits() - get_sum_of_digits()

    def approach_2(self, n):
        product = 1
        sum = 0
        while n > 0:
            product *= n % 10
            sum += n % 10
            n //= 10
        return product - sum


result = Solution().approach_2(234)
print(result)
