def solution_v2():
    N = int(input())
    board = [0] * (N + 1)
    ans = 0

    def check(k):
        nonlocal board
        for i in range(1, k):
            same_col = board[k] == board[i]
            same_digonal = (k - i) == abs(board[k] - board[i])
            if same_col or same_digonal:
                return False
        return True

    def dfs(k):
        nonlocal ans, board
        if k > N:
            ans += 1
            return

        for i in range(1, N + 1):
            # 같은 열에 있거나 혹은 대각선 라인에 존재하거나(행, 열의 차이의 절대값이 같음)
            board[k] = i
            if check(k):
                dfs(k + 1)

    dfs(1)
    return ans


print(solution_v2())

from collections import deque
import copy


def solution():
    """백준 메모리 초과, board를 복사하지 말고 recursion 재귀로 풀어야함!"""
    N = int(input())
    q = deque([])
    board = [0] * (N + 1)
    ans = 0

    def check(k, board):
        for i in range(1, k):
            if board[i] == board[k] or (k - i) == abs(board[i] - board[k]):
                return False
        return True

    for i in range(1, N + 1):
        board[1] = i
        q.append((1, copy.deepcopy(board)))

    while q:
        k, b = q.popleft()

        if k == N:
            ans += 1
            continue

        for i in range(1, N + 1):
            b[k + 1] = i
            if check(k + 1, b):
                q.append((k + 1, copy.deepcopy(b)))

    return ans


def solution_v3():
    """
    col,left,right의 checking memory 할당하여 검사 방법
    """
    from sys import stdin

    N = int(stdin.readline().strip())
    S, R, L = [False] * N, [False] * (2 * N - 1), [False] * (2 * N - 1)

    ans = 0  # answer

    def dfs(x):
        nonlocal ans
        if x == N:
            ans += 1
            return

        for row in range(N):

            if not (S[row] or R[row + x] or L[N - 1 + x - row]):
                S[row] = R[row + x] = L[N - 1 + x - row] = True
                dfs(x + 1)
                S[row] = R[row + x] = L[N - 1 + x - row] = False

    dfs(0)
    print(ans)


# solution_v3()
