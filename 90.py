class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        def dfs(index, tmp):
            res.append(tmp[:])
            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                tmp.append(nums[i])
                dfs(i + 1, tmp)
                tmp.pop()

        dfs(0, [])
        return res