class Solution:
    def busy_student(self, start_time, end_time, query_time):
        busy_student = 0
        for i in range(len(start_time)):
            busy_student += 1 if start_time[i] <= query_time <= end_time[i] else 0
        return busy_student


print(Solution().busy_student(start_time=[9, 8, 7, 6, 5, 4, 3, 2, 1], end_time=[
      10, 10, 10, 10, 10, 10, 10, 10, 10], query_time=5))
