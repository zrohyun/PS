from collections import Counter
def solution(want, number, discount):
    answer = 0
    
    want_d = {w:n for w,n in zip(want, number)}
    window = Counter(discount[:10])

    if dict_compare(want_d,window):
        answer += 1
    
    for i in range(10,len(discount)):
        window[discount[i-10]] -=1
        window[discount[i]] +=1
        
        if dict_compare(want_d,window):
            answer+=1
    
    
    return answer

def dict_compare(a,b):
    for k,v in a.items():
        if( k not in b )or (b[k] < v):
            return False
    
    return True
    
    
