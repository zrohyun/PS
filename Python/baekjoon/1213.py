from collections import Counter as cou
def solution():

    arr = sorted(list(map(str,input())))
    pal = []
    alpha_cnt = cou(arr)
    appear_odd = []
    for i in alpha_cnt.keys():
        if alpha_cnt[i] %2 ==1: 
            appear_odd.append(i)
            



print(solution())
