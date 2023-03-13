from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Dynamic Programming Solution
        
        dp = nums
        
        for i in range(1,len(nums)):
            dp[i] = max(dp[i],dp[i-1] + dp[i])
        
        return max(nums)
        
        # dp = [0]*len(nums)
        # dp[0] = nums[0]
        # for i,v in enumerate(nums[1:]):
        #     if (s := dp[i] + v) >= 0:
        #         dp[i+1] = max(v,s)
        #     else:
        #         dp[i+1] = v
        # return max(dp)

        # cur = 0
		# maxSum = max(nums) # if all numbers are negatives, then max(nums) is the result
    
		# for i in range(0,len(nums)):
		# 	cur += nums[i]
		# 	if cur > maxSum:
		# 		maxSum = cur
		# 	if cur < 0: # if current value is smaller than 0, then it cannot contribute to provide the max subarray
		# 		cur = 0

		# return maxSum