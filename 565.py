from typing import List
# 暴力解法 差两个没通过
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)

        res = 0
        for i in range(n):
            cur, cnt = i, 0
            visited = [0] * n
            while not visited[cur]:
                visited[cur] = 1
                cur = nums[cur]
                cnt += 1
            res = max(res, cnt)
        return res


# 做一点稍微的改动 O(n)时间 O(n)空间
# 维护一个visited数组 遍历每一个开头元素 如果为0则 可以完成一个环
# 如果为1就跳过 因为一定会落入环
# 因此每一个元素都遍历了一遍！时间复杂度是O(n)
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [0] * n
        res = 0
        for i in range(n):
            if visited[i] == 0:
                cur, cnt = i, 0
                while not visited[cur]:
                    visited[cur] = 1
                    cur = nums[cur]
                    cnt += 1
                res = max(res, cnt)

        return res



print(Solution().arrayNesting(nums = [5, 4, 0, 3, 1, 6, 2]))