from bisect import bisect_right

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        dp = [0] * (n + 1)
        end_times = [job[1] for job in jobs]
        for i in range(1, n + 1):
            start, end, p = jobs[i - 1]
            idx = bisect_right(end_times, start)
            dp[i] = max(dp[i - 1], dp[idx] + p)
        return dp[n]


# Teste rápido
if __name__ == "__main__":
    sol = Solution()
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    print("Max Profit:", sol.jobScheduling(startTime, endTime, profit))