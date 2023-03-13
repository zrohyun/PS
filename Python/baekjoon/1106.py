import math
from sys import stdin
input = stdin.readline
def solution():
    c,n = list(map(int,input().split()))
    dp = [987654321]*1001

    # 비용, 얻을  수 있는 고객 수  
    costs = [list(map(int,input().split())) for _ in range(n)]
    
    for i in range(1,c+1):
        for x,y in costs:
            if i >= y:
                dp[i] = min(dp[i],dp[i-y] + x)
            dp[i] = min(dp[i],math.ceil(i/y)*x)
            
        assert dp[i] == min(*[dp[i-y] + x for x,y in costs if i >= y] , *[math.ceil(i/y)*x for x,y in costs])
    return dp[c]

print(solution())
