import sys

input = sys.stdin.readline


def solution():
    max_ = int(-1e10)
    loc = (-1, -1)
    for i in range(1, 10):
        row = list(map(int, input().split()))
        for j in range(1, 10):
            if max_ < row[j - 1]:
                max_ = row[j - 1]
                loc = (i, j)
    print(max_)

    print(*loc)


solution()
