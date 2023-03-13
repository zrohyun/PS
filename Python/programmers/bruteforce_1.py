#모의고사
#https://programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    answer = []
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    ans = [0,0,0]
    for n,i in enumerate(answers):
        if person1[n%5] == i:
            ans[0] += 1
        
        if person2[n%len(person2)] == i:
            ans[1] += 1
        
        if person3[n%len(person3)] == i:
            ans[2] += 1

    
    if set(ans) ==1:
        answer = [1,2,3]

    else:
        for n,a in enumerate(ans):
            if a == max(set(ans)):
                answer.append(n+1)
    
    return answer

assert solution([1,2,3,4,5]) == [1]