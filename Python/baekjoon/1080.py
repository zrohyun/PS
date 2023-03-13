from sys import stdin
input = stdin.readline
def solution():
    n, m = list(map(int, input().split()))
    a = [list(map(str, input())) for _ in range(n)]
    b = [list(map(str, input())) for _ in range(n)]
    
    comp_arr = []
    for a_,b_ in zip(a,b):
        comp_arr.append([not (a__ == b__) for a__,b__ in zip(a_,b_)]) # False if a__==b__ else True
    
    #comprehension
    #comp_arr = [list(map(lambda x,y: False if x==y else True, a_,b_)) for a_,b_ in zip(a,b)]


    # base case
    if n < 3 or m < 3:
        # if sum([sum(i) for i in comp_arr]) == 0: return 0
        if sum(map(sum,comp_arr)) == 0: return 0
        else: return -1

    ans = 0
    for y in range(len(comp_arr) - 3 + 1):
        for x in range(len(comp_arr[0]) -3 +1):
            
            # same coordinate skip
            if not comp_arr[y][x]: 
                # early stopping condition
                # if (x == len(comp_arr[0])-3) and (sum(comp_arr[y][x:]) != 0): return -1
                continue
            
            ans += 1
            for i in range(3):
                for j in range(3):
                    comp_arr[y+i][x+j] = not comp_arr[y+i][x+j]
    
    # if sum([sum(i) for i in comp_arr]) == 0:
    if sum(map(sum,comp_arr)) == 0: #all false => all 
        return ans
    else:
        return -1
    # print(comp_arr)

print(solution())