import sys

sys.setrecursionlimit(10000)


def solution():
    """
    이항 계수 2
    첫째 줄에 N,K가 주어진다.
    이항계수(N,K)의 10007로 나눈 나머지를 구하라.
    """
    N, K = map(int, input().split())

    def bino_coef_recur(n, k):
        if n == k or k == 0:
            return 1

        return bino_coef(n - 1, k) + bino_coef(n - 1, k - 1)

    cache = dict()

    # def bino_coef_with_cache(n, k):

    #     if (n, k) in cache:
    #         return cache[(n, k)]

    #     if n == k or k == 0:
    #         cache[(n, k)] = 1
    #         return 1

    #     cache[(n, k)] = (bino_coef_with_cache(n - 1, k) + bino_coef_with_cache(
    #         n - 1, k - 1
    #     )) % 10007

    #     return cache[(n, k)]

    def bino_coef(n, r):
        # 1.
        cache = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

        # 2.
        for i in range(n + 1):
            cache[i][0] = 1
        for i in range(r + 1):
            cache[i][i] = 1

        # 3.
        for i in range(1, n + 1):
            for j in range(1, r + 1):
                cache[i][j] = (cache[i - 1][j] + cache[i - 1][j - 1]) % 10007

        return cache[n][r]

    ans = bino_coef(N, K)
    # assert ans == bino_coef(N, K)
    return ans


ans = solution()
print(ans)
