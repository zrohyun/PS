# direction = ["U","D",'L',"R"]
"""
00 01 02
10 11 12
20 21 22
"""
# D 일때
# y = n-1부터 -2씩 옮겨가며 row append()
# temp saving board 생성 후 여기에 append하는 것이 나을 듯

# U일때 0부터 2씩 더해가며
#L 일때 0부터 2씩 더해가며
from typing import List
from collections import deque
def moveU(gb:List[List[int]],r:int,c:int)-> List[List[int]]:
    ans = []
    for x in range(c):
        res = [(gb[0][x],0)]
        for y in range(1,r):
            (a,ch),b = res.pop(),gb[y][x]
            if ch:
                res.append((a,1))
                if b: res.append((b, 0))
                continue

            if a == 0 or b == 0:
                res.append((a + b, 0))

            elif a == b:
                res.append((a + b, 1))
            else:
                res.append((a, 0))
                res.append((b, 0))

        ans.append([i for i,_ in res])

    egb = [[0]*c for _ in range(r)] #empty game board
    for i,a in enumerate(ans):
        for j,v in enumerate(a):
            egb[j][i] = v

    return egb

def moveD(gb,r,c):
    ans = []
    for x in range(c):
        res = [(gb[r-1][x],0)]
        for y in range(r-2, -1, -1):
            (a,ch), b = res.pop(),gb[y][x]
            if ch:
                res.append((a, 1))
                if b: res.append((b, 0))
                continue

            if a == 0 or b == 0:
                res.append((a + b, 0))

            elif a == b:
                res.append((a + b, 1))
            else:
                res.append((a, 0))
                res.append((b, 0))

        ans.append([i for i,_ in res])

    egb = [[0] * c for _ in range(r)]  # empty game board
    for i, a in enumerate(ans):
        for j, v in enumerate(a):
            egb[-1-j][i] = v

    return egb
def moveR(gb,r,c):
    ans = []
    for y in range(r):
        res = [(gb[y][c-1],0)]
        for x in range(c-2, -1, -1):
            (a,ch), b = res.pop(),gb[y][x]
            if ch:
                res.append((a, 1))
                if b: res.append((b, 0))
                continue

            if a == 0 or b == 0:
                res.append((a + b, 0))

            elif a == b:
                res.append((a + b, 1))
            else:
                res.append((a, 0))
                res.append((b, 0))

        ans.append([i for i,_ in res])

    egb = [[0] * c for _ in range(r)]  # empty game board
    for i, a in enumerate(ans):
        egb[i][c-len(a):] = a[::-1]

    return egb

def moveL(gb,r,c):
    ans = []
    for y in range(r):
        res = [(gb[y][0],0)]
        for x in range(1, c):
            (a,ch), b = res.pop(), gb[y][x]
            if ch:
                res.append((a, 1))
                if b: res.append((b, 0))
                continue

            if a == 0 or b == 0:
                res.append((a + b, 0))

            elif a == b:
                res.append((a + b, 1))
            else:
                res.append((a, 0))
                res.append((b, 0))

        ans.append([i for i,_ in res])

    egb = [[0] * c for _ in range(r)]  # empty game board
    for i, a in enumerate(ans):
        egb[i][:len(a)] = a[:]

    return egb

# print(moveU([[2,2,2],[4,4,4],[8,8,8]],3,3))
# print(moveD([[2,2,2],[4,4,4],[8,8,8]],3,3))
# print(moveR([[2,2,2,0],[4,4,4,3],[8,8,8,3]],3,4))
# print(moveL([[2,2,2],[4,4,4],[8,8,8]],3,3))

print(moveU([[2,4,16,8],[8,4,0,0],[16,8,2,0],[2,8,2,0]],4,4))
print(moveD([[2,4,16,8],[8,4,0,0],[16,8,2,0],[2,8,2,0]],4,4))
print(moveR([[2,4,16,8],[8,4,0,0],[16,8,2,0],[2,8,2,0]],4,4))
print(moveL([[2,4,16,8],[8,4,0,0],[16,8,2,0],[2,8,2,0]],4,4))


