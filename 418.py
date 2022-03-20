from typing import List
import numpy as np
import random

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)
        dp = [0] * n
        # dp[i] 表示从 sentence[i] 开始往后 能放入多少个
        for i in range(n):
            curWordIndex = i
            curLen = 0
            count = 0
            while curLen + len(sentence[curWordIndex]) <= cols:
                curLen += len(sentence[curWordIndex]) + 1
                curWordIndex += 1
                count += 1
                if curWordIndex == n:
                    curWordIndex = 0

            dp[i] = count

        res = 0
        start = 0
        for i in range(rows):
            res += dp[start]
            start = (start + dp[start]) % n


        # 总共能放入res个 再除以n 表明能够放入多少个sentence的组合
        return res // n




print(Solution().wordsTyping(rows = 3, cols = 6, sentence = ["a", "bcd", "e"]))