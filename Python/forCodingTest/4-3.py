# 예제 4-3 왕실의 나이트
# 

#book bolution
def solution(loc = 'a1'):
    # input_data = input()
    input_data = loc
    y = int(input_data[1])
    x = int(ord(input_data[0]) - int(ord('a'))) + 1

    steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
    result = 0

    for step in steps:
        nx = x + step[0]
        ny = y + step[1]

        if nx >= 1 and nx <=8 and ny >=1 and ny <= 8: result +=1

    return result

    


#my solution
def solution2(loc = "a1"):
    di = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}

    #loc = str(input())
    x,y = (di[loc[0]] , int(loc[1])-1)

    move = []
    for i in [1,-1]:
        for j in [2,-2]:
            move.append((i,j))
            move.append((j,i))

    ans = 0
    for mx,my in move:
        nx = x + mx
        ny = y + my
        if (0<=nx) and (nx < 8) and (0<=ny) and (ny <8):
            ans +=1
    return ans

loc = input()
print(solution(loc))

#all case test
# for i in "abcdefgh":
#     for j in range(1,9):
#         loc = i+str(j)
#         print(solution(loc)== solution2(loc))
