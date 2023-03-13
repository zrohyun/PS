from collections import Counter
def solution(genres, plays):
    answer = 0
    play_with_gen = dict()
    gen_cnt = dict()

    for i,(g,p) in enumerate(zip(genres,plays)):
        gen_cnt[g] = gen_cnt.get(g,0) + p
        play_with_gen[g] = play_with_gen.get(g,[]) + [(p,i)]
    
    gen_cnt = sorted(gen_cnt.items(), key=lambda item: item[1],reverse=True)
    # print(gen_cnt)
    
    ans = []
    for k,n in gen_cnt:
        ans += [i[1] for i in sorted(play_with_gen[k],key = lambda x:(-x[0],x[1]))[:2]]
        
    return ans