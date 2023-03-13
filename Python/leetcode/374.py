# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
pick = 6


def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# class Solution:
#     def guessNumber(self, n: int) -> int:
#         l, r, m = 1, n, 0
#         while l <= r:
#             g = guess(m := (l + r) >> 1)
#             if g == -1: r = m - 1
#             elif g == 1: l = m + 1
#             else: break
#         return m

# class Solution:
#     def guessNumber(self, n, s=1):

#         while s <= n:
#             x = (n + s) // 2          # [1] Take the middle point...
#             g = guess(x)              # [2] ...and guess!
#             if g == 0 : return x      # [3] Yay, we found the number!
#             if g < 0  : n = x - 1     # [4] Nope, it's smaller...
#             if g > 0  : s = x + 1     # [5] ...or larger.
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2
            gss = guess(mid)
            if gss == 0:
                return mid
            elif gss == -1:
                r = mid - 1
            elif gss == 1:
                l = mid + 1

        # return bisect_left(range(n), 0, key=lambda x: -guess(x))


Solution().guessNumber(10)
