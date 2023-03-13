def solution(reference, track):

    answer = 0
    dp = [1 for i in range(len(track))]
    ref = sub_str(reference)
    for i in range(len(track)):
        for j in range(i + 1):
            print(track[i - j : i + 1], dp)
            print(i - j)
            if track[i - j : i + 1] in ref:
                if i - j > 0:
                    dp[i] = min(j + 1, dp[i - j - 1])
                else:
                    dp[i] = j + 1
                print(dp)
                print(dp[i], dp[i - j - 1] + 1)
    return dp[-1]


def sub_str(reference):
    ans = set()
    for i in range(len(reference)):
        for j in range(1, len(reference) - i + 1):
            ans.add(reference[i : i + j])

    print(ans)
    return ans


# solution("abc", "bcab")
# solution("vxrvip", "xrviprvipvxrv")
solution("abc", "abc")
