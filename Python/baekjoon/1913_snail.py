dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
# N = int(input())
# R = int(input())

N = 7
R = 35

y,x = (0,0)
ans = [[0]*N for i in range(N)]

idx = 0
input_val = N**2

def is_out_of_bound():
    con = ((x + dx[idx] < 0) or 
                (x + dx[idx] >= N) or 
                (y + dy[idx] < 0) or 
                (y + dy[idx] >= N) or 
                ans[y+dy[idx]][x+dx[idx]])
    return con
while True:

    ans[y][x] = input_val

    #base
    if R == input_val: 
        coordinate = (x,y)
    if input_val ==1: break

    if is_out_of_bound():
        idx = (idx+1)%4
    x += dx[idx];y+=dy[idx]
    
    input_val -= 1
    
for i in ans:
    for j in i:
        print(j,end=" ")
    print()

y,x = coordinate

print(x+1,y+1)