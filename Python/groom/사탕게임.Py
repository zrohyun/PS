# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
gurumi = 0
friend = 0
for i in list(map(int, input().split())):
    if i % 4 == 0:
        friend += 1
    else:
        gurumi += 1
    print(gurumi, friend)
ans = "tie" if gurumi == friend else max(gurumi, friend)
print(ans)
