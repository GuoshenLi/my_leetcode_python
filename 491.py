class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        unique = set()

        def dfs(start, tmp):

            if len(tmp) >= 2:
                if '-'.join(map(str, tmp)) not in unique:
                    res.append(tmp[:])
                    unique.add('-'.join(map(str, tmp)))

            for end in range(start, length):
                if not tmp or nums[end] >= tmp[-1]:
                    tmp.append(nums[end])
                    dfs(end + 1, tmp)
                    tmp.pop()

        dfs(0, [])

        return res
