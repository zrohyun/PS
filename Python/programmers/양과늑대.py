from collections import deque

"""
https://blog.encrypted.gg/1029
완전 탐색이 아닌 풀이
"""


def solution(info, edges):
    answer = 0
    n = len(info)
    tree = {i: [] for i in range(n)}
    for p, s in edges:
        tree[p].append(s)
    q = deque([[0, tree[0], 1, 0]])
    while q:
        now, nxt, sheep, wolf = q.popleft()
        if answer < sheep:
            answer = sheep
        for i, node in enumerate(nxt):
            if info[node] == 1:
                if sheep > wolf + 1:
                    q.append(
                        [node, nxt[:i] + nxt[i + 1 :] + tree[node], sheep, wolf + 1]
                    )
            else:
                q.append([node, nxt[:i] + nxt[i + 1 :] + tree[node], sheep + 1, wolf])

    return answer
