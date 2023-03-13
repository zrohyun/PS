class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:

        logs = sorted(logs, key=lambda x: x[1])
        start = logs[0][1]
        longgest = logs[0][1]
        man = logs[0][0]

        for iid, times in logs[1:]:
            if longgest <= (times - start):
                man = iid if longgest != (times - start) else min(man, iid)
                longgest = times - start

            start = times
        return man


