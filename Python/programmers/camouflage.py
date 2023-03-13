from itertools import compress,product
from functools import reduce
from math import prod
def solution(clothes):
    answer = 1
    clo_dict = dict()
    for clo,loc in clothes:
        clo_dict[loc] = clo_dict.get(loc,[]) + [clo]
    val_list = [len(i) for i in clo_dict.values()]
    # for mask in product([1,0],repeat=len(clo_dict.keys())):
    #     li = list(compress(val_list,mask))
    #     if li: answer += prod(li)
    for i in val_list:
        answer *= (i+1)
        
    return answer-1

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
#a*b*c = abc로 조합가능한 모든 경우의 수, 하지만 안입는 경우도 존재하기 때문에 각각 +1을 해줌, 하지만 abc 전부 안입는 경우는 제외해야 하므로 -1
"""
other solution
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1


ef solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
"""