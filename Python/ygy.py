# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")

# from heapq import heappush,heappop
# import heapq
# def solution(stack1, stack2, stack3):
#     stack4 = []
#     len123 = len(stack1) + len(stack2)+ len(stack3)
#     for n,i in zip([1,2,3],[stack1,stack2,stack3]):
#         for j in i:
#             heappush(stack4,(j,n))

#     stack4 = heapq.nlargest(len123,stack4)

#     return "".join([str(s) for v,s in stack4])

# import spacy

# nlp = spacy.load("en_core_web_sm")

# def anonymize_text(sentences):
#     anony_txt = sentences

#     doc = nlp(sentences)

#     for e in reversed(doc.ents):
#         start = e.start_char
#         end = start + len(e.text)
#         anony_txt = anony_txt[:start] + "X"*len(e.text) + anony_txt[end:]

#     return anony_txt

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# from collections import defaultdict, deque
# def solution(S, C):

#     # memory alphbet location
#     word_dict = defaultdict(list)
#     for i,s in enumerate(S,start=1):
#         word_dict[s].append(i)

#     #split boundary memory
#     two_occur = deque([])
#     for v in word_dict.values():
#         two_occur += deque([(v[i-1],v[i]) for i in range(1,len(v))])

#     if not two_occur: return 0

#     for i,n in enumerate(C,start=1):
#         for _ in range(len(two_occur)):
#             # if i can split same alphabet pop from the boundary queue
#             left_idx,right_idx = two_occur[0]
#             if left_idx <= n < right_idx:
#                 two_occur.popleft()
#             else:
#                 two_occur.rotate(-1)

#         if not two_occur: return i

#     return -1
