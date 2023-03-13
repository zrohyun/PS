from collections import Counter
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        vowels = list('aeiou')

        a,b = Counter(s[:len(s)//2]),Counter(s[len(s)//2:])
        cnt_a,cnt_b = 0,0
        
        for v in vowels:
            cnt_a += a[v]
            cnt_b += b[v]
        
        return cnt_a == cnt_b
