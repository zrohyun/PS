def solution():
    N = int(input())
    nums = list(map(int,input().split()))
    dp = [nums[0]]

    for i in nums[1:]:
        dp.append(max(dp[-1]+i, i))

    return max(dp)

print(solution())