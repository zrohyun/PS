from math import ceil


def solution(n, stations, w):
    answer = 0
    range_ = []

    idx = 1

    for s in stations:

        if idx <= s - w - 1:
            range_.append((idx, s - w - 1))

        idx = s + w + 1

    if idx <= n:
        range_.append((idx, n))

    return sum(ceil((b - a + 1) / (w * 2 + 1)) for a, b in range_)
