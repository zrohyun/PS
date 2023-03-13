# def solution(N, M, K, X, g):
#     """
#     시간초과
#     """

#     city = [[int(1e10)] * (N + 1) for _ in range(N + 1)]
#     for i in range(1, N + 1):
#         city[i][i] = 0
#     for s, d in g:
#         city[s][d] = 1

#     for k in range(1, N + 1):
#         for s in range(1, N + 1):
#             for d in range(1, N + 1):
#                 city[s][d] = min(city[s][d], city[s][k] + city[k][d])
#     ans = []
#     for i, n in enumerate(city[X][1:], start=1):
#         if n == K:
#             ans.append(str(i))

#     if ans:
#         print("\n".join(ans))
#     else:
#         print(-1)

from heapq import heappush, heappop
from collections import deque


def solution(N, M, K, X, g):
    route = [int(1e10)] * (N + 1)
    route[X] = 0

    q = deque([X])
    while q:
        now = q.popleft()
        for d in g[now]:
            if route[d] == int(1e10):
                route[d] = route[now] + 1
                q.append(d)

    # 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
    check = False
    for i in range(1, N + 1):
        if route[i] == K:
            print(i)
            check = True

    # 만약 최단 거리가 K인 도시가 없다면, -1 출력
    if check == False:
        print(-1)


if __name__ == "__main__":
    N, M, K, X = map(int, input().split())
    g = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, d = list(map(int, input().split()))
        g[s].append(d)

    solution(N, M, K, X, g)
