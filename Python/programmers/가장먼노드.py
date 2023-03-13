# from heapq import heappush,heappop
# def solution(n, edge):
#     INF = int(1e10)
#     distance = [INF]*(n+1)
#     graph = [[] for _ in range(n+1)]
    
#     for s,d in edge:
#         graph[s].append((1,d))
#         graph[d].append((1,s))
    
#     q = []
#     heappush(q, (0,1))
#     distance[:2] = [0,0]
#     while q:
#         # print(q)
#         dis,now = heappop(q)
#         if dis > distance[now]:
#             continue
        
#         for _,i in graph[now]:
#             if distance[i] > dis+1:
#                 distance[i] = dis+1
#                 heappush(q,(dis+1,i))
    
#     max_dis = max(distance)
    
#     return distance.count(max_dis)

from heapq import heappush,heappop
def solution(n, edge):
    INF = int(1e10)
    distance = [INF]*(n+1)
    visited = [False] *(n+1)
    graph = [[] for _ in range(n+1)]
    
    for s,d in edge:
        graph[s].append(d)
        graph[d].append(s)
    
    q = [ (i,1) for i in graph[1]]
    distance[:2] = [0,0]
    visited[0] = [True]
    
    while q:
        nxt,c = q.pop(0)
        if distance[nxt] != INF:
            continue
        
        distance[nxt] = c
        for i in graph[nxt]:
            q.append((i,c+1))
        
        
    print(distance)
    return distance.count(max(distance))
    