from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(start, tmp):
            if start == len(s):
                res.append(tmp[:])
                return None
            for end in range(start, len(s)):
                if self.is_valid_palindrome(s, start, end):

                    tmp.append(s[start: end + 1])
                    dfs(end + 1, tmp)
                    tmp.pop()


        dfs(0, [])
        return res

    def is_valid_palindrome(self, s, left, right):
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


print(Solution().partition(s = 'aab'))


# dp数组先判断是不是i，j预处理判断回文
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        is_palin = [[True] * n for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                is_palin[i][j] = is_palin[i + 1][j - 1] and (s[i] == s[j])

        def dfs(tmp, start):
            if start == n:
                res.append(tmp[:])
                return None

            for end in range(start, n):
                if is_palin[start][end]:
                    tmp.append(s[start: end + 1])
                    dfs(tmp, end + 1)
                    tmp.pop()

        dfs([], 0)
        return res
