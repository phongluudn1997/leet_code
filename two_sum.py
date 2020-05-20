# Given an array and a number, find in the array two number that sums up the number


class Solution:
    def double_loop_approach(self, array, num):
        """ O(n^2) time | O(1) space """
        for i in range(0, len(array) - 1):
            first_number = array[i]
            for j in range(i + 1, len(array)):
                second_number = array[j]
                if first_number + second_number == num:
                    return [first_number, second_number]
        return []

    def hash_table_approach(self, array, target_number):
        """ O(n) space | O(n) time """
        hash_table = dict()
        for num in array:
            potential_number = target_number - num
            if potential_number in hash_table:
                return [potential_number, num]
            else:
                hash_table[num] = True
        return []

    def two_pointer_approach(self, array, target_number):
        """ O(nlog(n)) time | O(1) space """
        array.sort()
        left_pointer = 0
        right_pointer = len(array) - 1
        while left_pointer < right_pointer:
            current_sum = array[left_pointer] + array[right_pointer]
            if current_sum == target_number:
                return [array[left_pointer], array[right_pointer]]
            elif current_sum < target_number:
                left_pointer += 1
            elif current_sum > target_number:
                right_pointer -= 1
        return []


array = [1, 8, 3, -2, 7, 14]
number = 6
solution_instance = Solution()

print(f'approach #1: {solution_instance.double_loop_approach(array, number)}')
print(f'approach #1: {solution_instance.hash_table_approach(array, number)}')
print(f'approach #1: {solution_instance.two_pointer_approach(array, number)}')
