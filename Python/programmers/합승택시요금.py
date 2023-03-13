from heapq import heappush, heappop
from collections import defaultdict


def solution(n, s, a, b, fares):
    g = [[int(1e10)] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        g[i][i] = 0

    for c, d, f in fares:
        g[c][d] = f
        g[d][c] = f

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    ans = int(1e10)
    for i in range(1, n + 1):
        # print(s,a,b,i)
        ans = min(ans, g[s][i] + g[i][a] + g[i][b])

    return ans
