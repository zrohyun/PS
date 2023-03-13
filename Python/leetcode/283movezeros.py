from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import deque, Counter
        zcnt = nums.count(0)
        tmp = []
        for n,v in enumerate(nums):
            if v:
                tmp.append(v)
        
        nums[:] = tmp[:] + [0]*zcnt

"""
other solution
l=0
        for r in range(len(nums)):
            if nums[r]:
                #print(nums[r])-->picks only +ve values(then swap)
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
        return nums

#2
i = count = 0
        while count < len(nums):
            if nums[i] == 0: nums.append(nums.pop(i))
            else: i += 1
            count += 1

"""