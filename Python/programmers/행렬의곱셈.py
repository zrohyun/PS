def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    arr2 = [[arr2[j][i] for j in range(r2)] for i in range(c2)]
    answer = [[0] * c2 for _ in range(r1)]

    # for i in range(r1):
    #     for j in range(c2):
    #         answer[i][j] = sum([a*b for a,b in zip(arr1[i],arr2[j])])

    for n in range(r1 * c2):
        i = n // c2
        j = n % c2
        answer[i][j] = sum([a * b for a, b in zip(arr1[i], arr2[j])])

    return answer


# def solution(A, B):
#     return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

# 행,행,행--->열,열로 반환해주는
# [(1, 3, 5), (2, 4, 6)] <<< zip(*[[1,2], [3,4], [5,6]])
