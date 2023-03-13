# 여행경로
# 1. set(모든 공항)
# 2. 모든 공항 수 ^2
# 3. 배열 생성
# 4. 노드 값 삽입.
from calendar import different_locale
import copy
import enum
from copy import deepcopy


matrix = []


def solution1(tickets):

    # init
    global matrix
    airtport_arr = []
    for i in tickets:
        for j in i:
            airtport_arr.append(j)
    airtport_arr = sorted(list(set(airtport_arr)))
    airtport_arr.remove("ICN")
    airtport_arr = ["ICN"] + airtport_arr

    matrix = [[0] * len(airtport_arr) for _ in range(len(airtport_arr))]
    name_2_idx = {name: idx for idx, name in enumerate(airtport_arr)}
    idx_2_name = {idx: name for idx, name in enumerate(airtport_arr)}

    for src, dst in tickets:
        src_idx = airtport_arr.index(src)
        dst_idx = airtport_arr.index(dst)
        matrix[src_idx][dst_idx] = 1

    print(matrix)

    print(airtport_arr)
    answer = []
    return answer


def dfs(src):
    global matrix
    dst = [i for i, x in enumerate(matrix[src]) if x == 1]

    if len(dst) == 0:
        return src

    for i in dst:
        matrix[src][i] = 0
        dfs(i)
        matrix[src][i] = 1


from heapq import heappush, heappop
from collections import defaultdict


def solution(tickets):
    answer = []
    # airports = set([t[0] for t in tickets] +[t[1] for t in tickets])

    g = defaultdict(list)
    for s, d in tickets:
        g[s].append(d)

    for s, _ in tickets:
        sorted(g[s])

    def dfs(graph, c, d):
        if len(graph[c]) == 0:
            return [c] if d == 0 else -1

        for i in graph[c]:
            graph[c].remove(i)
            a = dfs(graph, i, d - 1)
            if a != -1:
                return [c] + a

            graph[c].append(i)
            sorted(graph[c])

    return dfs(g, "ICN", len(tickets))


def solu(tickets):
    g = defaultdict(list)
    for s, d in tickets:
        g[s].append(d)

    # for s, _ in tickets:
    #     g[s].sort()

    def dfs(graph, c, d):
        if len(graph[c]) == 0:
            return [c] if d == 0 else -1

        lup = sorted(copy.deepcopy(graph[c]))
        for i in lup:
            # temp = graph[c]
            # graph[c] = temp
            graph[c].remove(i)
            a = dfs(graph, i, d - 1)
            if a != -1:
                return [c] + a
            graph[c].append(i)

        return -1

    print(dfs(g, "ICN", len(tickets)))


a = solu(
    [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
)
print(a)

a = solu(
    [
        ["ICN", "AAA"],
        ["ICN", "CCC"],
        ["CCC", "DDD"],
        ["AAA", "BBB"],
        ["AAA", "BBB"],
        ["DDD", "ICN"],
        ["BBB", "AAA"],
    ]
)
print(a)
