def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        t = bin(a | b)[2:]
        answer.append(
            "".join([" "] * (n - len(t)) + ["#" if i == "1" else " " for i in t])
        )
    return answer


# def solution(n, *maps):
#     return [line(n, a | b) for a, b in zip(*maps)]


# def line(n, x):
#     return ''.join(' #'[int(i)] for i in f'{x:016b}'[-n:])
