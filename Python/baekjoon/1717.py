import sys

input = sys.stdin.readline


def solution():

    n, m = map(int, input().split())

    parent = [i for i in range(n + 1)]

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px > py:
            parent[py] = px
        else:
            parent[px] = py

    for _ in range(m):
        op, a, b = map(int, input().split())

        if op == 0:  # union
            union(a, b)
        else:
            print("YES") if find(a) == find(b) else print("NO")


solution()
