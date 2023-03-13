from collections import defaultdict


def solution():
    N = int(input())

    return N // 5 + N // 25 + N // 125


ans = solution()
print(ans)
