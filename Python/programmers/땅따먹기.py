def solution(land):

    for i in range(1, len(land)):
        land[i][:] = [
            land[i][j] + max(land[i - 1][:j] + land[i - 1][j + 1 :]) for j in range(4)
        ]

    return max(land[-1])
