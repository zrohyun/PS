#https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers,target):
    answer = dfs(numbers,target)
    
    return answer

def dfs(numbers,target):
    if len(numbers) == 0 and target == 0:
        return 1
    elif len(numbers) == 0 and target != 0:
        return 0
    
    return dfs(numbers[1:],target-numbers[0]) + dfs(numbers[1:],target+numbers[0])


def other_sol(numbers,target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

from itertools import product
def other_sol2(numbers, target):
    
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

# numbers = [1, 1, 1, 1, 1]
# l = [(x, -x) for x in numbers]
# print(list(product([1,2],[2,3],[5,6])))