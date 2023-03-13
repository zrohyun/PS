from typing import List


def solution(key, lock):
    """
    condition
    자물쇠 N*N, N = [3,20]
    열쇠 M*M, M = [3,20]
    M <= N, 열쇠는 자물쇠보다 항상 작거나 같다.
    0 - 홈, 1 - 돌기
    """

    M = len(key)
    N = len(lock)

    for i in range(4):
        # print(key)
        moved = range(-M + 1, N)
        # print(list(moved))
        for mr in moved:
            for mc in moved:
                fit(key, lock, mr, mc)
                if is_fit(lock):
                    return True
                unfit(key, lock, mr, mc)

        key = rotate_key(key)

    return False


def fit(key, lock, sr, sc):

    for i in range(len(key)):
        for j in range(len(key)):
            if 0 <= i + sr < len(lock) and 0 <= j + sc < len(lock):
                lock[i + sr][j + sc] += key[i][j]


def unfit(key, lock, sr, sc):
    for i in range(len(key)):
        for j in range(len(key)):
            if 0 <= i + sr < len(lock) and 0 <= j + sc < len(lock):
                lock[i + sr][j + sc] -= key[i][j]


def is_fit(lock):
    for i in lock:
        for j in i:
            if j != 1:
                return False
    return True


def rotate_key(key: List[List[int]]) -> List[List[int]]:
    M = len(key)
    rotate = [[0] * M for _ in range(M)]
    for n in range(M * M):
        r, c = n // len(key), n % len(key)

        rotate[c][M - 1 - r] = key[r][c]

    return rotate


solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
solution(
    [[0, 0, 0, 0], [1, 1, 0, 0], [1, 0, 1, 1], [1, 1, 1, 1]],
    [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
)
