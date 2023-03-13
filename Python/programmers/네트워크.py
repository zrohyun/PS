def solution(n, computers):
    answer = 0

    parent = [i for i in range(n)]

    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)

        if px != py:
            if px <= py:
                parent[px] = py
            else:
                parent[py] = px

    for a in range(n * n):

        i = a // n
        j = a % n

        if i == j:
            continue

        if computers[i][j]:
            union(i, j)

    for i in range(n):
        find(i)

    return len(set(parent))
