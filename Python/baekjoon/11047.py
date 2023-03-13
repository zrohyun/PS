
def solution():
    ans = 0
    N, K = list(map(int,input().split()))
    coins = [int(input()) for _ in range(N)]

    for i in coins[::-1]:
        ans += (K // i)
        K %= i



    return ans

print(solution())