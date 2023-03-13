from collections import deque
from heapq import heappush, heappop
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        return self.dp_ver(nums, k)
        # return self.heapq_ver(nums,k)
        # return self.dp_ver_TLE(nums,k)

    def dp_ver(self, nums: list[int], k: int) -> int:
        q = deque([nums[0]])
        # print(nums)
        for i in range(1, len(nums)):

            # 현재 시점 i, i까지의 윈도우 사이즈 시작점 i-k+1
            # 즉, q[0]이 i-k번째의 값이라면 pop해주어야 함.
            if q and i >= k + 1 and q[0] == nums[i - k - 1]:
                q.popleft()

            nums[i] += q[0]

            while q and q[-1] < nums[i]:
                q.pop()

            q.append(nums[i])

            print(q)
        print(nums)
        return nums[-1]

    def heapq_ver(self, nums: List[int], k: int) -> int:

        # heap 사용
        q = [(-nums[0], 0)]

        for i in range(1, len(nums)):

            if i <= k:
                nums[i] += -q[0][0]
            else:
                while q[0][1] < i - k:
                    # 현재 지점에서 벗어나는 최대값 삭제
                    heappop(q)
                nums[i] += -q[0][0]

            heappush(q, (-nums[i], i))

        return nums[-1]

    def dp_ver_TLE(self, nums: List[int], k: int) -> int:

        """
        dp -> time limit exeeded
        deque로 해도 TLE
        """
        dp = copy.deepcopy(nums)
        a = deque([nums[0]], maxlen=k)

        for i in range(1, len(nums)):

            dp[i] = max(a) + dp[i]
            a.append(dp[i])

        print(dp)
        return dp[-1]


Solution().maxResult([1, -1, -2, 4, -7, 3], k=2)
