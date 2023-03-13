def solution():
    """
    서로 다른 부분 문자열의 개수
    """
    S = str(input().rstrip())
    s_set = set(list(S))
    for i in range(2, len(S) + 1):
        for j in range(len(S) - i + 1):
            # print(j, j + i)
            s_set.add(S[j : j + i])
    print(len(s_set))


solution()
