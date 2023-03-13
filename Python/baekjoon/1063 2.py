from sys import stdin
input = stdin.readline

def solution():
    king,stone,n = list(map(str,input().split()))
    # move definition (my,mx)
    movings = {"R":(0,1),"L":(0,-1),"B":(-1,0),"T":(1,0),
            "RT":(1,1),"LT":(1,-1),"RB":(-1,1),'LB':(-1,-1)}

    moves = [input().strip() for _ in range(int(n))]

    
    king = (int(king[1])-1,ord(king[0])-ord('A'))    
    stone =(int(stone[1])-1,ord(stone[0])-ord('A'))     

    # XYcoordinate to board coordinate    
    ret_board_coord = lambda y,x: chr(ord("A") +x) + str(y+1)

    # check in_bound
    # in_bound = lambda ny,nx: return ((0<=ny<= 7) and (0<=nx<=7))

    for i in moves:
        # print(king,stone)
        ny,nx = (king[0]+ movings[i][0] , king[1]+movings[i][1])

        # move to same direction king and stone
        if (ny,nx) == stone:
            #out_of_board check
            if in_board(ny + movings[i][0],nx + movings[i][1]):
                king = (stone[0],stone[1])
                stone = (ny + movings[i][0],nx+movings[i][1])
        
        elif in_board(ny,nx):
            king = (ny,nx)



    print(ret_board_coord(*king))
    print(ret_board_coord(*stone))

def in_board(ny,nx):
    return ((0<=ny<= 7) and (0<=nx<=7))

solution()