# 팀 결성
def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    parent = [i for i in range(n)]

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootx, rooty = find(x), find(y)
        if rootx != rooty:
            if rootx < rooty:
                parent[rooty] = rootx
            else:
                parent[rootx] = rooty

    ans = []
    for i in range(m):
        o, a, b = map(int, input().split())
        if o == 0:
            union(a - 1, b - 1)
        elif o == 1:
            if find(a - 1) == find(b - 1):
                ans.append("YES")
            else:
                ans.append("NO")

    return ans


print(solution())


"""
input
7 8 
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""
