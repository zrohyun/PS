import sys;
input = sys.stdin.readline

N = int(input())

# x, y, d, g
curve = [list(map(int,input().split())) for _ in range(N)]

dx = (1,0,-1,0)
dy = (0,-1,0,1)
ans = 0
# 좌표가 드래곤 커브에 포함이 되는지 체크해줄 리스트
check = [[0] * (101) for _ in range(101)]

for c in curve:
    x,y,d,g = c
    # 먼저 시작하는 x,y 좌표는 방문체크
    check[x][y] = 1
    d_curve = [d]
    for i in range(g):
        d_list = []
        for dc in d_curve[::-1]:
            # nx = x + dx[d%4]
            # ny = y + dy[  d% 4]
            d_list.append((dc+1)%4)
        d_curve.extend(d_list)

    for m in d_curve:
        nx = x + dx[m]
        ny = y + dy[m]
        check[nx][ny] = 1  # 체크처리
        x, y = nx, ny  # 방향을 현재 움직인 방향으로 갱신
    # print(d_curve)
    # ans.update([(a,b) for a,b,c in d_curve])

for i in range(100):
    for j in range(100):
        if check[i][j] == 1 and check[i+1][j] == 1 and check[i][j+1] == 1 and check[i+1][j+1] == 1:
            ans += 1
print(ans)


## 다른 풀이

"""

R, U, L, D = 0, 1, 2, 3
curves = [[]] * 11
curves[0] = [R]

'''
R -> U
U -> L
L -> D
D -> R
'''

# 0 : R
# 1 : R U
# 2 : R U L U
# 3 : R U L U L D L U
for i in range(1, 11):
    new = [((x+1) % 4) for x in curves[i-1]]
    new.reverse()
    curves[i] = curves[i-1] + new

field = [[False for _ in range(101)] for _ in range(101)]

num_of_curve = int(input(''))
for _ in range(num_of_curve):
    x, y, d, g = list(map(int, input('').split(' ')))
    for step in curves[g]:
        field[x][y] = True
        direction = (step + d) % 4
        if direction is R:
            x += 1
        elif direction is U:
            y -= 1
        elif direction is L:
            x -= 1
        elif direction is D:
            y += 1
    field[x][y] = True

num_of_square = 0
for i in range(100):
    for j in range(100):
        if field[i][j] and field[i][j+1] and field[i+1][j] and field[i+1][j+1]:
            num_of_square += 1

print(num_of_square)

"""