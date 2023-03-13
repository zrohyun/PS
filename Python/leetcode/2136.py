from heapq import heappush, heappop
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
        plantTime은 최적화될 수 없음. 최대한 growTime을 겹치게 세팅해야함.
        그럴려면 sum(plantTime) 시간 내에 growTime이 오래 걸리는 것들은 치워내고
        sum(plantTime)이후에 가장 짧게 growTime이 걸리는 식물을 배치하는 것이 가장 짧은 길이를 얻을 수 있는 해가 될 듯.
        heap으로 했지만 뭐 굳이 그렇게 할 필요는 없을 듯.
        """
        heap = []
        for p,g in zip(plantTime, growTime):
            heappush(heap, (-g,p))
        
        p,g = 0,0
        
        while heap:
            ng,np = heappop(heap)
            p += np
            g = max(g,p-ng)
        
        return g

    
# class Solution:
#     def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
#         '''
#         As plantTime cannot be optimized (only can grow one at a time), we try to optimize growTime (all plants can grow together)
#         Hence we should plant the one that takes the longest to grow first to save time.
#         '''
#         time_tuples = sorted(list(zip(plantTime,growTime)),key = lambda x:x[1], reverse = True)
        
#         ans = 0
#         plant_time = 0
        
#         for p,g in time_tuples:
#             plant_time += p
#             ans = max(ans,plant_time+g)
            
#         return ans