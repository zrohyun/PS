def solution(goods):
    ans = [set() for i in range(len(goods))]

    for n,i in enumerate(goods):
        for j in range(1,len(i)+1):
            for k in range(len(i)-j+1):
                    ans[n].add(i[k:k+j])

    answer = deepcopy(ans)
    for n,i in enumerate(ans):
        for j in range(len(ans)):
            if n == j: continue
            answer[n] = answer[n].difference(ans[j])
        

    ans = []
    for i in answer:
        a = sorted(list(i),key =lambda x: len(x))
        
        a = [i for i in a if len(a[0])>=len(i)]
        a = sorted(a)
        if len(a) != 0: 
            ans.append(" ".join(a))
        else:
            ans.append("None")
        

    return ans
print(solution(["pencil","cilicon","contrabase","picturelist"]))
print(solution(["abcdeabcd","cdabe","abce","bcdeab"]))
print(solution(['aa','aaa']))