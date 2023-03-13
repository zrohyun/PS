from functools import reduce


def solution(n):

    if n == 1:
        return [1]

    d, y, x = 0, 0, 0
    directions = [(1, 0), (0, 1), (-1, -1)]
    tri = [[0] * (i + 1) for i in range(n)]

    maxim = (n * (n + 1)) // 2

    tri[0][0] = 1
    cnt = 2
    while cnt != (maxim + 1):
        ny, nx = y + directions[d][0], x + directions[d][1]
        if 0 <= ny < n and 0 <= nx < len(tri[ny]) and tri[ny][nx] == 0:
            tri[ny][nx] = cnt
        else:
            d = (d + 1) % 3
            continue

        y, x = ny, nx
        cnt += 1

    # return sum(tri,[]) # 맛있지만 쥰내 오래걸림
    # return reduce(lambda z, y :z + y, tri)
    answer = []
    for i in tri:
        answer.extend(i)

    return answer
