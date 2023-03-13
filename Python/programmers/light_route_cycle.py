#https://programmers.co.kr/learn/courses/30/lessons/86052
gmap = []
dm = []
def solution(grid):
    global gmap,md
    answer = []
    
    # 각 그리드마다 같은 길이의 칸(S or L or R)이 있음
    # 각 칸 당 4방향의 방문점을 확인해야 한다.
    # 그러면 데이터는 R * C * 4만큼의 방문 check map을 확보해야 한다.
    gmap = [[[0]*4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    #move direction
    md = [(1,0),(0,-1),(-1,0),(0,1)]

    # 모든 방문 포인트를 체크해야한다.
    # 같은 칸이라도 왼쪽 오른쪽 위 아래 방문 포인트가 다름. 모든 지점으로 진입하는
    # 경우를 전부 생각해야함.
    # 다만 이미 진입 흔적이 있다면 순환이 되면 그 순환에 해당하는 어떤 지점에서 접근을 하던
    # 다시 원래의 접근 포인트로 접근할 수 있다는 뜻이고
    # 만약 흔적이 있는데 순환이 되지 않았다면 어떤 접근 포인트든 순환이 안된다는 의미.
    # 따라서 방문 포인트를 체크한 뒤에 다시 지워줄 필요는 없음.
    for y in range(len(gmap)):
        for x in range(len(gmap[0])):
            for i in range(4):
                if not gmap[y][x][i]: #not visited
                    cycle = dfs(y,x,i,grid)
                    if cycle: answer.append(cycle)
            
    return sorted(answer)

def dfs(y,x,i,grid):
    global gmap,md
    ny,nx,ni = y,x,i
    gmap[y][x][i] = 1
    cnt = 0
    while True:
        ny =  (ny + md[ni][0]) % len(grid)
        nx = (nx + md[ni][1]) % len(grid[0])
        cnt += 1 
        
        # move_dirction의 순서는
        # 현재 향하는 방향에 +1은 R, -1은 L이다.
        if grid[ny][nx] == 'R':
            ni = (ni+1)%4
        elif grid[ny][nx] == 'L':
            ni = (ni-1)%4
        
        if gmap[ny][nx][ni]:
            if (ny,nx,ni) == (y,x,i):
                return cnt
            else: #접근한 포인트인데 시작 포인트와 다르다? -> 순환 X case
                return 0
        
        gmap[ny][nx][ni] = 1
        
        
            
        
            
    