def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    if len(nums) == 1: return nums[0]**2
    else:
        return nums[0]* nums[-1]
    

print(solution())