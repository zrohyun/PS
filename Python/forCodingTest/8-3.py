# def solution():
#     n = int(input())
#     store = list(map(int, input().split()))
#     store = store[::-1]
#     return rec_sum(store)


# def rec_sum(store):
#     if len(store) < 3:
#         return max(store)

#     return max(store[0] + rec_sum(store[2:]), rec_sum(store[1:]))

# print(solution())

def solution():
    n = int(input())
    store = list(map(int, input().split()))
    dp = [0]*100
    dp[0] = store[0]
    dp[1] = max(store[:2])
    for i in range(2,n):
        dp[i] = max(dp[i-1],dp[i-2]+store[i])
    
    return dp[n-1]