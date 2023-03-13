# from itertools import permutations as per
# def solution(n, k):
#     """효율성 통과 못하는 코드"""
#     return per(range(1,n+1),n)[k-1]
from collections import deque
from math import factorial as fac


def solution(n, k):
    deq = deque(list(range(1, n + 1)))
    fac_dp = [1] * (n + 1)
    for i in range(2, n + 1):
        fac_dp[i] = fac_dp[i - 1] * i
    answer = []
    k -= 1

    for _ in range(n):

        order = k // fac_dp[n - 1]
        print(order)
        answer.append(deq[order])
        deq.remove(deq[order])
        k %= fac_dp[n - 1]
        n -= 1
    return answer


import math


# def solution(n, k):
#     lst = [x for x in range(1, n + 1)]
#     answer = []
#     k -= 1

#     for i in range(n, 0, -1):
#         max_num = math.factorial(n)
#         split_num = max_num // n
#         answer.append(lst[k // split_num])
#         lst.pop(k // split_num)
#         k %= split_num
#         n -= 1
#     return answer


solution(3, 5)
