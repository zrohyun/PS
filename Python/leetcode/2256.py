from math import floor
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left,right = 0,sum(nums)
        min_idx_val = (-1,1e10)
        for i in range(len(nums)):
            left += nums[i]
            right -= nums[i]
            if right != 0:
                mad = abs(left//(i+1) - right//(len(nums)-i-1))
            else:
                mad = abs(left//(i+1))
            if min_idx_val[1] > mad:
                min_idx_val = (i,mad)
        return min_idx_val[0]
			
			
			

ans = Solution().minimumAverageDifference([2,5,3,9,5,3])

print(ans)
