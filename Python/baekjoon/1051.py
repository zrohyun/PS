from sys import stdin
input = stdin.readline

def solution():
    n,m = list(map(int,input().split()))
    square = [list(str(input())) for _ in range(n)]

    def find_square(y,x):
        num = square[y][x]
        size = 1
        for i in range(min(n-y,m-x)):
            if len(set([num,square[y][x+i],square[y+i][x],square[y+i][x+i]])) == 1:
                size = max(size, (i+1)*(i+1))
        
        return size

    size = 1
    for y in range(n):
        for x in range(m):
            size = max(size, find_square(y,x))
    
    return size

print(solution())
