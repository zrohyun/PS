from sys import stdin
input = stdin.readline

def solution():
    n,k = list(map(int,input().split()))
    coins = [int(input().rstrip()) for _ in range(n)]
    coins = sorted(list(set(coins)))
    dp = [int(1e9)]*(k+1)
    dp[0] = 0
    for c in coins:
        for i in range(c,k+1):
            dp[i] = min(dp[i],dp[i-c]+1)
     
    return dp[k] if dp[k] != int(1e9) else -1

print(solution())