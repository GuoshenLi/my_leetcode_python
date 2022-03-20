from typing import List
# 0 1背包问题
from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        length = len(strs)
        # dp[i][j][k]
        dp = [[[0] * (n + 1) for i in range(m + 1)] for i in range(length + 1)]

        # strs的前i个字符串最多能够构成j个0和k个1的最大子集大小

        count_str = [Counter(string) for string in strs]


        for i in range(1, length + 1):
            num_0, num_1 = count_str[i - 1]['0'], count_str[i - 1]['1']

            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= num_0 and k >= num_1:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - num_0][k - num_1] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[length][m][n]


#0-1 背包 的记忆化递归
from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        c = [Counter(item) for item in strs]
        length = len(strs)
        @lru_cache(None)
        def dfs(index, count0, count1):
            if index == length: return 0

            # 能够取的情况下分两种 取还是不取 要最大的
            if c[index]['0'] + count0 <= m and c[index]['1'] + count1 <= n:
                return max(dfs(index + 1, count0, count1), 1 + dfs(index + 1, count0 + c[index]['0'], count1 + c[index]['1']))
            # 不能够取 只能向下递归
            else:
                return dfs(index + 1, count0, count1)

        return dfs(0, 0, 0)


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.res = 0
        length = len(strs)
        def dfs(index, tmp):

            self.res = max(self.res, self.calculate(tmp, m, n))

            for i in range(index, length):
                tmp.append(strs[i])
                dfs(i + 1, tmp)
                tmp.pop()

        dfs(0, [])
        return self.res

    def calculate(self, tmp, m, n):
        if not tmp: return 0
        count0 = 0
        count1 = 0

        for item in tmp:
            count0 += item.count('0')
            count1 += item.count('1')

        return len(tmp) if count0 <= m and count1 <= n else 0




from collections import Counter

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        c = [Counter(item) for item in strs]

        self.res = 0
        length = len(strs)

        @lru_cache(None)
        def dfs(index, count0, count1, step):

            self.res = max(self.res, step)

            for i in range(index, length):
                if c[i]['0'] + count0 <= m and c[i]['1'] + count1 <= n:
                    dfs(i + 1, c[i]['0'] + count0, c[i]['1'] + count1, step + 1)

        dfs(0, 0, 0, 0)
        return self.res

print(Solution().findMaxForm(["10","0001","111001","1","0"], 5, 3))