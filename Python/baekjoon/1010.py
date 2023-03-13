import math
from sys import stdin
input = stdin.readline
def solution():
    N = int(input())
    for _ in range(N):
        N,M = tuple(map(int, input().split()))
        # M개 중 N개 선택 조합
        # mCn
        facto = math.factorial
        
        def mulm2n(m,n=1):
            ans = 1
            for i in range(n+1,m+1):
                ans *=i
            return ans
        
        ans = int(facto(M)/(facto(M-N)*facto(N)))
        # ans = int(mulm2n(M,M-N) / mulm2n(N))
        # assert ans == ans1
        print(ans)


solution()