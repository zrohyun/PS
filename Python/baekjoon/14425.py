import sys

input = sys.stdin.readline


def solution():
    """
    문자열 집합
    N개의 문자열로 이루어진 집합 S
    M개의 문자열 중 S에 포함된 것의 개수
    """
    N, M = map(int, input().split())
    S = set()
    for _ in range(N):
        S.add(str(input()))

    cnt = 0
    for _ in range(M):
        if str(input()) in S:
            cnt += 1

    return cnt


ans = solution()
print(ans)
