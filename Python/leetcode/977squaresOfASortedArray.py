from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #return sorted([v**2 for v in nums])
        return sorted(map(lambda x: x**2,nums))