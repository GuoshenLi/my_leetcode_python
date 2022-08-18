'''
一个环，有n个点, 问从0点出发，经过k步回到原点有多少种方法（字节面试题，java解法）
'''

'''
https://blog.csdn.net/m0_37605197/article/details/107938339?spm=1001.2101.3001.4242
'''

from typing import List
class Solution:
    def reversePairs(self,n: int, k: int) -> int:
        if n == 0: return 1
        if n == 2: return k % 2 == 0

        dp = [[0] * n for i in range(k + 1)]
        dp[0][0] = 1
        # dp[0][j] = 0 if j >= 1

        for i in range(1, k + 1):
            for j in range(n):

                dp[i][j] = dp[i - 1][(j - 1) % n] + dp[i - 1][(j + 1) % n]

        return dp[k][0]

