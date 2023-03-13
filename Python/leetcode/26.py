from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        bag = set()
        for i, n in enumerate(nums):
            if n in bag:
                continue
            else:
                bag.add(n)
        ans = len(bag)
        nums[:] = sorted(list(bag)) + ["_"] * (len(nums) - ans)

        return ans
