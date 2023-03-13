def shap_to_lower(s):  # 샵이 포함된 음을 소문자로 변경
    s = (
        s.replace("C#", "c")
        .replace("D#", "d")
        .replace("F#", "f")
        .replace("G#", "g")
        .replace("A#", "a")
    )
    return s


def solution(m, musicinfos):
    data = []
    m = shap_to_lower(m)
    for i in musicinfos:
        i = i.split(",")
        data.append(
            [
                int(i[1][:2]) * 60
                + int(i[1][3:])
                - (int(i[0][:2]) * 60 + int(i[0][3:])),  # 재생시간
                i[2],  # 제목
                shap_to_lower(i[3]),
            ]
        )  # 멜로디

    data.sort(key=lambda x: (-x[0]))  # 재생시간 긴 순으로 정렬

    for i in range(len(musicinfos)):
        # 재생시간에 해당하는 악보? 만들기
        a, b = divmod(data[i][0], len(data[i][2]))
        text = data[i][2] * a + data[i][2][:b]

        if m in text:  # 멜로디가 악보 안에 있는 경우
            return data[i][1]  # 해당 곡의 제목 반환
    else:  # 일치하는 곡이 없는 경우
        return "(None)"


"""
실패한 방식
"""
# def minute_range(st,end):
#     a = int(st[:2])*60 + int(st[3:])
#     b = int(end[:2])*60 + int(end[3:])
#     return b-a

# def cvt_info2fullstr(musicinfo):
#     st,end,title,music = musicinfo.split(',')
#     rng = minute_range(st,end)
#     music = get_music_len(music)
#     return music*(rng // len(music)) + music[:rng%len(music)], title

# def get_music_len(music):
#     sound = set(['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'])
#     assert len(sound) == 12
#     ans = []
#     while music:
#         if len(music) > 1 and music[:2] in sound:
#             ans.append(music[:2])
#             music = music[2:]
#         else:
#             ans.append(music[0])
#             music = music[1:]

#     return ans

# from collections import deque

# def solution(m, musicinfos):
#     answer = ''
#     candi = []
#     for mu in musicinfos:
#         candi.append(cvt_info2fullstr(mu))
#     # print(candi)
#     a = get_music_len(m)
#     a_set = set(a)
#     for i,title in candi:

#         if len(a) > len(i):
#             continue

#         if a in i:
#             return title
# #         if not (a_set.intersection(set(i)) == a_set):
# #             continue

# #         p = 0
# #         p_t = i.index(a[0])
# #         while p < len(a):
# #             # print(a[p],i[p_t])
# #             if a[p] == i[p_t]:
# #                 p+=1
# #                 p_t = (p_t+1)%len(i)
# #                 continue
# #             break
# #         if p == len(a):
# #             return title

#     return "(None)"
