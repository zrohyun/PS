# 1 = 1(1)
# 2 = 2(00,11)
# 3 =3(001,100,111) 
# 4 = 5(0000,0011,1100,1111,1001)
def solution():

    N = int(input())
    dp = list([0]*1000002)
    dp[1] = 1
    dp[2] = 2
    num = 3
    while num <= N:
        dp[num] = (dp[num-1] + dp[num-2]) % 15746
        num += 1

    print(dp[N])

solution()

