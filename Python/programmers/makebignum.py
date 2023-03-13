def solution(number, k):
    
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            k -= 1
            stack.pop()
        stack.append(n)
    
    return ''.join(stack[:len(stack)-k])
    
    
    return answer