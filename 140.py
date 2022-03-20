from typing import List
# 普通回溯  可以过
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        res = []

        def dfs(start, tmp):
            if start == n:
                res.append(' '.join(tmp))

            for end in range(start, n):
                if s[start: end + 1] in wordDict:
                    tmp.append(s[start: end + 1])
                    dfs(end + 1, tmp)
                    tmp.pop()

        dfs(0, [])
        return res

# 记忆化递归 不能叫回溯感觉
# 目标很明确 dfs(3) 表明从下标为3开始到最后能够分割的所有可能组合
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        memo = {}
        def dfs(start):
            if start == n: return ['']
            if start in memo:
                return memo[start]
            res = []
            for end in range(start, n):
                slice = s[start : end + 1]
                if slice in wordDict:
                    tmp = dfs(end + 1)
                    for word in tmp:
                        res.append((slice + ' ' + word).strip())

            memo[start] = res
            return res


        return dfs(0)


Solution().wordBreak("catsanddog")



print(Solution().wordBreak(s = "aaa", wordDict = ["aa","a"]))