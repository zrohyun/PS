from collections import deque as dq
def solution(s):
    answer = 0
    pairs = {'(':')','[':']','{':'}'}
    s = dq(s)
    # slist = [list(s)]
    for _ in range(len(s)-1):
        s.rotate(1)
        # slist.append(list(s))
        answer += check_pairs(s,pairs)

    # for i in slist:
    #     answer += check_pairs(i,pairs)

    return answer

def check_pairs(s,pairs):
    stack = []
    for j in s:
        if j in pairs:
            stack.append(j)
        elif j.isalpha():
            continue
        elif not stack: 
            return False
        elif pairs[stack.pop()] != j:
            return False 
    return not stack

print(solution(str(input())))
