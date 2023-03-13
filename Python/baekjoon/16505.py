board = []

def solution():
    global board
    N = int(input())
    
    # 조금 더 생각하면 될 것 같기도 한데 그냥 board를 그리는 게 나을 것 같다.
    #stars = build_star(N) 
    board = [[" "]*(2**N) for _ in range(2**N)]

    set_star(N,0,0)
    print_board()
    
def print_board():
    l = len(board)
    for i in range(l):
        print("".join(board[i][:l-i]))

    # print("\n".join(["".join(board[i][:l-i]) for i in range(l)]))

def set_star(N, x,y):

    if N == 0:
        board[y][x] = "*"

    else:
        set_star(N-1, x,y)
        set_star(N-1, x,y + 2**(N-1))
        set_star(N-1, x + 2**(N-1), y)
    

#폐기(discard)
def build_star(N):
    
    if N ==0:
        return '*'
    
    tmp = [build_star(N-1) for _ in range(3)]
    return tmp



solution()
# print(board)

    
# 꽤 괜찮은 solution
"""
def star(n):
	l=[]
	if n==0:
		return ['*']
	for i in star(n-1):
		l.append(i + ' '*((2**(n-1))-len(i)) + i)
	for i in star(n-1):
		l.append(i)
	return l
n=int(input())
print('\n'.join(star(n)))

"""