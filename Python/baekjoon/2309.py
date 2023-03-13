from sys import stdin
input = stdin.readline
from itertools import combinations
def solution():

    smalls = sorted([int(input().strip()) for _ in range(9)])

    for i in combinations(smalls,7):
        if sum(i) ==100:
            print("\n".join(map(str,i)))
            break

solution()