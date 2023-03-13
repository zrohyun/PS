from collections import Counter
import sys
input = sys.stdin.readline

def solution():
    """
    숫자 카드2

    숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때 각각 몇 개의
    숫자카드를 가지고 있는지.
    """
    N = input()
    sanggeun = Counter(list(map(int, input().split())))
    M = input()
    print(*[sanggeun[i] for i in list(map(int, input().split()))])


solution()
