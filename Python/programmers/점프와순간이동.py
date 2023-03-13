def solution(n):
    if n == 0:
        return 0

    return solution(n - 1) + 1 if n & 1 else solution(n // 2)


# def solution(n):
#     return bin(n).count("1")
