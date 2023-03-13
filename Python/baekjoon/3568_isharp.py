import re

# example
# input: int& a*[]&, b, c*;
# output: int&&[]* a;
#         int& b;
#         int&* c;

def solution():
    a = str(input()).replace(",","").replace(";","").split()

    # print(a)

    dtype = a[0]
    sign = ['&','[',']','*']

    # 각 변수마다 sign이 있는지 검사한다.
    # sign이 있으면 개수를 파악해서 개수만큼 없애고

    ans = []
    for i in a[1:]:
        i = i.replace("[]","][")
        while i[-1] in sign:
            dtype += i[-1]
            i = i[:-1]
        dtype += " "
        for j in i:
            if j.isalpha():
                dtype += j
        dtype += ";"
        ans.append(dtype)
        dtype = a[0]
        

    for i in ans:
        print(i)

def solution2():
    s = input().replace(',', '')[:-1].split(' ')

    for i in range(1, len(s)):
        s[i] = s[i].replace('[]', '][')

    common = s[0]
                    
    for i in range(1, len(s)):
        print(common, end="")
        word = s[i]
        
        for idx in range(len(word)-1, 0, -1):
            c = word[idx]
            if not c.isalpha():
                print(c, end='')

        print('', end=' ')
        
        for idx in range(0, len(word)):
            if word[idx].isalpha():
                print(word[idx], end='')
        
        print(';')

solution()