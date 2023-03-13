def solution():
    x = int(input())
    if x == 0:
        print(1)
    else:
        res = 1
        for i in range(1,x+1):
            res *= i
        print(res)

import sys
sys.setrecursionlimit(10000)
from functools import lru_cache
@lru_cache(maxsize=None)
def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n-1)

print(facto(10))