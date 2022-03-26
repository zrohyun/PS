def solution():

    N = int(input())
    arr = list(map(int, input().split()))

    dp = [1]*len(arr)

    for i in range(1,len(arr)):
        # 현 상태(숫자)에 대해 이전 숫자들의 저장상태들에서
        # 가장 나은 선택의 가지를 따른다.
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
    


    return max(dp)


print(solution())