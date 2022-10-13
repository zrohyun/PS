n, m = map(int,input().split())
board = [list(map(str,input())) for _ in range(n)]

# get R,B balls' location and hole's location
rr,rc,br,bc,o_r,o_c = 0,0,0,0,0,0
for r in range(n):
    for c in range(m):
        if board[r][c] == 'R':
            # red starting x, y
            rr, rc = r, c
        if board[r][c] == 'B':
            # blue starting x, y
            br, bc = r, c
        if board[r][c] == 'O':
            # hole x, y
            o_r, o_c = r, c

def move(r, c, dr, dc):
    count = 0 # 이동한 칸 수
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while board[r+dr][c+dc] != '#' and board[r][c] != 'O':
        r += dr
        c += dc
        count += 1
    return r,c, count
from collections import deque
def solution():
    visited = {}

    moves = [(-1,0),(0,1),(1,0),(0,-1)]
    visited[(rr, rc, br, bc)] = True
    s = deque([[rr, rc, br, bc, 1]])

    while s:
        #bfs
        rbr,rbc,bbr,bbc,cnt = s.popleft()
        if cnt > 10: break

        # dfs로 풀 거면 min(answer)처럼 값을 냈어야함.
        # rbr, rbc, bbr, bbc, cnt = s.pop()

        for i in range(len(moves)):
            next_rx, next_ry, r_count = move(rbr, rbc, moves[i][0], moves[i][1])  # RED
            next_bx, next_by, b_count = move(bbr, bbc, moves[i][0], moves[i][1])  # BLUE

            if board[next_bx][next_by] == 'O':  # 파란 구슬이 구멍에 떨어지지 않으면(실패 X)
                continue
            if board[next_rx][next_ry] == 'O':  # 빨간 구슬이 구멍에 떨어진다면(성공)
                return cnt
            if next_rx == next_bx and next_ry == next_by:  # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
                if r_count > b_count:  # 이동 거리가 많은 구슬을 한칸 뒤로
                    next_rx -= moves[i][0]
                    next_ry -= moves[i][1]
                else:
                    next_bx -= moves[i][0]
                    next_by -= moves[i][1]

            # BFS 탐색을 마치고, 방문 여부 확인
            if (next_rx,next_ry,next_bx,next_by) not in visited:
                visited[(next_rx  ,next_ry,next_bx,next_by)] = True
                if cnt <= 9: s.append((next_rx, next_ry, next_bx, next_by, cnt + 1))

    return -1

print(solution())