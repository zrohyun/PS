from itertools import permutations
sample = list(map(chr,range(65,70)))

def permutation():
    visit = [0]* len(sample)
    ret = []
    def permute(visit,p):
        if all(visit):
            ret.append(p)
        else:
            for i,s in enumerate(sample):
                if not visit[i]:
                    visit[i] = 1
                    p.append(s)
                    permute(visit,p)
                    visit[i] = 0
                    p.pop()
    permute(visit,[])
    return ret

def nPm(n,m):
    if m>n:
        raise ValueError("m cannot be larger than n")

    from math import factorial as facto
    return int(facto(n)/facto(m-n))

if __name__ == '__main__':
    numsam = len(sample)
    assert len(permutation()) == nPm(numsam, numsam)
    assert len(list(permutations(sample))) == nPm(numsam, numsam)