def solution():
    l,r = list(map(list,input().split()))
    answer = 0

    if len(l) != len(r): return answer

    for l_,r_ in zip(l,r):
        if l_ == r_ == '8':
            answer +=1
        elif l_ != r_:
            break

    

    return answer
print(solution())
