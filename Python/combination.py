sample = list(map(chr,range(65,68)))

def nCm(n,m):
    if m>n:
        raise ValueError("m cannot be larger than n")

    from math import factorial as facto
    return int((facto(n)/facto(m))/facto(m-n))

def combination2(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combination2(array[i+1:], r-1):
                yield [array[i]] + next

# for i in combinations_2(sample,2):
#     print(i)
def combination(m):
    ret = []
    def comb(sam,combi):
        if len(combi) == m:
            ret.append(combi)
        else:
            for i,s in enumerate(sam):
                comb(sam[i+1:],combi + [s])
    comb(sample,[])
    return ret

if __name__ == '__main__':
    from itertools import combinations
    a = len(combination(2))
    b = len([i for i in combination2(sample,2)])
    c = len([i for i in combinations(sample,2)])
    assert c == b
    assert a == b 
