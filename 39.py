# 回溯算法 candidate没有重复数字 不用避免相同 不用排序
class Solution(object):
    def combinationSum(self, nums, target):
        res = []
        n = len(nums)

        # index为你可以从candidate的第几个数开始取值
        # tmp为要append到res的临时数组
        def dfs(index, tmp):
            if sum(tmp) == target:
                res.append(tmp[:])
                return None
            if sum(tmp) > target:
                return None

            for i in range(index, n):
                tmp.append(nums[i])
                # append进来再进行判断
                dfs(i, tmp)
                # dfs(i, tmp) 一定是i不是index因为要从i开始取 
                tmp.pop()

        dfs(0, [])
        return res