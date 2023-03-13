import re


def solution(user_id, banned_id):

    a = list([i.replace("*", ".") for i in banned_id])

    pair = {i: set() for i in set(a)}

    for i in user_id:
        for aa in set(a):
            k = re.compile(aa)
            if k.match(i) and k.match(i).end() == len(i):
                pair[aa].add(i)
    ans = set()

    def dfs(i, selected):
        nonlocal pair, a
        if i == len(a):
            ans.add(tuple(sorted(selected)))
            return

        p = a[i]

        for s in pair[p]:
            if s not in selected:
                dfs(i + 1, selected + [s])

    dfs(0, [])

    return len(ans)


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["fr*d*", "*rodo", "******", "******"],
)
"""
처음 구현 실패 요인.
순서가 상관 없는 백트래킹 문제에서
순서가 있는 dfs 문제처럼
dfs(){for p in patterns} 
과 같이 문제를 풀었음. 이건 필요 없고 어떤 순서든 p를 하나씩 제거하면 되는 거라
idx를 하나씩 증가시키면서 하면 될듯.
"""

"""
import re
from itertools import product

def solution(user_id, banned_id):
    matched_id = (
        [i for i, id in enumerate(user_id) if re.match(f"^{p.replace('*', '.')}$", id)]
        for p in banned_id
    )
    # selected_id = [set(id) for id in product(*matched_id)]  # <- 시간초과
    selected_id = (set(id) for id in product(*matched_id))  # <- 통과
    selected_id = set(tuple(id) for id in selected_id if len(id) == len(banned_id))
    return len(selected_id)

https://school.programmers.co.kr/questions/31212 permutation을 이용한 풀이
생각해보면 permutation도 나쁘지 않음. 다만 전체로 하지말고 우선 매칭되는 list를 뽑아서 순열을 구성하면
훨씬 빠를듯

"""
