#https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3
#Stack 사용

def solution():
    s = list(str(input()))
    stack = [s[0]]

    if len(s)%2: return 0

    for i in s[1:]:
        if len(stack) > 0 and stack[-1] == i: 
            stack.pop(i)
        else:
            stack.append(i)
    
    return 0 if len(stack) else 1

def functional_solution():
    from functools import reduce as rd
    s = list(str(input().strip()))
    if len(s)%2: return 0
    def remove(x,y):
        if len(x) > 0 and x[-1] == y:
            return x[:-1]
        else:
            return x+y
    
    return 0 if len(rd(remove,s)) else 1

# print(solution())
print(functional_solution())
