def solution():
    nums = set([i for i in range(1, 31)])
    for _ in range(28):
        nums.remove(int(input()))

    for i in sorted(list(nums)):
        print(i)


solution()
