import re
def solution(s):
    # if re.search("meow",s):
    #     return 0
    # elif re.search("(meo([a-z])*|me[.]w|m[.]ow|[a-z]*eow)",s):
    #     return 1
    # elif re.search("(m[a-z]{0,2}w|eo|me|ow)",s):
    #     return 2
    # elif set(s) & set({'m','e','o','w'}):
    #     return 3
    # else:
    #     return 4
    ans = 0
    alph = {'m','e','o','w'}
    check = False
    n = len(s)
    for i in range(n):
        if n-i >= 3:
            tmp = s[i:i+4]
            if tmp == 'meow':
                return 0
            elif re.search("(me.w|m.ow|emow|moew|mewo)",tmp):
                return 1
        if n-i >= 2: 
            if re.search("(meo|eow|mew|mow)",s[i:i+3]):
                return 1
            elif re.search("(emo|moe|oew|ewo|emw|mwe|omw|mwo|mwe)",s[i:i+3]):
                return 2

        if n -i >= 4:
            if re.search("(me.ow|m.eow|meo.w)",s[i:i+5]):
                return 1
            elif re.search("(em.ow|me.wo|mo.ew|e.mow|m.oew|m.ewo|moe.w|mew.o|emo.w|)",s[i:i+5]):
                return 2

        if n-i>= 1:
            if re.search("(me|eo|ow|mw|mo|ew)",s[i:i+2]):
                return 2
        if s[i] in alph and not check:
            check=True

    if check: return 3
    else: return 4
        
    # 0개 meow
    # 1개(3개만족) meo,mew,mow,eow, me ow, m eow, meo w , emow, moew, mewo
    # 2개(2개만족) me,eo,ow,mw,mo,ew
    # 3개(1개만족)


print(solution(str(input())))