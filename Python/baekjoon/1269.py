import sys

input = sys.stdin.readline


def solution():
    """
    대칭 차집합
    """
    an, bn = map(int, input().split())
    A = set(list(map(int, input().split())))
    B = set(list(map(int, input().split())))

    return len(A.union(B) - A.intersection(B))


ans = solution()
print(ans)
