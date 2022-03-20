from typing import List
# 超时
class Solution(object):

    # 回溯法
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def back(start):
            if start == len(s):
                return True
            for end in range(start, len(s)):
                sub_str = s[start : end + 1]
                if sub_str in wordDict:
                    flag = back(end + 1)
                    if flag is True:
                        return True
            return False
        return back(0)

# 记忆化递归 要背！就加了几行代码
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        def dfs(start):
            if start == n: return True
            if start in memo:
                return memo[start]
            for end in range(start, n):
                slice = s[start: end + 1]
                if slice in wordDict and dfs(end + 1):
                    memo[start] = True
                    return True
            memo[start] = False
            return False

        memo = {}
        return dfs(0)

print(Solution().wordBreak(s = "aaa", wordDict = ["a", "aa"]))