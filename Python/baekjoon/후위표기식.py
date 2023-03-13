from collections import deque

prior = {"(": 0, ")": 0, "*": 2, "/": 2, "+": 1, "-": 1}


def solution(nota_):
    ans = ""
    stack = deque()
    for i in nota_:
        if i.isalpha():
            ans += i
        else:
            if i == "(":
                stack.append(i)
            elif i == ")":
                while stack[-1] != "(":
                    ans += stack.pop()
                stack.pop()
            else:
                while stack and prior[stack[-1]] >= prior[i]:
                    ans += stack.pop()
                stack.append(i)

    while stack:
        ans += stack.pop()

    return ans


ans = solution(input())
print(ans)

# solution("A*(B+C)")
# solution("A+B")
# solution("A+B*C")

assert solution("A*(B+C)") == "ABC+*"
assert solution("A+B") == "AB+"
assert solution("A+B*C") == "ABC*+"
assert solution("A+B*C-D/E") == "ABC*+DE/-"
