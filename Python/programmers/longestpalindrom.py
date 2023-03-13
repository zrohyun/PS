def solution(s):
    return v3(s)


def dp_ver(s):
    ans = 1
    dp = [[False] * len(s) for i in range(len(s))]

    for i in range(len(s) - 1):
        dp[i][i + 1] = True if s[i] == s[i + 1] else False


def isPalindrome(s, i, j) -> int:
    l = len(s)
    while i >= 0 and j < l and s[i] == s[j]:
        i -= 1
        j += 1
    return j - i - 1


def v3(s):
    ans = 1
    for i in range(1, len(s) - 1):
        ans = max(ans, isPalindrome(s, i - 1, i))
        ans = max(ans, isPalindrome(s, i - 1, i + 1))

    return ans


def v2(s):
    """time complexity is N^2"""
    rs = s[::-1]
    store = dict()
    store[s] = set([rs])
    store[rs] = set([s])
    for n in range(2, len(s)):
        for i in range(len(s) - n + 1):
            pair = [s[i : i + n], rs[len(s) - n - i : len(s) - i]]
            print(pair)
            store[pair[0]] = set([pair[1]])
            store[pair[1]] = set([pair[0]])

    answer = 1
    for k in store.keys():

        if k in store[k]:
            answer = max(answer, len(k))

    return answer


def v1(s):
    """time complexity is N^2"""
    rs = s[::-1]
    store = dict()
    store[s] = set([rs])
    store[rs] = set([s])

    for n in range(2, len(s)):
        for i in range(len(s) - n + 1):
            pair = [s[i : i + n], rs[len(s) - n - i : len(s) - i]]
            print(pair)
            store[pair[0]] = set([pair[1]])
            store[pair[1]] = set([pair[0]])

    # print(store.items())
    for n in range(len(s), 2, -1):
        for i in range(len(s) - n + 1):
            if s[i : i + n] in store[s[i : i + n]]:
                print(s[i : i + n], store[s[i : i + n]])
                return n

    return 1


print(solution("abacde"))
