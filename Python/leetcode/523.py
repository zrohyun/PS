class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        idx = {0: -1}
        cur = 0
        for i, num in enumerate(nums):
            cur = (cur + num) % k
            if cur in idx:  # 이전에 동일한 나머지가 나왔던 기록이 있으면 그 구간을 빼주면 된다.
                if i - idx[cur] > 1:
                    return True
            else:
                idx[cur] = i
        return False
