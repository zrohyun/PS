from copy import deepcopy

M = 0
ans_rec = []

def find(m,r,sort_rec,rr):

    global ans_rec
    if (len([i for i in rr if i == 0]) == 0):
        ans_rec.append(deepcopy(rr))

        return 
        
    sn = sort_rec[0]

    indices = [n for n,_ in enumerate(r) if r[n]==sn]
    while m <= sn and m <= M:
        
        for i in indices:
            rr[i] = m
        
        find(m+1,r,sort_rec[1:],rr)
    


        for i in indices:
            rr[i] = 0

        m += 1
    
def solution(n, m, k, records):
    ans = []
    global M, ans_rec
    M = m
    answer = []
    for r_idx,r in enumerate(records):
        sort_rec = sorted(set(r))
        

        rr = [0 for _ in range(len(r))]
        find(1,r,sort_rec,rr)
        answer.append(ans_rec)
        ans_rec = []



    answer_ = set([tuple(i) for i in answer[0]])
    for i in answer[1:]:
        answer_=answer_.intersection(set([tuple(j) for j in i] ))
    
    answer_ = sorted([list(i) for i in answer_])
    
    # print(answer_)
    return answer_[-1]




solution(8,4,4,[[1, 5, 1, 3], [5, 7, 5, 6]])
print()
solution(10,3,3,[[1, 2, 3], [5, 7, 10]])