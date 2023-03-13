from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort(reverse=True)

        #         for idx in range(len(nums) - 2):

        #             if nums[idx] < nums[idx+1] + nums[idx+2]:
        #                 return sum(nums[idx:idx+3])

        for a, b, c in zip(nums, nums[1:], nums[2:]):
            if a < b + c:
                return a + b + c
        return 0