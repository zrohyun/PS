from collections import deque
map_ = []
def solution(N, road, K):
    global map_
    
    map_ = [[0]*(N+1) for _ in range(N+1)]
    
    for a,b,c in road:
        if m:=map_[a][b]:
            map_[a][b] = map_[b][a] = min(m,c)
        else:
            map_[a][b] = map_[b][a] = c

    return len(bfs(K))

def bfs(K):
    global map_
    queue = deque([(b,v) for b,v in enumerate(map_[1]) if v])
    minlen = {b:v if v else 9876543221 for b,v in enumerate(map_[1])}
    minlen[1] = 0
    
    ans = set({1})
    while queue:
        des,r = queue.popleft()
        if r <= K: ans.add(des)

        for b,v in enumerate(map_[des]):
            if v and minlen[b] > v+r:
                minlen[b] = v+r 
                queue.append((b,v+r))

    return ans

# print(solution(1,[[]],2))
print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))