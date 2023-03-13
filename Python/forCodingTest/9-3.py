def solution():
    n, m, c = list(map(int, input().split()))
    INF = int(1e10)

    graph = [[INF] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    for _ in range(m):
        x, y, z = list(map(int, input().split()))
        graph[x - 1][y - 1] = z

    for k in range(n):
        for s in range(n):
            for d in range(n):
                graph[s][d] = min(graph[s][d], graph[s][k] + graph[k][d])

    print(graph)
    total_city = 0
    total_time = 0
    for i in graph[c - 1]:
        if i < INF:
            total_city += 1
            total_time = max(total_time, i)

    return total_city - 1, total_time


def solution_dijk():
    from heapq import heappop, heappush

    n, m, c = list(map(int, input().split()))
    INF = int(1e10)

    graph = [[] for _ in range(n)]

    distance = [INF] * n
    # distance[c - 1] = 0

    for _ in range(m):
        x, y, z = list(map(int, input().split()))
        graph[x - 1].append((y - 1, z))

    def dijkstra(start):
        q = []
        heappush(q, (0, start - 1))
        distance[start - 1] = 0
        while q:
            z, now = heappop(q)
            if z > distance[now]:
                continue

            for g in graph[now]:
                cost = z + g[1]
                if distance[g[0]] > cost:
                    distance[g[0]] = cost
                    heappush(q, (cost, g[0]))

    dijkstra(c)
    print(distance)


print(solution())
# print(solution_dijk())


""""""
#reimplementation

def dijkstra(start):
    n = 10
    dist = [1e10]*n
    g = [] #graph
    q = [(0,start)]
    while q:
        d,now = q.pop()
        if dist[now] < d:
            continue

        for weight,node in g[now]:
            if d + weight < dist[node]:
                dist[node] = d+weight
                q.append((d+weight,node))



