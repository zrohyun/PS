def solution(n, lost, reserve):
    answer = n
    reserve_ = set(set(reserve) - set(lost)) # reserve 학생도 도난당할 수 있음
    lost_ = set(set(lost) - set(reserve))

    for r in reserve_:
        if r-1 in lost_:
            lost_.remove(r-1)
        elif r+1 in lost_:
            lost_.remove(r+1)
    
    return answer - len(lost_)