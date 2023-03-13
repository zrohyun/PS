from sys import stdin
input = stdin.readline
from collections import deque
def solution():
    n = int(input())
    ans = deque()
    for _ in range(n):
        i = int(input())
        if i: ans.append(i)
        else: ans.pop()
    
    return sum(ans)

print(solution())

