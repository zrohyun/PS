N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())

import math
def solution():
    ans = N
    for a in A:
        remain = a-B
        if remain<=0:
            continue

        ans += math.ceil(remain/C)
    print(ans)

solution()













