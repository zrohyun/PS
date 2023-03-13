def solution():
    pass


import collections, heapq


def minCostPath(g_nodes, g_from, g_to, g_weight, x, y):
    INF = float("inf")

    n, e = g_nodes, len(g_from)

    g = collections.defaultdict(list)

    for s, d, w in zip(g_from, g_to, g_weight):
        g[s].append([d, w])
        g[d].append([s, w])

    v1, v2 = x, y

    def dijkstra(s):
        dist = [INF] * (g_nodes + 1)
        dist[s] = 0
        q = [[dist[s], s]]
        while q:
            u = heapq.heappop(q)[1]
            for v, c in g[u]:
                if dist[v] > dist[u] + c:
                    dist[v] = dist[u] + c
                    heapq.heappush(q, [dist[v], v])
        return dist

    def solve():
        from_1 = dijkstra(1)
        from_v1 = dijkstra(v1)
        from_v2 = dijkstra(v2)

        path1 = from_1[v1] + from_v1[v2] + from_v2[n]
        path2 = from_1[v2] + from_v2[v1] + from_v1[n]

        result = min(path1, path2)

        if result < INF:
            return result
        else:
            return -1

    return solve()


from heapq import heappush, heappop


def minCostPath(g_nodes, g_from, g_to, g_weight, x, y):
    # Write your code here
    print(g_weight)
    INF = float("inf")

    def dijkstra(start, end):
        dis = [INF] * (g_nodes + 1)
        dis[start] = 0
        q = [[0, start]]
        while q:
            k, u = heappop(q)
            if k > dis[u]:
                continue
            for w, v in G[u]:
                if dis[v] > dis[u] + w:
                    dis[v] = dis[u] + w
                    heappush(q, [dis[v], v])

        return dis[end]

    G = [[] for _ in range(g_nodes + 1)]
    for s, d, w in zip(g_from, g_to, g_weight):
        G[s].append([w, d])
        G[d].append([w, s])

    # 1 -> x -> y -> N
    path1 = dijkstra(1, x) + dijkstra(x, y) + dijkstra(y, g_nodes)

    # 1 -> y -> x -> N
    path2 = dijkstra(1, y) + dijkstra(y, x) + dijkstra(x, g_nodes)

    if path1 >= INF and path2 >= INF:
        return -1
    else:
        return min(path1, path2)


print(solution())
