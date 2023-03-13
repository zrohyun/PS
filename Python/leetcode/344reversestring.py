from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


"""
Using Recursion

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i=0
        j=len(s)-1
        def rev(s,i,j):
            if i>=j:
                return
            s[i],s[j]=s[j],s[i]
            rev(s,i+1,j-1)
        rev(s,i,j)
Using Iteration

class Solution:
    def reverseString(self, s: List[str]) -> None:
       
        size = len(s)
        for i in range(size//2):
            s[i], s[-i-1] = s[-i-1], s[i]
Two Pointer

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i,j=0,len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
Using Python

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:]=s[::-1]

"""