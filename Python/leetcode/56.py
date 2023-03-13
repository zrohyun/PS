class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        
        intervals = sorted(intervals,key=lambda x: x[0])
        
        for s,e in intervals:
            if not ans:
                ans.append([s,e])
            else:
                s_,e_ = ans[-1]
                if s_ <= s <= e_:
                    ans[-1][1] = max(e_,e)
                else:
                    ans.append([s,e])
        
        return ans
