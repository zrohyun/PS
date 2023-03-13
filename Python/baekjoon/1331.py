move = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
def solution():
    route = []   
    
    #input
    for _ in range(36):
        x,y = str(input())
        x = ord(x) - ord('A')
        y = int(y) - 1
        route.append((x,y))
    
    # 제자리로 돌아가야한다.
    route.append(route[0])

    if len(set(route)) != 36:
        return "Invalid"


    x,y = route[0]
    for nx,ny in route[1:]:

        if (nx - x,ny -y) not in move:
            return "Invalid"

        x,y = nx,ny
    
    return "Valid"

ans = solution()
print(ans)