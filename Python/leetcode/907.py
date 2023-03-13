from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans, stack = [], []
        for i, x in enumerate(arr):
            while stack and arr[stack[-1]] >= x:
                stack.pop()  # mono-stack (increasing)
            if stack:
                ii = stack[-1]
                ans.append(ans[ii] + x * (i - ii))
            else:
                ans.append(x * (i + 1))
            stack.append(i)
        return sum(ans) % 1_000_000_007


Solution().sumSubarrayMins([3, 1, 2, 4])
