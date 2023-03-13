from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i,v in enumerate(nums):
        #     try:
        #         a = nums.index(target - nums[i])
        #         if  a != -1 and a != i :
        #             return sorted([i,a])
        #     except:
        #         continue
        # nums[i:].index(x) + i => 이런식으로 했어도 됐을 듯
        log = dict()
    
        for i ,v in enumerate(nums):
            m = target - nums[i]
            # print(log)
            if v in log:
                return [log[v],i]
  
            else:
                log[m] = i