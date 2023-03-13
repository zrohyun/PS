mod = 10**9 + 7
from collections import deque
from functools import cache


class Solution:
    # Simple top down Dynamic Programming Solution in Python
    # Base Case is you completing the n throws to get the target sum
    # Hence base case should return 1
    # For initial cases add a number that can come on the dice and see if it can take you to the base case

    def numRollsToTarget1(self, n: int, k: int, target: int) -> int:
        @cache
        def helper(currsum, d):
            if d == n:
                return 1 if currsum == target else 0

            ways = 0
            for i in range(1, min(k + 1, target - currsum + 1)):
                ways += helper(currsum + i, d + 1)
            return ways % mod

        return helper(0, 0)

    from collections import deque

    def numRollsToTarget(self, n, k, target):
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for i in range(1, min(k + 1, target + 1)):
            dp[1][i] = 1

        for i in range(2, n + 1):
            for j in range(i, min(i * k + 1, target + 1)):
                # dp[i][j] = sum([dp[i-1][j-q] for q in range(1,k+1) if j-q>=0])%mod
                for q in range(1, k + 1):
                    if j - q >= 0:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - q]) % mod

        # print(dp)
        # print(dp[-1][-10:])
        return dp[-1][-1]

    def memoryless(self, n, k, target):
        dp = deque([[0] * (target + 1)])

        for i in range(1, min(k + 1, target + 1)):
            dp[-1][i] = 1

        for i in range(2, n + 1):
            save = [0] * (target + 1)
            for j in range(i, min(i * k + 1, target + 1)):
                for q in range(1, k + 1):
                    if j - q >= 0:
                        save[j] = (save[j] + dp[-1][j - q]) % mod

            dp.append(save)
            dp.popleft()


"""
refer
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/2650021/Python-Easy-Solution-Explained
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/2648360/Python-oror-Easily-Understood-oror-Faster-than-96-oror-using-DP
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/2649136/Python-or-Triple-loop-DP
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/2649168/Python3%3A-Faster-than-99.35
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/2649360/Python-Simple-Python-Solution
신기한 코드
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/2651831/Python-DP-or-O(N-*-Target)


"""
