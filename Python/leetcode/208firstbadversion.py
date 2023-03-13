#https://leetcode.com/problems/first-bad-version/submissions/
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s,e = 1,n
        
        while s<=e:
            
            p = (s+e)//2

            if isBadVersion(p):
                # if not isBadVersion(p-1):
                #     return p
                e = p-1
            else:
                s = p+1
        return s