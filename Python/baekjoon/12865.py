def solution():
    N, K = map(int, input().split())
    goods = [[0, 0]]
    for i in range(N):
        goods.append(list(map(int, input().split())))

    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            w = goods[i][0]
            v = goods[i][1]

            if j < w:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            print_dp(dp)

    return dp[-1][-1]


def print_dp(dp):
    for i in dp:
        print(i)
    print()


solution()
