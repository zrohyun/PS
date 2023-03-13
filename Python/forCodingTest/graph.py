from heapq import heappop, heappush


def minimun_spanning_tree():
    """
    https://velog.io/@jiggyjiggy/Data-Structure-Algorithm-신장-트리-크루스칼-알고리즘-shortest-path
    # Kruskal Algorithm
    # edges[i] = (cost,src v, dst v)
    """

    v, e = list(map(int, input().split()))
    parent = [i for i in range(v)]

    edges = []

    # min heap tree
    for _ in range(e):
        cost, a, b = map(int, input().split())
        heappush(edges, (cost, a, b))

    def find(x):
        if x == parent[x]:
            return x

        parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        roota, rootb = find(a), find(b)
        if roota != rootb:
            if roota > rootb:
                parent[rootb] = roota
            else:
                parent[roota] = rootb

    result = []
    while edges:
        cost, a, b = heappop(edges)

        if find(a - 1) == find(b - 1):
            continue

        union(a - 1, b - 1)
        result.append((cost, a, b))

    print(result)


# minimun_spanning_tree()


def topological_sort():
    pass


def disjoint_set():
    v, e = map(int, input().split())
    parent = [i for i in range(v)]

    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        roota, rootb = find(a), find(b)

        if roota != rootb:
            if roota < rootb:
                parent[roota] = rootb
            else:
                parent[rootb] = roota

    edges = []
    for i in range(e):
        a, b = map(int, input().split())
        edges.append((a, b))

    for edge in edges:
        s, d = edge
        if find(s - 1) != find(d - 1):
            union(s - 1, d - 1)

        print(parent)


disjoint_set()
