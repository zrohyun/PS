import sys
from collections import defaultdict
from heapq import heappush,heappop

input = sys.stdin.readline


def solution():
    """
    V,E input first line
    Start Vertex number input second line
    (u,v,w) E number of Edges starting from  line 3
    """
    V, E = map(int, input().split())
    SV = int(input())
    graph = [[0] * (V + 1) for i in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u][v] = w

    d = graph[SV]
    hq = [(SV,0)]

    while hq:

        current ,v = heappop(hq)
        v = -v

        if d[current] < v:
            continue

        for i in range(1,V+1):

            





if __name__ == "__main__":
    pass
