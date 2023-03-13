# 문자열 뒤집기
# S = 111001111
# 연속된 하나 이상의 숫자를 잡고 뒤집는 것

count1 = 0
count0 = 0

data = input()

if data[0] =='1': count0=1
else: count1 = 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 +=1
        else:
            count1 +=1
    
print(min(count0,count1))