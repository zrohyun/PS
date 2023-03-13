N,M = map(int, input().split())
y,x,d = map(int, input().split())

# N,M = 4,4
# y,x,d = 1,1,0

# d = [[0]*N for _ in range(M)]

map_ = [list(map(int, input().split())) for _ in range(M)]
# map_ = [[1,1,1,1],
#         [1,0,0,1],
#         [1,1,0,1],
#         [1,1,1,1]]

move = [(-1,0), (0,1),(1,0),(0,-1)] # 북,동, 남,서

def turn_left():
    global d
    d -= 1
    if (d == -1): d = 3

map_[y][x] = -1

def out_of_bound(y,x,my,mx):
    nx = x + mx
    ny = y + my
    if (nx < 0) or (nx >= N) or (ny <0) or (ny >= M): return True

    return False

# 현재 바라보고 있는 방향을 기준으로 왼쪽부터 고려
# 왼쪽에 가보지 않은 곳이라면 go or just turn
# 네 방향 모두 가본 곳이거나 바다로되어 있는 경우 뒤로 가고 1부터 다시 수행
# 뒤쪽에 바다라면 종료

while True:
    
    # 4 direction check
    can_go = False
    for my,mx in move:
        #print(x,y,my,mx)
        
        if out_of_bound(y,x,my,mx):
            continue

        if (map_[y+my][x+mx] == 1) or (map_[y+my][x+mx]==-1):
            continue
        else:
            can_go = True 
            break
    
    # 4방향 모두 갈 수 없다면 back
    if not can_go:
        #print("back")
        x = x - move[d][1]
        y = y - move[d][0]
        if map_[y][x] == 1: break
        continue
    
    # 왼쪽 턴
    turn_left()
    if out_of_bound(y,x,move[d][0],move[d][1]):
        continue
    
    #갈 수 있는 방향이면 고 아니면 다시 왼쪽 턴
    if(map_[y+move[d][0]][x+move[d][1]] == 0):
        map_[y+move[d][0]][x+move[d][1]] = -1
        y =y+move[d][0] 
        x =x+move[d][1]
    
    # process test
    # print(y,x,d)    
    # for i in map_:
    #     print(i)
    # print()    
    
    

ans = 0
for i in map_:
    ans += sum([1 if j == -1 else 0 for j in i])
print(ans)   
