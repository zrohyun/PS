from re import I


def solution():
    n = int(input())
    ans = 0
    while True:

        if n % 5 == 0:
            return ans + n //5
        
        if n % 3 == 0: 
            ans += 1
            n -= 3
            continue
        
        if n > 5:
            ans += 1
            n -= 5
        elif n > 3:
            ans += 1
            n -= 3
        else:
            return -1
def solution2():
    n = int(input())
    ans = 0
    while True:
        
        if n == 0: return ans
        if n<3: return -1
        if n %5 ==0 : return ans + n//5

        n -= 3
        ans +=1


def solution_dp():
    n = int(input())

    if n ==3:return 1
    elif n ==4: return -1

    dp = [-1] * (n+1)
    dp[3] = dp[5] = 1

    for i in range(6, n+1):
        # if dp[i-3] and dp[i-5]:
        #     dp[i] = min(dp[i-3]+1, dp[i-5]+1)
        # elif dp[i-3]:
        #     dp[i] = dp[i-3] +1        
        # elif dp[i-5]:
        #     dp[i] = dp[i-5] + 1

        if min(dp[i-3]+1, dp[i-5]+1):
            dp[i] = min(dp[i-3], dp[i-5]) + 1
        elif max(dp[i-3]+1, dp[i-5]+1):
            dp[i] = max(dp[i-3], dp[i-5]) + 1


    # print(list(range(n+1)))
    # print(dp)
    
    return dp[n]
    #return dp[n] if dp[n] else -1 # list of zero
    


# print(solution())
print(solution_dp())
    
