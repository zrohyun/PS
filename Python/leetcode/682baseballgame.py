class Solution:
    from typing import List
    def calPoints(self, ops: List[str]) -> int:

        stack = []
        
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))

        return sum(stack)
        # expc = lambda : stack.pop()
        # expd = lambda : stack.append(stack[-1]*2)
        # expp = lambda : stack.append(sum(stack[-2:]))
        
        # exp = {
        #     "C": expc,
        #     "D": expd,
        #     "+": expp
        #       }
        
        # for i in ops:
        #     if i in exp:
        #         exp[i]()
        #     else:
        #         stack.append(int(i))
        #     # if i.isnumeric() or self.isnegativenum(i):
        #     #     stack.append(int(i))
        #     # else:
        #     #     exp[i]()
        
        return sum(stack)
    
    def isnegativenum(self, num) -> bool:
        return num.replace('-','').isnumeric()
    
    