def solution():
    big_mod = 1000000000
    N = int(input())
    dp = [[0]*10 for _ in range(N)]
    dp[0] = [0,1,1,1,1,1,1,1,1,1]
    
    for n in range(1,N):
        for i in range(len(dp[n])):
            if i==0:
                dp[n][i] = dp[n-1][i+1]
            elif i == (len(dp[n])-1):
                dp[n][i] = dp[n-1][i-1]
            else:
                dp[n][i] = dp[n-1][i-1]+dp[n-1][i+1]
                
    
    ans = 0

    for i in dp[N-1]:
        ans = (ans + i) % big_mod
        
    return ans
    
    
    


print(solution())