def solution():

    N = int(input())
    scores = [0] + list(map(int, [input() for i in range(N)]))
    #print(scores)
    #vs append
    dp = [0]*301

    if N==1:
        return scores[1]
    elif N==2: 
        return scores[1] + scores[2]
    
    dp[1] = scores[1]
    dp[2] = dp[1] + scores[2]
    
    num = 3
    while num <= N:

        dp[num] = max(scores[num-1] + scores[num]+ dp[num-3],dp[num-2]+scores[num])
        num+=1

    return dp[N]

print(solution())


N = int(input())

stair = [0]
for _ in range(N):
    stair.append(int(input()))

if N == 1:
    print(stair[1])
else:
    dp = [0] * (N+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2] 

    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])  

    print(dp[N])
