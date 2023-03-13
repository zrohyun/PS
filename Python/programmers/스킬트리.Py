def solution(skill, skill_trees):
    nessary_order = set(skill)
    free_skills = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) - nessary_order

    skill_order = {s: i for i, s in enumerate(skill, start=1)}
    ans = 0
    for sk in skill_trees:
        minimum_ = 0
        learn = True
        for s in sk:
            # free skill 통과
            if s in free_skills:
                continue

            # print(minimum_, skill_order[s])

            if minimum_ + 1 == skill_order[s]:
                minimum_ = skill_order[s]
            else:
                learn = False
                break

            # print(s,minimum_)

        if learn:
            # print(sk)
            ans += 1

    return ans


# def solution(skill, skill_trees):
#     answer = 0

#     for skills in skill_trees:
#         skill_list = list(skill)

#         for s in skills:
#             if s in skill:
#                 if s != skill_list.pop(0):
#                     break
#         else:
#             answer += 1

#     return answer
