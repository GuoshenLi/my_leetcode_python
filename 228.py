class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        i = 0
        res = []

        for j in range(len(nums)):

            if j + 1 < len(nums) and nums[j + 1] - nums[j] == 1:
                continue

            if i == j:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[i]) + "->" + str(nums[j]))

            i = j + 1

        return res

