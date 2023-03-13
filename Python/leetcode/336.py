from itertools import combinations as comb

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ret = []
            
        # store = {i:set([words[i],words[i][::-1]]) for i in range(len(words))}
        store = {n[::-1]:i for i,n in enumerate(words)}
        is_zero_in = self._iszeroin(words)
        
        for i,w in enumerate(words):
            
            if w in store and store[w] != i: #totally reversed case
                ret.append([i,store[w]])
                
            if is_zero_in!= -1 and self.isPalindrome(w): #solo palindrome      
                if is_zero_in != store[w]:
                    ret.append([is_zero_in,store[w]])
                    ret.append([store[w],is_zero_in])
            # if w != "" and "" in store and w == w[::-1]:
            #     ret.append([i, store[""]])
            #     ret.append([store[""], i])
            
            for j in range(len(w)):
                if w[j:] in store and w[:j] == w[j-1::-1]:
                    ret.append([store[w[j:]],i])
                if w[:j] in store and w[j:] == w[:j-1:-1]:
                    ret.append([i,store[w[:j]]])
        return ret
    
    def isPalindrome(self, word) -> bool:
        for i in range(int(len(word)/2)):
            if word[i] != word[-i-1]:
                return False
        return True
    
    def _iszeroin(self, words) -> bool:
        for i,w in enumerate(words):
            if len(w) == 0:
                return i
        return -1
