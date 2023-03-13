import bisect
from math import ceil,sqrt
from re import I
def solution():

    for n in range(2**65):
        
        if  not (n & (n-1)): 
            print(n)
        s = 0
        e = n


        try:
            a = ceil(sqrt(n))
            assert s  == a
        except:
            print(s,a)

def bis(n):
    s,e = 0,n
    while s <= e:
        mid = (s + e) // 2
        if mid ** 2 < n:
            s = mid + 1
        else:
            e = mid - 1
    return s

def cesq(n):
    return ceil(sqrt(n)) 

import timeit
n = 2**64
st = timeit.default_timer()
bis(n)
end = timeit.default_timer()
a = end-st
cesq(n)
b = timeit.default_timer()-end
print(a>b)

# solution()