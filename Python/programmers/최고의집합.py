from itertools import combinations_with_replacement as comb
from functools import reduce


def solution(n, s):

    """
    condition
    최고의 집합 - 각 원소 합이 S, 원소의 곱이 최대
    """

    answer = [s // n] * n
    for i in range(s % n):
        answer[i] += 1

    return [-1] if not all(answer) else sorted(answer)


def tle():
    a = list(filter(lambda x: sum(x) == s, comb(range(1, s + 1), n)))
    if not a:
        return [-1]
    # print(a)
    mul = 0
    answer = []
    for i in a:
        if (s := reduce(lambda x, y: x * y, i)) > mul:
            mul_ = s
            answer = i
