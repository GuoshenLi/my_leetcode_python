# 死背 经久不衰的面试题目 二维dp
# 操作加权重怎么办 字节跳动面试题



# 啥叫编辑距离？我们说word1和word2的编辑距离为X，意味着word1经过X步，变成了word2，咋变的你不用管，反正知道就需要X步，并且这是个最少的步数。
#
# 我们有word1和word2，我们定义dp[i][j]的含义为：word1的前i个字符和word2的前j个字符的编辑距离。意思就是word1的前i个字符，变成word2的前j个字符，最少需要这么多步。
# 背下来dp矩阵的含义
# 例如word1 = "horse", word2 = "ros"，那么dp[3][2]=X就表示"hor"和“ro”的编辑距离，即把"hor"变成“ro”最少需要X步。
#
# 如果下标为零则表示空串，比如：dp[0][2]就表示空串""和“ro”的编辑距离
#
# 定理一：如果其中一个字符串是空串，那么编辑距离是另一个字符串的长度。比如空串“”和“ro”的编辑距离是2（做两次“插入”操作）。再比如"hor"和空串“”的编辑距离是3（做三次“删除”操作）。
#
# 定理二：当i>0,j>0时
# 如果word1[i][j] = word2[i][j]，显而易见，则dp[i][j] = dp[i - 1][j - 1] 因为i,j字母一样不用变换，所以和dp[i][j]和dp[i - 1][j - 1]一样
# 啥意思呢？举个例子，word1 = "abcde", word2 = "fgh",我们现在算这俩字符串的编辑距离，就是找从word1，最少多少步，能变成word2？那就有三种方式：
# 如果word1[i][j] != word2[i][j] 有三种情况了
# 知道"abcd"变成"fgh"多少步（假设X步），那么从"abcde"到"fgh"就是"abcde"->"abcd"->"fgh"。（一次删除，加X步，总共X+1步）
# 知道"abcde"变成“fg”多少步（假设Y步），那么从"abcde"到"fgh"就是"abcde"->"fg"->"fgh"。（先Y步，再一次添加，加X步，总共Y+1步）
# 知道"abcd"变成“fg”多少步（假设Z步），那么从"abcde"到"fgh"就是"(abcd)e"->"(fgh)e"->"fg" （先Z步，再一次替换，总共Z+1步）
# 就算字节面试 操作加权重怎么办 也很简单上面三种情况分别对应删除添加替换 因此在那一步加上权重即可

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)


        dp = [[float('+inf') for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i # 删除

        for j in range(n + 1):
            dp[0][j] = j # 增加

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:

                    dp[i][j] = min(1 + dp[i - 1][j], 1 + dp[i][j -  1], 1 + dp[i - 1][j - 1])


        # word1 = 'abcde'  word2 = 'fgh'
        # 1): 'abcde' -> 'fg'  dp[i][j - 1] + 1 'abcde' -> 'fg' ->'fgh' 对应增加一个
        # 2): 'abcd'  ->'fgh'  dp[i - 1][j] + 1 'abcde' -> 'abcd' + 'fgh' 对应删除一个字符
        # 3): 'abcd' -> 'fg'  dp[i - 1][j - 1] + 1
        # '(abcd)e' -> '(fg)e' -> '(fg)h'  对应替换一个字符

        return dp[-1][-1]



# 记忆化递归
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == -1:
                return j + 1

            if j == -1:
                return i + 1

            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i - 1, j - 1)
                return memo[(i, j)]

            else:
                memo[(i, j)] = min(1 + dfs(i, j - 1), 1 + dfs(i - 1, j), 1 + dfs(i - 1, j - 1))
                return memo[(i, j)]

        return dfs(len(word1) - 1, len(word2) - 1)
