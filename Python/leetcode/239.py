class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = []
        res = []
        # R points to the 'to-be-added' elem
        for R in range(len(nums)):
            # Pop nums[R-k] (if it is the head of the window !)
            if q and R >= k and q[0] == nums[R-k]:
                q.pop(0)

            # Push nums[R]
            # 1) pop all that are less than nums[R]
            while q and q[-1] < nums[R]:
                q.pop(-1)
            # 2) append nums[R]
            q.append(nums[R])

            # Save result, q[0] always is the largest in the window
            if R >= k-1:
                res.append(q[0])
        return res
