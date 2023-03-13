#미로탈출
def solution():
    from collections import deque
    n,m = map(int, input().split())
    map_ = [list(map(int, input())) for i in range(n)]
    queue = deque([(0,0)])
    while queue:
        y,x = queue.popleft()
        mxy = [(0,1),(0,-1),(-1,0),(1,0)]
        for ny,nx in mxy:
            if not (0<=y+ny<n and 0<=x+nx<m): continue

            if map_[y+ny][x+nx] == 0: continue

            if map_[y+ny][x+nx] == 1: 
                map_[y+ny][x+nx] = map_[y][x]+1
                queue.append((ny+y,nx+x))

    
    print("\n".join([" . ".join(map(str,i)) for i in map_]))
    return map_[n-1][m-1]

print(solution())