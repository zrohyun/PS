INF = int(1e10)

n = int(input())
m = int(input())

# graph map
graph = [[INF] *(n+1) for _ in range(n+1)]

# self link initial
for i in range(1,n+1):
    graph[i][i] = 0

# init edge information
for _ in range(m):
    a,b,c = list(map(int,input().split()))
    graph[a][b] = c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b] , graph[a][k]+graph[k][b])