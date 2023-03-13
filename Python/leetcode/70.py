class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0, 1, 2, 3, 5, 8, 13]

        if n < len(dp):
            return dp[n]

        for i in range(7, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]

    def climbStairs_v1(self, n: int) -> int:
        one_step, two_step = 1, 1
        for i in range(n - 1):
            one_step, two_step = one_step + two_step, one_step
        return one_step

    def climbStairs_v2(self, n: int) -> int:
        # TLE(Time Limit Exceeded)
        1, 1, 2, 3
        if n < 3:
            return n

        return self.climbStairs_v2(n - 1) + self.climbStairs_v2(n - 2)
