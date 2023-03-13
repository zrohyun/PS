import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    S, X, Y = map(int, input().split())  # 행-x, 열-y
    dx = (0, 1, 0, -1)  # row
    dy = (1, 0, -1, 0)  # col
    q = []
    for i in range(N * N):
        x, y = i // N, i % N
        if board[x][y] != 0:
            heappush(q, (1, board[x][y], x, y))

    while q:
        s, v, x, y = heappop(q)

        if s > S:
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                board[nx][ny] = v
                heappush(q, (s + 1, v, nx, ny))

    return board[X - 1][Y - 1]


ans = solution()
print(ans)
