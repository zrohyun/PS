from cgitb import small
from sys import stdin

input = stdin.readline
INF = int(1e9)
distance = []


def solution():
    n, m = list(map(int, input().split()))
    st_node = int(input())

    graph = [[] for i in range(n + 1)]
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    # heap 이용가능
    def get_smallest_node():
        min_value = INF
        index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
        for i in range(1, n + 1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        import heapq

        distance[start] = 0

        # using heapq
        q = []
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue

            for b, c in graph[now]:
                cost = dist + c
                if cost < distance[b]:
                    distance[b] = cost
                    heapq.heappush(q, (cost, b))

        # visited[start] = True
        # for des,l in graph[start]:
        #     distance[des] = l
        # # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
        # for i in range(n - 1):
        #     # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        #     now = get_smallest_node()
        #     visited[now] = True
        #     # 현재 노드와 연결된 다른 노드를 확인
        #     for j in graph[now]:
        #         cost = distance[now] + j[1]
        #         # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
        #         if cost < distance[j[0]]:
        #             distance[j[0]] = cost

    dijkstra(st_node)

    # 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if distance[i] == INF:
            print("INF")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(distance[i])


def my_implementation():
    n, m = list(map(int, input().split()))
    st_node = int(input())
    start = input()
    graph = [[] for i in range(n + 1)]
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    # 간선 정보 입력 받기
    # a to b, c is cost
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    # get shortest node from current node in unvisited
    def smallest_node() -> int:
        MIN_VAL = INF
        idx = 0
        for i in range(1, n + 1):
            if not visited[i] and distance[i] <= MIN_VAL:
                MIN_VAL = distance[i]
                idx = i
        return idx

    def dijkstra(start):
        distance[start] = 0
        visited = True
        # init distance from starting node
        for g in graph[start]:
            distance[g[0]] = g[1]

        for i in range(n - 1):
            now = smallest_node()
            visited[now] = True

            for j in graph[now]:
                cost = distance[now] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

    dijkstra(start)


def implementation_with_heapq():
    from heapq import heapify, heappop, heappush

    n, m = list(map(int, input().split()))
    st_node = int(input())
    start = input()
    graph = [[] for i in range(n + 1)]
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    # 간선 정보 입력 받기
    # a to b, c is cost
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    def dijkstrak(start):
        q = []
        heappush(q, (0, start))
        distance[start] = 0
        while q:
            d, now = heappop(q)

            # heap에 의해 이미 처리된 node라면
            # q에 추가된 d보다 작아 먼저 처리되었을 것.
            if distance[now] < d:
                continue

            for g in graph[now]:
                cost = d + g[1]
                if cost < distance[now]:
                    distance[g[0]] = cost
                    heappush(q, (cost, g[0]))

    dijkstrak(start)


from collections import defaultdict
