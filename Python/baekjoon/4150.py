def solution():
    fibo = [0,1,1,2]
    for i in range(4,int(input())+1):
        fibo.append(sum(fibo[i-2:i]))

    return fibo[-1]

print(solution())