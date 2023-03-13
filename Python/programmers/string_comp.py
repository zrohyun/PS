def solution(s):
    answer = 0
    min_ = []
    if len(s) <=2: return len(s)
    for i in range(1,len(s)//2+1):
        min_.append(compress(s,i))
    print(min_) 
    answer = min(min_)
    print(min_)
    return answer

def compress(s,i):
    stack = [[s[0:i],1]]
    s = s[i:]
    while len(s) > 0:
        
        if len(s) < i:
            stack.append([s,1])
            break
        elif stack[-1][0] == s[:i]:
            stack[-1][1] +=1
        else: 
            stack.append([s[:i],1])
        
        s = s[i:]

    print(stack)
    return sum([len(x)+len(str(y)) if y !=1 else len(x) for x,y in stack])

print(solution(str(input())))