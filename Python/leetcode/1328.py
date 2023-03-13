class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        if len(palindrome) == 1:
            return ""

        palindrome = list(palindrome)
        l = len(palindrome) // 2

        for i in range(l):
            if palindrome[i] != "a":
                palindrome[i] = "a"
                return "".join(palindrome)

        for i in range(l):
            if palindrome[-i - 1] != "a":
                palindrome[-i - 1] = "a"
                return "".join(palindrome)
            else:
                palindrome[-i - 1] = "b"
                return "".join(palindrome)

        return ""


