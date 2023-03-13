def solution(babbling):
    answer = 0
    three = {"a": "aya", "w": "woo"}
    two = {"y": "ye", "m": "ma"}
    a = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        l = len(i)
        s = 0
        stack = []
        while s < l:
            t = i[s]

            if t in three:
                if l > s + 2 and (i[s : s + 3] in three.values()):
                    if stack and (stack[-1] == i[s : s + 3]):
                        break
                    stack.append(i[s : s + 3])
                    s += 3

                else:
                    break

            elif t in two:
                if l > s + 1 and (i[s : s + 2] in two.values()):
                    if stack and (stack[-1] == i[s : s + 2]):
                        break
                    stack.append(i[s : s + 2])
                    s += 2

                else:
                    break
            else:
                break

        if s == l:
            answer += 1

    return answer
