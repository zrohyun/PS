def solution():

    N = int(input())
    # len(arr) = N+1
    arr = [0] + list(map(int, input().split()))

    dp = [0]*(N+1)
    # dp = {i:0 for i in range(N+1)}

    for i in range(1,N+1):
        # 현 상태(숫자)에 대해 이전 숫자들의 저장상태들에서
        # 가장 나은 선택의 가지를 따른다.
        # print(i)
        dp[i] = arr[i]
        for j in range(1,i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+arr[i])
    
    # print(dp)
    return max(dp)

def solution1():
    n=int(input())
    data=list(map(int,input().split()))
    #dp=[0]*1001 # data[i]의 최대 크기는 1000이다.
    dp = {i:0 for i in range(1001)}
    for i in data:
        #dp[i]=max(dp[:i])+i
        dp[i] = max(list(dp.values())[:i])+i
    # print(dp)
    return max(dp.values())

print(solution())