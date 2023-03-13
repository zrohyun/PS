import sys

input = sys.stdin.readline


def solution():
    """
    구간  합 구하기 4
    """
    # v1()
    # v2()
    v3()

def v3():

    N, M = map(int, input().split())
    Ns = list(map(int, input().split()))
    accum = [0]* (N+1)

    for i in range(N):
        accum[i+1] = accum[i] + Ns[i]
    
    for _ in range(M):
        i,j = map(int,input().split())
        print(accum[j] - accum[i-1])


def v2():
    N, M = map(int, input().split())
    Ns = list(map(int, input().split()))
    sums = [[0] * (N + 1 - i) for i in range(N + 1)]
    for i in range(N + 1):
        for j in range(1, i + 1):
            sums[j][i - j] = Ns[i - 1] + sums[j - 1][i - j]

    for _ in range(M):
        i, j = map(int, input().split())
        print(sums[j - i + 1][i - 1])


def v1():
    """TLE"""
    N, M = map(int, input().split())
    Ns = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        print(sum(Ns[i - 1 : j]))


solution()
