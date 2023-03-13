import sys

input = sys.stdin.readline


def solution():
    """
    나는야 포켓몬 마스터 이다솜.

    """
    str_int = dict()
    int_str = dict()
    N, M = map(int, input().split())
    for i in range(N):
        s = str(input().rstrip())
        str_int[s] = i + 1
        int_str[i + 1] = s

    for _ in range(M):
        s = str(input().rstrip())
        if s.isdigit():
            print(int_str[int(s)])
        else:
            print(str_int[s])


solution()
