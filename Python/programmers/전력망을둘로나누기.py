def solution(n, wires):
    """
    condition
    n [2,100]
    1 <= v1 < v2 <= n
    """
    g = [[0] * (n + 1) for _ in range(n + 1)]

    for i, j in wires:
        set_g(g, i, j, 1)

    answer = 1e10
    for s, d in wires:
        set_g(g, s, d, 0)
        visited = [False] * (n + 1)

        q = [(i, node) for i, node in enumerate(g[s]) if node == 1]
        linked = 0 if q else 1

        while q:
            i, node = q.pop()
            if visited[i]:
                continue

            visited[i] = True
            linked += 1
            for i, node in enumerate(g[i]):
                if node:
                    q.append((i, node))

        answer = min(answer, abs(n - 2 * linked))

        set_g(g, s, d, 1)

    return answer


def set_g(g, s, d, n):
    g[s][d] = n
    g[d][s] = n


# uf = []

# def find(a):
#     global uf
#     if uf[a] < 0: return a
#     uf[a] = find(uf[a])
#     return uf[a]

# def merge(a, b):
#     global uf
#     pa = find(a)
#     pb = find(b)
#     if pa == pb: return
#     uf[pa] += uf[pb]
#     uf[pb] = pa

# def solution(n, wires):
#     global uf
#     answer = int(1e9)
#     k = len(wires)
#     for i in range(k):
#         uf = [-1 for _ in range(n+1)]
#         tmp = [wires[x] for x in range(k) if x != i]
#         for a, b in tmp: merge(a, b)
#         v = [x for x in uf[1:] if x < 0]
#         answer = min(answer, abs(v[0]-v[1]))

# return answer

# def solution(n, wires):
#     ans = n
#     for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
#         s = set(sub[0])
#         [s.update(v) for _ in sub for v in sub if set(v) & s]
#         ans = min(ans, abs(2 * len(s) - n))
#     return ans
