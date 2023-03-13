from heapq import heappop as hpop, heappush as hpush

# 도시분할 계획
def solution():
    """
    condition
    n개의 집과 m개의 link
    m개의 link는
    a,b,c의 공백 a-b 연결하는 유지비 c
    """
    n, m = map(int, input().split())
    q = []
    parent = [i for i in range(n)]
    for i in range(m):
        a, b, c = map(int, input().split())
        hpush(q, (c, a, b))

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        roota, rootb = find(a), find(b)
        if roota != rootb:
            if roota < rootb:
                parent[rootb] = roota
            else:
                parent[roota] = rootb

    ans = 0
    remain_path = []
    last = 0
    while q:
        c, a, b = hpop(q)

        if find(a - 1) == find(b - 1):
            continue

        union(a - 1, b - 1)
        ans += c
        last = c
        remain_path.append((a, b, c))

    print(remain_path)
    return ans - last


print(solution())

"""
input sample
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4 
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

"""
