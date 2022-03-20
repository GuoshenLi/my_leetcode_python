from typing import List
#思路1：可以长度为0遍历一次，长度为1遍历一次，长度为2遍历一次

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 第78题和第90题
        n = len(nums)
        self.res = []
        for i in range(n + 1):
            self.dfs(nums, 0, [], i)

        return self.res

    def dfs(self, nums, index, tmp, target_level):
        if len(tmp) == target_level:
            self.res.append(tmp[:])
            return None

        for i in range(index, len(nums)):
            tmp.append(nums[i])
            self.dfs(nums, i + 1, tmp, target_level)
            tmp.pop()

#思路二：一次回溯搞定
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(index, tmp):
            res.append(tmp[:])
            for i in range(index, n):
                tmp.append(nums[i])
                dfs(i + 1, tmp)
                tmp.pop()

        dfs(0, [])
        return res


print(Solution1().subsets([1,2,3]))




