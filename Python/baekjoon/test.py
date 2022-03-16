import os
def print_arr(ans):
    for i in ans:
        join_blank = " "*len(str(max(i)))
        i = [j if j != 0 else join_blank for j in i]
        
        print(" ".join(map(str,i)))
    
    import time, os
    time.sleep(0.3)
    os.system("clear")

def snail_simulation(M = 5,N=3):
# M,N = map(int,input().split())

    matrix = [[0]*N for _ in range(M)]
    dxy = [(0,1),(1,0),(0,-1),(-1,0)]
    idx = 0

    x,y = 0,0
    matrix[y][x] = 1
    ans = 0
    for _ in range(M*N-1):
        #print(x,y)
        nx = x + dxy[idx][1]
        ny = y + dxy[idx][0]
        if (0>nx) or (nx >= N) or (0>ny) or (ny >= M) or matrix[ny][nx]:
            idx = (idx+1)%4
            ans += 1

        x = x + dxy[idx][1] 
        y = y + dxy[idx][0] 
        
        matrix[y][x] = 1
    
    return ans