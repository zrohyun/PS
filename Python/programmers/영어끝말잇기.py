def solution(n, words):
    answer = [0, 0]
    appear_set = set()
    for i, w in enumerate(words):

        if i == 0:
            before = w
            appear_set.add(w)
            continue

        if (w not in appear_set) and (w[0] == before[-1]):
            appear_set.add(w)
            before = w
        else:
            print(i, before[-1], w[0])
            return [i % n + 1, i // n + 1]

    return answer


# def solution(n, words):
#     for p in range(1, len(words)):
#         if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
#     else:
#         return [0,0]
