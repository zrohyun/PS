
def solution(participant, completion):
    from collections import Counter
    answer = Counter(participant)
    answer.subtract(Counter(completion))

    for k,v in answer.items():
        if v: return k


"""
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""
