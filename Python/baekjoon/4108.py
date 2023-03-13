from sys import stdin
input = stdin.readline
def solution():
    while True:
        r,c = list(map(int,input().split()))
        if not(r or c) : break

        m = [['x']*(c+2)] + [list("x" + str(input().strip())+"x") for _ in range(r)]+[['x']*(c+2)]

        check_point = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for y in range(1,r+1):
            for x in range(1,1+c):
                if m[y][x] == '.':
                    m[y][x] = str(sum([1 if m[y+ny][x+nx] == '*' else 0 for ny,nx in check_point]))
        for i in m[1:-1]:
            print("".join(i[1:-1])) 


solution()