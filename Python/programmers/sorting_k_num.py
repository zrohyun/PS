# k번째  수
# arr가 주어졌을 때 i,j,k가 주어진다.append
# arr가 [1,5,2,6,3,7,4]
# i=2,j=5,k=3이라면 
# 5 2 6 3을 정렬해 나온 3번째 arr[i-1:j][k-1]


def solution(array, commands):
    # answer = []
    # for i,j,k in commands:
    #     answer.append(sorted(array[i-1:j])[k-1])

    answer = [sorted(array[i-1:j])[k-1] for i,j,k in commands]

    return answer