def solution():
    x = int(input())
    sticks = [64]

    while True:
        if sum(sticks) == x: 
            return len(sticks)
        tmp = sticks[-1]
        if tmp//2 + sum(sticks[:-1]) >= x :
            sticks = sticks[:-1] + [tmp//2]
        else:
            sticks = sticks[:-1] + [tmp//2]*2
        # print(sticks)
print(solution())        

