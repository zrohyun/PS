class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        
        pairs = {'(':')','[':']','{':'}'}
        stack = deque([])
        
        for i in s:
            if i in pairs:
                stack.append(i)
            elif not stack: 
                return False
            else:
                if i != pairs[stack.pop()]:
                    return False
        
        # if stack: return False
        
        return not stack