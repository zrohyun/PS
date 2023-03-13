import sys
from collections import defaultdict

input = sys.stdin.readline


def solution():

    f = int(input())
    num = defaultdict(lambda: 1)
    parent = defaultdict(str)

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            num[py] += num[px]
        # if px > py:
        #     parent[py] = px
        #     num[px] += num[py]
        # elif px < py:
        #     parent[px] = py
        #     num[py] += num[px]

        return parent[px]

    for _ in range(f):
        a, b = map(str, input().rstrip().split())
        parent.setdefault(a, a)
        parent.setdefault(b, b)
        p = union(a, b)

        print(num[p])


for _ in range(int(input())):
    solution()
