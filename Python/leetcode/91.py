from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:

        """
        condition
        letter decode 1 to 26
        """
        # word_dict = {}
        # for i in range(26):
        #     chr_ = chr(65 + i)
        #     word_dict[str(i + 1)] = chr_

        # 65 is offset of A
        word_dict = {str(i + 1): chr(65 + 1) for i in range(26)}

        s_len = len(s)
        dp = [0] * s_len

        if s_len > 2 and dp[1] != "0":
            if s[0] in word_dict:
                dp[0] = 1

        for i in range(1, s_len):
            if s[i] == "0":
                continue

            if i + 1 < s_len:
                if s[i + 1] != "0":
                    if s[i] in word_dict:
                        dp[i] += dp[i - 1] + 1
            else:
                dp[i] += dp[i - 1] + 1

            if i + 2 < s_len:
                if s[i + 2] != "0":
                    if s[i : i + 2] in word_dict:
                        dp[i] += dp[i - 2] + 1
            else:
                dp[i]

        print(dp[-1])
        return dp[-1]


Solution().numDecodings("11106")


class Solution1:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        h = {str(i + 1): chr(65 + 1) for i in range(26)}

        # O(2^N) time, O(N) space DFS solution. Caching reduces it to O(N) time
        @cache
        def traverse(i):
            if i >= n:
                return 1

            ans = 0
            if s[i] in h:
                ans += traverse(i + 1)
            if i + 1 < n and s[i] + s[i + 1] in h:
                ans += traverse(i + 2)
            return ans

        return traverse(0)
