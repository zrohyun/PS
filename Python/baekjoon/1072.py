import math
def solution():
    x,y = list(map(int,input().split()))
    z = (y*100)//x
    if z >= 99:
        return -1

    ans = int(math.ceil((100*y - x*(z + 1)) / (z -99)))
    return ans

print(solution())