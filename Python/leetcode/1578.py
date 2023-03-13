class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        return self.minCost_dpver(colors, neededTime)

    #         idx = 0
    #         cnt = 0

    #         while idx < len(colors):
    #             tmp = 0
    #             nxt = idx + 1

    #             # add all times of the same colors for removing
    #             while nxt < len(colors) and colors[nxt] == colors[idx]:
    #                 tmp += neededTime[nxt-1]
    #                 nxt+=1
    #             tmp += neededTime[nxt-1]

    #             # and remain maximum color balloon
    #             cnt += tmp - max(neededTime[idx:nxt])
    #             idx = nxt

    # return cnt

    def minCost_dpver(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        dp = [0] * n

        cur = colors[0]
        curmax = neededTime[0]
        for i in range(1, n):

            if cur == colors[i]:
                dp[i] = dp[i - 1] + min(curmax, neededTime[i])
                curmax = max(curmax, neededTime[i])

            else:
                dp[i] = dp[i - 1]
                curmax = neededTime[i]
                cur = colors[i]
        print(dp)
        return dp[-1]


"""
refer
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/discuss/2653885/Python-Solution-with-min-heap
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/discuss/2653821/Python-Greedy-O(n)-Time-or-Beats-98
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/discuss/2654028/Python-Solution
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/discuss/2653800/Python-Made-Easy-O(n)-or-Stack-based-or-Greedy-approach-or-Explained
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/discuss/2653692/Python-O(n)-dp

"""
