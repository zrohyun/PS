def solution():
    n = int(input())
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 3
    if n < 3: return dp[n]

    for i in range(3,n+1):
        dp[i] = (dp[i-2] * 2 + dp[i-1]) % 796796
    print(dp)
    return dp[n]
print(solution())
