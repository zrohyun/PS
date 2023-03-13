import math


class Solution:
    """
    two pointer solution
    두 가지 경우에 대해서 나누어 계산함.
    https://leetcode.com/problems/longest-palindromic-substring/discuss/2587483/Python-Two-Pointers-Solution-or-O(n2)-Time-or-O(1)-Space
    """

    def longestPalindrome(self, s: str) -> str:
        maxL = 0
        ans = ""
        for i in range(len(s)):
            # even len of substr "aba": no need to compare i
            subStr = self.isPalindrome(s, i - 1, i + 1)
            if len(subStr) > maxL:
                maxL = len(subStr)
                ans = subStr
            # odd len of substr "bb": need to compare i with i+1
            subStr = self.isPalindrome(s, i, i + 1)
            if len(subStr) > maxL:
                maxL = len(subStr)
                ans = subStr
        return ans

    def isPalindrome(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        # left, right have been moved. so need to l+1,r-1
        return s[left + 1 : right]


class Solution:
    """
    solution
    엄청 빠른 풀이지만 뭔소린지 모르겠다;
    """

    def longestPalindrome(self, s: str) -> str:
        t = "#".join("^{}$".format(s))
        print(t)  # 각 알파벳 사이에 #을 끼워넣음

        n = len(t)

        p = [0] * n
        c = r = 0

        for i in range(1, n - 1):
            print(c, r, i, p)
            if i < r:
                p[i] = min(r - i, p[2 * c - i])
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
            if i + p[i] > r:
                c, r = i, i + p[i]
            print(c, r, i, p)
        i = p.index(max(p))
        print(p)
        return s[(i - p[i]) // 2 : (i + p[i]) // 2]


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        """
        https://leetcode.com/problems/longest-palindromic-substring/discuss/1652109/Python-DP-120ms-(97.52)-TC%3A-O(N*K*K)-MC%3A-O(N)
        """
        n = len(s)
        dp = [(i, i) for i in range(n)]

        def isPalindrome(st):
            return st == st[::-1]

        for i in range(1, n):
            start = max(dp[i - 1][0] - 1, 0)
            for j in range(start, i):
                if isPalindrome(s[j : i + 1]):
                    dp[i] = (j, i)
                    break

        res = max(dp, key=lambda x: x[1] - x[0])
        return s[res[0] : res[1] + 1]


class Solution1:
    def longestPalindrome(self, s: str) -> str:
        """
        my solution
        dp를 2차원으로 memoization하는 것은 TLE(Time Limit Exceeded)
        dp를 1차원으로 바로 이전 알파벳에 대해서만 memoization하면 간신히 TLE를 넘김
        """

        dp = []

        # initial setting first letter
        # dp.append([1 if s[0] == s[i] else 0 for i in range(len(s))])

        max_len = 1  # 가장 긴 팰린드롬의 총 길이
        st_idx = 0  # 그 시작점

        for idx in range(len(s)):

            # affinity matrix is symmetric
            t = [0] * idx if idx else []

            for j in range(idx, len(s)):

                # 현재 단어(idx)와 짝이 될 단어(j) 비교
                if len(dp) == 0 or j == (len(s) - 1):
                    # Dont use dp, when first or last alphabet case
                    accum = 1 if s[idx] == s[j] else 0
                else:
                    # TLE version
                    # pal_len = 1 + dp[-1][j + 1] if s[idx] == s[j] else 0
                    accum = 1 + dp[j + 1] if s[idx] == s[j] else 0

                t.append(accum)
                # 2가지 케이스에 대해서 생각해야함.
                # 1. 가운데 알파벳 하나를 두고 팰린드롬
                #    이 경우 총 길이는 홀수, max 길이가 j==idx일 때 발생함. dp[i][j] = 1 + dp[i-1][j+1]
                #    총 단어의 길이는 (dp[i][j]*2 - 1)이 됨.
                #    시작 index는 현재 idx(==j) - (단어길이-1)//2
                # 2. 짝수개 팰린드롬.
                #    이 경우 총 길이는 짝수, max 길이가 j+1 == idx일 때 발생함. s[idx] == s[j]
                #    총 단어의 길이는 dp[i][j]*2(이전 단어비교에서 내려온 기억값 +1, 즉, 양쪽의 각 단어를 비교한 것이 더해져 왔으므로 *2만 해주면 됨)
                #    시작 index는 j(=idx+1) - 단어길이(=dp[i][j]*2)

                if j == idx:

                    # 길이가 홀수일 때
                    len_palin = accum * 2 - 1
                    if max_len < len_palin:

                        max_len = len_palin
                        st_idx = idx - (len_palin - 1) // 2

                    continue

                if (j == (idx + 1)) and (s[j] == s[idx]):
                    len_palin = accum * 2
                    if max_len < len_palin + 1:

                        max_len = len_palin
                        st_idx = (idx + 1) - len_palin // 2

            # TLE version
            # dp.append(t)
            dp = t

        ans = s[st_idx : st_idx + max_len]

        # print inform
        # for d in dp:
        #     print(d)
        # print(st_idx, max_len)
        # print("String " + s)
        # print("longgest palindrome: " + ans)

        return ans


for s in ["cbbd", "babababd", "ababad", "b", "bb"]:
    print(Solution2().longestPalindrome(s))


class Solution:
    """
    One pointer라는데..
    https://leetcode.com/problems/longest-palindromic-substring/discuss/2609291/Python-One-Pointer
    """

    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s) * 2):
            i = i / 2
            offset = i - int(i)
            while (i - offset) >= 0 and (i + offset) < len(s):
                if s[int(i - offset)] == s[int(i + offset)]:
                    offset = offset + 1
                else:
                    break

            if offset == 0.5 or offset == 0:
                continue
            offset = offset - 1
            if len(result) < (offset * 2 + 1):
                result = s[int(i - offset) : int(i + offset + 1)]
        return result
