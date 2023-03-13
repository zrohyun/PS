class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        모든 후보가 2개씩 주어짐. 팰린드롬은 무조건 짝수일 수 밖에 없음
        그러면 나랑 반대되는 애 쌍을 찾으면 될 듯?
        """

        counts = Counter(words)
        has_double = False

        for word in counts.keys():
            if word != word[::-1]:
                counts[word] = min(counts[word], counts[word[::-1]])
            else:
                if counts[word] % 2:
                    has_double = True
                counts[word] = counts[word] - (counts[word] % 2)
        return 2 * (sum(counts.values()) + int(has_double))
