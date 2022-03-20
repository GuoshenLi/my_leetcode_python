# 这样python超时 83 / 84
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        N = len(envelopes)
        envelopes.sort()
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)





# 动态规划方法
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        if not envelopes: return 0
        n = len(envelopes)
        dp = [1 for i in range(n)]
        envelopes.sort(key = lambda x: (x[0], -x[1]))

        for i in range(n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)


        return max(dp)




# 二维的最长递增子序列
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes: return 0

        res = []
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        for i in range(len(envelopes)):
            if not res or res[-1] < envelopes[i][1]:
                res.append(envelopes[i][1])

            else:
                idx = self.binary_search(res, envelopes[i][1])
                res[idx] = envelopes[i][1]

        return len(res)

    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        # 同样也找第一个大于等于它的
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left



class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n == 1: return 1

        envelopes.sort(key = lambda x: (x[0], -x[1]))

        res = []
        for i in range(n):
            if not res or envelopes[i][1] > res[-1][1]:
                res.append(envelopes[i])

            else:

                left = 0
                right = len(res) - 1

                while left < right:
                    # 找第一个大于等于 envelopes[i][1]
                    mid = (left + right) // 2
                    if res[mid][1] < envelopes[i][1]:
                        left = mid + 1
                    else:
                        right = mid

                res[left] = envelopes[i]

        return len(res)
