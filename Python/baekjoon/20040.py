import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def solution():
    n, m = map(int, input().split())

    parent = [i for i in range(n)]

    def find(x):
        # if x != parent[x]:
        #     parent[x] = find(parent[x])
        px = x
        while px != parent[px]:
            px = parent[px]

        parent[x] = px
        return px

    def union(x, y):
        px, py = find(x), find(y)

        if px != py:
            parent[px] = py

    for i in range(1, m + 1):
        s, d = map(int, input().split())

        if find(s) == find(d):
            return i

        union(s, d)

    return 0


ans = solution()
print(ans)
