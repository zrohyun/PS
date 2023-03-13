from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
#         b = nums[-k:]
#         a = nums[:-k]
#         nums[:len(b)] = b
#         nums[len(b):] = a
        nums[:] = nums[-k:] + nums[:-k]