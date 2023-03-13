class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        
        x = list(str(x))
        
        while x:
            if len(x) == 1:
                return True
            
            if x[0] == x.pop():
                x = x[1:]
            else:
                return False
        
        return True

"""
return str(x) == str(x)[::-1]
return False if x < 0 else x == int(str(x)[::-1])
"""