# U일때 0부터 2씩 더해가며
# L 일때 0부터 2씩 더해가며
from typing import List
from collections import deque
def moveU(gb: List[List[int]], r: int, c: int) -> List[List[int]]:
    ans = []
    for x in range(c):
        res = [(gb[0][x], 0)]
        for y in range(1, r):
            (a, ch), b = res.pop(), gb[y][x]
            if ch:
                res.append((a, 1))
                if b: res.append((b, 0))
                continue

            if a == 0 or b == 0:
                res.append((a + b, 0))

            elif a == b:
                res.append((a + b, 1))
            else:
                res.append((a, 0))
                res.append((b, 0))

        ans.append([i for i, _ in res])

    egb = [[0] * c for _ in range(r)]  # empty game board
    for i, a in enumerate(ans):
        for j, v in enumerate(a):
            egb[j][i] = v

    return egb

def moveD(gb, r, c):
    ans = []
    for x in range(c):
        res = [(gb[r - 1][x], 0)]
        for y in range(r - 2, -1, -1):
            (a, ch), b = res.pop(), gb[y][x]
            if ch:
                res.append((a, 1))
                if b: res.append((b, 0))
                continue

            if a == 0 or b == 0:
                res.append((a + b, 0))

            elif a == b:
                res.append((a + b, 1))
            else:
                res.append((a, 0))
                res.append((b, 0))

        ans.append([i for i, _ in res])

    egb = [[0] * c for _ in range(r)]  # empty game board
    for i, a in enumerate(ans):
        for j, v in enumerate(a):
            egb[-1 - j][i] = v

    return egb

def moveR(gb, r, c):
    ans = []
    for y in range(r):
        res = [(gb[y][c - 1], 0)]
        for x in range(c - 2, -1, -1):
            (a, ch), b = res.pop(), gb[y][x]
            if ch:
                res.append((a, 1))
                if b: res.append((b, 0))
                continue

            if a == 0 or b == 0:
                res.append((a + b, 0))

            elif a == b:
                res.append((a + b, 1))
            else:
                res.append((a, 0))
                res.append((b, 0))

        ans.append([i for i, _ in res])

    egb = [[0] * c for _ in range(r)]  # empty game board
    for i, a in enumerate(ans):
        egb[i][c - len(a):] = a[::-1]

    return egb

def moveL(gb, r, c):
    ans = []
    for y in range(r):
        res = [(gb[y][0], 0)]
        for x in range(1, c):
            (a, ch), b = res.pop(), gb[y][x]
            if ch:
                res.append((a, 1))
                if b: res.append((b, 0))
                continue

            if a == 0 or b == 0:
                res.append((a + b, 0))

            elif a == b:
                res.append((a + b, 1))
            else:
                res.append((a, 0))
                res.append((b, 0))

        ans.append([i for i, _ in res])

    egb = [[0] * c for _ in range(r)]  # empty game board
    for i, a in enumerate(ans):
        egb[i][:len(a)] = a[:]

    return egb

    # print(moveU([[2,2,2],[4,4,4],[8,8,8]],3,3))
    # print(moveD([[2,2,2],[4,4,4],[8,8,8]],3,3))
    # print(moveR([[2,2,2,0],[4,4,4,3],[8,8,8,3]],3,4))
    # print(moveL([[2,2,2],[4,4,4],[8,8,8]],3,3))

    # print(moveU([[2,4,16,8],[8,4,0,0],[16,8,2,0],[2,8,2,0]],4,4))
    # print(moveD([[2,4,16,8],[8,4,0,0],[16,8,2,0],[2,8,2,0]],4,4))
    # print(moveR([[2,4,16,8],[8,4,0,0],[16,8,2,0],[2,8,2,0]],4,4))
    # print(moveL([[2,4,16,8],[8,4,0,0],[16,8,2,0],[2,8,2,0]],4,4))

def solution():
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))

    q = [(moveU(board, n, n), 1),
         (moveL(board, n, n), 1),
         (moveR(board, n, n), 1),
         (moveD(board, n, n), 1)]
    ans = 0
    # cnt=0

    while q:
        b, t = q.pop()
        if t == 5:
            ans = max(max(max(i) for i in b), ans)
            # print(b)
            continue
        for i in [moveU, moveL, moveR, moveD]:
            q.append((i(b, n, n), t + 1))
    # print(cnt)
    return ans


print(solution())
