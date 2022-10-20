from collections import deque

# 오른쪽에 있는 톱니 돌리기
def rotate_right(x, d):
    if x > 4 or gears[x - 1][2] == gears[x][6]:
        return

    if gears[x - 1][2] != gears[x][6]:
        rotate_right(x + 1, -d)
        gears[x].rotate(d)

#왼쪽에 있는 톱니 돌리기
def rotate_left(x, d):
    if x < 1 or gears[x][2] == gears[x + 1][6]:
        return

    if gears[x][2] != gears[x + 1][6]:
        rotate_left(x - 1, -d)
        gears[x].rotate(d)


# 톱니날 구성 입력
gears = {}
for i in range(1, 5):
    gears[i] = deque((map(int, input())))

# 왼쪽 오른쪽 톱니 돌리고 본인 돌리기
for _ in range(int(input())):
    x, d = map(int, input().split())

    rotate_right(x + 1, -d)
    rotate_left(x - 1, -d)
    gears[x].rotate(d)


ans = 0
for i in range(4):
    ans += gears[i + 1][0] * (2 ** i)


## 다른 풀이
"""
https://www.acmicpc.net/source/14974310
S, T, K = [input() for i in range(4)], [0, 0, 0, 0], int(input())

def mv(n, lth) : return (n+8+lth)%8

def rotate(kth, cw, p):
    nxt = kth + p
    if nxt != -1 and nxt != 4 and S[kth][mv(T[kth], 2*p)] != S[nxt][mv(T[nxt],-2*p)] :
        rotate(nxt, -cw, p)
    T[kth] = mv(T[kth], -cw)

while K > 0:
    a, b = map(int, input().split())
    a -= 1
    rotate(a, b, 1)
    T[a] = mv(T[a], b)
    rotate(a, b, -1)
    K -=1

ans = 0
for i in range(4):
    ans += 2**i * (int(S[i][T[i]]))

print(ans)

"""