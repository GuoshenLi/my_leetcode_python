# 用数组不超时
#  最后一个被戳破的气球
# 在(i, j)开区间当中，最后一个戳破气球k。其中i < k < j。
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        n = len(nums)
        memo = [[None] * n for i in range(n)]

        def dfs(i, j):
            if i + 1 == j: return 0
            if memo[i][j]: return memo[i][j]

            res = 0
            for k in range(i + 1, j):
                if not memo[i][k]:
                    memo[i][k] = dfs(i, k)

                if not memo[k][j]:
                    memo[k][j] = dfs(k, j)

                res = max(res, memo[i][k] + memo[k][j] + nums[i] * nums[k] * nums[j])
            memo[i][j] = res
            return memo[i][j]

        return dfs(0, n - 1)


# 动态规划
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        #nums首尾添加1，方便处理边界情况
        nums.insert(0,1)
        nums.insert(len(nums),1)

        store = [[0]*(len(nums)) for i in range(len(nums))]

        def range_best(i,j):
            m = 0
            #k是(i,j)区间内最后一个被戳的气球
            for k in range(i+1,j): #k取值在(i,j)开区间中
                #以下都是开区间(i,k), (k,j)
                left = store[i][k]
                right = store[k][j]

                store[i][j] = max(store[i][j], left + nums[i] * nums[k] * nums[j] + right)


        # 对每一个区间长度进行循环
        # 区间要从小到大
        for n in range(2, len(nums)): #区间长度 #长度从3开始，n从2开始
            #开区间长度会从3一直到len(nums)
            #因为这里取的是range，所以最后一个数字是len(nums) - 1

            #对于每一个区间长度，循环区间开头的i
            for i in range(0, len(nums) - n): #i + n = len(nums) - 1

                #计算这个区间的最多金币
                range_best(i, i + n)

        return store[0][len(nums) - 1]




class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # 区间dp
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for i in range(n)]

        # dp[i][j] 表示从下标i 到j 开区间，最大的硬币数量
        # 枚举的时候一定要从最短区间开始枚举，长度为3

        for length in range(2, n):
            for i in range(n - length):
                # 区间i, j为 i, i + length
                j = i + length
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k])

        return dp[0][n - 1]