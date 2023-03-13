def solution():
    """
    숫자 카드
    숫자 카드 N개, 정수 M개
    이 수가 상근이가 가지고 있는지 아닌지 판단.
    """
    N = input()
    sangguen = set(list(map(int, input().split())))
    M = input()
    nums = list(map(int, input().split()))

    print(*[1 if i in sangguen else 0 for i in nums])


solution()
