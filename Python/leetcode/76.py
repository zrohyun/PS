# from collections import deque, defaultdict, Counter
# from copy import deepcopy as dcp

# # My Solution TLE(Time Limit Exceeded)
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         q = deque([])
#         check_t = Counter(t)
#         if len(s) < len(t): return ""

#         def slide_window(dict_,s_l,s_r,window_size):

#             for i in range(len(s_r)):
#                 dict_[s_r[i]] +=1 # add new alpha
#                 dict_[s_l[0]] -=1 # remove before alpha

#                 if dict_[s_l[0]] ==0:
#                     del dict_[s_l[0]]

#                 s_l = s_l[1:] + s_r[i]

#                 q.append((dcp(dict_), s_l ,s_r[i+1:],window_size))

#         before_alpha_dict = Counter(s[:len(t)])

#         # dict, substring, remain, window_size
#         q.append((dcp(before_alpha_dict),s[:len(t)],s[len(t):], len(t)))

#         slide_window(before_alpha_dict,s[:len(t)],s[len(t):],len(t))
#         # print(q)


#         while q:
#             alfa_dict, sub,remain , window_size = q.popleft()
#             # print(sub)
#             if check_satisfy(alfa_dict,check_t): return sub

#             if not remain: continue


#             alfa_dict[remain[0]]+=1
#             sub = sub + remain[0]
#             remain = remain[1:]
#             q.append((dcp(alfa_dict),sub,remain,window_size+1))

#             slide_window(alfa_dict,sub,remain,window_size+1)

#         return ""


#     def check_satisfy(self,d_s,d_t):
#         for k,v in d_s.items():
#             if k in d_t and d_t[k] > v:
#                 return False
#         return True


# def check_satisfy(d_s,d_t):
#     """
#     d_s가 d_t를 포함해야함.
#     """
#     for k,v in d_t.items():
#         if k not in d_s:
#             return False

#         if d_s[k] < v:
#             return False

#     return True

from collections import deque, defaultdict, Counter
from copy import deepcopy as dcp


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t)  # counter for t to check with
        window = Counter()  # sliding window
        ans = ""  # answer
        last = 0  # last index in our window
        for i, char in enumerate(s):
            window[char] = window.get(char, 0) + 1  # add this character to our window
            while (
                window >= tCounter
            ):  # while we have all the necessary characters in our window
                if ans == "" or i - last < len(
                    ans
                ):  # if the answer is better than our last one
                    ans = s[last : i + 1]  # update ans
                window[s[last]] -= 1  # remove the last element from our counter
                last += 1  # move the last index forward
        return ans  # return answer
