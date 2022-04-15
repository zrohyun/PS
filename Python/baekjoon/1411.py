def solution():
    n = int(input())
    from collections import deque,Counter
    pocket = [str(input()) for _ in range(n)]
    check = [0]*n
    ans = []
    for j in range(n):
        
        if check[j]: continue
        std = pocket[j]
        check[j] = 1
        group = [std]
        for i in range(j,n):
            if check[i]: continue
            chek_dict = {}
            # chek_dict.get(x,0)
            for x,y in zip(std,pocket[i]):
                if x in chek_dict:
                    
                    if chek_dict[x] != y:
                        break
                else:
                    if y in chek_dict.values(): break
                    chek_dict[x] = y
            else:
                group.append(pocket[i])
                check[i] = 1
        ans.append(group)
    
    #print(ans)
    answer=0
    for i in ans:
        l = len(i)
        answer += l*(l-1)/2
    return int(answer)

print(solution())

