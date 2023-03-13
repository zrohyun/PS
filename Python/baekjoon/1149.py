def solution():
    N = int(input())

    costs = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0]*3 for _ in range(1001)]
 
    dp[0] = costs[0]
 
    for i,(r,g,b) in enumerate(costs[1:]):
        dp[i+1] = [min(dp[i][1:])+r,min(dp[i][0],dp[i][2])+g,b+min(dp[i][:2])]
        


    print(min(dp[N-1]))


solution()

    