def solution():
    n, m = list(map(int, input().split()))

    INF = int(1e10)

    graph = [[INF] * n for _ in range(n)]

    # self connection
    for i in range(n):
        graph[i][i] = 0

    # graph link
    for i in range(m):
        s, d = list(map(int, input().split()))
        graph[s - 1][d - 1] = 1
        graph[d - 1][s - 1] = 1

    # 최종 목적지 x, 중간 소개팅 k
    x, k = list(map(int, input().split()))

    for r in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][r] + graph[r][b])

    ans = graph[0][k - 1] + graph[k - 1][x - 1]
    return ans if ans < INF else -1


print(solution())
