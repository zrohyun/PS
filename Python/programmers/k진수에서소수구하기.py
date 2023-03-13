import re


def solution(n, k):
    answer = 0
    num_str = n2k(n, k) if k != 10 else str(n)
    for i in re.split("[0]+", num_str):
        if not i:
            continue
        i = int(i)
        if is_prime(i) and i != 1:
            answer += 1
    return answer


import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def n2k(n, k):

    ans = ""
    while n > 0:
        ans = str(n % k) + ans
        n = n // k

    return ans


# def convert(n, k):
#     result = ''
#     while n > 0:
#         n, mod = divmod(n, k)
#         result += str(mod)
#     return result[::-1]

# def is_prime(num):
#     if num == 1: return False

#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0: return False
#     return True


# def solution (n, k):
#     k_ary= convert(n, k)
#     total = 0
#     for num in k_ary.split('0'):
#         if num.isdigit():
#             if is_prime(int(num)):
#                 total += 1
#     return total
