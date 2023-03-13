class MyCalendarThree:
    """
    condition
    k-booking check, k <=400
    0 <= start < end <= 1e9
    """

    def __init__(self):
        self.table = []
        self.ans = 1

    def book(self, start: int, end: int) -> int:
        ans = 1
        duration = end - start

        self.table.append((start, duration))
        self.table.sort()

        return self.ans

# from sortedcontainers import SortedList

# class MyCalendarThree:

#     def __init__(self):
#         self.k = 1
#         self.events = SortedList()

#     def book(self, start: int, end: int) -> int:
#         self.events.add((start, 1))
#         self.events.add((end, -1))

#         curMax = 0
#         for _, edge in self.events:
#             curMax += edge
#             self.k = max(self.k, curMax)

#         return self.k

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)