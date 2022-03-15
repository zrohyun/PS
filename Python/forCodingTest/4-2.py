# 예제 4-2 시각
# 정수 N이 입력되면 00시 00분 00초부터 Ntl 59분 59초까지의 모든 시각 중에서 
# 3이 하나라도 포함되는 모든 경우의 수

#N = int(input())
N = 5

    

## book solution
def solution1(N):
    ans = 0        
    for k in range(N+1):
        for i in range(60):
            for j in range(60):
            
                if '3' in str(k) + str(i) + str(j):
                    # print(str(k) +" "+ str(i) + " " + str(j))
                    ans += 1
    return ans

def solution2(N):
    case_have_3 = (N + 1) * 6 * 10 * 6 * 10
    if N<3: 
        case_no_have_3 = (N+1) * 5 * 9 * 5 * 9 
    elif N<13 :
        case_no_have_3 = (N) * 5 * 9 * 5 * 9  
    elif N<23:
        case_no_have_3 = (N-1) * 5 * 9 * 5 * 9
    else:
        case_no_have_3 = (N-2) * 5 * 9 * 5 * 9 
    return case_have_3 - case_no_have_3

print(solution1(N) == solution2(N))
