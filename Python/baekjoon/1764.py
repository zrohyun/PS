import sys

input = sys.stdin.readline


def solution():
    """
    듣보잡

    """
    N, M = map(int, input().split())
    unheard = set()
    for _ in range(N):
        unheard.add(str(input().rstrip()))

    unseen = set()
    for _ in range(M):
        unseen.add(str(input().rstrip()))

    print(len(unheard.intersection(unseen)))
    for i in sorted(list(unheard.intersection(unseen))):
        print(i)


solution()
