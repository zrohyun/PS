from collections import Counter
def solution(name):
    cnt_name = Counter(name)
    answer = len(name)-1
    if "A" in cnt_name.keys(): 
        cnt_name.pop("A")


    for i in cnt_name.keys():
        answer += min(ord(i) - ord("A"), abs(ord(i) - ord("A")-26))*cnt_name[i]
        print(i,answer)
    return answer




print(solution("JEROEN"))