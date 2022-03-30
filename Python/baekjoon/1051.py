from sys import stdin
input = stdin.readline

def solution():
    n,m = list(map(int,input().split()))
    square = [list(str(input())) for _ in range(n)]

    # 정사각형의 크기를 구하는지 몰랐다. 직사각형되 되는 줄 알았다.
    # 정사각형만 구한다면 크기를 topdown으로 가장 큰 크기부터
    # 계산해내려오면 된다. 처음 조건에 맞는 정사각형을 찾게된다면
    # 바로 탐색을 중지할 수 있다.
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
