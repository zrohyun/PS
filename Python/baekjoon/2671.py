import re
def solution(s):
    if re.fullmatch("(100+1+|01)+",s):
        return "SUBMARINE"
    else:
        return "NOISE"

print(solution(str(input())))