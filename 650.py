# 最简单动态规划 dp[i] 存储结果为i个'A' 要复制粘贴的最少次数
# dp数组定义：能够打印出 i 个 'A' 的最少操作次数


class Solution:
    def minSteps(self, n: int) -> int:

        dp = [0] * (n + 1)
        for i in range(2, n + 1):

            dp[i] = i  # 最多复制一次再粘贴若干次
            for j in range(1, i):
                if i % j == 0:
                    # i 个 'A' 可以由j个'A'得来
                    # j个'A'先复制1次再粘贴i // j - 1次
                    # 因此 dp[j] + i // j
                    dp[i] = min(dp[i], dp[j] + i // j)

        return dp[-1]