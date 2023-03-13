import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    M = int(input())
    g = {i: set() for i in range(1, N + 1)}
    parent = {i: i for i in range(1, N + 1)}

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)

        if px != py:
            parent[px] = py
            g[py] = g[py].union(g[px])

    for i in range(1, N + 1):
        cities = map(int, input().split())
        for j, n in enumerate(cities, start=1):
            if n == 1:
                g[i].add(j)
                g[j].add(i)
                union(i, j)

    route = list(map(int, input().split()))
    for i in range(M - 1):
        if find(route[i]) != find(route[i + 1]):
            return "NO"
    return "YES"


print(solution())
