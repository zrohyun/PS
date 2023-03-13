def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    nums_rev = nums[::-1]
    dp_asc = [0] * (n)
    dp_des = [0] * (n)
    dp_des1 = [0] * (n)

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp_asc[i] = max(dp_asc[i], dp_asc[j]+1)
            if nums[i] < nums[j]:
                dp_des[i] = max(dp_des[i], dp_des[j]+1)
    
    for i in range(n):
        for j in range(i):
            if nums_rev[i] > nums_rev[j]:
                dp_des1[i] = max(dp_des1[i], dp_des1[j]+1)
    print(dp_asc, dp_des1[::-1], max([x+y+1 for x,y in zip(dp_asc, dp_des1[::-1])]))
    print(dp_asc,dp_des, max([x+y-1 for x,y in zip(dp_asc, dp_des)]))

print(solution())