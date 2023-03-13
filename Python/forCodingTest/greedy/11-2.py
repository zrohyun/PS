# 곱하기 혹은 더하기
# 숫자로 이루어진 문자열 S가 주어짐
# 각 숫자 사이에 +,*를 넣어 가장 큰 숫자를 만들어라
# 연산은 왼쪽에서 오른쪽으로 이루어진다.

nums = list(map(int,list(input())))

res = nums[0]
for i in nums[1:]:
    if res <=1 or i <= 0: 
        res += i
    else:
        res *= i

print(res)

## solution
# 첫 번째 문자를 숫자로 변경하여 대입
# result = int(data[0])

# for i in range(1, len(data)):
#     # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num

# print(result)