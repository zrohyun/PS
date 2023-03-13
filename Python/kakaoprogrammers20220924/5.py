from heapq import heapify, heappush, heappop


def solution(n, m, x, y, r, c, k):
    x, y, r, c = x - 1, y - 1, r - 1, c - 1
    # miro = [["."] * n for _ in range(m)]
    # miro[y][x] = "S"
    # miro[c][r] = "E"
    a = path(n, m, x, y, r, c, k)

    return a


def path(n, m, x, y, r, c, k):
    queue = []
    answer = []
    heapify(answer)
    heapify(queue)
    for d, nx, ny in next_direction(n, m, x, y):
        # heappush(queue, [abs(r - nx) + abs(c - ny), d, nx, ny, 1])
        heappush(queue, [d, nx, ny, 1])

    while queue:
        # howfar, route, cx, cy, l = heappop(queue)  # current position
        route, cx, cy, l = heappop(queue)  # current position

        for d, nx, ny in next_direction(n, m, cx, cy):

            if k == (l + 1):
                if nx == r and ny == c:
                    return route + d
                    # heappush(answer, route + d)
            else:
                # if answer:
                #     if answer[0] < route + d:
                #         continue
                # heappush(queue, [abs(r - nx) + abs(c - ny), route + d, nx, ny, l + 1])
                heappush(queue, [route + d, nx, ny, l + 1])

    return answer[0] if answer else "impossible"


def next_direction(n, m, curr_x, curr_y):
    d_option = []
    if 0 <= curr_x - 1:
        d_option.append(["u", curr_x - 1, curr_y])
    if curr_y + 1 < m:
        d_option.append(["r", curr_x, curr_y + 1])

    if 0 <= curr_y - 1:
        d_option.append(["l", curr_x, curr_y - 1])

    if curr_x + 1 < n:
        d_option.append(["d", curr_x + 1, curr_y])

    return d_option


print(solution(3, 4, 2, 3, 3, 1, 5))


"""
from heapq import heapify, heappush, heappop


def solution(n, m, x, y, r, c, k):
    x, y, r, c = x - 1, y - 1, r - 1, c - 1
    # miro = [["."] * n for _ in range(m)]
    # miro[y][x] = "S"
    # miro[c][r] = "E"
    a = path(n, m, x, y, r, c, k)
    # print(a)
    if isinstance(a, str):
        return a
    else:
        return a[0]


def path(n, m, x, y, r, c, k):
    queue = []
    answer = []
    heapify(answer)
    for d, nx, ny in next_direction(n, m, x, y):
        queue.append([d, nx, ny, 1])
    while queue:
        route, cx, cy, l = queue.pop()  # current position
        if k == l:
            if cx == r and cy == c:  # condition
                heappush(answer, route)
                continue
            else:
                continue

        for d, nx, ny in next_direction(n, m, cx, cy):
            if answer:
                if answer[0] > route + d:
                    continue

            queue.append([route + d, nx, ny, l + 1])

    return answer if answer else "impossible"


def next_direction(n, m, curr_x, curr_y):
    d_option = []
    if 0 <= curr_x - 1:
        d_option.append(["u", curr_x - 1, curr_y])
    if curr_y + 1 < m:
        d_option.append(["r", curr_x, curr_y + 1])

    if 0 <= curr_y - 1:
        d_option.append(["l", curr_x, curr_y - 1])

    if curr_x + 1 < n:
        d_option.append(["d", curr_x + 1, curr_y])

    return d_option
    """
