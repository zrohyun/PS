from collections import deque as dq
m = []
def solution(rows, columns, queries):
    global m
    answer = []
    m = [[j*columns +i for i in range(1,columns+1)] for j in range(rows)]
    # print(m)
    for x1,y1,x2,y2 in queries:
        answer.append(rotate(y1-1,x1-1,y2-1,x2-1))
        # print(m)
    return answer

def rotate(x1,y1,x2,y2):
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    nx,ny = x1,y1
    tmp = dq() 
    tmp_xy = dq() 
    for my,mx in move:
        while x1<=nx+mx<=x2 and y1<=ny+my<=y2:
            tmp.append(m[ny+my][nx+mx])
            nx,ny = nx+mx,ny+my
            tmp_xy.append((ny,nx))
    
    # print(tmp)
    tmp.rotate(2) 
    tmp_xy.rotate(1)
    # print(tmp_xy)
    for (y,x),v in zip(tmp_xy,tmp):
        m[y][x] = v
    
    return min(tmp)
    

ans=solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
ans=solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]])
# ans=solution(100, 97, [[1, 1, 100, 97]])
print(ans)