def solution(matrix_sizes):
    """
    dp 너무 어렵다.
    https://source-sc.tistory.com/24 - 참고

    """
    answer = 0
    dp = [[1e10] * len(matrix_sizes) for _ in range(len(matrix_sizes))]
    n = len(dp)
    for i in range(n):  # n-1개의 마지막 결합 형태
        for j in range(n - i):
            a = j
            b = j + i

            if a == b:
                dp[a][b] = 0

            for k in range(a, b):
                dp[a][b] = min(
                    dp[a][b],
                    dp[a][k]
                    + dp[k + 1][b]
                    + (matrix_sizes[a][0] * matrix_sizes[k][1] * matrix_sizes[b][1]),
                )

    return dp[0][-1]
