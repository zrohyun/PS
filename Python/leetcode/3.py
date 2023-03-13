from typing import List
class MySolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not len(s):
            return 0
        
        dp = [[1,set(i)] for i in s]
        for i in range(1,len(s)):
            v,ss = dp[i-1]
            if not ((ss & (b:=dp[i][1]))):
                dp[i] = [v+1,ss.union(b)]
            else:
                #tmp set 만들고 거꾸로 돌면서 
                #tmp와 교집합 없으면 ++하고 진행
                #교집합 있으면 정지하고 i에 넣음
                tmp = set()
                cnt = 0
                for j in range(i,-1,-1):
                    if not(tmp & set(s[j])):
                        tmp.add(s[j])
                        cnt +=1
                    else:
                        break
                dp[i] = [cnt,tmp]
        print(dp)
        
        return max(dp)[0]
        
            
            
        
        