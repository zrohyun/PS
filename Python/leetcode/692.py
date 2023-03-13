from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        cnt_words = sorted(Counter(words).items(), key=lambda x: (-x[1], x[0]))[:k]

        answer = [cnt_words[i][0] for i in range(k)]

        return answer
