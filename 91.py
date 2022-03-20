class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [None for i in range(n)]
        def dfs(start):
            if start == n: return 1
            if memo[start]: return memo[start]
            res = 0
            for end in range(start, min(start + 2, n)):
                            # 每次只用考虑两个 一个或两个字母 注意越界
                tmp = s[start: end + 1]
                if len(tmp) == len(str(int(tmp))) and 1 <= int(tmp) <= 26:
                    res += dfs(end + 1)
            memo[start] = res
            return memo[start]

        return dfs(0)




class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for i in range(n + 1)]
        dp[0] = 1 # 空串也有一种解码方式 解码出来也是空串

        # 前i个字符能够构成的解码方法总数

        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i - 2 >= 0 and s[i - 2] != '0' and int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]


        return dp[n]