from collections import deque

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution():
    N = int(input())
    k = int(input())
    board = [[0] * N for _ in range(N)]
    for _ in range(k):
        r, c = map(int, input().split())
        board[r - 1][c - 1] = 1
    # apples = [list(map(int,input().split())) for _ in range(k)]

    L = int(input())
    directions = [list(map(str, input().split())) for _ in range(L)]

    head = [0, 0]
    snail = deque([(0, 0)])
    head_direction = 0
    ans = 0
    for s, d in directions:
        s = int(s)
        for i in range(s - ans):
            nr = head[0] + moves[head_direction][0]
            nc = head[1] + moves[head_direction][1]
            if isvalid(N, nr, nc, board):
                move(nr, nc, board, snail)
            else:
                return ans + i + 1

            head = [nr, nc]
        ans = s
        head_direction = (
            (head_direction + 1) % 4 if d == "D" else (head_direction - 1) % 4
        )
        # if d == "D":
        #     head_direction = (head_direction + 1) % 4
        # else:
        #     head_direction = head_direction - 1 if head_direction != 0 else 3

    while True:
        ans += 1
        nr = head[0] + moves[head_direction][0]
        nc = head[1] + moves[head_direction][1]
        if isvalid(N, nr, nc, board):
            move(nr, nc, board, snail)
        else:
            break
        head = [nr, nc]

    return ans


def move(nr, nc, board, snail):
    snail.append((nr, nc))
    if board[nr][nc] == 1:
        pass
    else:
        r, c = snail.popleft()
        board[r][c] = 0
    board[nr][nc] = 2


def isvalid(N, nr, nc, board):
    # 범위가 가능한 범위인지
    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != 2:
        return True
    return False


print(solution())
