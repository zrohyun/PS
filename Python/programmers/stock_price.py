def solution(prices):
    
    loc_dict = dict()
    for i, n in enumerate(prices):
        loc_dict[n] = loc_dict.get(n,[]) + [i]
    
    keys = list(loc_dict.keys())
    for i,k in enumerate(keys):
        for compk in keys[i+1:]:
            if compk > k:
                for ki in loc_dict[k]:
                    for idx in range(len(loc_dict[compk])):
                        if loc_dict[compk] - ki < 0:
                            loc_dict[compk] = -1*(loc_dict[compk] - ki)
    print(loc_dict)
    
    
if __name__ == '__main__':
    print(solution([1,2,3,4,5]))
    # efficiency no sufficient
#     answer = [[n,0] for n in prices]
#     for i in range(len(prices)):
#         n = prices[i]
#         for j in range(i):
            
#             if answer[j][0] == -1: 
#                 continue
            
#             if n < answer[j][0]:
#                 answer[j][0] = -1

#             answer[j][1] += 1
            
#     print(answer)       
#     return [b for a,b in answer]
