import bisect
from collections import deque


class MedianFinder:
    def __init__(self):
        self.li = deque()
        self.mid = 0
        self.cnt = 0

    def addNum(self, num: int) -> None:
        loc = bisect.bisect(self.li, num)
        if self.cnt % 2 == 0 and self.cnt != 0:
            self.mid += 1

        self.li.insert(loc, num)
        self.cnt += 1

    def findMedian(self) -> float:
        if self.cnt % 2:
            return self.li[self.mid]
        else:
            return (self.li[self.mid] + self.li[self.mid + 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
