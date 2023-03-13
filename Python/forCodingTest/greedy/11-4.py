# 만들 수 없는 금액

#숫자 배열 입력받기
# 숫자 정렬하기
# 정렬된 숫자 조합하기


N = int(input())
nums = list(map(int, input().split()))
nums.sort()

target = 1
for n in nums:
    if target < n: 
        break
    target += n

print(target)
