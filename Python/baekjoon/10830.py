from typing import List

Matrix = List[List[int]]

def solution():
    N, B = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    for i in mat_power(A, B):
        print(*i)


def mat_mul(A : Matrix, B : Matrix) -> Matrix:
    ans : Matrix = [[0] * len(A) for _ in range(len(A))]
    for r in range(len(A)):
        # for bc in range(len(A)):
        #     for ac in range(len(A)):
        #         ans[r][bc] += (A[r][ac] * B[ac][bc])
        #     ans[r][bc] %= 1000
        for i in range(len(A)**2):
            bc,ac = i//len(A),i%len(B)
            ans[r][bc] += (A[r][ac] * B[ac][bc])
            ans[r][bc] %= 1000

    # for i in range(len(A)**3):
    #     r = i // (len(A)**2)
    #     i = i % (len(A)**2)
    #     bc,ac =  i // len(A), i%len(A)
    #     ans[r][bc] += (A[r][ac] * B[ac][bc])
    #     ans[r][bc] %= 1000

    return ans


def mat_power(A : Matrix , B : int):
    if B == 1:
        return [[i % 1000 for i in a] for a in A]

    devided_mat = mat_power(A, B // 2)

    if B % 2 == 1:
        return mat_mul((mat_mul(devided_mat, devided_mat)), A)
    else:
        return mat_mul(devided_mat, devided_mat)

solution()