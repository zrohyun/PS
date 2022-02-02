# 예제 4-1 상하좌우
N = int(input())
M = list(map(str, input().split()))
# N = 5
# M = ['R','R','R','U','D','D']
moving_op = {'R':(0,1), "L":(0,-1), "U":(-1,0),"D":(1,0)}
x,y = 1,1


def is_over_space(x,y):
    if x < 1 or y < 1 or x > N or y > N: 
        return True
    
    return False
    
    
for i in M:
    mv = moving_op[i]
    nx = x + mv[0]
    ny = y + mv[1]
    if not is_over_space(nx,ny):
        x,y = nx,ny

print(x,y)
