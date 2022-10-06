from collections import defaultdict


def solution(maps):

    print(maps)
    answer = []
    return answer


def parts(maps):
    part_num = 0
    powers = dict()
    map_part = [[-1] * len(maps[0]) for _ in range(len(maps))]
    for i in len(maps):
        for j in len(i):
            if map_part[i][j] == -1:
                continue

            maps[i][j]
