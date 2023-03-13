def solution():
    n,m = list(map(int,input().split()))
    coins = [int(input()) for _ in range(n)]
    dp = [10000]*(m+1)
    dp[0] = 0
    coins.sort()
    for c in coins:
        for i in range(c,m+1):
            if dp[i-c] != 10000:
                dp[i] = min(dp[i],dp[i-c]+1)
    print(dp)
    return dp[m] if dp[m] != 10000 else -1
    

print(solution())