# 一定要用pair记录一下原来的位置在哪里
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        pairs = []
        for i in range(len(nums)):
            pairs.append([nums[i], i])
        pairs.sort(key=lambda a: a[0], reverse=True)
        for i in range(len(nums)):
            if i == 0:
                nums[pairs[i][1]] = "Gold Medal"
            if i == 1:
                nums[pairs[i][1]] = "Silver Medal"
            if i == 2:
                nums[pairs[i][1]] = "Bronze Medal"
            if i > 2:
                nums[pairs[i][1]] = str(i + 1)
        return nums

