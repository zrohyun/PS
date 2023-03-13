class Solution:
    def isUgly(self, n: int) -> bool:
        primes = set()
        if n <= 0:
            return False

        d = 2
        while d <= n:

            if d > 5:
                return False

            if n % d == 0:
                primes.add(d)
                n = n // d
            else:
                d += 1

        for i in primes:
            if i not in {2, 3, 5}:
                return False

        return True


"""
class Solution:
    def isUgly(self, n: int) -> bool:
        # A non-positive integer cannot be ugly
        if n <= 0:
            return False

        # Keep dividing dividend by divisor when division is possible
        def keep_dividing_when_divisible(dividend, divisor):
            while dividend % divisor == 0:
                dividend //= divisor
            return dividend

        # Factorize by dividing with permitted factors
        for factor in [2, 3, 5]:
            n = keep_dividing_when_divisible(n, factor)

        # Check if the integer is reduced to 1 or not.
        return n == 1

"""

"""
class Solution:
    def isUgly(self, n: int) -> bool:
        return False if n<=0 else pow(2*3*5,32) % n == 0
"""
