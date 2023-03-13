import re


def solution(dartResult):
    answer = 0
    li = []
    while dartResult:
        s, d = re.search("\d+(S|D|T)[#|*]*", dartResult).regs[0]
        match = dartResult[s:d]
        dartResult = dartResult[d:]
        i1, i2 = re.search("\d+", match).regs[0]
        li.append((int(match[:i2]), match[i2:]))

    answer_li = [0] * len(li)

    for i, (s, b) in enumerate(li):
        b, o = b if len(b) > 1 else (b, -1)

        if b == "S":
            answer_li[i] = s
        elif b == "D":
            answer_li[i] = s**2
        elif b == "T":
            answer_li[i] = s**3

        if o == "*":
            answer_li[i] = answer_li[i] * 2
            if i > 0:
                answer_li[i - 1] = answer_li[i - 1] * 2
        elif o == "#":
            answer_li[i] = -1 * answer_li[i]

    return sum(answer_li)


# def solution(dartResult):
#     bonus = {'S' : 1, 'D' : 2, 'T' : 3}
#     option = {'' : 1, '*' : 2, '#' : -1}
#     p = re.compile('(\d+)([SDT])([*#]?)')
#     dart = p.findall(dartResult)
#     for i in range(len(dart)):
#         if dart[i][2] == '*' and i > 0:
#             dart[i-1] *= 2
#         dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

#     answer = sum(dart)
#     return answer

# def solution(dartResult):
#     dart = {'S':1, 'D':2, 'T':3}
#     scores = []
#     n = 0

#     for i, d in enumerate(dartResult):
#         if d in dart:
#             scores.append(int(dartResult[n:i])**dart[d])
#         if d == "*":
#             scores[-2:] = [x*2 for x in scores[-2:]]
#         if d == "#":
#             scores[-1] = (-1)*scores[-1]
#         if not (d.isnumeric()):
#             n = i+1

#     return sum(scores)

# def solution(dartResult):
#     point = []
#     answer = []
#     dartResult = dartResult.replace('10','k')
#     point = ['10' if i == 'k' else i for i in dartResult]
#     print(point)

#     i = -1
#     sdt = ['S', 'D', 'T']
#     for j in point:
#         if j in sdt :
#             answer[i] = answer[i] ** (sdt.index(j)+1)
#         elif j == '*':
#             answer[i] = answer[i] * 2
#             if i != 0 :
#                 answer[i - 1] = answer[i - 1] * 2
#         elif j == '#':
#             answer[i] = answer[i] * (-1)
#         else:
#             answer.append(int(j))
#             i += 1
#     return sum(answer)
