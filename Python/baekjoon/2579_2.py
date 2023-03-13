def solution_v():
    """
    계단 오르기
    """
    N = int(input())
    S = [0] + [int(input().rstrip()) for _ in range(N)]
    dp = [[0, 0, 0] for _ in range(N + 1)]

    if N == 1:
        return S[N]

    # dp[k][1] = max(dp[k-2][2] , dp[k-2][1]) + S[k]
    # dp[k][2] = dp[k-1][1] + S[k]

    dp[1][1] = S[1]
    dp[1][2] = 0
    dp[2][1] = S[2]
    dp[2][2] = S[1] + S[2]

    for k in range(3, N + 1):
        dp[k][1] = max(dp[k - 2][2], dp[k - 2][1]) + S[k]
        dp[k][2] = dp[k - 1][1] + S[k]

    return max(dp[N][1], dp[N][2])


ans = solution_v()
print(ans)
