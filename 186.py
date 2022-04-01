class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """


        s[:] = list(' '.join(''.join(s).split()[::-1]))



class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(s: List[str], L: int, R: int) -> None:
            while L < R:
                s[L], s[R] = s[R], s[L]
                L += 1
                R -= 1

        n = len(s)
        L = 0
        for R in range(n):
            if s[R] == ' ':
                reverse(s, L, R - 1)
                L = R + 1
        reverse(s, L, n - 1)        #做好收尾工作

        reverse(s, 0, n - 1)
