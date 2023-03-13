def solution():
    N = int(input())
    YN2TF = lambda x: 0 if x=='N' else 1
    friends = [list(map(YN2TF,input())) for _ in range(N)]
    # print(friends)

    # gh = [[0]*N for _ in range(N)]
    gh = [0]*N

    for i in range(N):
        for j in range(i+1,N):
            if friends[j][i] == 0: 
                # mutual friend check
                for f in range(N):
                    if f == j: continue
                    if friends[f][i] and friends[f][j]:
                        # gh[j][i] = 1
                        # gh[i][j] = 1
                        gh[i] +=1
                        gh[j] +=1
                        break
            else: 
                # gh[j][i] = 1
                # gh[i][j] = 1
                gh[i] +=1
                gh[j] +=1
    
    # print(max([sum(i) for i in gh]))
    print(gh)
    print(max(gh))

solution()