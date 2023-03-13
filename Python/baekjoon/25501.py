import sys

input = sys.stdin.readline


def solution():
    N = int(input())
    for _ in range(N):
        s = str(input().rstrip())
        print(*is_palindrome(s))


def is_palindrome(s):
    return recur(s, 0, len(s) - 1, 1)


def recur(s, l, r, dpth):
    if l >= r:
        return 1, dpth
    elif s[l] != s[r]:
        return 0, dpth

    return recur(s, l + 1, r - 1, dpth + 1)


solution()
