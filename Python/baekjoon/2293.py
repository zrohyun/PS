from sys import stdin
input = stdin.readline
def solution():
    n,k = list(map(int,input().split()))
    coins = [int(input().rstrip()) for _ in range(n)]
    coins = [c for c in coins if c <= k]
    # print(n,k, coins)
    dp = [0]*(k+1)
    dp[0] = 1
    # for i in range(1,k+1):
    #     for c in coins:
    #         if i>c:
    #             dp[i] += dp[i - c]
    #         elif i == c: 
    #             dp[i] +=1
    
    # 가격을 중심으로 올라가다 보면 중복 처리에 대해서 고민하고
    # 그 중복을 제거하는 것이 쉽지 않다.
    # 그렇다면 작은 동전부터 그 동전만 사용하여 가격을 구성하는 것부터 생각하면 된다.
    # 그렇다면 1,2,3 동전으로 6원을 만든다고 했을 때 111111, 1122,222,33,3111,11112 321
    #   원  1 2 3 4 5 6
    # 1.1원 1 1 1 1 1 1 
    # 2.2원 1 1 2 3 4 5
    # 3.3원 1 2 3 4 5 7
    # 3원 story -> 1원으로 만드는 경우 1 + 2원으로 만드는 경우 1 + 3원으로 만드는 경우 1
    for i in range(len(coins)):
        for j in range(coins[i],k+1):
            dp[j] += dp[j-coins[i]]
    return dp[k]

print(solution())
    