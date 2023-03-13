"""
condition
N [1,1000000]
"""

from collections import defaultdict
from heapq import heapify, heappop, heappush


def solution():
    n = int(input())
    lines = []
    for _ in range(n):
        s, e = map(int, input().split())
        heappush(lines, [s, e])
        heappush(lines, [e, 0])

    print(lines)
    live = []
    heapify(live)
    answer = defaultdict(lambda: [float("inf"), float("inf")])
    while lines:
        s, e = heappop(lines)

        # remove passed line
        if e == 0:
            answer[len(live)][1] = s
            live.remove(s)
            continue

        while live and live[0] <= s:
            heappop(live)

        heappush(live, e)
        if answer[len(live)][0] == float("inf"):
            answer[len(live)][0] = s
        elif answer[len(live)][1] == float("inf"):
            answer[len(live)][1] = live[0]
        print(live)
    print(answer)

    pass


# solution()

import sys


def solution1():
    lines = []

    for i in range(int(sys.stdin.readline())):
        s, e = map(int, sys.stdin.readline().split())
        lines.append((s, 1))
        lines.append((e, -1))

    lines.sort()

    cnt = 0
    ans = 0
    for i in lines:
        cnt += i[1]
        ans = max(ans, cnt)
    print(ans)
    return ans


solution1()
