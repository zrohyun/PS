import math


def solution():
    N = int(input())
    nums = sorted([int(input()) for _ in range(N)])
    a = nums[1] - nums[0]
    for i in range(1, len(nums) - 1):
        a = gcd(a, nums[i + 1] - nums[i])

    print(" ".join(map(str, sorted(list(common_nums(a))))))


def common_nums(n):
    a = set([n])
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return a


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


solution()
