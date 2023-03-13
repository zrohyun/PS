def solution():
    n = int(input())
    time = sorted(list(map(int, input().split())))
    ans = 0
    wait = 0
    for i in time:
        ans += wait+ i
        wait += i
    return ans

print(solution())

from sys import stdin
stdin.rea