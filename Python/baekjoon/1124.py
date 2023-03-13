from math import sqrt


def solution():
    a,b = list(map(int,input().split()))
    dp = [0]*(b+1)
    # primes = {2:0,3:0} #list말고 해쉬를 써야함 
    dp[0:4] = [0,0,1,1]
    pnum = prime(b)
    for i in range(4,b+1):
        if i in pnum: #if prime_check(i):
            # primes[i] = 0
            dp[i] = 1
        else:
            for j in pnum:
                if i % j == 0:
                    dp[i] = dp[i//j] +1
                    break
    # print(dp)
    return len(list(filter(lambda x: x in pnum, dp[a:])))

def prime_check(num):
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, int(num**0.5)+1):
            if (num % i) == 0:
                # if factor is found, set flag to True
                break
                # break out of loop
        else:
            flag=True
                
    return flag

def prime(n):
    ans = {2:0,3:0}
    for i in range(4,n+1):
        for j in range(2,int(i**0.5)+1):
            if i % j == 0: break
        else:  
            ans[i]=0
    # print(ans)
    return ans


print(solution())
