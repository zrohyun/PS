class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        # nums.sort()
        numscnt = Counter(nums)
        nums[:] = [0]*numscnt[0] + [1]*numscnt[1] + [2]*numscnt[2]
        
