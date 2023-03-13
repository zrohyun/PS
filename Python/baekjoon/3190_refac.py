from collections import deque

# move나 direction 하나로 하는 것보다 dr,dc나 dy,dx로 하는 게 더 나을듯
# 이제 웬만하면 그냥 dy,dx로 통일해서 코드 짜도록 해보자.
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def solution(N, board, dci):

    # current
    y, x = 1, 1
    board[y][x] = 2
    snail = deque([[y, x]])
    hd = 0  # head_direction = 0(right)
    time = 0
    while True:
        time += 1

        ny, nx = y + dy[hd], x + dx[hd]
        if isvalid(N, ny, nx, board):
            move(ny, nx, board, snail)
        else:
            return time
        y, x = ny, nx

        if time in dci:
            hd = (hd + 1) % 4 if dci[time] == "D" else (hd - 1) % 4


def move(ny, nx, board, snail):
    snail.append((ny, nx))
    if board[ny][nx] != 1:
        py, px = snail.popleft()  # pop y,pop y
        board[py][px] = 0
    board[ny][nx] = 2


def isvalid(N, nr, nc, board):
    # 범위가 가능한 범위인지
    return 0 < nr <= N and 0 < nc <= N and board[nr][nc] != 2


if __name__ == "__main__":
    N = int(input())
    k = int(input())
    board = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(k):
        y, x = map(int, input().split())
        board[y][x] = 1

    L = int(input())

    # direction changing info
    dci = {}
    for _ in range(L):
        sec, command = map(str, input().split())
        dci[int(sec)] = command

    ans = solution(N, board, dci)
    print(ans)
