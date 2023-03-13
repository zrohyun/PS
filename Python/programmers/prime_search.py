from itertools import permutations as per
import math
def solution(numbers):
    answer = 0
    nums = set()
    for i in range(1,len(numbers)+1):
        nums.update([int("".join(i)) for i in per(numbers,i)])
    # print(nums)
    answer = list(map(prime_check, nums))
    # print(answer)
    return sum(answer)

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