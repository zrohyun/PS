from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         check = dict()
        
#         for i in nums:
#             if i in check:
#                 return True
#             else:
#                 check[i] = 1
#         return False

        if len(set(nums)) == len(nums):
            return False
        return True
        
        # from collections import Counter
        # if Counter(nums).most_common(1)[0][1] == 1:
        #     return False
        # return True