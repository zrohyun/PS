#https://programmers.co.kr/learn/courses/30/lessons/42586

import math
def solution(progresses, speeds):
    answer = []
    times = []
    for a,b in zip(progresses,speeds):
        times.append(math.ceil((100 - a) / b))
    
    min_day = times[0]
    day_count = 1
    for i in times[1:]:
        if min_day >= i:
            day_count += 1
        else:
            min_day = i
            answer.append(day_count)
            day_count = 1

    
    if day_count:
        answer.append(day_count)
        
    return answer


def sol_run_onetime(progresses,speeds):
    q = []
    for a,b in zip(progresses,speeds):
        fin_date = math.ceil((100 - a) / b)
        if len(q) == 0:
            q.append([fin_date,1])
        elif q[-1][0] < fin_date:
            q.append([fin_date,1])
        else:
            q[-1][1]+=1
    
    return [c for d,c in q]



print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
print(sol_run_onetime([93, 30, 55],[1, 30, 5]))
print(sol_run_onetime([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))