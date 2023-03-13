from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        comp = strs[0]
        for s in strs[1:]:
            prefix = ""
            for a,b in zip(comp,s):
                if a==b: prefix += a
                else: break
            comp = prefix
            if not len(comp): break
                    
        return comp
            
"""
other solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = min(strs, key=len)
        s=0
        for each in range(len(result)):
            p=0
            for ind in strs:
                if ind[each]==(strs[0])[each]:
                    p=p+1
                else:
                    break
            if p==len(strs):
                s=s+1
            else:
                break
        if s==0:
            return("")
        else:
            return((strs[0])[0:s])
"""