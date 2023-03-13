from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    """
    condition
    rectangle = [lx,ly,rx,ry]
    x,y = [1,50]
    """
    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)
    board = [[0] * 52 for _ in range(52)]

    item = (itemY, itemX)
    for rec in rectangle:
        fill_rec(*rec, board)

    q = deque([(0, characterY, characterX)])
    visited = set([(characterY, characterX)])

    while q:
        cnt, *now = q.popleft()
        if tuple(now) == item:
            return cnt
        for i in range(4):
            ny, nx = now[0] + dy[i], now[1] + dx[i]

            if (ny, nx) not in visited:
                if check(ny, nx, board):
                    q.append((cnt + 1, ny, nx))
                    visited.add((ny, nx))

                # elif i in (1, 3):
                #     if check(ny, nx, board):
                #         q.append((cnt + 1, ny, nx))
                #         visited.add((ny, nx))

    return 0


def sum_9direc(y, x, board):
    from itertools import product as pro

    # print(list(pro([0, 1, -1], repeat=2)))
    return sum(board[y + a][x + b] for a, b in pro([0, 1, -1], repeat=2))


def check(y, x, board):
    temp = sum_9direc(y, x, board)
    if temp != 9 and board[y][x] == 1:
        return True
    return False


def fill_rec(lx, ly, rx, ry, board):
    for y in range(ly, ry + 1):
        for x in range(lx, rx + 1):
            board[y][x] = 1


a = solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)
print(a)

# a = solution([[1, 1, 5, 7]], 1, 1, 4, 7)
# print(a)
# a = solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1)
# print(a)
