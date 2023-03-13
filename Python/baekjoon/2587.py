def solution():
    nums = sorted([int(input()) for _ in range(5)])

    print(sum(nums) // len(nums))
    print(nums[2])


solution()
