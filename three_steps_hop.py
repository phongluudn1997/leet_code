class Solution:
    def count_ways(self, nth_step):
        if nth_step < 0:
            return 0
        elif nth_step == 0:
            return 1
        else:
            return self.count_ways(nth_step - 3) + self.count_ways(nth_step - 2) + self.count_ways(nth_step - 1)


print(Solution().count_ways(37))
