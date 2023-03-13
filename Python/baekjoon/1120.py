import math
def solution(a,b):
    
    dif = len(b) - len(a)
    min_ = 987654321
    for i in range(dif+1):
        min_ = min(min_,sum(map(lambda x,y: 0 if x ==y else 1 , a,b[i:i+len(a)])))
        # print(a,b[i:i+len(a)],min_)
        
    return min_


a,b = list(map(str,input().split()))
print(solution(a,b))
"""
adaabc aababbc
hello xello
koder topcoder
abc topabcoder
giorgi igroig
"""
