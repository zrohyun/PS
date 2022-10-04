def solution(k):
    nums = {
        "0": 6,
        "1": 2,
        "2": 5,
        "3": 5,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 3,
        "8": 7,
        "9": 6,
    }

    q = []
    ans = set()
    for key, val in nums.items():
        if val < k:
            q.append((key, val))
        elif val == k:
            ans.add(key)

    while q:
        s_num, accum = q.pop()
        for key, val in nums.items():
            if accum + val < k:
                q.append((s_num + key, accum + val))
            elif (accum + val) == k and key != "0":
                ans.add(s_num + key)

    #dp로 풀었어야 했는데..
    dp = [set()]*k
    for keys,vals in nums.items():
        dp[vals].add(keys)
    
    for i in range(k):
        for keys,vals in nums.items():
            
    

    # print(ans)
    # print(len(ans))
    return len(ans)
