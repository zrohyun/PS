import sys

#백준에서 resursion관련 문제를 풀때 런타임에러(RecursionError)가 발생하는 경우
#재귀의 깊이가 한계를 넘어가기 때문에 발생한다. 아래처럼 limit을 정해주면 백준에서 python으로
#문제를 풀 경우 recursionError를 막아줄 수 있는 것 같다.
sys.setrecursionlimit(10000)

# input을 sys 모듈로 보꾸는 것만으로 332ms -> 80으로 시간이 배이상 빨라졌음
# 원래 input()보다 sys.stdin.readline이 조금 더 빠르다는 것은 알고 있었지만 
# 아마 한번의 line으로 입력하는 게 아니라 K의 개수만큼 여러 번 input을 해주어야해서 그런듯
input = sys.stdin.readline

# sol1 - dfs 사용, sol2 - queue사용
# 두가지 솔루션의 경우 queue를 사용하는 방법이 월등히 빠를 것이라고 생각했지만
# 80ms, 76ms로 드라마틱한 속도차이를 보이지는 않았다.

def solution():
    ans = 0
    M, N, K = list(map(int, input().split()))

    map_ = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = list(map(int, input().split()))
        map_[y][x] = 1

    que = [] 
    def move(x, y):
        
        if y< N-1 : 
            if (map_[y+1][x] == 1):
                map_[y+1][x] = 0
                que.append((x,y+1))
                # move(x,y+1)
        if (y > 0):
            if (map_[y-1][x] == 1):
                map_[y-1][x] = 0
                que.append((x, y-1))
                # move(x,y-1)
        if (x < M-1):
            if (map_[y][x+1] == 1 ):
                map_[y][x+1] = 0
                que.append((x+1, y))
                # move(x+1,y)
        if (x > 0):
            if (map_[y][x-1] == 1 ):
                map_[y][x-1] = 0
                que.append((x-1, y))
                # move(x-1,y)

    for my in range(N):
        for mx in range(M): 
            if map_[my][mx] == 1:
                ans += 1
                # move(mx,my)
                que = [(mx,my)]
                while len(que) != 0:
                    px,py = que.pop()
                    move(px,py)
    
    return ans
           

    
    
T = int(input())
for _ in range(T):
    print(solution())