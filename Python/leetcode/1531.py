from functools import lru_cache
from math import inf


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        condition
        s.length [1,100]
        k [0,s.length]


        method1
        index,k,char_cnt,prev_char로 매개변수를 가지고
        index를 하나씩 올려가며 length를 계산하는 알고리즘

        method2
        어쨌든 앞부터 탐색해나가며 변경되는 알파벳을 삭제할까말까가
        이 문제의 포인트이다. 그러면 이전에 등장했던 알파벳과 다른 알파벳이
        등장하는 지점을 n번의 탐색으로 저장한다. 그러면 변경되는 b개의 지점이 있을 때
        bCk개의 조합에 대하여 길이를 계산하면 되는데 처음부터 전부 구하면 당연히 시간이 엄청
        걸리고 b 지점에 대하여 이전에 계산됐던 길이를 저장해두면 어떨까 싶은데 이러면 k가 처음일 때만
        효과적으로 계산할 수 있다. 어떻게 해결할 수 있을지는 고민해봐야할 문제..

        https://leetcode.com/problems/string-compression-ii/discuss/2704272/Daily-LeetCoding-Challenge-October-Day-15
        위의 java 코드를 보면 i,k로 dp 메모리를 구성한 것을 볼 수 있다. 생각해보면 i번째 알파벳에 대하여 k번째 삭제연산이 이루어진다고 했을때
        당연히 최소 조건에 대한 메모이제이션이 일어났을 테니 그 후의 연산에 대해서만 고려하면 될 것이다.

        """
        n = len(s)

        @lru_cache(None)
        def counts(k, i, j, c):

            if k < 0:
                return inf

            if i >= n:
                return 0

            if 0 <= j < n and s[i] == s[j]:
                return int(c == 1 or c == 9 or c == 99) + counts(k, i + 1, i, c + 1)

            return min(1 + counts(k, i + 1, i, 1), counts(k - 1, i + 1, j, c))

        return counts(k, 0, -1, 0)