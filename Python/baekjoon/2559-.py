from functools import reduce
from time import time
#from itertools import pairwise -> python 3.10
def solution():
    n,k = list(map(int,input().split()))
    nums = list(map(int, input().split()))

    ans = -9987654321


    for i in range(n-k):
        ans = max(ans, sum(nums[i:i+k]))
    #reduce(lambda x,y: max(x,y),[sum(nums[i:i+k]) for i in range(n-k)])

    
    return ans

print(solution())