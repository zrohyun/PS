#https://leetcode.com/problems/binary-search/submissions/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        try:
            i =  nums.index(target)
            return i
        except:
            return -1

        # self binary search 꼴등 
        # s,e = 0,len(nums)-1
        
        # while s<=e:
            
        #     p = (s+e)//2
        #     if nums[p] == target:
        #         return p
        #     elif nums[p] < target:
        #         s = p+1
        #     else:
        #         e = p-1
        # return -1
        """
        import bisect
        bl = bisect.bisect_left(nums,target)
        # br = bisect.bisect_right(nums,target)

        if bl == len(nums): return -1
        
        if nums[bl] == target:
            return bl
        else:
            return -1
        """
print(Solution().search([-1,0,3,5,9,12],9))