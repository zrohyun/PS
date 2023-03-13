def solution():
    N, M = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        mat[i][:] = [a + b for a, b in zip(list(map(int, input().split())), mat[i])]

    for i in mat:
        print(*i)


solution()
