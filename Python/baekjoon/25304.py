def solution():
    total = int(input())
    n = int(input())
    check = 0
    for _ in range(n):
        p, cnt = map(int, input().split())
        check += p * cnt

    if total == check:
        print("Yes")
    else:
        print("No")


solution()
