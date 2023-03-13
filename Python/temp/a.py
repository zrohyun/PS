# maxprime = 10000


# def primes(n):
#     multiples = set()
#     prime = []
#     for i in range(2, n + 1):
#         if i not in multiples:
#             prime.append(i)
#             multiples.update(set(range(i * i, n + 1, i)))
#     return prime


# def truncatableprime(n):
#     "Return a longest left and right truncatable primes below n"
#     primelist = [str(x) for x in primes(n)[::-1]]
#     primeset = set(primelist)
#     for n in primelist:
#         # n = 'abc'; [n[i:] for i in range(len(n))] -> ['abc', 'bc', 'c']
#         alltruncs = set(n[i:] for i in range(len(n)))
#         if alltruncs.issubset(primeset):
#             # truncateleft = int(n)
#             break
#     for n in primelist:
#         # n = 'abc'; [n[:i+1] for i in range(len(n))] -> ['a', 'ab', 'abc']
#         alltruncs = set([n[: i + 1] for i in range(len(n))])
#         if alltruncs.issubset(primeset):
#             truncateright = int(n)
#             break
#     return truncateleft, truncateright


# print(truncatableprime(maxprime))
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from functools import reduce
import math


def solution():
    N = int(input())

    # prime = set([i for i in range(2,int(10**N)) if isPrime(i)])
    # print(prime)
    # prime = primes(int(10**n))
    prime = eratos(int(10**N))

    ans = set()
    cache = set()
    for i in range(int(10 ** (N - 1)), int(10**N)):
        isfulfill = True
        a = i
        temp = set()
        while i > 0:
            temp.add(i)
            if i in cache:
                break
            if i in prime:
                i = i // 10
                continue
            else:
                isfulfill = False
                break

        if isfulfill:
            ans.add(a)
            cache.update(temp)

    return sorted(list(map(str, ans)))


def eratos(n):
    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    return set(primes)


# def primes(n):
#     multiples = set()
#     prime = []
#     for i in range(2, n + 1):
#         if i not in multiples:
#             prime.append(i)
#             multiples.update(set(range(i * i, n + 1, i)))
#     return prime

# def isPrime(n):
#   for i in range(2,int(math.sqrt(n))+1):
#     if (n%i) == 0:
#       return False
#   return True
# def isPrime(number):
#     """returns True for a prime number, False otherwise."""
#     factor = 2
#     while factor * factor <= number:
#         if number % factor == 0:
#             return False
#         factor += 1
#     return True

ans = solution()
print(" ".join(ans))
