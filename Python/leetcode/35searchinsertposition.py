#https://leetcode.com/problems/search-insert-position/
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        import bisect as b
        return b.bisect_left(nums,target)

