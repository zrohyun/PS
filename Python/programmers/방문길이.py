def solution(dirs):
    answer = 0
    
    move = {
        "L" : (0,-1),
        "R" : (0,1),
        "U" : (1,0),
        "D" : (-1,0)
    }
    now = [0,0]
    li = set()
    for d in dirs:
        y,x = now
        nx = x + move[d][1]
        ny = y + move[d][0]
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            li.add((y,x,ny,nx))
            li.add((ny,nx,y,x))
            now = [ny,nx]
            
    return len(li)//2