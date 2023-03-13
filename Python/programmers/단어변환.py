from collections import defaultdict, deque
import copy


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    g = defaultdict(list)
    visited = {}

    for i in range(len(words)):
        visited[words[i]] = False
        for j in range(i + 1, len(words)):
            if diff(words[i], words[j]) == 1:
                g[words[i]].append(words[j])
                g[words[j]].append(words[i])

    q = deque([])
    for i in words:
        if diff(i, begin) == 1:
            v = copy.deepcopy(visited)
            v[i] = True
            q.append((i, 1, v))

    while q:
        w, c, v = q.popleft()
        if w == target:
            return c

        for i in g[w]:
            if not v[i]:
                temp_v = copy.deepcopy(v)
                temp_v[i] = True
                q.append((i, c + 1, temp_v))

    return answer


def diff(s, t):
    cnt = 0
    for a, b in zip(s, t):
        if a != b:
            cnt += 1

    return cnt


assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4
assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
