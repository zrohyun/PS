from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter
        from itertools import combinations as comb
        nums_cnt = Counter(nums)
        
        if k == 0:
            ans = 0
            for k,v in nums_cnt.items():
                if v > 1: ans +=1
            return ans
        else:
            ans = 0
            # for a,b in comb(nums_cnt.keys(),2):
            #     if abs(a-b) == k:
            #         ans += 1
            # return ans
            # li = list(nums_cnt.keys())
            # for i in range(len(li)):
            #     for j in range(i+1,len(li)):
            #         if abs(li[i] - li[j]) == k:
            #             ans += 1
            # return ans
            for a in nums_cnt:
                if a-k in nums_cnt:
                    ans +=1
            return ans
                

"""
Other Solution
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = collections.Counter(nums)
        # return sum(d.get(n-k,0) > (not k) for n in d)
        return sum(d[n-k] > (not k) for n in d)
"""        