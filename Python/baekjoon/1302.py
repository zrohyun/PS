from collections import defaultdict


def solution():
    n = int(input())
    d = dict() #defaultdict(int)를 사용해도 된다.
    for i in range(n):
        a = str(input())
        d[a] = d.get(a,0)+1  #d[a] +=1 
        # if a in d: d[a] +=1
        # else: d[a] = 1
    mv = max(d.values())
    ans = [k for k,v in d.items() if v == mv]
    # ans = []
    # for k,v in d.items():
    #     if v == mv:
    #         ans.append(k)
    
    # d = dict(sorted(d.items(), key=lambda item: item[1],reverse=True))


    print(ans,sorted(ans))
    return sorted(ans)[0]

solution()