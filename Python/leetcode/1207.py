class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        uniq = Counter(arr)

        return True if len(set(uniq.values())) == len(uniq.values()) else False
